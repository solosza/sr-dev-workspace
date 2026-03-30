# Copy run-task.sh to Spec Factory

## Context
One-shot task runner with resume + skip support.

## Type
BUILD

## Dependencies
- None

## Requirements
- Copy `C:/Users/solos/my_ai_projects/sr-dev-workspace/run-task.sh` to `C:/Users/solos/my_ai_projects/domain-spec-factory/run-task.sh`
- Use absolute paths, no cd

## Acceptance Criteria
- [ ] `run-task.sh` exists at spec factory root (verify: file_exists)

## Gates Satisfied
SYNC-20

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
