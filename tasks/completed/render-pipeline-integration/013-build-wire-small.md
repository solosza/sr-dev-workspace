# 013 — Wire the render step into /small

Type: BUILD
Depends: 004

## Deliverable
Edit `.claude/skills/small/SKILL.md` to add the final render step (adapter → serve-and-watch).

## Acceptance Criteria
- [ ] small SKILL references `[[../render/steps/step-serve-and-watch]]` as the final render step.
- [ ] States: pass the small output through the adapter, then serve-and-watch.
- [ ] Modular/optional note present.
- [ ] No other behavior changed.

## Verify
`grep -rq 'step-serve-and-watch' .claude/skills/small/`
