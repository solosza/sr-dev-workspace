# Verify run-task.sh is Executable

## Context
Test that run-task.sh has execute permission and no syntax errors.

## Type
TEST

## Dependencies
- 020

## Phase Gate
- [ ] settings.local.json updated with hook registrations (task 022 complete)

## Requirements
- Verify `test -x C:/Users/solos/my_ai_projects/domain-spec-factory/run-task.sh`
- If not executable, chmod +x

## Acceptance Criteria
- [ ] run-task.sh is executable (verify: `test -x` exits 0)

## Gates Satisfied
FUNC-07

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
