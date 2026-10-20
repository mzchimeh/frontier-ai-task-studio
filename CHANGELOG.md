# Changelog

All released software changes are recorded here using Semantic Versioning. Release dates use the user's local calendar date. Released entries and archives are preserved; corrections go into a later release.

## Unreleased

No changes recorded yet.

## 1.0.6 — 2026-10-20

### Documentation

- Rewrote the README, automated installation reference and distribution policy as standalone technical documentation. Removed conversational instructions, authoring-session narratives and publication-preparation statements that no longer described the published project.
- Retained installation commands, workflow constraints, rights notices, verification limits and task-authorship requirements. Added documentation-style and standard-workflow requirements to AGENTS.md.
- Preserved application logic, architecture comments, storage formats, source documents, runtime data and existing releases.

### Verification

- Checked local Markdown links, required setup commands, editorial patterns and version consistency.
- Confirmed all application scripts and original source documents remain byte-identical to v1.0.5. Verified the new ZIP against its SHA-256 manifest and preserved the prior archive unchanged. No task evaluations or dependency installations were performed for this documentation correction.


## 1.0.5 — 2026-10-19

### Documentation

- Added INSTALL_FOR_AGENTS.md with prerequisite discovery, official installation sources, safe extraction/upgrades, local startup, verification, failure handling and user handoff.
- Linked the guide from README.md and AGENTS.md. It distinguishes installation from task execution and model-provider review, and preserves user approval, restart, credential and agreement requirements.
- No application behavior, storage schema, runner, source documents, task files or existing release archives changed.

### Verification

- Checked guide commands against the shipped launcher/server and current official Harbor, uv and Docker documentation; the Python detection check passed.
- Verified unchanged application scripts and source documents against v1.0.4, consistent version labels and metadata, and the new ZIP's CRC and SHA-256 manifest. No prerequisites were reinstalled or evaluation jobs started for this documentation update.


## 1.0.4 — 2026-10-19

### Fixed

- Removed the machine-specific Python path from the Windows launcher; added interpreter detection, explicit interpreter selection, readiness checks, and wrong-folder detection.
- Documented setup, portable server startup, current verification limits, public packaging restrictions and private document handling.
- Restored Git exclusion/line-ending files and excluded sample backups/publication output. Existing data and history remain untouched.

### Verification

- Passed fresh-folder Windows smoke tests for Python detection/override, missing-interpreter errors, startup with a path containing spaces, all five page loads, empty task discovery, existing-server reuse, wrong-folder rejection and direct-Python fallback. PowerShell 7 launcher execution passed; Windows PowerShell 5.1 script execution was blocked by existing host policy, which was not changed.
- Verified authorized source documents and validation runner remain byte-identical; prior releases and local drafts/data preserved.
- Audited the allowlisted source package for excluded runtime/credential/task data, personal machine paths and common secret patterns; verified ZIP CRC and SHA-256 manifest. This is not a full Git-history secret audit or an independent second-computer test.

### Publication decisions

- Owner retained all rights to application code; no open-source/reuse license was granted.
- Owner confirmed redistribution permission for both unchanged source documents.
- No GitHub upload, commit, push, Git-history rewrite or credential configuration performed.

## 1.0.3 — 2026-10-19

### Fixed

- Validation review now distinguishes an explicitly recorded, task-scoped sample-only exception from an unresolved conflict. Approval never marks a check passed or establishes external acceptance.
- Preserved existing notes, storage keys, backup schema, runtime evidence, runner behavior and all unrelated functionality. Older backups default to unresolved.

### Verification

- Passed focused tests for approved versus unresolved status, task scoping, real-task rejection, missing approvals, and old/new backup restoration.
- Verified the page preserves saved notes and shows the authorized sample exception without the incorrect stop message. Pending checks remain pending.
- Source documents, runner, task data and prior evidence remain unchanged. Runner session history is session-only, as before; this fix does not add persistence.

## 1.0.2 — 2026-10-18

### Changed

- Renamed the application to Frontier AI Task Studio in all five screen titles/headers, current documentation, release metadata, and startup message.
- Preserved storage keys, backup formats, runner API, mandatory rules, and existing releases. No data migration required.

### Verification

- Checked all five name/version labels and verified behavior scripts and original documents unchanged from v1.0.1.
- Python runner compilation and ZIP checksum/manifest verification passed. Existing end-to-end testing limitations remain documented below.

## 1.0.1 — 2026-10-18

### Changed

- Renamed the application from Task Author to Frontier Task Studio across all five screen headers/titles, current documentation, release metadata, and runner startup message.
- Preserved existing folder paths, storage keys, backup schemas, and runner API for compatibility. No data migration or draft reset.
- Preserved v1.0.0 unchanged. All earlier verification limits remain in force.

### Verification

- Confirmed all five screens use the new name and v1.0.1 label.
- Verified behavior scripts and original source documents are byte-identical to v1.0.0; branding-only runner change compiles.

## 1.0.0 — 2026-10-18

### Added

- Five-stage local workflow: idea/eligibility, specification, bundle preparation, validation, and submission/payment tracking.
- Source document preservation and mandatory rule register, with unresolved source contradictions shown explicitly.
- Browser drafts, stage-specific JSON backups, metadata preparation, ZIP export, and selected structural checks.
- Loopback-only Harbor runner with fixed commands, prerequisite checks, task snapshots, fingerprints, logs, and evidence records.
- Self-reported review gate history, revision checks, and fixed $300 approval/payment tracking.
- Version identity, release manifest, archive checksum, and software versioning policy.

### Verification

- JavaScript syntax checks and Python compilation completed during development.
- Automated checks exercised bundle metadata, ZIP integrity, path boundaries, runtime evidence collection, approval/payment conditions, and revision/conflict rules.
- Browser checks covered screen rendering, incomplete forms, conflict feedback, missing prerequisites, and premature approval rejection.

### Known limitations

- Harbor and Docker were not available on the development command path. Real Harbor runs and provider quality review remain unverified.
- Browser-native folder selection, ZIP download, and backup import/export still need end-to-end testing.
- No external platform integration: no task has been submitted, approved, or paid through this app.
- Local runner has no in-app process/container cancellation manager. Keep it running until checks finish.
- Browser drafts depend on browser/origin. Runtime run history is session-based; export evidence and all relevant stage backups.
- Static checks do not certify all source rules, scientific correctness, originality, sealed boundaries, or cheating resistance.
- The source documents disagree on difficulty lower bounds and mention multi-container examples despite explicit single-container requirements. These contradictions are unresolved.

This version identifies the saved baseline; it is not a certification of complete verification or project acceptance.
