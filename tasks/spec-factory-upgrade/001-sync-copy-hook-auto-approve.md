# Copy auto-approve-claude-writes.py to Spec Factory

## Context
PermissionRequest hook for auto-approving .claude/ writes

## Type
BUILD

## Dependencies
- None

## Requirements
- Copy `C:/Users/solos/my_ai_projects/sr-dev-workspace/.claude/hooks/auto-approve-claude-writes.py` to `C:/Users/solos/my_ai_projects/domain-spec-factory/.claude/hooks/auto-approve-claude-writes.py`
- Use absolute paths, no cd

## Acceptance Criteria
- [ ] `auto-approve-claude-writes.py` exists at `C:/Users/solos/my_ai_projects/domain-spec-factory/.claude/hooks/auto-approve-claude-writes.py` (verify: file_exists)

## Gates Satisfied
SYNC-01

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
