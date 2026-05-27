# Edit step-07-plan-review.md — Add skip_plan_review Flag

## Context
Task-builder step 7 (plan review) is currently always executed. The execute-pipeline command needs to skip it when running autonomously. Adding a flag check at the top of the step so it can be bypassed when `pipeline_mode.skip_plan_review` is set in session_state.json.

## Type
BUILD

## Execution
inline

## Dependencies
- None

## Requirements
- Add a flag check section at the TOP of `.claude/skills/task-builder/references/step-07-plan-review.md`, before the existing "When This Step Applies" section
- Check: read `session_state.json`, if `pipeline_mode.skip_plan_review` is `true`, skip this step and proceed to step 8
- The check must be clearly labeled so it's obvious this is a conditional skip
- Do NOT modify any other content in the file
- Standalone task-builder usage is unchanged (flag is not set by default)

## Acceptance Criteria
- [ ] `grep -q 'skip_plan_review' .claude/skills/task-builder/references/step-07-plan-review.md` exits 0
- [ ] The flag check section appears BEFORE the existing "When This Step Applies" section
- [ ] Existing plan review logic is unchanged

## Gates Satisfied
- BUILD-01

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
