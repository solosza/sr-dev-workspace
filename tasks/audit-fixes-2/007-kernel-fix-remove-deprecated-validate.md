# Remove Deprecated validate.md from Command Tree

## Context
Audit gap #15: validate.md is marked DEPRECATED (merged into anchor Part B) but still appears in CLAUDE.md command tree. Confusing for new agents.

## Dependencies
- None

## Requirements
- Remove validate.md from CLAUDE.md command tree listing
- Keep the actual validate.md file (it has "DEPRECATED" header — serves as redirect)
- Or delete the file entirely since anchor Part B covers it completely

## Acceptance Criteria
- [ ] CLAUDE.md command tree does NOT list validate.md (verify: `grep -v 'validate' CLAUDE.md` shows no validate in command tree)
- [ ] If file kept: validate.md still has DEPRECATED header
- [ ] If file deleted: verify it's gone
- [ ] Read CLAUDE.md command tree — confirm clean

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
