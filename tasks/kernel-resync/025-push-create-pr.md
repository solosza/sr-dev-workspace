# Push branch + create PR

## Context
Push and open PR.

## Type
BUILD

## Execution
inline

## Dependencies
- 024

## Phase Gate
- [ ] Committed (024)

## Requirements
- Run `git -C C:/Users/solos/my_ai_projects/isagawa-kernel push -u origin feature/kernel-v2-updates` then `gh pr create --repo isagawa-co/isagawa-kernel --title 'feat: kernel v2 updates' --body 'Task-builder 8-step, audit atomicity, lessons, hooks, settings'`

## Acceptance Criteria
- [ ] PR created (verify: gh pr list)

## Gates Satisfied
BUILD-18

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
