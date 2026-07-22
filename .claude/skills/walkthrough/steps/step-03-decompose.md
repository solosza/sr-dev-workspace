# Step 3: Decompose

## Purpose

Produce the section map, get it approved, initialize loop state. The map is a proposal — the user shapes it before the loop starts.

## Input

- Artifact + input type (Step 1), `sources_read` (Step 2)
- Strategy: `.claude/docs/design/walkthrough/references/decomposition-strategies.md`
- Contract: `contracts/step-03-contract.json`

## Output

- User-approved section map
- `.claude/state/walkthrough-state.json` initialized

## Acceptance Criteria

- [ ] Strategy for the input type applied (only this reference knows input types)
- [ ] Map is dependency-ordered; sections one-sitting sized; names in domain vocabulary; ≤ ~10 sections
- [ ] Map presented and user approved / reordered / added / removed (HITL)
- [ ] State written: artifact, input_type, mode, depth, sections, `cursor: 0`, `ledger: []`, sources_read, `status: active`

## References

- `.claude/docs/design/walkthrough/references/decomposition-strategies.md`
- `contracts/step-03-contract.json`

## Procedure

1. Read `.claude/docs/design/walkthrough/references/decomposition-strategies.md`; apply the row for the input type.
2. Present numbered map, one line per section.
3. Incorporate user changes; confirm.
4. Write state file.

## Verification

Contract: state file exists, `sections` non-empty, `cursor == 0`, `sources_read` non-empty.

## Failure Recovery

| Situation | Action |
|-----------|--------|
| >10 natural sections | Propose splitting into multiple walkthroughs |
| User rejects map entirely | Re-decompose with their framing; the user's mental model wins |
