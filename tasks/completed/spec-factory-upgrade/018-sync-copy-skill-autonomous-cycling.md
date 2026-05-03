# Copy autonomous-cycling skill directory to Spec Factory

## Context
UPDATED — Phase Gate support

## Type
BUILD

## Dependencies
- None

## Requirements
- Copy `C:/Users/solos/my_ai_projects/sr-dev-workspace/.claude/skills/autonomous-cycling/` to `C:/Users/solos/my_ai_projects/domain-spec-factory/.claude/skills/autonomous-cycling/`
- Use `cp -r` with absolute paths, no cd

## Acceptance Criteria
- [ ] `C:/Users/solos/my_ai_projects/domain-spec-factory/.claude/skills/autonomous-cycling/SKILL.md` exists (verify: file_exists)

## Gates Satisfied
SYNC-18

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
