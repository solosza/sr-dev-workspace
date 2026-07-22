# Build: Page v2 — Poll, Confirm Bars, Results, Dry-Run Toggle

## Context
Backlog 233. READ FIRST: templates/review-board/generate.py (v1, whole file) + annotation-contract.md "Reply Channel (v2)" (reply schema + dry-run semantics). Additive changes to the generated page's JS/CSS — keep the v1 card/queue/send mechanics intact.

## Type
BUILD
## Execution
inline
## Dependencies
- None

## Requirements
- Poll `GET /status` every ~2s (setInterval + fetch); on failure or malformed JSON → treat as `{"status":"idle"}` (the board NEVER crashes on reply problems)
- Status strip under the session banner: idle / processing / closed (+ last-updated time from reply `at`)
- For each `confirms[]` entry: render an inline confirm bar ON the matching card ("[question]" + Confirm / Cancel buttons); Confirm POSTs `{target, action: "confirm", raw_words: null, at}`, Cancel POSTs `action: "cancel"`; bar disappears once a result for that target arrives
- For each `results[]` entry: flip the matching card to its outcome (✓ accepted / → outcome text / ✗ rejected: reason), remove its buttons
- Dry-run toggle (top of board, clearly labeled "Dry run — nothing will be routed"): while ON, every annotation queued carries `"test": true`; `dry_run_ack` targets show "acknowledged (dry run — not routed)"
- Self-contained page (inline everything); HTML-escape all reply-derived text; keep both themes working

## Acceptance Criteria
- [ ] Generated page implements all five behaviors; v1 mechanics unchanged

## Gates Satisfied
- RC-03 (build half)

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
