# 001 — Edit step-03: Re-enable Plan Review (Gap 1)

## Type
BUILD

## Requirements
- Edit `.claude/skills/execute-pipeline/references/step-03-run-task-builder.md`
- Change `"skip_plan_review": true` to `"skip_plan_review": false` in the pipeline mode flags JSON
- Update the process description text to say plan review now runs (remove "skip step 7" language)
- Update the task-builder behavior list item for step 7 to say it runs, not skips

## Acceptance Criteria
- [ ] `step-03-run-task-builder.md` contains `"skip_plan_review": false`
- [ ] File does NOT contain the text `skip_plan_review: true` or `"skip_plan_review": true`
- [ ] Step 7 bullet says plan review runs (not skips)
