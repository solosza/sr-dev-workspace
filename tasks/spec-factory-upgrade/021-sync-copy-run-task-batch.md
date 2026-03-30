# Copy run-task-batch.sh to Spec Factory

## Context
Batch task runner with timeout support.

## Type
BUILD

## Dependencies
- None

## Requirements
- Copy `C:/Users/solos/my_ai_projects/sr-dev-workspace/run-task-batch.sh` to `C:/Users/solos/my_ai_projects/domain-spec-factory/run-task-batch.sh`
- Use absolute paths, no cd

## Acceptance Criteria
- [ ] `run-task-batch.sh` exists at spec factory root (verify: file_exists)

## Gates Satisfied
SYNC-21

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
