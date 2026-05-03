# 007 — L1 Verify All Fixes Present in Source

## Type
TEST

## Description
Verify all structural fixes are present in `run-task.sh` and `lib/common.sh`.

## Requirements
- Verify `run-task.sh` contains file-based output capture (grep for `> "$logfile"`, not `$()`)
- Verify `lib/common.sh` contains `taskkill` in `kill_process_tree`
- Verify `run-task.sh` contains pre-iteration exit guard (grep for `PRECHECK` or `all_done` before loop body)
- Verify `run-task.sh` contains `LOG_PREFIX` for log namespacing
- Verify `run-task.sh` trap includes SIGTERM

## Acceptance Criteria
- [ ] All 5 structural checks pass

## Gates
BUILD-01 through BUILD-05
