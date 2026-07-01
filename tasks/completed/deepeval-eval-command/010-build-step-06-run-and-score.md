# Write step-06-run-and-score.md

## Context
Layer 3 step file for the final step — running deepeval tests and producing the scored report. Executes the generated test suite, scores per metric, determines pass/fail, updates score history, and detects regressions.

## Type
BUILD

## Execution
inline

## Dependencies
- None

## Requirements
- File: `.claude/skills/eval/steps/step-06-run-and-score.md`
- Must contain:
  - **What to do**: execute `deepeval test run` against the generated test suite, produce scored report
  - **Pre-generation checkpoint**: read `references/step-06/metric-selection.md` and `references/step-06/report-format.md`
  - **What to produce**: scored report with per-metric scores (0-1), pass/fail per metric (score vs threshold), overall pass/fail, failing metrics with triage recommendations
  - **Score history**: write/update `eval/results/score-history.json` in the SOURCE repo (not test repo — test repo is disposable)
  - **Regression detection**: compare current scores against last entry in score-history.json; flag score drops > 0.1
  - **Output format**: table format (Metric, Score, Threshold, Status) plus summary line, gaps list, new components list
  - **Verification**: report file exists, all metrics have numeric scores, score-history.json is valid JSON
  - **Error handling**: if deepeval execution fails, capture stderr, check for missing dependencies (pip install deepeval), retry once
- Source material: `docs/backlog/157-kernel-build-deepeval-command-testing/eval-loop.md` (Step 6 + Output sections)
- Must be under 200 lines

## Acceptance Criteria
- [ ] File exists at `.claude/skills/eval/steps/step-06-run-and-score.md`
- [ ] `grep -q "score-history" .claude/skills/eval/steps/step-06-run-and-score.md` passes
- [ ] `grep -q "regression" .claude/skills/eval/steps/step-06-run-and-score.md` passes
- [ ] `grep -q "report-format" .claude/skills/eval/steps/step-06-run-and-score.md` passes
- [ ] File is under 200 lines

## Gates Satisfied
BUILD-10

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
