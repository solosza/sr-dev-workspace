# Replace task-builder skill with 8-step version

## Context
Overwrites old 6-step from merged branch.

## Type
BUILD

## Execution
inline

## Dependencies
- 006

## Phase Gate
- [ ] Branch created (006)

## Requirements
- Run `rm -rf C:/Users/solos/my_ai_projects/isagawa-kernel/.claude/skills/task-builder && cp -r C:/Users/solos/my_ai_projects/sr-dev-workspace/.claude/skills/task-builder C:/Users/solos/my_ai_projects/isagawa-kernel/.claude/skills/task-builder`

## Acceptance Criteria
- [ ] step-03-resolve-template.md exists (verify: file_exists)

## Gates Satisfied
BUILD-02

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
