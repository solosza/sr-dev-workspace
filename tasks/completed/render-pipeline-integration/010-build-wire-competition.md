# 010 — Wire the render step into /competition

Type: BUILD
Depends: 004

## Deliverable
Edit `.claude/skills/competition/SKILL.md` to add the final render step (adapter → serve-and-watch).

## Acceptance Criteria
- [ ] competition SKILL references `[[../render/steps/step-serve-and-watch]]` as the final render step.
- [ ] States: pass the competition output through the adapter, then serve-and-watch.
- [ ] Modular/optional note present.
- [ ] No other behavior changed.

## Verify
`grep -rq 'step-serve-and-watch' .claude/skills/competition/`
