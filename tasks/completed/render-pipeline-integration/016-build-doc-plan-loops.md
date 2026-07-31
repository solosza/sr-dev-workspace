# 016 — Document that plan-shaped loops need their own board template

Type: BUILD
Depends: 004

## Deliverable
Edit `.claude/skills/render/templates/INDEX.md` to add a note.

## What it does
The leaderboard fits ranked-list loops. Plan-shaped loops (offer, gtm, launch, operate) emit a plan, not a ranked list, so they are deliberately NOT wired to the leaderboard. Record this so it is a known gap, not an omission.

## Acceptance Criteria
- [ ] render templates/INDEX.md contains a note naming offer, gtm, launch, operate as plan-shaped loops that need their own board template (future work), and states they are intentionally not wired to the leaderboard.
- [ ] The note points to the venture-board template as the closest existing option for stage/plan views.

## Verify
`grep -qiE 'offer|gtm|launch|operate' .claude/skills/render/templates/INDEX.md && grep -qi 'plan-shaped\|plan shaped\|own template\|own board' .claude/skills/render/templates/INDEX.md`
