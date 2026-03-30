# Verify Skill SKILL.md Count in Spec Factory

## Context
Structural test: confirm all 4 skill SKILL.md files exist.

## Type
TEST

## Dependencies
- 016-019, 023

## Phase Gate
- [ ] settings.local.json updated with hook registrations (task 022 complete)

## Requirements
- Glob for `C:/Users/solos/my_ai_projects/domain-spec-factory/.claude/skills/*/SKILL.md`
- Must find 4 files

## Acceptance Criteria
- [ ] Glob count = 4 (verify: run_code)

## Gates Satisfied
FUNC-06

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
