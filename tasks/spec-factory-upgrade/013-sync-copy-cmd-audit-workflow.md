# Copy audit-workflow.md to Spec Factory

## Context
Kernel command file sync.

## Type
BUILD

## Dependencies
- None

## Requirements
- Copy `C:/Users/solos/my_ai_projects/sr-dev-workspace/.claude/commands/kernel/audit-workflow.md` to `C:/Users/solos/my_ai_projects/domain-spec-factory/.claude/commands/kernel/audit-workflow.md`
- Do NOT copy validate.md (deprecated)
- Use absolute paths, no cd

## Acceptance Criteria
- [ ] `audit-workflow.md` exists at `C:/Users/solos/my_ai_projects/domain-spec-factory/.claude/commands/kernel/audit-workflow.md` (verify: file_exists)

## Gates Satisfied
SYNC-13

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
