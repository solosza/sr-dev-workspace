# Test: Transient Retry Succeeds

## Context
Backlog 200 (V-BASE): verify the happy retry path with real behavior, not existence.

## Type
TEST

## Execution
inline

## Dependencies
- 002

## Phase Gate
- [ ] retry.py exists on the branch (RTY-02)

## Requirements
- Run a python script (PYTHONPATH to target `framework/`): a counter-tracked operation raises ConnectionError on calls 1-2, returns a sentinel on call 3; `retry_operation(op, max_attempts=3, delay_seconds=0.01, exceptions=(ConnectionError,))` returns the sentinel and the counter is exactly 3
- Non-zero exit = failure → fix → /kernel/learn

## Acceptance Criteria
- [ ] Script exits 0

## Gates Satisfied
- RTY-04

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
