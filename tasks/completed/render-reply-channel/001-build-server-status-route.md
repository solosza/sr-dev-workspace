# Build: Server v2 — GET /status Route

## Context
Backlog 233. READ FIRST: .claude/skills/render/lib/render_server.py (v1, whole file) + design payload annotation-contract.md "Reply Channel (v2)". The write surface is FROZEN — this task adds a READ route only.

## Type
BUILD
## Execution
inline
## Dependencies
- None

## Requirements
- Extend `do_GET` in render_server.py: path `/status` → if `<session_dir>/session-reply.json` exists, serve it (200, application/json); else serve `{"status": "idle"}` (200)
- Everything else byte-consistent with v1 behavior (GET /, POST /annotate, validation, atomic append, PORT= stdout)
- Update the module docstring's law statement: writes unchanged {tmp → annotations.json}; served reads now {page.html, session-reply.json}
- NO new imports beyond the existing stdlib set

## Acceptance Criteria
- [ ] /status route works both cases; no new write paths anywhere

## Gates Satisfied
- RC-01 (build half)

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
