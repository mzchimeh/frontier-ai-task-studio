# GitHub publication preparation

Nothing has been uploaded, published or pushed by this preparation.

## Decisions recorded — 2026-10-19

The project owner selected **rights reserved** for the application code; see LICENSE.txt. Do not describe this project as open source or imply a general reuse license. Technical ability to run the app is separate from permission to reuse its code. Public GitHub repositories are subject to GitHub's viewing/forking terms: https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/licensing-a-repository

The project owner confirmed permission to redistribute Authoring tasks.docx and Project Summit.pdf. They are included unchanged in the reviewed source package. This records the owner's confirmation; it does not transfer ownership or extend downstream rights beyond the documents' applicable terms.

## Files intended for publication

The reviewed source archive includes app code, setup/version documentation, rights notice, the rule register, original source documents and a SHA-256 file manifest. It excludes .git history, runtime/, workspace/tasks/, workspace/sample-backups/, release snapshots, virtual environments, credentials, browser backups and generated publication output. Local data is retained on your computer.

Use the reviewed source ZIP for a clean upload or new repository. Do not upload the entire working folder. .gitignore does not remove files already tracked or in Git history. Existing history was not rewritten, committed or pushed by this preparation. If publishing that history instead, review it separately for private data and credentials first.

## Run after downloading

Extract the ZIP into a normal folder and follow README.md. The local app needs Python 3.11+; executing checks additionally needs Harbor and a running Docker engine. Install prerequisites separately from their official sources. Provider review requires your own account and explicit acknowledgement and may incur charges. No credentials or task data are provided by the archive.

PowerShell scripts may be restricted by local policy. Follow that policy; use the direct Python command in README.md instead of weakening it. GitHub Pages cannot host the Python/Docker runner. Keep the runner on loopback; this release does not offer hosted multi-user accounts or shared storage.

## Verification limits

Fresh-folder testing is performed on this Windows machine, with a path containing spaces. It is not an independent second-computer, macOS, or Linux certification. The publication scan checks the allowlisted package for common secret formats and personal machine paths; it is not a proof that arbitrary repository history is free of secrets. The actual sample's earlier Harbor results do not establish external task acceptance. Read CHANGELOG.md for the checks completed for this release.
