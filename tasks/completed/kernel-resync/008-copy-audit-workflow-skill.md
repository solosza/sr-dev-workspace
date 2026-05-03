# Replace audit-workflow skill with 8-step version

## Context
Adds atomicity scan step.

## Type
BUILD

## Execution
inline

## Dependencies
- 006

## Phase Gate
- [ ] Branch created (006)

## Requirements
- Run `rm -rf C:/Users/solos/my_ai_projects/isagawa-kernel/.claude/skills/audit-workflow && cp -r C:/Users/solos/my_ai_projects/sr-dev-workspace/.claude/skills/audit-workflow C:/Users/solos/my_ai_projects/isagawa-kernel/.claude/skills/audit-workflow`

## Acceptance Criteria
- [ ] step-07-scan-atomicity.md exists (verify: file_exists)

## Gates Satisfied
BUILD-03

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
