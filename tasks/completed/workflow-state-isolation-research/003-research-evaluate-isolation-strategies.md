# Evaluate Isolation Strategies

## Context
Given the consumer map and field classification, evaluate each isolation strategy for feasibility, complexity, and risk.

## Type
RESEARCH

## Execution
agent

## Dependencies
- 001-research-map-workflow-state-consumers
- 002-research-classify-fields-by-scope

## Phase Gate
- [ ] `projects/workflow-state-isolation-research/consumer-map.md` exists
- [ ] `projects/workflow-state-isolation-research/field-classification.md` exists

## Requirements
- Evaluate each strategy against the consumer map and field classification:

### Strategy A: Per-Agent Workflow Files
- Pattern: `agent-{id}-workflow.json` (same as actions log fix)
- Each agent reads/writes its own file
- Parent merges on completion
- Assess: what consumers break? How does merge work?

### Strategy B: File Locking
- Advisory lock before read-modify-write
- Assess: deadlock risk, latency, cross-platform (Windows)

### Strategy C: Carry-and-Merge
- Agent carries state in prompt context, writes only on completion
- Assess: context window cost, what if agent crashes mid-flight?

### Strategy D: Redesign — Split File by Scope
- Global fields stay in sr_dev_workflow.json
- Per-agent fields move to agent-{id}-cycling.json
- Assess: how many consumers need modification? Migration path?

### Strategy E: Scoped Write Guard
- Extend actions-log-appender pattern: when agent_id is set, only write per-agent fields
- Global fields frozen during parallel execution
- Assess: complexity of field-level write filtering

- For each strategy: pros, cons, files to modify, estimated change count, risk
- Consider: does the strategy work for both parallel and sequential execution?

## Deliverable
Write to `projects/workflow-state-isolation-research/strategy-evaluation.md`

## Acceptance Criteria
- [ ] File exists with evaluation of all 5 strategies
- [ ] Each strategy has pros, cons, files-to-modify, risk
- [ ] Sequential execution compatibility confirmed for each
- [ ] Clear winner or top-2 candidates identified

## Gates Satisfied
- RESEARCH-03

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
