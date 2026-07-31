# 015 — Wire the render step into /source

Type: BUILD
Depends: 004

## Deliverable
Edit `.claude/skills/source/SKILL.md` to add the final render step (adapter → serve-and-watch).

## Acceptance Criteria
- [ ] source SKILL references `[[../render/steps/step-serve-and-watch]]` as the final render step.
- [ ] States: pass the source hunter output (the ranked found ideas) through the adapter, then serve-and-watch.
- [ ] Modular/optional note present.
- [ ] No other behavior changed.

## Verify
`grep -rq 'step-serve-and-watch' .claude/skills/source/`
