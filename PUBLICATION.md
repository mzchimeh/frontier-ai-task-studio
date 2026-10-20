# Distribution policy

## Application rights

Application code is rights reserved under LICENSE.txt. No open-source or general reuse license is granted. Availability for download does not extend those permissions. Public repositories remain subject to [GitHub's viewing and forking terms](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/licensing-a-repository).

## Third-party documents

Authoring tasks.docx and Project Summit.pdf are distributed unchanged with permission confirmed for this project on 2026-10-19. Their ownership and applicable terms remain separate from the application code. Inclusion does not grant permission to relicense the documents.

## Release contents

Release packages contain application code, setup and version documentation, the rights notice, the rule register, original source documents and a SHA-256 file manifest.

The following are excluded:

- Git metadata and previous release snapshots.
- runtime/, workspace/tasks/ and workspace/sample-backups/.
- Browser backups, credentials and virtual environments.
- Generated publication output and local working data.

Local data remains in the installation directory and browser storage. The release archive is not a backup of that data.

## Repository and release workflow

Use the existing repository for normal review, staging, commit, push, tag and release operations. Review staged files and any relevant Git history before publication. .gitignore excludes matching untracked files; it does not remove tracked files or historical content.

Publish only verified release assets. Keep existing release archives unchanged and issue corrections under a new version. Match release metadata, visible page versions, the manifest and the ZIP checksum. GitHub source hosting does not provide the application's Python or Docker execution service.

## Installation and verification limits

Installation requires Python 3.11+. Executing checks additionally requires Harbor and a running Docker Linux engine. Provider-based quality review requires a separately configured account and explicit transmission consent and may incur charges. No credentials or private task data are included in the release.

Fresh-folder startup checks were performed on Windows, including a path containing spaces. This does not certify operation on an independent second computer, macOS or Linux. Package scans check an allowlisted file set for common credential patterns and personal machine paths; they are not exhaustive security guarantees for arbitrary repository history.

Task-validation results do not establish external acceptance. Version history and verification details are recorded in CHANGELOG.md. Setup instructions are in README.md and INSTALL_FOR_AGENTS.md.
