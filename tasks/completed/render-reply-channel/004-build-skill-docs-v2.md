# Build: Skill Docs v2 — step-05 + workflow

## Context
Backlog 233. Routing behavior changes: confirms move from chat to the reply file; dry-run rule added. READ FIRST: steps/step-05-route.md + workflow.md (v1).

## Type
BUILD
## Execution
inline
## Dependencies
- None

## Requirements
- steps/step-05-route.md: replace the "destructive re-confirmed in chat" procedure with: destructive entries → session writes `confirms[]` to `<session_dir>/session-reply.json` (status: processing) and re-arms the watcher; on the confirm/cancel annotation arriving, route or log-declined the ORIGINAL action. Add the dry-run rule: `test: true` → append target to `dry_run_ack` in the reply file, never route. Add: session writes `results[]` after each routing so the page reflects reality.
- workflow.md: error-handling table row — "Malformed/missing session-reply.json → page degrades to idle; board never crashes"; lifecycle diagram note for the reply file (written by session at route time, served read-only)
- Keep both files under 200 lines; link to annotation-contract.md rather than restating schema

## Acceptance Criteria
- [ ] RC-05: both docs updated, chat-confirm language gone from step-05

## Gates Satisfied
- RC-05

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
