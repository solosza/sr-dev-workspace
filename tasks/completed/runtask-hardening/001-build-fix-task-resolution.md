# Task 001: Fix Task/Model Resolution

**Type:** BUILD | **Gates:** RH-01

## Action
ONE edit to run-task.sh (worktree copy): replace the CURRENT_TASK-from-state lookup with direct resolution — list tasks/{subfolder}/ numbered .md files (exclude 000-index, gate-contract, _context, _test), subtract completed_tasks + skipped_tasks from the routed agent workflow json (utf-8-sig read), take the first remaining file. Set CURRENT_TASK to its basename and TASK_FILE_PATH to its path; route_model then receives a real file. Keep the state-based value as fallback ONLY if the folder listing is empty.

## Acceptance
bash -n clean; [MODEL] line format shows the filename; RH-01 semantics.
