# Verify Functional Gates

## Context
Direct verification of run_code and run_test gates.

## Type
TEST

## Dependencies
- 090

## Phase Gate
- [ ] Gate cycling completed (task 090)

## Requirements
- For each run_code gate: execute, check exit 0
- For each run_test: pytest
- Record per-gate pass/fail

## Acceptance Criteria
- [ ] All functional gates checked with log (verify: read log)

## Gates Satisfied
VAL-12

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
