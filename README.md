# Frontier AI Task Studio

A local application for preparing, validating and tracking expert-authored AI-agent benchmark tasks through a five-stage workflow.

Current release: **v1.0.6 — 2026-10-20**. Application code is rights reserved; see [LICENSE.txt](LICENSE.txt). Release packages exclude private tasks, runtime logs, credentials and browser backups.

## Requirements and startup

The local server requires Python 3.11+ and a modern browser. Task execution additionally requires Harbor and a running Docker Linux engine. Model-based quality review requires a separately configured provider account and explicit transmission consent; charges may apply. The server uses the Python standard library and does not install dependencies or configure accounts automatically.

Extract the package and open a terminal in the directory containing validation_server.py. On Windows, where script policy permits:

```powershell
& '.\Start App.ps1'
```

The launcher detects Python, verifies that an existing runner serves the intended directory, waits for readiness and opens the validation page. `-Check` verifies Python without starting the server. `-NoBrowser` suppresses browser startup. `-PythonPath 'C:\path\to\python.exe'` selects an interpreter explicitly.

If PowerShell scripts are restricted, retain the policy and start the server directly:

```powershell
py -3 .\validation_server.py
```

Use `python` if that is the installed Python 3.11+ command. On macOS/Linux, use `python3 validation_server.py`. Keep the server terminal open. Windows startup has been tested; independent macOS/Linux verification remains pending.

Open http://127.0.0.1:8765/dist/index.html . For form drafting without execution, dist/index.html can also be opened directly, although local-file browser storage varies. Use a consistent browser and origin and export backups regularly.

