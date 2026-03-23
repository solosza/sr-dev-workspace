# Fix auto-approve-claude-writes.py — Document Broad Matcher

## Context
Audit gap #10: PermissionRequest matcher is Edit|Write for ALL files, but hook only approves .claude/ paths. Every Edit/Write hits this hook. Works correctly but adds latency. Need to document why or narrow if possible.

## Dependencies
- None

## Requirements
- Check Claude Code docs: does PermissionRequest support path-based matchers?
- If yes: narrow the matcher to only .claude/ paths
- If no: add documentation comment to the hook and settings.local.json explaining the broad matcher is required
- Update hook docstring to explain the filtering logic

## Acceptance Criteria
- [ ] Hook has comment explaining why matcher is broad OR matcher is narrowed (verify by reading)
- [ ] Read the file — confirm documentation is clear

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
