# Step 6: Record

## Purpose

Persist the settled decision, then advance. Order is load-bearing: append before advance — a crash between the two loses position, never a decision.

## Input

- Settled decision (Step 5)
- `.claude/docs/design/walkthrough/references/ledger-spec.md` (entry schema)
- State file (current ledger + cursor)

## Output

- Updated `.claude/state/walkthrough-state.json`

## Acceptance Criteria

- [ ] Ledger entry appended: `{section, settled, notes, timestamp}` — `settled` in self-contained full sentences, readable without the conversation
- [ ] State saved after append, cursor still on the recorded section
- [ ] Cursor incremented, state saved again
- [ ] Invariant holds: `len(ledger) == cursor`
- [ ] If sections remain: next Explain happens on the user's NEXT turn — never same-turn
- [ ] If exhausted (deferred revisited): proceed to Step 7

## References

- `.claude/docs/design/walkthrough/references/ledger-spec.md`

## Procedure

1. Read `.claude/docs/design/walkthrough/references/ledger-spec.md`; compose the entry.
2. Append to `ledger`, save state.
3. Increment `cursor`, save state.
4. Announce position briefly ("recorded; 5 of 9 next: logging") and stop.

## Verification

`len(ledger) == cursor` after save. Entry readable standalone.

## Failure Recovery

| Situation | Action |
|-----------|--------|
| `len(ledger) != cursor` found | Ledger is the source of truth: set `cursor = len(ledger)` |
| Write fails | Retry; if state is unwritable, dump the entry into the conversation verbatim so it is recoverable, then fix state |
