# Test: Full Circle E2E (L3, programmatic)

## Context
Backlog 233. Both directions in one run, honestly, in a temp session. The session side is SIMULATED by the test (writing the reply file) — real routing stays session behavior.

## Type
TEST
## Execution
inline
## Dependencies
- 005, 006
## Phase Gate
- [ ] RC-01/02/03 green

## Requirements
- Temp session: items.json (3 samples) → generate v2 page → start v2 server → capture port
- Circle 1 (confirm flow): POST `{target:"145", action:"reject", raw_words:"e2e reason", at:...}` → test-as-session writes session-reply.json with confirms[] for 145 → GET /status returns it byte-exact → POST `{target:"145", action:"confirm", ...}` → annotations.json now has both entries, order preserved, raw_words verbatim
- Circle 2 (dry run): POST `{target:"188", action:"accept", test:true, ...}` → test-as-session writes dry_run_ack:["188"] → GET /status reflects it → assert NO other side effects anywhere (temp dir file listing fixed)
- Live-state safety: hash .claude/state/review-status.json before/after — identical; the LIVE render session (port 52105) untouched — assert its session dir mtimes unchanged
- Teardown by PID; no stray listeners; failure → fix → /kernel/learn; env problem → L3-BLOCKED honestly

## Acceptance Criteria
- [ ] Both circles green; isolation proven

## Gates Satisfied
- RC-06, RC-07

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
