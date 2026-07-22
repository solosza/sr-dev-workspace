# Task 006: Add Ledger Read-Back to anchor.md Step 5

**Type:** BUILD
**Gates Satisfied:** AC-06

## Action

Edit `.claude/commands/kernel/anchor.md` Step 5 (Restore conversation context): add ledger read-back instructions (ONE edit).

## Spec

READ the current Step 5 first. Add after the existing context-restore bullets:

- If `context.ledger` exists, read every entry. `failure` entries are the highest-value signal after compaction — do NOT retry an approach a ledger failure entry records as already failed; `decision` entries carry rationale that must not be re-litigated; `constraint` entries remain binding.
- State in the anchor output (Part A summary) how many ledger entries were restored and whether any failure entry affects the stated next action.

## Acceptance Criteria (mechanical)

- grep anchor.md Step 5 section: `ledger` mentioned with failure/decision/constraint handling
- grep: `do NOT retry` (or equivalent phrasing) tied to failure entries
- Step 5's existing bullets unchanged
