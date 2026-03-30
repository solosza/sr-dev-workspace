# Copy universal-gate-enforcer.py to Spec Factory

## Context
PreToolUse hook for enforcement (updated counter fix)

## Type
BUILD

## Dependencies
- None

## Requirements
- Copy `C:/Users/solos/my_ai_projects/sr-dev-workspace/.claude/hooks/universal-gate-enforcer.py` to `C:/Users/solos/my_ai_projects/domain-spec-factory/.claude/hooks/universal-gate-enforcer.py`
- Use absolute paths, no cd

## Acceptance Criteria
- [ ] `universal-gate-enforcer.py` exists at `C:/Users/solos/my_ai_projects/domain-spec-factory/.claude/hooks/universal-gate-enforcer.py` (verify: file_exists)

## Gates Satisfied
SYNC-03

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
