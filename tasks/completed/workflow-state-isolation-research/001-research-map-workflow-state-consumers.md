# Map Workflow State Consumers

## Context
Before we can isolate sr_dev_workflow.json, we need to know every command, hook, and script that reads or writes it.

## Type
RESEARCH

## Execution
agent

## Dependencies
- None

## Requirements
- Read sr_dev_workflow.json to understand its current schema
- Grep the entire .claude/ directory for references to workflow.json, sr_dev_workflow, workflow_state
- Grep run-task.sh for workflow state reads/writes
- For each consumer found, document:
  - Which file/command
  - Which fields it reads
  - Which fields it writes
  - When it runs (session-start, anchor, complete, cycling, hook)
- Produce a consumer map table

## Deliverable
Write to `projects/workflow-state-isolation-research/consumer-map.md`

## Acceptance Criteria
- [ ] File exists with consumer map table
- [ ] Every command that touches workflow state is listed
- [ ] Every hook that touches workflow state is listed
- [ ] run-task.sh workflow interactions documented
- [ ] Read vs write distinguished for each consumer

## Gates Satisfied
- RESEARCH-01

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
