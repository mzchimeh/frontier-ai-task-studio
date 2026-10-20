# Versioning and release policy

Current release: **1.0.5**, released **2026-10-19**. Original baseline: **1.0.0**.

Use Semantic Versioning: MAJOR.MINOR.PATCH.

| Change | Next release from 1.0.0 |
| --- | --- |
| Compatible bug fix, rule-check correction, security fix, or documentation correction | 1.0.1 |
| New feature that preserves existing supported behavior and data compatibility | 1.1.0 |
| Breaking change to supported behavior, stored drafts, backup formats, runner API, or required workflow | 2.0.0 |

For unreleased testing, use prerelease identifiers such as 1.0.1-rc.1. Reset PATCH on a MINOR increase, and reset MINOR and PATCH on a MAJOR increase. Use monotonically increasing releases; do not reuse a released version.

## Workflow for future changes

1. Read AGENTS.md, PROJECT_RULES.md, and the original source documents. Explain conflicts and obtain the user's permission before any conflicting work; project acceptance rules remain external requirements.
2. Modify the working app, leaving archived releases untouched. Document changes under Unreleased in CHANGELOG.md, including the problem, correction, and relevant data compatibility impact.
3. Run focused checks for the changed behavior. State what was tested and retain known verification limits; do not label pending checks as passed.
4. At release, choose the appropriate version, update VERSION and release.json, and apply the same version to every screen's visible label. Date the changelog and move the changes into the new release entry.
5. Preserve user data. A storage or backup change needs an explicit migration or backwards compatibility plan. Test upgrade and rollback behavior as relevant. Do not silently reset local drafts.
6. Create a new releases/vX.Y.Z/ snapshot, manifest, and ZIP, plus an archive checksum. Refuse to overwrite an existing release. Verify the archive against its manifest before reporting it saved.
7. Report the version, user-visible change, relevant verification, and remaining limitations.

## Release integrity and scope

VERSION is the authoritative app version. release.json repeats it for machine-readable metadata; they must agree. Changelog and screen labels must agree with both.

Released snapshots are immutable by policy. If a released file is wrong, describe the correction in a new release; do not rewrite the old release or its changelog entry. SHA-256 manifests identify the saved files and archive, but are not signed attestations.

Runtime logs, task folders, credentials, Python caches, and browser drafts are user/runtime data and are not part of a software release archive. The two unchanged project source documents and mandatory rule register are included. Export browser backups separately before an upgrade; copying an app archive does not back up browser storage.

Day-to-day status records, drafts, and task submissions do not change the software version. Public API and data-format schema versions are separate from the app release version; bump schemas only when their formats require it.
