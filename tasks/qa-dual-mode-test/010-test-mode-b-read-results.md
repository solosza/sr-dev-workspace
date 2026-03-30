# Read Mode B Results

## Context
Parse Mode B output to compare against Mode A.

## Type
RESEARCH
## Execution
inline

## Dependencies
- 009

## Phase Gate
- [ ] Mode B ran (task 009)

## Requirements
- Read pytest output from task 009
- Count: passed, failed, errors, skipped
- Note test names discovered

## Acceptance Criteria
- [ ] Mode B counts documented (verify: counts in context)

## Gates Satisfied
TEST-04

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
