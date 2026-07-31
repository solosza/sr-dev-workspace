# 002 — Build the adapter INDEX spec

Type: BUILD
Depends: 001

## Deliverable
`.claude/skills/render/adapters/INDEX.md`

## What it does
One-screen index describing the adapter: its input (loop decide/output), its output (leaderboard items.json), the baked-in rules (plain vocab, rank on merit, fit-as-tag, no em dashes), and how a loop calls it.

## Acceptance Criteria
- [ ] File exists at the deliverable path.
- [ ] Documents the `to_items()` signature and the items.json schema.
- [ ] States the three baked-in rules: plain vocabulary, rank on merit (fit is a displayed tag only), no em dashes.
- [ ] Links to `[[../templates/leaderboard/template.md]]` and `[[../steps/step-serve-and-watch]]`.
- [ ] Is an index (pointers), not a wall of implementation.

## Verify
`test -f .claude/skills/render/adapters/INDEX.md` and `grep -q 'to_items' .claude/skills/render/adapters/INDEX.md`.
