# Step 4: Generate Steps

## Purpose

Create one Layer 3 step file per workflow step from the design doc's step specifications.

## Input

- Design doc step specs (from workflow reference or dedicated step payload files)
- Template: > `.claude/docs/design/build-command/references/layer-templates.md#Step Files`

## Output

- `.claude/skills/[name]/steps/step-NN-[name].md` (one per step)

## Acceptance Criteria

- [ ] Step count matches design doc exactly (N steps > N files)
- [ ] Each step file has: Purpose, Input, Output, Acceptance Criteria, References, Procedure, Verification, Failure Recovery
- [ ] Missing fields from design doc generated as stubs (marked "To be defined")
- [ ] All step files under 200 lines

## References

- > `.claude/docs/design/build-command/references/layer-templates.md`
- > `.claude/docs/design/build-command/references/workflow.md`

## Procedure

For each step in the design doc:
1. Read the step spec (Purpose, Input, Output, Acceptance Criteria, Procedure, Verification, Failure Recovery)
2. Write `step-NN-[name].md` with all sections
3. Add References section pointing to relevant design doc reference files
4. Check line count — extract if > 200 lines

## Verification

- Count step files matches design doc step count
- Each file has all required sections
- No file exceeds 200 lines

## Failure Recovery

If a step spec has only Purpose + Procedure (minimum), generate stub sections for the rest.
