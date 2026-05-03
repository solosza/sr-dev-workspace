# Fix run-task.sh Zombie Processes on Windows

## Status
Open

## Priority
High — execute-pipeline is broken: run-task.sh spawns `claude -p` processes that don't terminate, iteration logs come back empty, and the loop aborts after 2 consecutive "failures" even though the tasks complete via orphaned processes

## Summary
When `run-task.sh` is launched via the Agent tool's background subprocess, `claude -p` output is not captured by bash command substitution on Windows (Git Bash). Iteration logs are 1 byte (empty). The `check_completion` function finds no signal, declares failure, and aborts. Meanwhile the `claude -p` processes keep running as orphans, completing tasks but never reporting back. Additionally, the loop spawns extra iterations after `ALL_TASKS_COMPLETE` is returned — the exit check happens after the next `claude -p` already launched.

## Requirements
- Diagnose why `raw_output=$(timeout "$TASK_TIMEOUT" claude ...)` returns empty on Windows when launched from background Agent subprocess
- Fix output capture: `claude -p --output-format json` must produce parseable output in `iteration_N.log`
- Fix process cleanup: when `timeout` kills a `claude -p` process on Windows, ensure the entire process tree is terminated (not just the parent)
- Fix loop exit: after `ALL_TASKS_COMPLETE`, do not spawn another iteration
- Add a log rotation or namespacing mechanism so iteration logs from different pipeline runs don't overwrite each other (currently `iteration_1.log` from pipeline 049 overwrites `iteration_1.log` from pipeline 048)
- Test on Windows (Git Bash) — the Linux path likely works fine

## References
- `run-task.sh` — main script
- `lib/common.sh` — shared helpers (extract_session_id, check_completion, write_log)
- Observed defect: pipeline 048 — background Agent launched run-task.sh, 2 consecutive failures with empty logs, but stuck `claude -p` processes (PID 48228, 75160) completed all 8 tasks independently
- Observed defect: pipeline 046 — extra `claude -p` process spawned after `ALL_TASKS_COMPLETE` on iteration 8

## Task Builder Input
- **Deliverable:** Working `run-task.sh` + `lib/common.sh` on Windows with proper output capture, process cleanup, and loop termination
- **Location:** `workspace`
- **Scope:** BUILD
- **Constraints:** Must work in Git Bash on Windows 11. Must not break Linux behavior. The `env -u CLAUDECODE` pattern must be preserved for nested `claude -p` invocations.
