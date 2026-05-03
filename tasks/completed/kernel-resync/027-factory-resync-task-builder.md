# Re-copy task-builder skill to factory

## Context
Factory needs 8-step version.

## Type
BUILD

## Execution
inline

## Dependencies
- 026

## Phase Gate
- [ ] Kernel main updated (026)

## Requirements
- Run `rm -rf C:/Users/solos/my_ai_projects/domain-spec-factory/.claude/skills/task-builder && cp -r C:/Users/solos/my_ai_projects/sr-dev-workspace/.claude/skills/task-builder C:/Users/solos/my_ai_projects/domain-spec-factory/.claude/skills/task-builder`

## Acceptance Criteria
- [ ] step-03-resolve-template.md exists in factory (verify: file_exists)

## Gates Satisfied
SYNC-01

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
