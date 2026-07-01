# Reference Scanner Build

Backlog: [[docs/backlog/153-kernel-build-reference-scanner]]
Design docs: [[docs/backlog/153-kernel-build-reference-scanner/scanner-loop]], [[docs/backlog/153-kernel-build-reference-scanner/pull-model]], [[docs/backlog/153-kernel-build-reference-scanner/build-command-integration]], [[docs/backlog/153-kernel-build-reference-scanner/state-schema]], [[docs/backlog/153-kernel-build-reference-scanner/design-decisions]]

## Tasks

| # | Task | Type | Depends |
|---|------|------|---------|
| 001 | [[001-build-scanner-core]] | BUILD | none |
| 002 | [[002-build-pull-model]] | BUILD | 001 |
| 003 | [[003-build-state-schema]] | BUILD | 001 |
| 004 | [[004-build-command-integration]] | BUILD | 002, 003 |
| 005 | [[005-test-scanner]] | TEST | 004 |
