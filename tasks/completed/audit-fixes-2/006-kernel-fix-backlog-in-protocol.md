# Fix Protocol — Add Backlog Command Reference

## Context
Audit gap #13: /kernel/backlog command exists but isn't referenced in the protocol index. A fresh agent reading the protocol won't know the command exists.

## Dependencies
- None

## Requirements
- Add backlog command to the protocol's Kernel references table
- Verify CLAUDE.md already has it in the command tree (it does — just confirm)

## Acceptance Criteria
- [ ] `grep -q 'backlog' .claude/protocols/sr_dev-protocol.md` (in protocol)
- [ ] `grep -q 'backlog' CLAUDE.md` (in CLAUDE.md — should already be there)
- [ ] Read protocol — confirm entry is in the right table

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
