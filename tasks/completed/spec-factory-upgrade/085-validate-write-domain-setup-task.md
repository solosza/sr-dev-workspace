# Write Domain-Setup Task

## Context
Create task file for domain-setup so run-task.sh can execute it.

## Type
TEST

## Dependencies
- 084

## Phase Gate
- [ ] Dependencies installed (084), kernel installed (083)

## Requirements
- Create `$WORKSPACE/tasks/setup/001-run-domain-setup.md`
- Create 000-index.md

## Acceptance Criteria
- [ ] Task file exists in workspace tasks/ (verify: file_exists)

## Gates Satisfied
VAL-05

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
