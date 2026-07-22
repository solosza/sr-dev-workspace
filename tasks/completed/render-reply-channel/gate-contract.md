# Gate Contract — 233 Render v2 Reply Channel

| Gate | Check | Method |
|------|-------|--------|
| RC-01 | Server v2: GET /status serves session-reply.json (200) or `{"status":"idle"}` when absent; GET / and POST /annotate behavior unchanged (v1 tests still pass) | run_test (005) |
| RC-02 | AMENDED LAW (AST ONLY, lessons #39/#43 methods): writes == {.annotations.tmp → annotations.json} EXACTLY (unchanged from v1); served reads == {page.html, session-reply.json}; stdlib-only | run_test (005) |
| RC-03 | Page v2: /status poll (~2s) in JS; status strip; confirm bars render per confirms[] targeting the right card; Confirm/Cancel POST ordinary annotations {target, action: confirm|cancel}; results[] flip cards to outcomes; dry-run toggle sets test:true on ALL queued annotations while ON; self-contained (zero external hosts) | run_test (006) |
| RC-04 | template.md v2: action map includes confirm/cancel as meta-actions + test flag semantics; ADDITIVE schema (v1 annotations still valid) | grep + read |
| RC-05 | Skill docs updated: step-05-route.md (reply-file confirms replace chat, dry-run never-route rule), workflow.md error row (malformed reply file → page degrades to idle, board never crashes) | grep |
| RC-06 | Full circle E2E, programmatic + honest: temp session; POST reject → (simulated session) write confirms[] to reply file → GET /status returns it → POST confirm annotation → linkage asserted; dry-run: POST with test:true → reply dry_run_ack → assert NOTHING routed/no side effects; live state untouched (hash compare); no stray listeners | run_test (007) |
| RC-07 | Live session isolation: port 52105 process untouched; its session dir unmodified | run_code |

## Test-Script Requirements (lessons #39/#43 — MANDATORY)
AST-based semantics checks only; docstrings excluded; body-scoped walks (fn.body per statement, decorator-aware). String-grep BANNED for semantics (docs-presence greps fine).

## Law Reminders
- Server write surface FROZEN — session-reply.json is written by the SESSION, only SERVED by the server
- Schema changes additive only; raw_words verbatim law unchanged
- Routing stays session behavior — do not build routing automation
