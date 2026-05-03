# Copy audit-workflow skill directory to Spec Factory

## Context
NEW — SKILL.md + 7 reference files

## Type
BUILD

## Dependencies
- None

## Requirements
- Copy `C:/Users/solos/my_ai_projects/sr-dev-workspace/.claude/skills/audit-workflow/` to `C:/Users/solos/my_ai_projects/domain-spec-factory/.claude/skills/audit-workflow/`
- Use `cp -r` with absolute paths, no cd

## Acceptance Criteria
- [ ] `C:/Users/solos/my_ai_projects/domain-spec-factory/.claude/skills/audit-workflow/SKILL.md` exists (verify: file_exists)

## Gates Satisfied
SYNC-17

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
