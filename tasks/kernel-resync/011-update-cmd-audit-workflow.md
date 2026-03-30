# Update audit-workflow.md command

## Context
Overwrite old version with 8-step version.

## Type
BUILD

## Execution
inline

## Dependencies
- 006

## Phase Gate
- [ ] Branch created (006)

## Requirements
- Run `cp C:/Users/solos/my_ai_projects/sr-dev-workspace/.claude/commands/kernel/audit-workflow.md C:/Users/solos/my_ai_projects/isagawa-kernel/.claude/commands/kernel/`

## Acceptance Criteria
- [ ] File exists (verify: file_exists)

## Gates Satisfied
BUILD-06

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
