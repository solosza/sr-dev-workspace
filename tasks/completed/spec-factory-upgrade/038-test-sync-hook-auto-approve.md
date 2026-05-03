# Test auto-approve-claude-writes.py in Spec Factory

## Context
Level 2 functional test: Pipe PermissionRequest JSON for .claude/ Write, verify approval output

## Type
TEST

## Dependencies
- 001, 022

## Phase Gate
- [ ] settings.local.json updated with hook registrations (task 022 complete)

## Requirements
- Pipe test JSON to `C:/Users/solos/my_ai_projects/domain-spec-factory/.claude/hooks/auto-approve-claude-writes.py`
- Pipe PermissionRequest JSON for .claude/ Write, verify approval output
- Use absolute paths

## Acceptance Criteria
- [ ] Hook exits 0 / produces expected output (verify: run_code)

## Gates Satisfied
FUNC-03

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
