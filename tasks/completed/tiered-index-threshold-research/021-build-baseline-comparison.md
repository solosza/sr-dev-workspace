# Compare Against Prior N=3 Baseline

## Context
Compare the 60K+ token results against the prior N=3 baseline at 12K tokens. This answers the core question: does corpus size change the flat vs tiered outcome?

## Type
BUILD

## Execution
inline

## Dependencies
- 019-build-score-all-results

## Phase Gate
- [ ] `D:/my_ai_projects/project_test_repos/evals/eval-ab-check-data-engine/60k/results/scores.json` exists

## Requirements
- Read prior baseline: `D:/my_ai_projects/project_test_repos/evals/eval-ab-check-data-engine/results/ab-report.md`
- Read new 60K scores from scores.json
- Compare:
  - Prior (12K tokens, N=3, gpt-4o-mini judge): No significant difference, flat 3 wins, tiered 2 wins, 10 ties
  - New (60K+ tokens, N=5, gpt-4o judge): [results from scoring]
- Analysis points:
  - Did corpus size change the verdict?
  - Which task types showed the largest deltas?
  - Did the "lost-in-the-middle" effect materialize at 60K?
  - Effect size comparison (Cohen's d at 12K vs 60K)
- Write to `D:/my_ai_projects/project_test_repos/evals/eval-ab-check-data-engine/60k/results/baseline-comparison.md`

## Acceptance Criteria
- [ ] `baseline-comparison.md` exists at the specified path
- [ ] Contains side-by-side comparison of 12K vs 60K results
- [ ] Contains analysis of whether corpus size changed the outcome
- [ ] References the prior baseline scores

## Gates Satisfied
- BUILD-12

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
