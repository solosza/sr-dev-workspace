# Kernel Minimalize Standalone Repo

Backlog: [[docs/backlog/156-kernel-refactor-minimalize-standalone-repo]]
Reference: [[docs/backlog/150-kernel-refactor-minimalize-kernel]]

## Tasks

| # | Task | Type | Depends |
|---|------|------|---------|
| 001 | [[001-build-create-repo]] | BUILD | none |
| 002 | [[002-build-strip-commands]] | BUILD | 001 |
| 003 | [[003-build-strip-skills]] | BUILD | 001 |
| 004 | [[004-build-strip-root-dirs]] | BUILD | 001 |
| 005 | [[005-build-strip-lib]] | BUILD | 001 |
| 006 | [[006-build-clean-lessons]] | BUILD | 001 |
| 007 | [[007-build-update-claudemd]] | BUILD | 002, 003 |
| 008 | [[008-build-readme-and-freeze]] | BUILD | 007 |
| 009 | [[009-test-validate-loop]] | TEST | 007, 008 |
