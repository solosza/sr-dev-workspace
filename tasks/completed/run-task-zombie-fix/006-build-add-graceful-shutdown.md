# 006 — Add Graceful Shutdown with SIGTERM Propagation

## Type
BUILD

## Description
Ensure the cleanup trap properly propagates signals to child `claude -p` processes.

## Requirements
- Verify the `cleanup()` function (lines 84-97) kills the active `claude -p` process via `kill_process_tree`
- Verify `CLAUDE_PID` is set before the background process starts and cleared after completion
- Add SIGHUP to the trap list (in addition to SIGINT, SIGTERM) for terminal close scenarios
- On Windows, verify `taskkill //F //T` works when the parent is also being killed (race condition check)
- If cleanup is already robust, verify and mark as no-op

## Acceptance Criteria
- [ ] Cleanup trap kills child `claude -p` on SIGINT, SIGTERM, SIGHUP
- [ ] No orphaned processes after parent script termination

## Gates
BUILD-05
