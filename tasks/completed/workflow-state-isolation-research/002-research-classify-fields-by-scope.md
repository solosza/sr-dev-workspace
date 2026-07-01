# Classify Workflow State Fields by Scope

## Context
Some workflow state fields are global (belong to the session), others are per-agent (belong to a specific run-task.sh invocation). Classification determines the isolation strategy.

## Type
RESEARCH

## Execution
agent

## Dependencies
- 001-research-map-workflow-state-consumers

## Phase Gate
- [ ] `projects/workflow-state-isolation-research/consumer-map.md` exists

## Requirements
- Read the consumer map from task 001
- For each field in sr_dev_workflow.json, classify:
  - **Global** — meaningful at session level, shared across agents (e.g., `anchored`, `domain`, `setup_complete`)
  - **Per-agent** — specific to one run-task.sh invocation (e.g., `completed_tasks`, `current_task`, `task_folder`, `total_tasks`)
  - **Ambiguous** — could go either way depending on strategy (e.g., `cycling`, `actions_since_anchor`)
- For ambiguous fields, document what breaks in each classification
- Produce a field classification table with rationale

## Deliverable
Write to `projects/workflow-state-isolation-research/field-classification.md`

## Acceptance Criteria
- [ ] File exists with classification table
- [ ] Every field in sr_dev_workflow.json classified
- [ ] Ambiguous fields have breakage analysis for both options
- [ ] Rationale column explains each classification

## Gates Satisfied
- RESEARCH-02

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
