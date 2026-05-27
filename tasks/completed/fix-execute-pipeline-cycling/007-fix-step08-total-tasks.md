# Fix step-08 — Pre-Write total_tasks + Post-Write Verify

## Context
Task-builder in a background agent can exhaust context mid-execution, leaving incomplete task sets. `total_tasks` gets set based on files found, not files planned. Fix: write `total_tasks` from the decomposition plan BEFORE writing individual files, and verify the count after writing.

## Type
BUILD

## Execution
inline

## Dependencies
None

## Requirements
- In `.claude/skills/task-builder/references/step-08-write-tasks.md`:
  - Add a new step before "Write each task file" (current step 5): "Set `total_tasks` in `[domain]_workflow.json` from the decomposition plan count BEFORE writing individual task files. This ensures the count reflects the plan, not files-on-disk."
  - Add to the existing "Verify all files written" step (step 6): "Compare file count on disk to `total_tasks` in workflow state. If they don't match, report the discrepancy — do not silently proceed."

## Acceptance Criteria
- [ ] `grep -q 'total_tasks' .claude/skills/task-builder/references/step-08-write-tasks.md` exits 0

## Gates Satisfied
BUILD-07

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
