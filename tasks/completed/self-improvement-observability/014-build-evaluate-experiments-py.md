# Create evaluate_experiments.py

## Context
Experiment evaluator that reads experiments.jsonl and metrics.jsonl, computes verdicts for active experiments past their evaluation window, and updates experiment status.

## Type
BUILD

## Execution
inline

## Dependencies
- 003 (experiments schema), 005 (aggregate.py)

## Phase Gate
- [ ] `D:/my_ai_projects/kernel-observatory/schemas/experiments.jsonl.schema.json` exists
- [ ] `D:/my_ai_projects/kernel-observatory/lib/aggregate.py` exists

## Requirements
- Create `D:/my_ai_projects/kernel-observatory/lib/evaluate_experiments.py`
- Reads experiments.jsonl and metrics.jsonl from specified paths
- For each active experiment past its evaluation window:
  - Compute metrics_before (from metrics before experiment start)
  - Compute metrics_after (from metrics after experiment start)
  - Compare against success_criteria
  - Set verdict: IMPROVED, NO_CHANGE, or DEGRADED
  - Update experiment status to "concluded"
- CLI: `python evaluate_experiments.py --experiments <path> --metrics <path>`
- CLI: `python evaluate_experiments.py --help`
- Python 3.10+ only, stdlib only
- Handle empty/missing files gracefully

## Acceptance Criteria
- [ ] `D:/my_ai_projects/kernel-observatory/lib/evaluate_experiments.py` exists
- [ ] `python D:/my_ai_projects/kernel-observatory/lib/evaluate_experiments.py --help` exits 0
- [ ] Script handles empty input without error

## Gates Satisfied
- BUILD-12, FUNC-02

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
