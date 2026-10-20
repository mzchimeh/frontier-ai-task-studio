# Frontier AI Task Studio

Saved software release: **v1.0.5 — 2026-10-19**. See CHANGELOG.md for release history and known limitations, and VERSIONING.md for all future corrections and releases. The versioned release archive excludes runtime data and browser drafts; export your stage backups separately.

For form drafting only, open dist/index.html in a browser. For the full workflow, start the local Python runner as described below. Use the same browser and origin for consistent draft storage and export JSON backups regularly. Browser storage behavior for local files varies.

For ChatGPT/Codex-assisted setup, ask the agent to read [INSTALL_FOR_AGENTS.md](INSTALL_FOR_AGENTS.md) and follow it on your computer. This requires file and command access; ordinary chat alone cannot install the app.

## Local runner for stage 4

The application runner needs Python 3.11 or newer and uses only the Python standard library. Harbor and Docker are needed only for executing stage 4 checks. Install them separately; the application never installs software or configures credentials automatically.

On Windows, install [Python](https://www.python.org/downloads/windows/), reopen PowerShell in the extracted project folder, and run:

```powershell
& '.\Start App.ps1'
```

The launcher tries `py -3`, `python`, and `python3`, checks the interpreter version, starts the loopback server, waits for it to respond, and opens the validation page. It uses this folder's files, including when its path contains spaces. If script execution is restricted, follow your organization's policy or run Python directly; the project does not require changing execution policy:

```powershell
py -3 .\validation_server.py
```

Keep that terminal open and visit http://127.0.0.1:8765/dist/index.html. Alternatively use `python` if `py` is unavailable. To select an interpreter explicitly, use `& '.\Start App.ps1' -PythonPath 'C:\path\to\python.exe'`. `-Check` checks Python without starting anything; `-NoBrowser` starts the runner without opening a browser. A runner already serving another folder is not silently reused.

On macOS or Linux, run `python3 validation_server.py` from the project folder and open the same local URL. The Python server is portable, but this release's native browser and Docker/Harbor validation have only been exercised on Windows; macOS/Linux execution is not certified.

For execution checks, install [Docker](https://docs.docker.com/get-started/get-docker/) and start its engine, then follow [Harbor's official installation instructions](https://github.com/harbor-framework/harbor). This project was tested with Harbor 0.24.0; a reproducible install is `uv tool install harbor==0.24.0` after installing [uv](https://docs.astral.sh/uv/getting-started/installation/). Harbor may manage a newer Python separately from the app runner. Reopen PowerShell after installation so the tools are available on PATH. Verify `harbor --version` and `docker info`, then use Refresh tools and tasks. Provider review requires your own supported account/credentials and an explicit transmission acknowledgement; charges may apply.

Default port: 8765. Set `TASK_AUTHOR_PORT` before startup only if needed, and use the resulting URL. Browser drafts belong to the exact origin (including port); export backups before changing it. Store shutdown/startup diagnostics under runtime/. Stop or manage checks with Harbor/Docker; the app has no process cancellation manager.

Extract each stage 3 ZIP to workspace/tasks/<task-slug>/ so the required files sit directly inside that directory. Refresh tools and tasks, choose the folder, review the rules, and explicitly start an oracle, nop, or quality check. Quality review requires an additional provider-transmission acknowledgement. The runner invokes only the documented fixed Harbor commands, without a shell. It copies the task to runtime/<run-id>/task, hashes the copy, runs from a separate directory, and collects process logs, binary reward files, CTRF-shaped JSON reports, and source-change information. It does not execute tasks automatically on selection or page load.

Runs are sequential. Do not close the runner during a check: this version has no process/container cancellation manager, and closing the app may leave Harbor/container processes active. Review logs and use Harbor/Docker's own management tools if necessary. Total command elapsed time includes build/harness overhead and is not a measured solution runtime.

The runner listens only on 127.0.0.1, checks Host and Origin, and requires an in-memory token for execution requests. It accepts task folders only inside workspace/tasks/, rejects symlinks and obvious structural conflicts, and does not serve task contents or runtime snapshots as static files. The logs/evidence API is intended for this local workspace. The preflight is a limited structural scan, not full rule certification; declarations and manual review still matter.

Stage 1 captures research context, expertise, problem and deliverables, difficulty, originality, provenance, independent ground truth, verification feasibility, and author declarations. It saves one draft, imports/exports versioned JSON, reports missing fields and declared conflicts, and provides an optional rate estimate based on authoring hours.

Stage 2 is available from the Specification link, or dist/specification.html. It captures identity, artifact paths, acceptance criteria, independent ground truth, numerical tolerances, reproducibility, resource/timing limits, environment plans, and personally authored instruction text. It reads the stage 1 draft without changing it. Use the same browser and origin for both pages. Stage 2 has a separate saved draft and a workspace JSON export/import containing both stages; stage 1's older idea-only export remains supported on its original page.

Stage 2 checks required declarations, slug format, resource limits, absolute artifact paths and duplicates, presence of each output path in instructions, Markdown headings/lists, and the exact source-prescribed ending. It flags proposed exceptions, stage 1 ground truth conflicts, missing measurements and pending external review. It never generates or rewrites author instruction prose. No solve-band threshold is chosen. Paths are conservatively restricted to file paths without whitespace for this app; this is an application limitation, not an additional source rule.

Stage 3 is available at dist/bundle.html. It collects remaining author metadata, tags, solution explanation, and a README; reads the saved stage 1/2 drafts; previews schema 1.4 task.toml; selects a local folder; checks required files, approved roots, unsafe paths, selected source policies and conflicts; and exports an uncompressed preparation ZIP with files at its root. Personally written instructions are copied unchanged from stage 2. Imported instruction.md, task.toml, or README.md that differ from saved/editor content block export rather than being silently replaced. Optional authoring/ evidence and binary files are preserved.

Folder files are memory-only and must be reselected after reload. Stage 3 metadata is saved separately and can be exported/imported as bundle-metadata.json; it is not included in stage 2's older workspace export. Back up both. The application limits folder size to 100 MB; this is an app limitation, not a source requirement. No hosted upload occurs.

Stage 4 is available at dist/validation.html. It offers prerequisite checks, task selection, local execution through the runner, evidence display/export, and saved manual review notes. Expected reward observations require exit code zero, exactly one reward with the expected value, and a CTRF-shaped report; this does not prove report completeness, coverage, or scientific correctness. Quality output always requires manual review. Imported notes never count as runner-observed results. Metadata/history backups from earlier stages remain separate from validation-evidence.json. Runtime files persist on disk, while visible run history belongs to the current server session.

Stage 5 is available at dist/submission.html. It records submission identity and revision, the selected ZIP's local SHA-256 checksum, the separate runner bundle fingerprint, eight automated gate states, human review, rejection reasons, approval references and payment evidence. All external statuses are explicitly self-reported. The app has no project-platform connection and never submits or verifies a task externally. ZIP hash calculation does not establish originality or archive structure. A different archive can still be a prohibited near-duplicate.

Drafts autosave; Append status record adds a snapshot to local history. Approval records require submitted state, all automated gates reported passed, approval date and evidence reference. Received payment needs approval plus payment date and reference. Amount is fixed at $300 USD per approved task, with no invented due date. Infrastructure failures remain distinct from task failures. A changed ZIP requires a new revision, and an identical hash recorded under another task/revision blocks a duplicate submission record. Substantive revision changes must be documented; all pipeline gates must run again on the platform.

Export tracker backup preserves the current draft and history in submission-tracker.json. Import merges valid history records by ID, preserves existing records, and loads the imported draft. Imported records remain unverified self-reports. Earlier-stage backups and validation evidence remain separate; export each relevant file when moving browsers or origins. A known conflict blocks appending a clean status record and requires discussion and user permission before any conflicting action. Draft conflict notes can still be retained/exported.

PROJECT_RULES.md records the mandatory requirements for the local AfterQuery workflow. The unchanged source documents are in workspace/ and included with the project owner’s confirmed redistribution permission. They remain subject to their own rights and terms. All five workflow screens are implemented. No AI instruction generation or external submission occurs. Stage 4 runs task code only after explicit run actions. A complete form does not establish acceptance or scientific validity. Source contradictions remain explicit. Source files and full manual review remain authoritative; static scans are intentionally limited and do not certify every pin, sealed boundary, or verifier behavior.

## Historical implementation checks

These paragraphs record earlier implementation passes, not the current installation status.

Verified in the browser: page loads, incomplete form produces missing-field/declaration feedback, reference-derived ground truth produces a rule-conflict warning, and saving/reloading restores the draft. Export/import are implemented but not exercised end to end in this pass.

Stage 2 verification: JavaScript syntax check; browser rendering and incomplete-form feedback; below-minimum agent timeout and relative artifact path rejected. Workspace import/export is implemented but not exercised end to end. Manual scientific review remains necessary.

Stage 3 verification: JavaScript syntax checks; isolated structural fixture tests for metadata, empty-tag rejection, and conflicting-file rejection; generated TOML independently parsed; ZIP CRC/binary/Unicode roundtrip verified with Python; browser rendering and incomplete-bundle export blocking checked. Native browser folder selection and final ZIP download have not been exercised end to end. No Harbor or project checks have run.

Stage 4 verification: Python compile and JavaScript syntax checks; five automated tests covering missing files, task-path boundaries, fingerprint change detection, binary reward/CTRF collection, rejection of unauthorized execution requests, and encoded runtime-file access. Browser verified connected/missing-prerequisite status, disabled run buttons, and zero-run status without false passes. Real Harbor execution, model-provider review, and end-to-end evidence download/import remain unverified because prerequisites are absent.

Stage 5 verification: JavaScript syntax checks and automated tests of draft/submission validity, approval gating, payment requirements/chronology, fixed payout amount, conflicting revisions and identical archive checks, infrastructure states, and rule-conflict blocking. Browser verified initial pending state and rejection of premature approval with no status record appended. Native ZIP selection, backup import/export, and final downloads still need end-to-end browser testing. No external submission, approval, or payment has occurred.


## Current verification and publication status

Earlier verification paragraphs above describe historical implementation passes and their limits. Subsequent Windows testing completed an executable synthetic sample: actual Harbor oracle rewards 1,1 and nop rewards 0,0 on one unchanged fingerprint, plus separate numerical/shortcut checks. Those tests do not establish AfterQuery approval or performance on other computers. Provider-based quality review and frontier difficulty remain unverified. Sample task data, personal review notes, runtime logs, credentials and release snapshots are not public source inputs.

For clean installation, publication exclusions, license decisions and private source documents, read PUBLICATION.md. GitHub source hosting does not run the Python server or Docker. This is a local application; GitHub Pages cannot provide its execution runner.

## Rights

Application code: all rights reserved; see LICENSE.txt. This is not an open-source license. The source documents and third-party tools retain their own terms. See PUBLICATION.md for the recorded decisions and package exclusions.
