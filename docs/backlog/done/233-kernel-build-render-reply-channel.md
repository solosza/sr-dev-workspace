# Build Render v2 Reply Channel — The Full Circle

## Status
Open

## Priority
High — user directive after the first live session; removes the chat round-trip for confirms and closes the loop bidirectionally (lavish parity via polled file instead of SSE)

## Summary
v1 proved page → session (annotations → watcher → routing). v2 adds session → page: the session writes `session-reply.json`; the server serves it read-only at `GET /status`; the page polls (~2s) and updates in place — inline confirm bars for destructive actions, live routing results on cards, dry-run acknowledgments. Confirm answers travel back as ordinary annotations. Design already updated: annotation-contract.md "Reply Channel (v2)" section is the governing spec.

## Requirements
- `render_server.py` v2: add `GET /status` → serves `<session_dir>/session-reply.json` (200 with JSON, or `{"status":"idle"}` if absent). WRITE SURFACE UNCHANGED — the AST law becomes: writes == {.annotations.tmp, annotations.json}; served reads == {page.html, session-reply.json}. Nothing else changes in the server.
- `generate.py` v2 (review-board): page polls `/status` every ~2s; renders from reply file: (a) status strip (processing/idle/closed), (b) inline confirm bar on the targeted card for each `confirms[]` entry — Confirm/Cancel buttons POST ordinary annotations `{target, action: "confirm"|"cancel", raw_words: null, at}`, (c) `results[]` flip cards to outcome display ("✓ accepted", "→ backlog #N created", "✗ rejected: reason"), (d) dry-run toggle at top — when ON, every queued annotation carries `"test": true`; `dry_run_ack` entries show "acknowledged (dry run — not routed)" on the card
- Annotation schema gains OPTIONAL `test` (bool, default false) and the two confirm actions — update `templates/review-board/template.md` action map accordingly (confirm/cancel are meta-actions: routed by matching the pending confirm, never directly to review-queue)
- Session-side routing rules (documented in skill step-05, not code): entries with `test: true` → acknowledge in reply file, NEVER route; destructive entries → write `confirms[]` to reply file instead of asking in chat; on confirm annotation → route the original; on cancel → log declined
- Tests: L2 server (GET /status absent→idle, present→content, still no new write paths — AST re-run with the amended law), L2 page (poll JS present, confirm-bar rendering from a sample reply file, test:true flag on toggled queue), L3 full circle programmatic: POST reject → session-side writes confirms[] → page-fetch /status shows it → POST confirm annotation → assert linkage; dry-run: POST test:true → reply ack → assert nothing routed. Non-destructive to live state (temp dirs, copies) — same discipline as 232
- Update skill docs: steps/step-05-route.md (reply-file confirms replace chat confirms; dry-run rule), workflow.md error table (reply file malformed → page shows idle, never crashes the board)

## References
- .claude/docs/design/render/references/annotation-contract.md — Reply Channel (v2) section (GOVERNING)
- .claude/skills/render/ (v1 runtime, backlog 232 — merged and live-validated)
- Live evidence driving this: 2026-07-15 first session — two test annotations required chat round-trips (held on #145/#146); dry-run toggle solves the test-noise-into-intent-chain problem
- Lavish parity map: their SSE `GET /events/:key` ≈ our polled `GET /status` (KEEP-SHIM addendum, backlog 232)

## Task Builder Input
- **Deliverable:** v2 server + v2 review-board template + updated template.md/step-05/workflow docs + L2/L3 full-circle test evidence; /kernel/render review-board serves the bidirectional board
- **Location:** workspace:.claude/skills/render/
- **Scope:** BUILD
- **Constraints:** Workspace build (no branch) — tests non-destructive (temp session dirs, copies of state). Annotation schema changes are ADDITIVE only (v1 annotations remain valid). Server write surface frozen (AST-gated with the amended law). Session routing behavior is documented in skill steps, not automated code (routing stays my job). Test scripts: lessons #39/#43 methods (AST, docstring-excluded, body-scoped, decorator-aware). The LIVE render session (port 52105) must not be touched by the pipeline — it runs old code until the user closes/re-renders.
