# Test: Exhaustion Re-raises, Undeclared Propagates

## Context
Backlog 200 (V-BASE): the utility's safety properties — never swallows, never catches what wasn't declared.

## Type
TEST

## Execution
inline

## Dependencies
- 002

## Phase Gate
- [ ] retry.py exists on the branch (RTY-02)

## Requirements
- Run a python script asserting BOTH: (1) an operation that always raises TimeoutError under `exceptions=(TimeoutError,)`, max_attempts=3 → TimeoutError propagates after exactly 3 calls; (2) an operation raising ValueError under `exceptions=(ConnectionError,)` → ValueError propagates on the FIRST call (undeclared exceptions are not retried)
- Non-zero exit = failure → fix → /kernel/learn

## Acceptance Criteria
- [ ] Script exits 0 (both properties verified)

## Gates Satisfied
- RTY-05

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
