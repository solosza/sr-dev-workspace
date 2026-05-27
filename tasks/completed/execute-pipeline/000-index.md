# Execute Pipeline — Task Index

## Goal
Build `/kernel/execute-pipeline` command + skill that chains backlog → task-builder → run-task.sh autonomously.

## Tasks

| # | Task | Type | Dependencies | Status |
|---|------|------|-------------|--------|
| 001 | [[001-build-edit-step07-flag]] | BUILD | none | pending |
| 002 | [[002-build-edit-step09-flag]] | BUILD | none | pending |
| 003 | [[003-build-create-skill-dirs]] | BUILD | none | pending |
| 004 | [[004-build-write-skill-md]] | BUILD | 003 | pending |
| 005 | [[005-build-write-step01-parse]] | BUILD | 003 | pending |
| 006 | [[006-build-write-step02-backlog]] | BUILD | 003 | pending |
| 007 | [[007-build-write-step03-task-builder]] | BUILD | 003 | pending |
| 008 | [[008-build-write-step04-execute]] | BUILD | 003 | pending |
| 009 | [[009-build-write-step05-validate]] | BUILD | 003 | pending |
| 010 | [[010-build-write-command-md]] | BUILD | 004 | pending |
| 011 | [[011-build-edit-claude-md]] | BUILD | 010 | pending |
| 012 | [[012-build-edit-protocol]] | BUILD | 004 | pending |
| 013 | [[013-test-l1-verify-files]] | TEST | 001-012 | pending |
| 014 | [[014-test-l2-verify-flags]] | TEST | 001, 002 | pending |
| 015 | [[015-test-l3-execute-backlog-031]] | TEST | 013, 014 | pending |

## Gate Contract
→ [[gate-contract.md]]

## Deliverables
- `/kernel/execute-pipeline` command installed and registered
- Execute-pipeline skill with 5 step references
- Task-builder modified with `skip_plan_review` and `no_execute` flags
- All tests passing including e2e with backlog 031
