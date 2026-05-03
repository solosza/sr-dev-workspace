# 005 — Edit run-task.sh: Add BACKLOG_PATH + Move-to-Done (Gap 6)

## Type
BUILD

## Requirements
- Edit `run-task.sh`
- Add `BACKLOG_PATH` as the 4th positional argument: `BACKLOG_PATH="${4:-}"`
- After the ALL_TASKS_COMPLETE banner (both the main loop detection and the pre-iteration guard), add move-to-done logic:
  ```bash
  # Move backlog to done
  if [ -n "$BACKLOG_PATH" ] && [ -f "$BACKLOG_PATH" ]; then
    mkdir -p docs/backlog/done
    mv "$BACKLOG_PATH" docs/backlog/done/
    BACKLOG_DIR="${BACKLOG_PATH%.md}"
    if [ -d "$BACKLOG_DIR" ]; then
      mv "$BACKLOG_DIR" docs/backlog/done/
    fi
  fi
  # Move task folder to completed
  if [ -n "$TASK_SUBFOLDER" ]; then
    mkdir -p tasks/completed
    mv "tasks/$TASK_SUBFOLDER" "tasks/completed/$TASK_SUBFOLDER"
  fi
  ```
- Update the Usage comment to show the 4th argument
- Update the Arguments comment to document BACKLOG_PATH

## Acceptance Criteria
- [ ] `run-task.sh` contains `BACKLOG_PATH="${4:-}"`
- [ ] `run-task.sh` contains `docs/backlog/done` (move logic)
- [ ] `run-task.sh` contains `tasks/completed` (move logic)
- [ ] Usage comment shows 4th argument
