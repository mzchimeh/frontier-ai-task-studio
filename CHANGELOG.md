# Changelog

All released software changes are recorded here using Semantic Versioning. Release dates use the user's local calendar date. Released entries and archives are preserved; corrections go into a later release.

## Unreleased

No changes recorded yet.

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
