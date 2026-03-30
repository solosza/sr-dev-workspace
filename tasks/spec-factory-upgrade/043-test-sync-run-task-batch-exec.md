# Verify run-task-batch.sh is Executable

## Context
Test that run-task-batch.sh has execute permission and no syntax errors.

## Type
TEST

## Dependencies
- 021

## Phase Gate
- [ ] settings.local.json updated with hook registrations (task 022 complete)

## Requirements
- Verify `test -x C:/Users/solos/my_ai_projects/domain-spec-factory/run-task-batch.sh`
- If not executable, chmod +x

## Acceptance Criteria
- [ ] run-task-batch.sh is executable (verify: `test -x` exits 0)

## Gates Satisfied
FUNC-08

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
