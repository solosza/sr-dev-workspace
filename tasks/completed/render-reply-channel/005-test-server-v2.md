# Test: Server v2 (L2 + amended AST law)

## Context
Backlog 233. v1 behavior must survive; /status is new; the write surface must be provably frozen. Temp dirs only.

## Type
TEST
## Execution
inline
## Dependencies
- 001

## Requirements
- Re-run the v1 cycle assertions (GET /, POST valid/malformed, atomicity, localhost-only) against the v2 server — all still green
- /status: absent reply file → 200 `{"status":"idle"}`; present → 200 with exact file content; reply file written EXTERNALLY (test writes it, simulating the session)
- AST (lessons #39/#43: docstring-excluded, body-scoped, decorator-aware): write targets STILL exactly {tmp_path, os.replace→annotations_path} — compare as a SET, not ordered (the 232 validation's walk-order false positive); served-read targets ⊆ {page.html, session-reply.json}; imports stdlib-only
- Kill by PID in finally; failure → fix → /kernel/learn

## Acceptance Criteria
- [ ] v1 green + /status both cases + amended law proven

## Gates Satisfied
- RC-01, RC-02

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
