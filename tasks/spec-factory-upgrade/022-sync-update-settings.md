# Update settings.local.json in Spec Factory

## Context
Add PermissionRequest (auto-approve) and PostToolUse (actions-log-appender) hooks to settings.

## Type
BUILD

## Dependencies
- 001-004 (hooks copied)

## Phase Gate
- [ ] All 4 hook files exist in spec factory hooks dir

## Phase Gate
- [ ] `auto-approve-claude-writes.py` exists at `C:/Users/solos/my_ai_projects/domain-spec-factory/.claude/hooks/auto-approve-claude-writes.py`
- [ ] `actions-log-appender.py` exists at `C:/Users/solos/my_ai_projects/domain-spec-factory/.claude/hooks/actions-log-appender.py`
- [ ] `universal-gate-enforcer.py` exists at `C:/Users/solos/my_ai_projects/domain-spec-factory/.claude/hooks/universal-gate-enforcer.py`
- [ ] `test-failure-detector.py` exists at `C:/Users/solos/my_ai_projects/domain-spec-factory/.claude/hooks/test-failure-detector.py`

## Requirements
- Read `C:/Users/solos/my_ai_projects/domain-spec-factory/.claude/settings.local.json`
- Add PermissionRequest hook entry for auto-approve-claude-writes.py
- Add PostToolUse entry for actions-log-appender.py
- Preserve all existing hooks

## Acceptance Criteria
- [ ] settings.local.json has PermissionRequest hook (verify: grep 'PermissionRequest')

## Gates Satisfied
SYNC-22, SYNC-23

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
