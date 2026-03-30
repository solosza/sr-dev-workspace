# Verify Command File Count in Spec Factory

## Context
Structural test: confirm all 11 kernel command files exist.

## Type
TEST

## Dependencies
- 005-015, 023

## Phase Gate
- [ ] settings.local.json updated with hook registrations (task 022 complete)

## Requirements
- Count .md files in `C:/Users/solos/my_ai_projects/domain-spec-factory/.claude/commands/kernel/`
- Must equal 11

## Acceptance Criteria
- [ ] `ls *.md | wc -l` = 11 (verify: run_code)

## Gates Satisfied
FUNC-05

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
