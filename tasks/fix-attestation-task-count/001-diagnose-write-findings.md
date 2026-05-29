# Task 001 — Diagnose: Write Findings

**Type:** BUILD
**Depends on:** (none)

## Objective

Write the diagnosis findings for the attestation `task_count` bug to `projects/fix-attestation-task-count/diagnosis.md`.

## Context

Research completed during pipeline setup revealed:
- All 5 May 27 bundles (087-091) have `task_count: null` and `completed_count: 0` in `predicate.metadata`
- Root cause: Python `dict.get("key", default)` returns `None` when the key is present but its value is `None` — the default only applies when the key is ABSENT
- At attestation time for May 27, the workflow state had `total_tasks: null` (pipeline completed, state reset)
- The old code was `workflow.get("total_tasks", 0)` — which returns `None` when `total_tasks: null`
- The current code was changed to `workflow.get("total_tasks") or 0` — which correctly handles `None`
- BUT even with `or 0`, if the workflow is reset before attestation (e.g., batch attestation after pipeline), `0` is still wrong
- The correct fix: derive `task_count` from the task folder itself (count `NNN-*.md` files, excluding `000-index.md` and `gate-contract.md`)

## Deliverable

Create `projects/fix-attestation-task-count/diagnosis.md` with:
1. Confirmed observation: which bundles have null task_count
2. Root cause: Python get() behavior + workflow state timing
3. The fix approach: use task-folder file count as authoritative source
4. Backfill plan: patch 5 May 27 bundles locally (no Rekor mutation)

## Acceptance Criteria

- [ ] File exists at `projects/fix-attestation-task-count/diagnosis.md`
- [ ] File contains the 5 affected bundle names with their null task_count confirmed
- [ ] File documents the Python get() bug
- [ ] File describes the fix approach
