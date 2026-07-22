# Test: Closed Loop E2E — Programmatic (L3)

## Context
Backlog 232. The whole point: prove page-generation → serve → annotate → file → watcher-wake, end to end, honestly. Non-destructive: COPY of real review data, temp session dir, live review-status.json byte-identical after.

## Type
TEST
## Execution
inline
## Dependencies
- 005, 006

## Requirements
- Hash live `.claude/state/review-status.json` (before)
- Build REAL input: run the review-board data-source discovery (diff done/ vs review-status COPY) → items JSON (should find 40+ items)
- `generate.py items.json <temp_session_dir>` → assert page.html self-contained (zero `http://`/`https://` resource refs), contains a card for a known item (e.g., 197), has the frozen-schema POST in its JS
- Start server; spawn a watcher subprocess that blocks until annotations.json exists then exits
- POST accept for one item + POST iterate with raw_words "go deeper on gnhf kernel compat" (exact string)
- Assert: annotations.json == expected two-entry array with raw_words BYTE-VERBATIM; watcher process exited within 2s of the write
- Assert (after): live review-status.json hash unchanged; no listener left on the port
- Routing (RND-05) is intentionally NOT exercised — session behavior, not runtime
- Env problem → report L3-BLOCKED honestly and STOP; any failure → fix → /kernel/learn

## Acceptance Criteria
- [ ] Full loop green programmatically; non-destructiveness proven

## Gates Satisfied
- RRT-05, RRT-07

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
