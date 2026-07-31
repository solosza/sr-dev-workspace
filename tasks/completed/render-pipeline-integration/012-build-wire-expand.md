# 012 — Wire the render step into /expand

Type: BUILD
Depends: 004

## Deliverable
Edit `.claude/skills/expand/SKILL.md` to add the final render step (adapter → serve-and-watch).

## Acceptance Criteria
- [ ] expand SKILL references `[[../render/steps/step-serve-and-watch]]` as the final render step.
- [ ] States: pass the expand output (the ranked reframes) through the adapter, then serve-and-watch.
- [ ] Modular/optional note present.
- [ ] No other behavior changed.

## Verify
`grep -rq 'step-serve-and-watch' .claude/skills/expand/`
