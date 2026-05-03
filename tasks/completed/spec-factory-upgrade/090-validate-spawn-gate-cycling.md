# Spawn Gate Cycling

## Context
Run gate verification tasks via run-task.sh.

## Type
TEST

## Dependencies
- 089

## Phase Gate
- [ ] Gate tasks generated (task 089)

## Requirements
- Clear cycling state
- Spawn `bash run-task.sh $WORKSPACE N` in background
- Wait for completion

## Acceptance Criteria
- [ ] run-task.sh exited (verify: background task completed)

## Gates Satisfied
VAL-10

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
