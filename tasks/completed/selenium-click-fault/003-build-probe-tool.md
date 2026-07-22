# Build: tools/selenium-click-probe.py

## Context
Backlog 235. The permanent regression probe — future breakage detected in seconds, referenced by lesson #41's env-sanity preflight.

## Type
BUILD
## Execution
inline
## Dependencies
- None

## Requirements
- File: `tools/selenium-click-probe.py` (workspace) — standalone, stdlib + selenium only, NO framework imports
- Serves its OWN two tiny pages via http.server (no Orderly dependency): page1 has a link to page2; page2 has a button whose onclick sets a DOM flag
- Flow: headless chrome → page1 → click link (nav) → click button → check flag; prints `PROBE: DELIVERED` or `PROBE: DEAD` + per-step timing; exit 0/1
- `--trials N` flag for delivery-rate measurement; total runtime <60s at default
- Clean teardown (own PIDs only)

## Acceptance Criteria
- [ ] Runs standalone, correct verdict against current machine state (expect DEAD ~15/16), exit codes right

## Gates Satisfied
- SCF-03

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
