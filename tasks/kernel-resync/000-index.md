# Kernel Resync — Task Index

## Goal
Merge all feature branches to isagawa-kernel main, create new branch with v2 kernel updates, merge, resync factory.

## Tasks

### Phase 1: Merge Existing Feature Branches

| # | Task | Type | Dependencies | Status |
|---|------|------|-------------|--------|
| 001 | [[001-merge-learn-indexed-protocol]] | BUILD | none | pending |
| 002 | [[002-merge-domain-setup-rerunability]] | BUILD | 001 | pending |
| 003 | [[003-merge-hook-fixes]] | BUILD | 002 | pending |
| 004 | [[004-merge-task-builder-audit]] | BUILD | 003 | pending |
| 005 | [[005-push-merged-main]] | BUILD | 004 | pending |

### Phase 2: New Feature Branch + Skills

| # | Task | Type | Dependencies | Status |
|---|------|------|-------------|--------|
| 006 | [[006-create-v2-branch]] | BUILD | 005 | pending |
| 007 | [[007-copy-task-builder-skill]] | BUILD | 006 | pending |
| 008 | [[008-copy-audit-workflow-skill]] | BUILD | 006 | pending |

### Phase 3: Update Commands (one per task)

| # | Task | Type | Dependencies | Status |
|---|------|------|-------------|--------|
| 009 | [[009-copy-cmd-backlog]] | BUILD | 006 | pending |
| 010 | [[010-update-cmd-task-builder]] | BUILD | 006 | pending |
| 011 | [[011-update-cmd-audit-workflow]] | BUILD | 006 | pending |
| 012 | [[012-update-cmd-anchor]] | BUILD | 006 | pending |
| 013 | [[013-update-cmd-complete]] | BUILD | 006 | pending |
| 014 | [[014-update-cmd-session-start]] | BUILD | 006 | pending |

### Phase 4: Update Hooks (one per task)

| # | Task | Type | Dependencies | Status |
|---|------|------|-------------|--------|
| 015 | [[015-update-hook-gate-enforcer]] | BUILD | 006 | pending |
| 016 | [[016-update-hook-test-failure]] | BUILD | 006 | pending |
| 017 | [[017-update-hook-auto-approve]] | BUILD | 006 | pending |
| 018 | [[018-copy-hook-actions-log]] | BUILD | 006 | pending |
| 019 | [[019-update-settings]] | BUILD | 015-018 | pending |

### Phase 5: Lessons + CLAUDE.md

| # | Task | Type | Dependencies | Status |
|---|------|------|-------------|--------|
| 020 | [[020-copy-lessons]] | BUILD | 006 | pending |
| 021 | [[021-update-claude-md]] | BUILD | 007-020 | pending |

### Phase 6: Test

| # | Task | Type | Dependencies | Status |
|---|------|------|-------------|--------|
| 022 | [[022-test-hooks-kernel]] | TEST | 015-019 | pending |
| 023 | [[023-prod-test-kernel-session]] | TEST | 021, 022 | pending |

### Phase 7: Commit + PR + Merge

| # | Task | Type | Dependencies | Status |
|---|------|------|-------------|--------|
| 024 | [[024-commit-v2]] | BUILD | 023 | pending |
| 025 | [[025-push-create-pr]] | BUILD | 024 | pending |
| 026 | [[026-merge-pr]] | BUILD | 025 | pending |

### Phase 8: Resync Factory

| # | Task | Type | Dependencies | Status |
|---|------|------|-------------|--------|
| 027 | [[027-factory-resync-task-builder]] | BUILD | 026 | pending |
| 028 | [[028-factory-resync-lessons]] | BUILD | 026 | pending |
| 029 | [[029-factory-verify-hooks]] | TEST | 027, 028 | pending |

### Phase 9: Cleanup

| # | Task | Type | Dependencies | Status |
|---|------|------|-------------|--------|
| 030 | [[030-cleanup-branches]] | BUILD | 026 | pending |

## Gate Contract
→ [[gate-contract.md]]

## Deliverables
- isagawa-kernel main with all branches merged + v2 updates
- domain-spec-factory resynced with latest kernel
- Old feature branches cleaned up
