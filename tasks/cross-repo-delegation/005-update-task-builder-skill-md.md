# Update task-builder SKILL.md with cross-repo reference

## Context
Add cross-repo-delegation.md to supporting references table.

## Type
BUILD

## Execution
inline

## Dependencies
- 004

## Phase Gate
- [ ] Reference doc written (004)

## Requirements
- Edit `C:/Users/solos/my_ai_projects/sr-dev-workspace/.claude/skills/task-builder/SKILL.md`
- Add to Supporting References table: `cross-repo-delegation.md` | Cross-repo agent delegation for factory tasks

## Acceptance Criteria
- [ ] SKILL.md has cross-repo-delegation in references (verify: grep 'cross-repo')

## Gates Satisfied
BUILD-05

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
