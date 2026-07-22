# Step 7: Exit

## Purpose

Make the ledger durable and hand off. The durable file is the deliverable; the state file was only the working copy.

## Input

- State file: full ledger, deferred sections
- `.claude/docs/design/walkthrough/references/ledger-spec.md` (durable file format, handoff contract)

## Output

- `docs/walkthroughs/YYYY-MM-DD-[artifact-slug].md` (or user-directed path)
- State: `status: complete`, `ledger_file` set

## Acceptance Criteria

- [ ] All DEFERRED sections revisited (settled or consciously left deferred with notes) before writing
- [ ] Durable file written per ledger-spec format (header, sources_read, decisions table, notes/deferred)
- [ ] User offered the destination override (e.g., into a project folder next to the design doc it served)
- [ ] Handoff offered with exactly three options: feed /design / fold into a design doc / stop
- [ ] State marked complete with `ledger_file` path

## References

- `.claude/docs/design/walkthrough/references/ledger-spec.md`

## Procedure

1. Revisit deferred sections with the user.
2. Confirm destination (default `docs/walkthroughs/`), write the file.
3. Update state: `status: complete`, `ledger_file`.
4. Summarize: sections covered, decisions settled, anything still open.
5. Offer handoff (HITL). If "feed /design": invoke it with the ledger as pre-settled requirements — downstream confirms, never re-litigates.

## Verification

File exists; state complete; summary delivered; handoff answered.

## Failure Recovery

| Situation | Action |
|-----------|--------|
| User exits early ("stop here") | Write the partial ledger anyway (marked partial), leave `status: active` for resume |
| Destination folder missing | Create it |
