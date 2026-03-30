# E2E Iteration 1: Domain-Setup

## Context
Spawn run-task.sh for domain-setup. Expect protocol created.

## Type
TEST

## Dependencies
- 102, 103

## Phase Gate
- [ ] Kernel + spec installed (tasks 102, 103)

## Requirements
- Write domain-setup task
- Spawn `bash run-task.sh $E2E 2` in background
- Wait for completion

## Acceptance Criteria
- [ ] Protocol file created (verify: file_exists)

## Gates Satisfied
INT-01

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
