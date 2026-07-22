# Test: Page v2 Rendering (L2)

## Context
Backlog 233. Prove the generated page's reply-channel behaviors from a sample reply file — static/JS-content assertions (no browser; the full circle is 007's job).

## Type
TEST
## Execution
inline
## Dependencies
- 002

## Requirements
- Generate page from 3 sample items into a temp session dir
- Assert in the generated HTML/JS: /status fetch with interval; confirm-bar rendering code keyed by confirms[].target; results[] outcome flip code; dry-run toggle wiring `test: true` into queued annotations; malformed-reply degradation to idle
- Self-containment: zero external host refs (check unquoted-JS-aware — do not naive-grep quoted keys; the 232 lesson)
- v1 mechanics intact: card queue/lock/send code unchanged in behavior (send still POSTs one annotation per request)
- Failure → fix → /kernel/learn

## Acceptance Criteria
- [ ] All page assertions pass

## Gates Satisfied
- RC-03

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
