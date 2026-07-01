# Create experiments.jsonl schema

## Context
Defines the JSON schema for experiments.jsonl — tracks kernel self-improvement experiments from creation through evaluation to verdict.

## Type
BUILD

## Execution
inline

## Dependencies
- 001 (observatory repo exists)

## Phase Gate
- [ ] `D:/my_ai_projects/kernel-observatory/schemas/` directory exists

## Requirements
- Create `D:/my_ai_projects/kernel-observatory/schemas/experiments.jsonl.schema.json`
- Experiment lifecycle: created → active → concluded
- Fields: experiment_id, created_at, status, hypothesis, change_description, learn_event_id, success_criteria, evaluation_window (pipeline count), metrics_before, metrics_after, verdict (IMPROVED|NO_CHANGE|DEGRADED), concluded_at
- Success criteria patterns: rate comparison (violation rate before/after), trend (metric improving over N pipelines), threshold (metric stays above/below value)

## Acceptance Criteria
- [ ] `D:/my_ai_projects/kernel-observatory/schemas/experiments.jsonl.schema.json` exists
- [ ] File is valid JSON
- [ ] Contains experiment lifecycle fields

## Gates Satisfied
- BUILD-03

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
