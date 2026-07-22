# Write Experiment Config

## Context
Create the experiment configuration JSON for the 60K+ token A/B test.

## Type
BUILD

## Execution
inline

## Dependencies
- 002-build-create-experiment-dir

## Phase Gate
- [ ] `D:/my_ai_projects/project_test_repos/evals/eval-ab-check-data-engine/60k/` exists

## Requirements
- Write `experiment-config.json` with:
  - artifact: "tiered-index-threshold"
  - source: "D:/my_ai_projects/project_test_repos/hmsa-healthcare-qa"
  - mode: "ab"
  - runs: 5
  - model: "claude-sonnet-4-6"
  - judge_model: "gpt-4o" (NOT gpt-4o-mini — higher accuracy for this experiment)
  - task_types: ["sequential", "precision", "crossref"]
  - metrics: ["compliance", "adherence", "completeness", "following", "drift"]
  - thresholds: { significant_delta: 0.05, win_rate_threshold: 0.67 }
  - corpus_size_target: "60000+"
  - prior_baseline: "../results/ab-report.md"
- Write to `D:/my_ai_projects/project_test_repos/evals/eval-ab-check-data-engine/60k/experiment-config.json`

## Acceptance Criteria
- [ ] `experiment-config.json` exists at the specified path
- [ ] Contains `judge_model: "gpt-4o"`
- [ ] Contains `runs: 5`
- [ ] Contains all 3 task types

## Gates Satisfied
- BUILD-09

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
