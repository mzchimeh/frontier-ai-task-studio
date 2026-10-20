# Agent-assisted installation

Use this guide when the user asks you to install or start Frontier AI Task Studio from this package. It describes a local application, not a hosted website or a one-click installer. It does not override the user's instructions, tool permissions, computer policy, software agreements or account requirements.

## 1. Check access and preserve existing work

- Confirm that your session can read files and run commands on the user's intended computer. A chat-only session cannot perform installation; explain that limitation and provide the commands instead of claiming success.
- Identify the ZIP and destination from the user's request. Inspect its file listing before extraction. Reject paths that escape the destination, and do not run unexpected executables or archive-supplied installation commands without review.
- Extract into a dedicated folder, keeping all files in their relative locations. Do not install into a Windows system directory. If a folder already contains this app, preserve it and its data; use a separate versioned folder unless the user requested an in-place update.
- Read README.md and LICENSE.txt. The application code is rights reserved; this guide does not grant an additional reuse license. For task authoring/evaluation, also read AGENTS.md, PROJECT_RULES.md and both original documents in workspace/. Keep source contradictions explicit.
- Check VERSION, release.json and the page labels for consistency. If RELEASE_MANIFEST.json is present, compare the listed sizes and SHA-256 hashes to the extracted files. Compare the ZIP checksum with a separately supplied checksum when available. Matching hashes establish integrity against that manifest, not the publisher's identity or trustworthiness.
- Preserve runtime/, workspace/tasks/, workspace/sample-backups/ and browser backups during upgrades. Browser drafts belong to the exact browser origin, including port; files alone do not back them up. Do not clear browser storage or rewrite Git history.

## 2. Inventory the prerequisites

Check before installing anything. Record versions and readiness without printing credentials or the runner token.

| Component | Required for | Check |
| --- | --- | --- |
| Python 3.11+ | Local app server | `py -3 --version`, `python --version`, or `python3 --version` |
| Modern browser | All five pages | Open the local URL after server startup |
| Harbor | Executing stage 4 checks | `harbor --version` |
| Docker with a running Linux engine | Executing stage 4 checks | `docker info` |
| Provider account/credentials | Optional model-based quality review | User configures privately; do not request secrets in chat |

For drafting/forms only, Python and a browser are sufficient. If the user requested full task-evaluation setup, also prepare Harbor and Docker. Do not replace a working installation unnecessarily. The app runner uses Python's standard library and has no app-level pip dependency list.

## 3. Install only missing prerequisites

Use the vendor's official installer, supported package source and current system requirements. Check the operating system and architecture first. Prefer non-admin, user-local installation where supported. Never disable security protections, change PowerShell execution policy, accept legal agreements, reboot, buy a subscription or configure billable services silently. Let the user handle agreements, credentials and any required administrator prompts. If a restart is needed, explain why and resume checks after the user restarts; do not restart automatically.

- Python: https://www.python.org/downloads/ and https://docs.python.org/3/using/windows.html . Install Python 3.11 or newer, reopen the terminal and check its version. Harbor may use a separately managed newer Python.
- Docker: https://docs.docker.com/get-started/get-docker/ . On Windows, follow its supported virtualization/WSL requirements. Start Docker and wait for the Linux engine to become ready. The `docker` executable being present is not proof that the engine works. Account and license requirements depend on the user's situation.
- uv, if missing: https://docs.astral.sh/uv/getting-started/installation/ . Use the official supported installation method and inspect any downloaded installer before executing it.
- Harbor: https://github.com/harbor-framework/harbor . This app's recorded execution tests used Harbor 0.24.0. For that reproducible baseline, after uv is available run:

```text
uv tool install harbor==0.24.0
harbor --version
```

uv can manage tools and their Python environments separately: https://docs.astral.sh/uv/guides/tools/ . If installation reports an incompatible interpreter, follow the package's published requirements and uv's documented interpreter-selection options. Do not silently install a different Harbor version or downgrade an existing working installation; explain compatibility differences first.

Reopen the terminal after PATH changes, then recheck `harbor --version` and `docker info`. Report network restrictions, unsupported systems or installer failures accurately; preserve logs locally without including secrets in the completion report.

## 4. Start this extracted copy

Run commands from the folder containing validation_server.py, not from the terminal's default folder. Paths below are relative to that folder; never reuse a developer's personal Python path.

Windows PowerShell, when local policy permits scripts:

```powershell
& '.\Start App.ps1' -Check
& '.\Start App.ps1'
```

The launcher detects Python, checks that an existing runner belongs to this folder, waits for startup and opens the browser. It also supports `-NoBrowser` and `-PythonPath 'C:\path\to\python.exe'`.

If script execution is restricted, keep that policy unchanged and use the direct-Python fallback:

```powershell
py -3 .\validation_server.py
```

Use `python .\validation_server.py` if that is the verified Python 3.11+ command on this computer. Keep its terminal open. On macOS/Linux, the corresponding command is:

```sh
python3 validation_server.py
```

Then open http://127.0.0.1:8765/dist/index.html . Stage 4 is http://127.0.0.1:8765/dist/validation.html . Native launcher testing was on Windows; do not claim other platforms were tested on the user's machine until you check them.

If port 8765 is occupied, identify the service; do not kill an unrelated process. Reuse only this folder's runner, or select a free port with TASK_AUTHOR_PORT before startup and tell the user the resulting URL. Do not expose the server beyond loopback, open firewall access, or set up public hosting as part of this installation.

## 5. Verify installation, without evaluating a task automatically

- Confirm the server responds, and that `/api/status` reports this folder's workspace/tasks path. Do not print or share its token.
- Open all five pages: `/dist/index.html`, `/dist/specification.html`, `/dist/bundle.html`, `/dist/validation.html`, `/dist/submission.html`. Check that they load with the package's version and that the browser has no installation-related errors.
- For full setup, confirm stage 4 detects Harbor, Docker and a ready engine. A fresh package normally has no tasks and no run history; do not fabricate sample data or results to fill it.
- If a Docker smoke test is needed within the user's authorized installation scope, `docker run --rm hello-world` can verify image download and execution. It downloads a public test image and is separate from project evaluation. Do not label it an oracle, scientific or AfterQuery pass.
- Do not execute uploaded task code, start model-based review, transmit task contents to a provider, or incur provider charges merely to finish installation. Task evaluation requires the user's authorization and the app's rule/consent checks. Read task code before running it.
- A previous sample-only exception for Harbor's network-control helper is not a blanket exception for another user's task or a real submission. Explain any conflicting setup and obtain that user's explicit permission before dependent execution. Keep verifier network isolation intact.
- Do not mark form declarations, originality, scientific correctness, frontier difficulty or external acceptance as passed based on installation checks.

## 6. Finish with a clear handoff

Tell the user the installation folder, app version, local launch command, browser URL, prerequisite versions and which checks actually passed. List remaining user actions separately, such as administrator approval, restart, Docker startup or private provider configuration. Explain how to reopen the app and preserve backups. If access or a prerequisite is blocked, say exactly what remains unavailable; do not report a partial setup as fully ready.

The app is local, single-workspace software. It does not upload tasks to AfterQuery, guarantee approval, host a shared evaluation service, or automatically supply model accounts. Follow README.md for operating limits and PUBLICATION.md for distribution details.
