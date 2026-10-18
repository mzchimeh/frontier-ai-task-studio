"""Loopback-only UI and fixed Harbor command runner. No third-party dependencies."""
from __future__ import annotations
import hashlib, json, os, re, secrets, shutil, subprocess, threading, time, tomllib, uuid
from datetime import datetime, timezone
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import urlparse

ROOT=Path(__file__).resolve().parent
TASKS=ROOT/'workspace'/'tasks'
RUNTIME=ROOT/'runtime'
PORT=int(os.environ.get('TASK_AUTHOR_PORT','8765'))
TOKEN=secrets.token_urlsafe(32)
JOBS={}
LOCK=threading.Lock()
REQUIRED=['instruction.md','task.toml','README.md','environment/Dockerfile','solution/solve.sh','tests/test.sh','tests/Dockerfile']
def now(): return datetime.now(timezone.utc).isoformat()
def tool(name):
    path=shutil.which(name)
    # Shell wrappers are not executed. Use the installed executable entrypoint.
    return path if path and Path(path).suffix.lower() not in ('.bat','.cmd','.ps1') else None
def available():
    harbor=tool('harbor'); docker=tool('docker'); ready=False; message='Docker executable not found.'
    if docker:
        try:
            p=subprocess.run([docker,'info','--format','{{.ServerVersion}}'],capture_output=True,text=True,timeout=8)
            ready=p.returncode==0;message=p.stdout.strip() if ready else 'Docker is installed but its engine is unavailable.'
        except (OSError,subprocess.TimeoutExpired): message='Docker engine did not respond.'
    return {'harbor':bool(harbor),'docker':bool(docker),'dockerReady':ready,'dockerDetail':message,'token':TOKEN,'tasks':[p.name for p in sorted(TASKS.iterdir()) if p.is_dir() and not p.is_symlink()] if TASKS.exists() else [],'taskRoot':str(TASKS)}
def resolve_task(name):
    if not isinstance(name,str) or not re.fullmatch(r'[a-zA-Z0-9][a-zA-Z0-9_-]{0,79}',name): raise ValueError('Choose a task folder with letters, numbers, hyphens, or underscores.')
    base=TASKS.resolve(); p=base/name
    if p.is_symlink() or not p.is_dir() or p.resolve().parent!=base: raise ValueError('Task must be a direct folder inside workspace/tasks/.')
    return p
def fingerprint(path):
    h=hashlib.sha256()
    for p in sorted(path.rglob('*')):
        if p.is_symlink(): raise ValueError('Symlinks are not supported in validation bundles.')
        if p.is_file():
            h.update(p.relative_to(path).as_posix().encode());h.update(b'\0')
            with p.open('rb') as f:
                for block in iter(lambda:f.read(1048576),b''):h.update(block)
            h.update(b'\0')
    return h.hexdigest()
