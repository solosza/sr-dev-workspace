# Update auto-approve-claude-writes.py

## Context
Overwrites version from hook-fixes merge with latest.

## Type
BUILD

## Execution
inline

## Dependencies
- 006

## Phase Gate
- [ ] Branch created (006)

## Requirements
- Run `cp C:/Users/solos/my_ai_projects/sr-dev-workspace/.claude/hooks/auto-approve-claude-writes.py C:/Users/solos/my_ai_projects/isagawa-kernel/.claude/hooks/`

## Acceptance Criteria
- [ ] File updated (verify: file_exists)

## Gates Satisfied
BUILD-12

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
