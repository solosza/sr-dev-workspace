# 009 — Wire the render step into /assay

Type: BUILD
Depends: 004

## Deliverable
Edit `.claude/skills/assay/SKILL.md` (and/or its final step file) to add a final step: after Decide, render the output via the shared render step.

## Acceptance Criteria
- [ ] assay SKILL (or its steps index) references `[[../render/steps/step-serve-and-watch]]` as the final "render the result as a live board" step.
- [ ] The pointer states: pass the decide output through the adapter, then serve-and-watch.
- [ ] Modular note: the step is optional/standalone (assay still runs headless without it).
- [ ] No other assay behavior changed.

## Verify
`grep -q 'step-serve-and-watch' .claude/skills/assay/SKILL.md .claude/skills/assay/steps/*.md`