def preflight(path):
    errors=[]
    for name in REQUIRED:
        p=path/name
        if not p.is_file() or not p.stat().st_size:errors.append('Missing or empty: '+name)
    for p in path.rglob('*'):
        rel=p.relative_to(path)
        if p.is_symlink():errors.append('Unsupported symlink: '+str(rel))
        if rel.parts[0] not in ['instruction.md','task.toml','README.md','environment','solution','tests','authoring']:errors.append('Unapproved root entry: '+str(rel))
        if 'cheat' in rel.parts or p.name.lower() in ('docker-compose.yml','docker-compose.yaml','compose.yml','compose.yaml'):errors.append('Prohibited entry: '+str(rel))
    if errors:return errors
    try:
        d=tomllib.loads((path/'task.toml').read_text(encoding='utf-8')); a=d['agent']['timeout_sec'];v=d['verifier'];e=d['environment'];m=d['metadata'];t=d['task']
        if d.get('schema_version')!='1.4':errors.append('Schema must be 1.4.')
        if not isinstance(a,(int,float)) or isinstance(a,bool) or not float(a).is_integer() or not 9000<=a<=28800:errors.append('Invalid agent timeout.')
        if not isinstance(v.get('timeout_sec'),(int,float)) or not 0<=v['timeout_sec']<=13500:errors.append('Invalid verifier timeout.')
        if e.get('network_mode')!='public' or v.get('environment',{}).get('network_mode')!='no-network' or v.get('environment_mode')!='separate':errors.append('Required network/isolation settings are missing.')
        if e.get('cpus') not in [1,2,4,8,16] or e.get('memory_mb') not in [1024,2048,4096,8192,16384] or not 0<e.get('storage_mb',0)<=40960:errors.append('Invalid resource limits.')
        if e.get('gpus') not in [0,1] or (e.get('gpus')==1 and e.get('gpu_types')!=['H100']):errors.append('Invalid GPU settings.')
        if 'allow_internet' in e:errors.append('Deprecated allow_internet key is prohibited.')
        if not re.fullmatch(r'afterquery/[a-z0-9]+(?:-[a-z0-9]+){0,2}',t.get('name','')):errors.append('Invalid task name.')
        for k in ['author_name','author_email','author_organization','author_profile','conflicts_of_interest','domain','field','subfield','subcategory','relevant_experience','difficulty_explanation','solution_explanation','verification_explanation']:
            if not isinstance(m.get(k),str) or not m[k].strip():errors.append('Metadata missing: '+k)
        if m.get('category')!='Science' or not m.get('tags') or not m.get('expert_time_estimate_hours',0)>0:errors.append('Invalid science metadata.')
        text=(path/'instruction.md').read_bytes().decode('utf-8');end='\n\nYou have '+str(int(a))+' seconds to complete this task. Do not cheat by using online solutions or hints specific to this task.'
        if not (text.endswith(end) or text.endswith(end+'\n')):errors.append('Instruction ending must match integer timeout exactly, using LF newlines.')
        if re.search(r'^\s{0,3}#{1,6}\s',text,re.M):errors.append('Instruction contains Markdown headings.')
        artifacts=d.get('artifacts')
        if not isinstance(artifacts,list) or not artifacts or any(not isinstance(x,str) or not x.startswith('/') or '..' in x.split('/') or x not in text for x in artifacts):errors.append('Artifact paths must be absolute, declared, and named in instructions.')
    except (KeyError,TypeError,ValueError,OverflowError,UnicodeError,OSError) as ex:errors.append('Cannot validate task configuration: '+str(ex))
    return errors
def gather(run):
    rewards=[];reports=[]
    for p in run.rglob('reward.txt'):
        if 'task' in p.relative_to(run).parts or not any('verifier' in x.lower() for x in p.relative_to(run).parts):continue
        if p.stat().st_size<100:
            value=p.read_text(errors='replace').strip();rewards.append({'path':str(p.relative_to(run)),'value':int(value) if value in ('0','1') else None})
    for p in run.rglob('*.json'):
        if 'task' in p.relative_to(run).parts or p.stat().st_size>5000000:continue
        try:
            obj=json.loads(p.read_text());results=obj.get('results',{})
            if isinstance(results,dict) and isinstance(results.get('tests'),list):reports.append(str(p.relative_to(run)))
        except (ValueError,OSError,AttributeError):pass
    return rewards,reports
def execute(job,path):
    run=RUNTIME/job['id'];run.mkdir(parents=True)
    try:
        snapshot=run/'task';shutil.copytree(path,snapshot,symlinks=False)
        job['fingerprint']=fingerprint(snapshot);errors=preflight(snapshot)
        if errors:raise ValueError('; '.join(errors))
        cmd=[tool('harbor') or 'harbor']
        if job['kind']=='quality':cmd+=['check',str(snapshot),'-m','anthropic/claude-opus-4-8']
        else:cmd+=['run','-p',str(snapshot),'-a',job['kind'],'-e','docker']
        job['command']=cmd;job['state']='running';job['startedAt']=now();started=time.monotonic()
        with (run/'process.log').open('w',encoding='utf-8') as out:
            p=subprocess.Popen(cmd,cwd=run,stdout=out,stderr=subprocess.STDOUT,stdin=subprocess.DEVNULL,shell=False,creationflags=getattr(subprocess,'CREATE_NO_WINDOW',0))
            job['pid']=p.pid;job['exitCode']=p.wait()
        job['elapsedSeconds']=round(time.monotonic()-started,2)
        job['rewards'],job['ctrfReports']=gather(run)
        job['state']='completed' if job['exitCode']==0 else 'process-failed'
        expected=1 if job['kind']=='oracle' else 0
        job['evidenceStatus']='requires-review' if job['kind']=='quality' else ('expected-reward-observed' if job['exitCode']==0 and len(job['rewards'])==1 and job['rewards'][0]['value']==expected and job['ctrfReports'] else 'missing-or-unexpected-evidence')
        job['sourceUnchanged']=fingerprint(path)==job['fingerprint']
    except Exception as ex:job['state']='blocked';job['error']=str(ex)
    finally:
        job['finishedAt']=now();(run/'run-record.json').write_text(json.dumps(job,indent=2),encoding='utf-8')
