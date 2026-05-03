# Copy domain-setup.md to Spec Factory

## Context
Kernel command file sync.

## Type
BUILD

## Dependencies
- None

## Requirements
- Copy `C:/Users/solos/my_ai_projects/sr-dev-workspace/.claude/commands/kernel/domain-setup.md` to `C:/Users/solos/my_ai_projects/domain-spec-factory/.claude/commands/kernel/domain-setup.md`
- Do NOT copy validate.md (deprecated)
- Use absolute paths, no cd

## Acceptance Criteria
- [ ] `domain-setup.md` exists at `C:/Users/solos/my_ai_projects/domain-spec-factory/.claude/commands/kernel/domain-setup.md` (verify: file_exists)

## Gates Satisfied
SYNC-08

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
