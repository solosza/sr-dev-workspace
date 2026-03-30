# Test universal-gate-enforcer.py in Spec Factory

## Context
Level 2 functional test: Pipe PreToolUse JSON, verify exits 0

## Type
TEST

## Dependencies
- 003, 022

## Phase Gate
- [ ] settings.local.json updated with hook registrations (task 022 complete)

## Requirements
- Pipe test JSON to `C:/Users/solos/my_ai_projects/domain-spec-factory/.claude/hooks/universal-gate-enforcer.py`
- Pipe PreToolUse JSON, verify exits 0
- Use absolute paths

## Acceptance Criteria
- [ ] Hook exits 0 / produces expected output (verify: run_code)

## Gates Satisfied
FUNC-01

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
