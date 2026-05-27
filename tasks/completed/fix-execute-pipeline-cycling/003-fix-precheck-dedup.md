# Fix Pre-Check Guard — Deduplicate completed_tasks

## Context
run-task.sh's pre-iteration exit guard counts `len(completed_tasks)` to check if all tasks are done. If `completed_tasks` has duplicate entries (from background agent bugs), the count is inflated and the guard triggers early, stopping the pipeline before all tasks are actually complete.

## Type
BUILD

## Execution
inline

## Dependencies
None

## Requirements
- In run-task.sh pre-iteration exit guard (the Python snippet around line 248-265), change:
  - `done = len(w.get('completed_tasks', []))` → `done = len(set(w.get('completed_tasks', [])))`
- This deduplicates before counting, preventing inflated counts from triggering early exit

## Acceptance Criteria
- [ ] `grep -q 'set(' run-task.sh` exits 0 (in the pre-check Python snippet)

## Gates Satisfied
BUILD-03

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
