# 011 — Wire the render step into /deep-dive

Type: BUILD
Depends: 004

## Deliverable
Edit `.claude/skills/deep-dive/SKILL.md` to add the final render step (adapter → serve-and-watch).

## Acceptance Criteria
- [ ] deep-dive SKILL references `[[../render/steps/step-serve-and-watch]]` as the final render step.
- [ ] States: pass the deep-dive output through the adapter, then serve-and-watch.
- [ ] Modular/optional note present.
- [ ] No other behavior changed.

## Verify
`grep -rq 'step-serve-and-watch' .claude/skills/deep-dive/`
