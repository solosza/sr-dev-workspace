# Cross-Repo Agent Delegation — Task Index

## Goal
Build factory execution mode into task-builder + cycling. Test with SSH spec factory run using platform-docker template.

## Tasks

### Phase 1: Update Task-Builder Skill

| # | Task | Type | Dependencies | Status |
|---|------|------|-------------|--------|
| 001 | [[001-update-write-tasks-execution-modes]] | BUILD | none | pending |
| 002 | [[002-update-execute-factory-logic]] | BUILD | 001 | pending |
| 003 | [[003-update-cycling-workflow]] | BUILD | 002 | pending |
| 004 | [[004-write-delegation-reference]] | BUILD | 003 | pending |
| 005 | [[005-update-task-builder-skill-md]] | BUILD | 004 | pending |

### Phase 2: Test Mechanics

| # | Task | Type | Dependencies | Status |
|---|------|------|-------------|--------|
| 006 | [[006-test-agent-reads-factory]] | TEST | none | pending |
| 007 | [[007-test-agent-reads-platform-docker]] | TEST | none | pending |
| 008 | [[008-test-agent-runs-factory-step]] | TEST | 006, 007 | pending |

### Phase 3: Full Factory SSH Spec Rebuild

| # | Task | Type | Dependencies | Status |
|---|------|------|-------------|--------|
| 009 | [[009-clean-old-ssh-output]] | BUILD | 008 | pending |
| 010 | [[010-factory-run-ssh-spec]] | TEST | 009 | pending |
| 011 | [[011-verify-factory-output]] | TEST | 010 | pending |

### Phase 4: Sync to Kernel Repo

| # | Task | Type | Dependencies | Status |
|---|------|------|-------------|--------|
| 012 | [[012-sync-to-kernel-repo]] | BUILD | 005 | pending |
| 013 | [[013-kernel-commit-push]] | BUILD | 012 | pending |

## Gate Contract
→ [[gate-contract.md]]

## Deliverables
- `factory` execution mode in task-builder + cycling
- cross-repo-delegation.md reference doc
- SSH spec rebuilt by factory using platform-docker template
- Kernel repo updated with new skill files
