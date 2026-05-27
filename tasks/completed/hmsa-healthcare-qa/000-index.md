# HMSA Healthcare QA Workspace — Task Index

## Goal
Build fully bootstrapped workspace at D:\my_ai_projects\project_test_repos\hmsa-healthcare-qa with kernel, domain-setup, and all 6 kernel features installed.

## Source
→ [[docs/backlog/031-domain-build-hmsa-healthcare-qa-workspace.md]]

## Tasks

| # | Task | Type | Dependencies | Status |
|---|------|------|-------------|--------|
| 001 | [[001-build-create-workspace-dir]] | BUILD | none | pending |
| 002 | [[002-build-git-init]] | BUILD | 001 | pending |
| 003 | [[003-build-copy-kernel]] | BUILD | 001 | pending |
| 004 | [[004-build-copy-claude-md]] | BUILD | 001 | pending |
| 005 | [[005-build-copy-run-task-scripts]] | BUILD | 001 | pending |
| 006 | [[006-build-copy-spec]] | BUILD | 001 | pending |
| 007 | [[007-build-initial-commit]] | BUILD | 002-006 | pending |
| 008 | [[008-build-run-domain-setup]] | BUILD | 007 | pending |
| 009 | [[009-test-validate-domain-setup]] | TEST | 008 | pending |
| 010 | [[010-build-copy-lessons-package]] | BUILD | 007 | pending |
| 011 | [[011-build-copy-delegation-package]] | BUILD | 007 | pending |
| 012 | [[012-build-copy-scanner-package]] | BUILD | 007 | pending |
| 013 | [[013-build-copy-test-packages]] | BUILD | 010-012 | pending |
| 014 | [[014-build-copy-research-docs]] | BUILD | 007 | pending |
| 015 | [[015-build-copy-updated-commands]] | BUILD | 007 | pending |
| 016 | [[016-test-run-all-tests]] | TEST | 010-015 | pending |
| 017 | [[017-test-verify-features]] | TEST | 016 | pending |
| 018 | [[018-build-commit-features]] | BUILD | 017 | pending |

## Gate Contract
→ [[gate-contract.md]]

## Deliverables
- Workspace at D:\my_ai_projects\project_test_repos\hmsa-healthcare-qa
- Kernel domain-setup complete (protocol, hooks, state)
- All 6 kernel features installed (lessons, delegation, scanner)
- All tests passing
- Everything committed