Detailed prerequisite installation and verification are documented in [INSTALL_FOR_AGENTS.md](INSTALL_FOR_AGENTS.md). Official sources: [Python](https://www.python.org/downloads/), [Docker](https://docs.docker.com/get-started/get-docker/), [Harbor](https://github.com/harbor-framework/harbor) and [uv](https://docs.astral.sh/uv/getting-started/installation/). The recorded Harbor baseline is 0.24.0; with uv installed, `uv tool install harbor==0.24.0` installs that version. Reopen the terminal after PATH changes, start Docker and verify `harbor --version` and `docker info` before execution.

## Workflow

### 1. Idea and eligibility

Record the research context, relevant expertise, problem, deliverables, difficulty, originality, data provenance, independent ground truth and verification approach. Complete the author declarations and review any conflicts. The idea check reports incomplete fields and declarations; it does not establish scientific validity or external approval. An optional rate estimate uses the entered authoring hours.

The page saves one draft and supports versioned JSON export/import. The original idea-only backup format remains supported on this page.

### 2. Specification

Define task identity, absolute artifact paths, acceptance criteria, ground-truth evidence, numerical tolerances, reproducibility, resources, timings and environment plans. Enter personally authored task instructions. The application does not generate or rewrite submission instruction prose.

Checks cover required declarations, slug/resource constraints, output paths, instruction formatting and the exact timeout suffix. Recorded conflicts, missing measurements and source contradictions remain explicit. Paths containing whitespace are not supported by the current artifact-path checks; this is an application limit rather than an additional source rule.

Stage 2 reads the idea draft without changing it, saves a separate specification draft and exports/imports a workspace JSON containing stages 1 and 2.

### 3. Bundle preparation and ZIP export

Complete author metadata, tags, the solution explanation and README. The page reads stages 1 and 2 and previews schema 1.4 task.toml. Select the prepared task folder and review structural/file-conflict feedback before exporting the preparation ZIP.

Required task files must be at the ZIP root. The export includes the saved instruction text unchanged. Imported instruction.md, task.toml or README.md that conflicts with the saved/editor content blocks export rather than being silently replaced. Allowed binary files and optional authoring/ evidence are preserved. Folder selection is memory-only and must be repeated after reload. The folder-size limit is 100 MB.

Stage 3 metadata has a separate bundle-metadata.json backup and is not part of stage 2's workspace export. The ZIP is created locally; no hosted upload occurs. Export alone does not establish submission readiness.

### 4. Validation

Extract the preparation ZIP into workspace/tasks/&lt;task-slug&gt;/, with required files directly inside that directory. Open the validation page through the local server, refresh tool/task discovery, select the task and review the execution consent before starting a check.

Reference-solution checks expect reward 1; no-operation checks expect reward 0. Repeat checks on an unchanged bundle and inspect the evidence. Quality review requires an additional provider-transmission acknowledgement and manual review of its findings.

Each run uses a task snapshot under runtime/&lt;run-id&gt;/task and records its fingerprint, command output, reward files, CTRF-shaped reports and source-change status. An expected-reward observation requires successful process completion, exactly one matching reward file and a report; it does not certify verifier coverage or scientific correctness. Command duration includes container/harness overhead and is not a measured solution runtime.

Manual review notes and declarations remain self-reported. A documented sample-only exception can be recorded for its exact -sm task; it does not approve a different task, a real submission or any pending check. Existing notes without explicit approval remain unresolved. Run summaries count records by task name; compare fingerprints before relying on repeated results.

Runs are sequential. This release has no in-app cancellation manager. Keep the runner open during a check and use Harbor/Docker management tools when necessary. Runtime files persist on disk, but visible run history belongs to the server session. Export validation-evidence.json before ending a session. Import restores review notes; imported run claims do not become runner-observed results.

### 5. Submission and payment tracking

Record submission identity/revision, the ZIP checksum, the separate runner bundle fingerprint, platform gate states, human review, rejection reasons and payment references. External states are self-reported. The application has no AfterQuery connection and does not submit tasks or verify external approval.

Appending a status record saves a local history snapshot. Approval entries require a submitted state, reported passing gates, an approval date and an evidence reference. Received-payment entries also require a payment date and reference. The recorded payout is $300 USD per approved task; no payment deadline is inferred.

A different ZIP requires a documented revision. Identical hashes under another task/revision are blocked as duplicate records; changed hashes do not prove originality. Infrastructure failures remain distinct from task failures. Tracker export/import uses submission-tracker.json, preserves existing valid history and treats imported statuses as unverified reports. Recorded conflicts prevent a clean status entry pending resolution.

## Data, security and operating limits

- Browser drafts belong to the exact origin, including port. Export each stage's relevant backup before changing browsers, ports or opening methods. Stage backups and runtime files are separate.
- The default port is 8765. TASK_AUTHOR_PORT can select another free port before startup. Do not stop an unrelated service to free the port.
- The runner listens on loopback, validates Host/Origin and requires an in-memory token for execution requests. Task folders must remain inside workspace/tasks/. Symlinks and selected structural conflicts are rejected; task contents and runtime snapshots are not served as static files.
- Structural checks are intentionally limited. They do not certify every dependency pin, sealed boundary, numerical tolerance, originality claim or task requirement.
- Edited task files do not automatically synchronize earlier form drafts. Keep the specification, selected files and tested fingerprint consistent.
- GitHub hosts source and release downloads, not the Python/Docker execution service. Hosted multi-user evaluation is not implemented.

## Requirements, verification and distribution

[PROJECT_RULES.md](PROJECT_RULES.md) summarizes the source requirements. The original documents in workspace/ remain authoritative and are distributed unchanged with permission. Source contradictions, including the eight-attempt lower solve bound, remain unresolved. A complete form or local pass does not establish AfterQuery acceptance.

Recorded checks include Windows fresh-folder startup, five-page loading, structural validation, selected invalid-input paths, ZIP integrity and repeated actual Harbor results for a synthetic example: oracle 1,1 and no-operation 0,0 on an unchanged fingerprint. Model-based quality review, external originality/authorship checks and frontier difficulty have not been established. Some browser import/export paths still require end-to-end coverage. Detailed verification history is in [CHANGELOG.md](CHANGELOG.md).

Release archives and manifests follow [VERSIONING.md](VERSIONING.md). Distribution contents, exclusions and third-party terms are documented in [PUBLICATION.md](PUBLICATION.md). No general code reuse license is granted by the package.
