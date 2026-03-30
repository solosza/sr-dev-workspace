# Copy updated task-builder skill to kernel repo

## Context
New cross-repo-delegation.md + updated step-06/step-07.

## Type
BUILD

## Execution
inline

## Dependencies
- 005

## Phase Gate
- [ ] All BUILD tasks complete (001-005)

## Requirements
- Run `rm -rf C:/Users/solos/my_ai_projects/isagawa-kernel/.claude/skills/task-builder && cp -r C:/Users/solos/my_ai_projects/sr-dev-workspace/.claude/skills/task-builder C:/Users/solos/my_ai_projects/isagawa-kernel/.claude/skills/task-builder`

## Acceptance Criteria
- [ ] cross-repo-delegation.md exists in kernel repo (verify: file_exists)

## Gates Satisfied
SYNC-01

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
