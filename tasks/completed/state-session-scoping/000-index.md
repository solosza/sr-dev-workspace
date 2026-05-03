# State Session Scoping — Task Index

## Goal
Isolate sub-agent workflow state from parent session to prevent state contention. Sub-agents spawned by run-task.sh must not reset the parent's `anchored: false` in the shared `{domain}_workflow.json`.

## Source
> [[docs/backlog/040-kernel-fix-state-session-scoping.md]]

## Approach
**one_shot bypass** — If `one_shot: true` in session_state.json (set by run-task.sh), session-start skips the `anchored: false` reset, and the gate enforcer skips anchor/counter gates for one-shot agents.

## Tasks

### Phase 1: Implementation (001-002)

| # | Task | Type | Dependencies | Status |
|---|------|------|-------------|--------|
| 001 | [[001-build-edit-session-start]] | BUILD | none | pending |
| 002 | [[002-build-edit-gate-enforcer]] | BUILD | none | pending |

### Phase 2: Verification (003-005)

| # | Task | Type | Dependencies | Status |
|---|------|------|-------------|--------|
| 003 | [[003-test-l1-verify-changes]] | TEST | 001, 002 | pending |
| 004 | [[004-test-l2-hook-smoke-test]] | TEST | 002 | pending |
| 005 | [[005-test-l3-one-shot-integration]] | TEST | 001, 002 | pending |

## Gate Contract
> [[gate-contract.md]]
