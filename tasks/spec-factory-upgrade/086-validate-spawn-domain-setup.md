# Spawn Domain-Setup via run-task.sh

## Context
Run domain-setup autonomously. Expect needs_restart then exit.

## Type
TEST

## Dependencies
- 085

## Phase Gate
- [ ] Domain-setup task exists (task 085)

## Requirements
- Spawn `bash run-task.sh $WORKSPACE 2` in background
- Wait for completion

## Acceptance Criteria
- [ ] run-task.sh exited (verify: background task completed)

## Gates Satisfied
VAL-06

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
