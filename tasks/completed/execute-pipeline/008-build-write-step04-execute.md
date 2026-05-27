# Write step-04-execute-tasks.md

## Context
Step 4 of execute-pipeline: spawn run-task.sh to execute the task folder produced by task-builder. Follows the prod-test pattern — outer agent spawns the process and waits.

## Type
BUILD

## Execution
inline

## Dependencies
- 003 (references directory must exist)

## Requirements
- Write `.claude/skills/execute-pipeline/references/step-04-execute-tasks.md`
- Read `pipeline_state.task_folder` and `pipeline_state.task_count` from session_state.json
- Spawn run-task-batch.sh (or run-task.sh) against the task folder:
  ```bash
  bash run-task-batch.sh . [task_folder_name] [timeout]
  ```
- Timeout calculation: 300s per task (5 min), minimum 600s
- run-task.sh runs in CURRENT repo — tasks use absolute paths if operating on external targets
- Wait for completion — do NOT poll
- Read results: exit code, workflow state (completed_tasks, skipped_tasks), logs
- Document failure handling: if run-task.sh exits non-zero, read logs and report
- Reference prod-test step-07-execute.md as structural model

## Acceptance Criteria
- [ ] `test -f .claude/skills/execute-pipeline/references/step-04-execute-tasks.md` exits 0
- [ ] File documents run-task.sh spawning with correct arguments
- [ ] File documents timeout calculation
- [ ] File documents failure handling

## Gates Satisfied
- BUILD-08

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
