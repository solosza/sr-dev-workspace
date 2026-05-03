# 004 — Fix Loop Exit After ALL_TASKS_COMPLETE

## Type
BUILD

## Description
Ensure the main loop does not spawn another `claude -p` iteration after ALL_TASKS_COMPLETE is returned.

## Requirements
- Verify the pre-iteration exit guard at line ~227 checks workflow state before spawning
- Verify the `all_done` branch at line ~288 calls `exit 0` immediately
- Check edge case: if `check_completion` returns `all_done` but the Python pre-check didn't catch it, both paths must exit cleanly
- If the fix is already in place, verify and mark as no-op

## Acceptance Criteria
- [ ] Pre-iteration guard prevents extra iteration spawns
- [ ] `all_done` status results in immediate exit

## Gates
BUILD-03
