# E2E: Verify All Results

## Context
Final check: protocol, hooks, tasks, state consistency.

## Type
TEST

## Dependencies
- 106

## Phase Gate
- [ ] All iterations completed (task 106)

## Requirements
- Read protocol - verify refs ssh-management-layer
- Read workflow - verify completed_tasks
- Read session - verify needs_learn: false
- Check consistency

## Acceptance Criteria
- [ ] Protocol refs SSH AND completed_tasks non-empty AND consistent (verify: read + grep)

## Gates Satisfied
INT-03

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
