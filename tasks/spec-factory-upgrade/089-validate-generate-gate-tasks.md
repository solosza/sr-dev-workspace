# Generate Gate Tasks

## Context
One task file per gate for cycling.

## Type
TEST

## Dependencies
- 088

## Phase Gate
- [ ] Gates parsed (task 088)

## Requirements
- Create `$WORKSPACE/tasks/gate-verification/`
- Write one task per gate
- Create 000-index.md

## Acceptance Criteria
- [ ] Task count matches gate count (verify: ls | wc -l)

## Gates Satisfied
VAL-09

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
