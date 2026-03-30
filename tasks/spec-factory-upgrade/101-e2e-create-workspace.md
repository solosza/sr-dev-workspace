# Create E2E Workspace

## Context
Clean workspace for production e2e testing.

## Type
TEST

## Dependencies
- 100

## Phase Gate
- [ ] Spec pushed (task 100)

## Requirements
- Create temp directory
- Record path in session context

## Acceptance Criteria
- [ ] E2E workspace exists and is empty (verify: test -d)

## Gates Satisfied
INT-01

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
