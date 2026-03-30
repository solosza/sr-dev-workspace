# Copy anchor.md to Spec Factory

## Context
Kernel command file sync.

## Type
BUILD

## Dependencies
- None

## Requirements
- Copy `C:/Users/solos/my_ai_projects/sr-dev-workspace/.claude/commands/kernel/anchor.md` to `C:/Users/solos/my_ai_projects/domain-spec-factory/.claude/commands/kernel/anchor.md`
- Do NOT copy validate.md (deprecated)
- Use absolute paths, no cd

## Acceptance Criteria
- [ ] `anchor.md` exists at `C:/Users/solos/my_ai_projects/domain-spec-factory/.claude/commands/kernel/anchor.md` (verify: file_exists)

## Gates Satisfied
SYNC-05

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
