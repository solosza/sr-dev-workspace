# Fix Context Field — Structured JSON Instead of Free-Text

## Context
Audit gap #12: The context field in session_state.json is a free-text string. After context compaction, the agent must parse a string like "batch-test cycling COMPLETE (2/2)..." to understand state. If context were a structured JSON object, resume would be deterministic.

## Dependencies
- None

## Requirements
- Change the context field from string to JSON object in session_state.json
- Define standard fields: current_task, progress, last_completed, next_step, task_folder, notes
- Update session-start.md to read structured context
- Update anchor.md Part C (step 10) to write structured context
- Update complete.md to write structured context
- Backwards-compatible: if context is a string (old format), treat it as `{ "notes": "..." }`

## Acceptance Criteria
- [ ] session_state.json context field is a JSON object (verify by reading)
- [ ] `grep -q 'current_task\|progress\|last_completed' .claude/commands/kernel/anchor.md` (structured fields referenced)
- [ ] `grep -q 'current_task\|progress\|last_completed' .claude/commands/kernel/complete.md` (structured fields referenced)
- [ ] Read session-start.md — confirms it reads structured context
- [ ] Backwards-compatible with string context (verify by reading logic)

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
