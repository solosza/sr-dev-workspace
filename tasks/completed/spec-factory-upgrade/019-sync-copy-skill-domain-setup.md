# Copy kernel-domain-setup skill directory to Spec Factory

## Context
Existing — verify current

## Type
BUILD

## Dependencies
- None

## Requirements
- Copy `C:/Users/solos/my_ai_projects/sr-dev-workspace/.claude/skills/kernel-domain-setup/` to `C:/Users/solos/my_ai_projects/domain-spec-factory/.claude/skills/kernel-domain-setup/`
- Use `cp -r` with absolute paths, no cd

## Acceptance Criteria
- [ ] `C:/Users/solos/my_ai_projects/domain-spec-factory/.claude/skills/kernel-domain-setup/SKILL.md` exists (verify: file_exists)

## Gates Satisfied
SYNC-19

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
