# Update complete.md command

## Context
Cycling modes + one-shot.

## Type
BUILD

## Execution
inline

## Dependencies
- 006

## Phase Gate
- [ ] Branch created (006)

## Requirements
- Run `cp C:/Users/solos/my_ai_projects/sr-dev-workspace/.claude/commands/kernel/complete.md C:/Users/solos/my_ai_projects/isagawa-kernel/.claude/commands/kernel/`

## Acceptance Criteria
- [ ] File updated (verify: file_exists)

## Gates Satisfied
BUILD-08

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
