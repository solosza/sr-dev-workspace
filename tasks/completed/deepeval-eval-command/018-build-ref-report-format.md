# Write step-06/report-format.md

## Context
Layer 4 reference payload for Step 6 (Run and Score). Defines the scored report template — the output format the eval command produces after running deepeval tests.

## Type
BUILD

## Execution
inline

## Dependencies
- None

## Requirements
- File: `.claude/skills/eval/references/step-06/report-format.md`
- Must contain:
  - **Report header**: `EVAL COMPLETE: [target]`
  - **Score table format**: columns for Metric, Score, Threshold, Status (PASS/FAIL)
  - **Summary line**: Overall: PASS/FAIL (N metrics below threshold)
  - **Gaps section**: list of failing metrics with description and triage recommendation
  - **New components section**: list of components created during this eval run
  - **Score history entry format**: JSON schema for score-history.json entries (timestamp, target, metrics array with name/score/threshold/status, overall_status, new_components_count)
  - **Regression warning format**: when score drop > 0.1, include REGRESSION WARNING with previous vs current score
  - **Example output**: complete example based on check-data eval (matching the example in eval-loop.md)
- Source material: `docs/backlog/157-kernel-build-deepeval-command-testing/eval-loop.md` (Output section)
- Must be under 200 lines

## Acceptance Criteria
- [ ] File exists at `.claude/skills/eval/references/step-06/report-format.md`
- [ ] `grep -q "EVAL COMPLETE" .claude/skills/eval/references/step-06/report-format.md` passes
- [ ] `grep -q "score-history" .claude/skills/eval/references/step-06/report-format.md` passes
- [ ] `grep -q "REGRESSION" .claude/skills/eval/references/step-06/report-format.md` passes
- [ ] File is under 200 lines

## Gates Satisfied
BUILD-18

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
