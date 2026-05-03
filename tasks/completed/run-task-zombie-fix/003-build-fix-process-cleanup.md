# 003 — Fix Process Tree Cleanup on Windows

## Type
BUILD

## Description
Ensure when `timeout` kills a `claude -p` process on Windows, the entire process tree is terminated.

## Requirements
- Verify `kill_process_tree()` uses `taskkill //F //T //PID` on Windows
- Add a post-kill verification: after killing, check if any child processes with the same PPID still exist
- Add cleanup on normal exit (not just timeout): when a `claude -p` process completes normally, verify no orphaned children remain
- If the Windows polling loop in `run_claude()` properly handles timeout + kill, verify and mark as no-op

## Acceptance Criteria
- [ ] `kill_process_tree` kills entire tree on Windows
- [ ] Post-kill verification added or existing implementation verified

## Gates
BUILD-02
