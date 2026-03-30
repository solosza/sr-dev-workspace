# Copy task-builder skill directory to Spec Factory

## Context
NEW — SKILL.md + 8 reference files

## Type
BUILD

## Dependencies
- None

## Requirements
- Copy `C:/Users/solos/my_ai_projects/sr-dev-workspace/.claude/skills/task-builder/` to `C:/Users/solos/my_ai_projects/domain-spec-factory/.claude/skills/task-builder/`
- Use `cp -r` with absolute paths, no cd

## Acceptance Criteria
- [ ] `C:/Users/solos/my_ai_projects/domain-spec-factory/.claude/skills/task-builder/SKILL.md` exists (verify: file_exists)

## Gates Satisfied
SYNC-16

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
