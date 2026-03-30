# Copy lessons directory

## Context
All lesson files.

## Type
BUILD

## Execution
inline

## Dependencies
- 006

## Phase Gate
- [ ] Branch created (006)

## Requirements
- Run `cp -r C:/Users/solos/my_ai_projects/sr-dev-workspace/.claude/lessons C:/Users/solos/my_ai_projects/isagawa-kernel/.claude/`

## Acceptance Criteria
- [ ] lessons.md exists (verify: file_exists)

## Gates Satisfied
BUILD-15

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
