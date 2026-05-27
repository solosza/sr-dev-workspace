# Fix MAX_CONSECUTIVE_FAILS — Too Aggressive

## Context
run-task.sh aborts the entire pipeline after 2 consecutive failures. With transient empty outputs from rate limits or slow startup, this triggers immediately. Increasing to 4 gives the pipeline breathing room.

## Type
BUILD

## Execution
inline

## Dependencies
None

## Requirements
- Edit `run-task.sh` line 29: change `MAX_CONSECUTIVE_FAILS=2` to `MAX_CONSECUTIVE_FAILS=4`

## Acceptance Criteria
- [ ] `grep -q 'MAX_CONSECUTIVE_FAILS=4' run-task.sh` exits 0

## Gates Satisfied
BUILD-01

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
