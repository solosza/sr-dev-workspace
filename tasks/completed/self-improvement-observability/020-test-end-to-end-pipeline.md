# End-to-end pipeline test

## Context
Validates the full observability pipeline: kernel command emits event → metrics.jsonl populated → aggregate.py reads it → report produced. This is the L3 integration test.

## Type
TEST

## Execution
agent

## Dependencies
- All prior tasks (001-019)

## Phase Gate
- [ ] All 3 kernel commands have emission hooks
- [ ] aggregate.py exists and runs
- [ ] evaluate_experiments.py exists and runs
- [ ] Regression gate wired into learn.md

## Requirements
- Create a sample metrics.jsonl with realistic data (3 learn events, 5 pipeline_complete events, 10 anchor events)
- Run `python D:/my_ai_projects/kernel-observatory/lib/aggregate.py --file <sample>` and verify:
  - Output includes event counts by type
  - Output includes computed averages
  - Output includes trend data
- Create a sample experiments.jsonl with one concluded experiment
- Run `python D:/my_ai_projects/kernel-observatory/lib/evaluate_experiments.py --experiments <exp> --metrics <met>` and verify:
  - Experiment gets a verdict
- Verify learn.md has all 4 additions: metrics emission, baseline snapshot, regression check, eval-results logging, learn-events recording
- Verify complete.md has metrics emission
- Verify anchor.md has metrics emission

## Acceptance Criteria
- [ ] Sample metrics.jsonl processed without error
- [ ] aggregate.py produces meaningful output (event counts, averages)
- [ ] evaluate_experiments.py produces verdict for sample experiment
- [ ] All kernel commands have their emission hooks
- [ ] learn.md has regression gate (baseline + post-check + logging)

## Gates Satisfied
- TEST-04

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
