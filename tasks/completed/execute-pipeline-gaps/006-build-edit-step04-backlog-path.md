# 006 — Edit step-04: Pass BACKLOG_PATH to run-task.sh (Gap 6)

## Type
BUILD

## Requirements
- Edit `.claude/skills/execute-pipeline/references/step-04-execute-tasks.md`
- Update the Agent prompt template to pass `pipeline_state.backlog_path` as the 4th argument to run-task.sh:
  ```
  env -u CLAUDECODE bash "[repo_path]/run-task.sh" "[repo_path]" [task_count + 2] [subfolder] [backlog_path]
  ```
- Add a note explaining that BACKLOG_PATH enables automatic move-to-done on completion

## Acceptance Criteria
- [ ] `step-04-execute-tasks.md` contains a 4th argument in the run-task.sh command
- [ ] The 4th argument references backlog_path or BACKLOG_PATH
