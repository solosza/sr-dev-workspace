# Generate Statistical Report

## Context
Analyze scores.json to produce a statistical report with Cohen's d effect sizes, win rates, and per-task-type breakdowns.

## Type
BUILD

## Execution
inline

## Dependencies
- 019-build-score-all-results

## Phase Gate
- [ ] `D:/my_ai_projects/project_test_repos/evals/eval-ab-check-data-engine/60k/results/scores.json` exists

## Requirements
- Read scores.json
- For each task type AND overall:
  - Calculate mean scores for flat (A) and tiered (B) per metric
  - Calculate delta (B - A) and std of delta
  - Calculate Cohen's d effect size per metric
  - Calculate win rates (A wins, B wins, ties) using delta > 0.01 threshold
  - Determine verdict: significant if delta > 0.05 AND win rate > 0.67
- Generate markdown report with:
  - Per-task-type tables (same format as prior ab-report.md)
  - Overall aggregate table
  - Per-run raw scores for each task type
  - Statistical summary: which task types show significant differences
- Write to `D:/my_ai_projects/project_test_repos/evals/eval-ab-check-data-engine/60k/results/statistical-report.md`

## Acceptance Criteria
- [ ] `statistical-report.md` exists at the specified path
- [ ] Contains per-task-type tables with Cohen's d
- [ ] Contains overall aggregate analysis
- [ ] Contains verdict per task type

## Gates Satisfied
- BUILD-11

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
