# E2E Iteration 2: Task + Complete

## Context
After restart: anchor, execute task, complete.

## Type
TEST

## Dependencies
- 104

## Phase Gate
- [ ] Protocol exists (task 104)

## Requirements
- Write simple task
- Spawn `bash run-task.sh $E2E 3` in background
- Wait for completion

## Acceptance Criteria
- [ ] completed_tasks has >= 1 entry (verify: read JSON)

## Gates Satisfied
INT-02

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
