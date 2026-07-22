# Test: Server Unit Cycle (L1/L2)

## Context
Backlog 232. Prove the transport in isolation, non-destructively (temp session dir).

## Type
TEST
## Execution
inline
## Dependencies
- 001

## Requirements
- Script in a TEMP dir: create session dir + dummy page.html; start render_server.py subprocess; capture PORT from stdout
- Assert: GET / → 200 + page bytes; GET bound to 127.0.0.1 (connection to the LAN IP fails or is refused)
- POST /annotate valid `{target:"231", action:"accept", raw_words:null, at:"..."}` → 2xx; annotations.json is a one-element array matching exactly
- POST second valid entry → array of two, order preserved (append semantics)
- POST malformed (missing action) → 4xx AND annotations.json unchanged (byte compare)
- Atomicity evidence: no `.annotations.tmp` left behind after each POST
- Kill server by PID in finally; failure → fix → /kernel/learn

## Acceptance Criteria
- [ ] All assertions pass; exit 0; no stray listener

## Gates Satisfied
- RRT-01

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
