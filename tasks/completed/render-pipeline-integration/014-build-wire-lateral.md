# 014 — Wire the render step into /lateral

Type: BUILD
Depends: 004

## Deliverable
Edit `.claude/skills/lateral/SKILL.md` to add the final render step (adapter → serve-and-watch).

## Acceptance Criteria
- [ ] lateral SKILL references `[[../render/steps/step-serve-and-watch]]` as the final render step.
- [ ] States: pass the lateral output through the adapter, then serve-and-watch.
- [ ] Modular/optional note present.
- [ ] No other behavior changed.

## Verify
`grep -rq 'step-serve-and-watch' .claude/skills/lateral/`
