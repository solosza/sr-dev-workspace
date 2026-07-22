# Create Experiment Directory

## Context
Create the 60k/ subdirectory in the existing eval-ab-check-data-engine repo for this experiment's files. Also create results/ subdirectory.

## Type
BUILD

## Execution
inline

## Dependencies
- None

## Requirements
- Create `D:/my_ai_projects/project_test_repos/evals/eval-ab-check-data-engine/60k/`
- Create `D:/my_ai_projects/project_test_repos/evals/eval-ab-check-data-engine/60k/results/`

## Acceptance Criteria
- [ ] `D:/my_ai_projects/project_test_repos/evals/eval-ab-check-data-engine/60k/` exists
- [ ] `D:/my_ai_projects/project_test_repos/evals/eval-ab-check-data-engine/60k/results/` exists

## Gates Satisfied
- BUILD-02

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
