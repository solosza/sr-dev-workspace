# Update anchor.md command

## Context
Concrete verbs + token confirmation.

## Type
BUILD

## Execution
inline

## Dependencies
- 006

## Phase Gate
- [ ] Branch created (006)

## Requirements
- Run `cp C:/Users/solos/my_ai_projects/sr-dev-workspace/.claude/commands/kernel/anchor.md C:/Users/solos/my_ai_projects/isagawa-kernel/.claude/commands/kernel/`

## Acceptance Criteria
- [ ] Has concrete verb rule (verify: grep 'concrete verb')

## Gates Satisfied
BUILD-07

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
