# Create observatory README

## Context
Documentation for the kernel-observatory repo: what it does, how to install extension commands into a workspace, how to use aggregate.py and evaluate_experiments.py.

## Type
BUILD

## Execution
inline

## Dependencies
- 001-017 (all components built)

## Phase Gate
- [ ] All observatory components exist (lib/, schemas/, commands/)

## Requirements
- Create `D:/my_ai_projects/kernel-observatory/README.md`
- Sections:
  - What kernel-observatory does (metrics, experiments, extension commands)
  - Installation: how to copy commands into workspace `.claude/commands/kernel/`
  - Usage: aggregate.py CLI examples, evaluate_experiments.py CLI examples
  - Schemas: overview of metrics.jsonl, experiments.jsonl, learn-events.jsonl
  - Architecture: data flow from kernel emission → JSONL files → aggregation → evaluation
  - Dependencies: Python 3.10+, no external packages
  - Integration with isagawa-kernel (Tier 1 emission hooks)
  - Integration with platform-deepeval (Tier 2 regression gate)

## Acceptance Criteria
- [ ] `D:/my_ai_projects/kernel-observatory/README.md` exists
- [ ] README explains installation into any kernel workspace
- [ ] README documents CLI usage for both Python scripts

## Gates Satisfied
- BUILD-16

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
