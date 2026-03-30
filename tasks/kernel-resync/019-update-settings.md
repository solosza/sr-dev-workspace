# Update settings.local.json with all hooks

## Context
Ensure PermissionRequest + PostToolUse (actions-log) are registered.

## Type
BUILD

## Execution
inline

## Dependencies
- 015-018

## Phase Gate
- [ ] All hooks copied (015-018)

## Requirements
- Read C:/Users/solos/my_ai_projects/isagawa-kernel/.claude/settings.local.json, ensure PermissionRequest (auto-approve) and PostToolUse (actions-log-appender) entries exist. Preserve existing hooks.

## Acceptance Criteria
- [ ] settings.local.json has PermissionRequest (verify: grep 'PermissionRequest')

## Gates Satisfied
BUILD-14

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
