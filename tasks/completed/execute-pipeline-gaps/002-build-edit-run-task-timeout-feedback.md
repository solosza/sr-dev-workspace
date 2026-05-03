# 002 — Edit run-task.sh: Per-Task Timeout Feedback (Gap 3)

## Type
BUILD

## Requirements
- Edit `run-task.sh`
- Before the `run_claude "fresh"` call in the main loop, add a Python snippet that reads `current_task` from workflow state and logs it: `echo "[TASK] Attempting: $CURRENT_TASK"`
- Update the timeout message in `run_claude()` to include `$CURRENT_TASK`: `echo "[TIMEOUT] Task '$CURRENT_TASK' — claude -p exceeded ${TASK_TIMEOUT}s (PID $claude_pid)"`
- Make `CURRENT_TASK` a global variable so run_claude can reference it

## Acceptance Criteria
- [ ] `run-task.sh` contains `[TASK] Attempting:`
- [ ] `run-task.sh` contains `CURRENT_TASK` variable assignment before run_claude call
- [ ] Timeout message in run_claude includes `CURRENT_TASK`