def public_job(job):
    obj=dict(job);p=RUNTIME/job['id']/'process.log'
    if p.exists():
        with p.open('rb') as f:f.seek(max(0,p.stat().st_size-60000));obj['log']=f.read().decode('utf-8',errors='replace')
    return obj
class Handler(SimpleHTTPRequestHandler):
    def __init__(self,*a,**kw):super().__init__(*a,directory=str(ROOT),**kw)
    def log_message(self,*args):pass
    def valid_host(self):return self.headers.get('Host')==f'127.0.0.1:{PORT}'
    def reply(self,status,obj):
        b=json.dumps(obj).encode();self.send_response(status);self.send_header('Content-Type','application/json');self.send_header('Cache-Control','no-store');self.send_header('Content-Length',str(len(b)));self.end_headers();self.wfile.write(b)
    def do_GET(self):
        if not self.valid_host():return self.reply(403,{'error':'Loopback host required.'})
        route=urlparse(self.path).path
        if route=='/api/status':return self.reply(200,available())
        if route=='/api/jobs':return self.reply(200,[public_job(j) for j in list(JOBS.values())])
        target=Path(self.translate_path(self.path)).resolve()
        if target==RUNTIME.resolve() or RUNTIME.resolve() in target.parents:return self.reply(403,{'error':'Use the evidence export; runtime files are not served.'})
        if target==TASKS.resolve() or TASKS.resolve() in target.parents:return self.reply(403,{'error':'Task files are not served.'})
        if ROOT.resolve() not in target.parents and target!=ROOT.resolve():return self.reply(403,{'error':'Workspace boundary required.'})
        if route=='/':self.path='/dist/validation.html'
        return super().do_GET()
    def do_POST(self):
        if not self.valid_host() or self.headers.get('Origin')!=f'http://127.0.0.1:{PORT}' or self.headers.get('X-Task-Author')!=TOKEN:return self.reply(403,{'error':'Open the app from this local runner.'})
        try:
            n=int(self.headers.get('Content-Length','0'))
            if n<=0 or n>10000:raise ValueError('Invalid request length.')
            data=json.loads(self.rfile.read(n))
            if not isinstance(data,dict):raise ValueError('Request must be an object.')
            if self.path!='/api/run':return self.reply(404,{'error':'Unknown endpoint.'})
            if data.get('kind') not in ['oracle','nop','quality']:raise ValueError('Unsupported check.')
            if data.get('reviewed') is not True:raise ValueError('Confirm task rule review before execution.')
            if data['kind']=='quality' and data.get('providerConfirmed') is not True:raise ValueError('Confirm the model/provider review before running.')
            path=resolve_task(data.get('task'));errors=preflight(path)
            if errors:return self.reply(422,{'error':'Local structural checks failed.','issues':errors})
            prereqs=available()
            if not prereqs['harbor'] or not prereqs['dockerReady']:return self.reply(409,{'error':'Harbor and a running Docker engine are required.'})
            with LOCK:
                if any(j['state'] in ('queued','running') for j in JOBS.values()):return self.reply(409,{'error':'A check is already active.'})
                job={'id':uuid.uuid4().hex,'task':path.name,'kind':data['kind'],'state':'queued','createdAt':now(),'evidenceStatus':'pending'};JOBS[job['id']]=job
            threading.Thread(target=execute,args=(job,path),daemon=True).start();return self.reply(202,job)
        except (ValueError,TypeError,OSError) as ex:return self.reply(400,{'error':str(ex)})
if __name__=='__main__':
    TASKS.mkdir(parents=True,exist_ok=True);RUNTIME.mkdir(exist_ok=True)
    print(f'Frontier AI Task Studio: http://127.0.0.1:{PORT}/dist/validation.html',flush=True)
    ThreadingHTTPServer(('127.0.0.1',PORT),Handler).serve_forever()
