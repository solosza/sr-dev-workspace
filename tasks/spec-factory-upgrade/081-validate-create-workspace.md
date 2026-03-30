# Create Validation Test Workspace

## Context
First validation step: create a clean, isolated directory for testing the SSH spec. NO git init — workspace is ephemeral.

## Type
TEST

## Dependencies
- 080

## Phase Gate
- [ ] Factory audit shows 0 gaps (task 080 complete)

## Requirements
- Create directory at temp location (e.g., `/tmp/ssh-spec-validation-$(date +%s)/`)
- Record workspace path in session context for subsequent tasks
- Verify directory is empty

## Acceptance Criteria
- [ ] Workspace directory exists and is empty (verify: `test -d $WORKSPACE && [ -z "$(ls -A $WORKSPACE)" ]`)

## Gates Satisfied
VAL-01

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
