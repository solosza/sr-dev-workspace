# Step 4: Explain

## Purpose

Render the current section per the format contract — exactly one section, ending with the settle prompt. This is the explain primitive (also the whole of one-shot mode).

## Input

- State: `sections[cursor]`, `depth` (re-read the file this turn — not from memory)
- `.claude/docs/design/walkthrough/references/format-contract.md`, `.claude/docs/design/walkthrough/references/depth-modes.md`
- Sources backing this section (from `sources_read`; re-read if context was compacted)

## Output

- One explanation message: seven parts (plain) or grounding + recommendation + settle (terse)

## Acceptance Criteria

- [ ] Exactly ONE section rendered — the settle prompt ends the turn
- [ ] All format parts present for the current depth
- [ ] Grounding cites only files in `sources_read`, by name
- [ ] Recommendation is for THIS user's case, with reasoning
- [ ] No dependence on unexplained later sections

## References

- `.claude/docs/design/walkthrough/references/format-contract.md` — the seven parts and hard rules
- `.claude/docs/design/walkthrough/references/depth-modes.md` — rendering per depth

## Procedure

1. Read state file; identify `sections[cursor]` and depth.
2. Read `.claude/docs/design/walkthrough/references/format-contract.md`.
3. Render the section: purpose → flow diagram → why-each-piece → grounding → recommendation → mental model → settle prompt (plain) | grounding → recommendation → settle (terse).
4. Stop. Wait for the user.

## Verification

One section, correct parts, settle prompt present, turn ended.

## Failure Recovery

| Situation | Action |
|-----------|--------|
| Section too big to render in one sitting | Split it in the map (insert sub-sections after cursor), explain the first |
| Grounding gap discovered mid-render | Stop, Read the missing source, then render |
