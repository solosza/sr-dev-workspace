# Task 002 — Fix attest.py: Task Count Derivation

**Type:** BUILD
**Depends on:** 001

## Objective

Fix `lib/attestation/attest.py` to derive `task_count` from the task folder itself (counting `NNN-*.md` task files), using the workflow state only as a supplement (not primary source).

## Deliverable

Edit `lib/attestation/attest.py`:

1. Add a helper function `_count_tasks_in_folder(task_folder: str) -> int` that:
   - Lists files in `task_folder`
   - Counts files matching `NNN-*.md` pattern (3+ leading digits), excluding `000-index.md` and `gate-contract.md`
   - Returns the count

2. In `run_attestation()`, replace the current task_count logic:
   ```python
   # OLD (relies on potentially-stale workflow state):
   task_count = workflow.get("total_tasks") or 0

   # NEW (derive from task folder, workflow as supplement):
   task_count = _count_tasks_in_folder(task_folder)
   if task_count == 0:
       task_count = workflow.get("total_tasks") or 0
   ```

3. Also fix `completed_count` to count from completed_tasks filtered to this folder:
   - Filter `completed_tasks` to only those matching the task folder basename
   - This ensures completed_count reflects THIS pipeline, not the cumulative total

## Acceptance Criteria

- [ ] `_count_tasks_in_folder` function exists in `lib/attestation/attest.py`
- [ ] Function correctly counts NNN-*.md files (excluding 000 and gate-contract)
- [ ] `run_attestation()` calls `_count_tasks_in_folder` as primary source for task_count
- [ ] Workflow state is used as fallback only when folder count is 0
- [ ] Function handles missing/empty folder gracefully (returns 0)
