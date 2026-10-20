# Automated installation reference

Installation procedures for Frontier AI Task Studio on a local computer. The application consists of browser pages and a loopback Python server. Harbor and Docker provide optional task execution; a hosted evaluation service is not included.

Automation requires local filesystem and command access. Interactive approval remains necessary for administrator prompts, software agreements, restarts and account configuration. Installation does not authorize task execution, provider transmission or billable model calls.

## Package preparation

1. Inspect the archive before extraction. Archive paths must remain inside the selected installation directory. Review unexpected executable files before running them.
2. Extract the complete package into a normal application directory. Keep relative paths intact. Avoid system directories and preserve any existing installation and its data.
3. Read README.md and LICENSE.txt. Task-authoring work also depends on AGENTS.md, PROJECT_RULES.md and the original documents in workspace/.
4. Check VERSION, release.json and the page version labels. Verify the extracted files against RELEASE_MANIFEST.json and compare the archive with a separately supplied SHA-256 checksum when available. Matching hashes verify consistency with the supplied manifest; they do not authenticate the publisher.
5. Preserve runtime/, workspace/tasks/, workspace/sample-backups/ and exported browser backups during upgrades. Browser drafts belong to a browser origin, including its port. Copying application files does not back them up.

The code is rights reserved. Installation documentation does not grant additional reuse rights or change third-party terms.

## Prerequisites

| Component | Purpose | Verification |
| --- | --- | --- |
| Python 3.11+ | Local application server | `py -3 --version`, `python --version`, or `python3 --version` |
| Modern browser | Workflow pages | Open the local application URL |
| Harbor | Stage 4 execution | `harbor --version` |
| Running Docker Linux engine | Stage 4 containers | `docker info` |
| Supported provider account | Optional model-based quality review | Configure credentials privately before separately authorizing review |

Python and a browser are sufficient for the local forms. Full execution setup additionally requires Harbor and Docker. The application server uses only the Python standard library. Preserve compatible existing installations rather than reinstalling them unnecessarily.

## Dependency installation

Check operating-system and architecture compatibility against current vendor requirements. Install missing dependencies from official sources:

- [Python downloads](https://www.python.org/downloads/) and [Windows setup](https://docs.python.org/3/using/windows.html).
- [Docker installation](https://docs.docker.com/get-started/get-docker/), including the applicable virtualization and WSL requirements on Windows.
- [uv installation](https://docs.astral.sh/uv/getting-started/installation/) and [tool management](https://docs.astral.sh/uv/guides/tools/).
- [Harbor installation](https://github.com/harbor-framework/harbor).

The recorded execution baseline is Harbor 0.24.0. With uv available:

```text
uv tool install harbor==0.24.0
harbor --version
```

Harbor may require a newer, separately managed Python interpreter than the application server. Follow the package requirements and uv's interpreter-selection documentation when needed. Review compatibility before changing an existing Harbor version.

Prefer user-local installation where supported. Keep security protections and execution policy intact. Software agreements, administrator prompts and credentials require interactive handling. Schedule any required restart explicitly; do not restart automatically. Reopen the terminal after PATH changes, start Docker and confirm `docker info` succeeds. An installed Docker executable alone does not establish engine readiness.

## Startup

Run startup commands from the directory containing validation_server.py.

On Windows, where script policy permits:

```powershell
& '.\Start App.ps1' -Check
& '.\Start App.ps1'
```

The launcher detects Python, checks the existing runner's application directory, waits for readiness and opens the validation page. Optional arguments:

- `-PythonPath 'C:\path\to\python.exe'`: select a specific interpreter.
- `-NoBrowser`: start without opening a browser.
- `-Check`: check Python without starting the server.

When PowerShell scripts are restricted, retain the policy and use Python directly:

```powershell
py -3 .\validation_server.py
```

Use `python .\validation_server.py` if that is the verified Python 3.11+ command. Keep the server terminal open. On macOS/Linux:

```sh
python3 validation_server.py
```

Default application URL: http://127.0.0.1:8765/dist/index.html . Validation URL: http://127.0.0.1:8765/dist/validation.html . Windows startup has been tested; independent macOS/Linux verification remains pending.

If the port is occupied, identify the service before taking action. Reuse only a runner serving the intended installation. TASK_AUTHOR_PORT can select another free port before startup. Changing the port changes the browser origin and access to existing drafts. Keep the server on loopback; public hosting and firewall exposure are outside installation scope.

## Installation verification

Installation is verified when:

- The server responds and `/api/status` reports the installation's workspace/tasks path. Do not expose the response token in logs or reports.
- All five pages load: index.html, specification.html, bundle.html, validation.html and submission.html under `/dist/`.
- The page labels match the package version and no installation-related browser errors appear.
- For execution setup, stage 4 detects Harbor, Docker and a ready engine.

A fresh installation normally contains no task data or visible run history. No sample output needs to be invented or imported to complete installation. If authorized for the installation check, `docker run --rm hello-world` verifies a public image download and container execution. It is not a task-validation result.

Uploaded task code requires a separate execution decision and rule review. Model review also requires separate provider-transmission consent. A previous sample-only exception does not apply to a different task or a real submission. Preserve verifier network isolation and resolve rule conflicts before dependent execution.

## Installation record and handoff

Record the application directory and version, launch command, local URL, dependency versions, completed checks and unresolved failures. List required interactive actions separately. Exclude credentials and the runner token from the record. Include reopening and backup instructions from README.md.

Installation checks establish local readiness, not scientific validity, originality, frontier difficulty or AfterQuery acceptance. External submission and approval remain separate processes. Operating limits are documented in README.md; distribution terms are documented in LICENSE.txt and PUBLICATION.md.
