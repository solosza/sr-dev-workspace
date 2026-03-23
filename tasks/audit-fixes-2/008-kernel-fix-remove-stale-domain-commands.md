# Remove Stale sr_dev Domain Commands

## Context
Audit gap #16: sr_dev-anchor.md and sr_dev-learn.md exist as top-level commands in .claude/commands/. These are domain-specific duplicates of /kernel/anchor and /kernel/learn. They may cause confusion — agent might use these instead of kernel commands.

## Dependencies
- None

## Requirements
- Read sr_dev-anchor.md and sr_dev-learn.md to understand what they do
- If they're just wrappers/duplicates of kernel commands: delete them
- If they have domain-specific additions: merge into the kernel commands or keep with documentation
- Remove from any references (CLAUDE.md, protocol) if deleted

## Acceptance Criteria
- [ ] sr_dev-anchor.md either deleted or documented as intentional
- [ ] sr_dev-learn.md either deleted or documented as intentional
- [ ] No stale references to these commands in CLAUDE.md or protocol
- [ ] Read .claude/commands/ listing — confirm clean

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
