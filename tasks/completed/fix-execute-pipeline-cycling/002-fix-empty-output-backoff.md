# Fix Empty Output Handling — Add Backoff + Distinction

## Context
run-task.sh treats all failures the same — empty output (transient, retry-worthy) and explicit task failure (skip-worthy) both increment CONSECUTIVE_FAILS equally. Empty outputs from rate limits or slow startup should get exponential backoff instead of immediate skip.

## Type
BUILD

## Execution
inline

## Dependencies
None

## Requirements
- Add an `EMPTY_OUTPUT_BACKOFF` variable initialized to `SLEEP_BETWEEN` (2 seconds)
- In the "no completion signal" handler (around line 327), before attempting resume:
  - If `LAST_RESULT` is empty (no output at all), apply backoff: `sleep $EMPTY_OUTPUT_BACKOFF` then double it (cap at 30s)
  - If `LAST_RESULT` has content but no completion signal, proceed to resume as normal (no backoff)
- Reset `EMPTY_OUTPUT_BACKOFF` to `SLEEP_BETWEEN` after any successful task completion

## Acceptance Criteria
- [ ] `grep -q 'EMPTY_OUTPUT_BACKOFF' run-task.sh` exits 0
- [ ] Backoff logic appears between the "no completion signal" comment and resume attempt

## Gates Satisfied
BUILD-02

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
