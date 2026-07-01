# Research: Workflow State Isolation for Parallel Agents

## Status
Open

## Priority
High — blocking reliable parallel pipeline execution. Proved by 150/151/152 test: 3 agents each completed only 1 task before shared state caused confusion.

## Summary
Backlog 153 fixed actions log contention (per-agent `agent-{id}-actions.jsonl`) but `sr_dev_workflow.json` remains shared mutable state. When multiple run-task.sh agents write concurrently, fields like `completed_tasks`, `task_folder`, `current_task`, `cycling`, and `anchored` collide. Agent B reads agent A's completion, thinks it's further along, picks wrong next task or skips. Need to research isolation strategies before building a fix.

## Evidence

Test run (2026-06-24): Spawned 3 parallel agents (backlogs 150, 151, 152) via run-task.sh. Results:
- Each agent completed exactly 1 task before state confusion
- `task_folder` set to last-writer-wins (`governance-depth-research`)
- `completed_tasks` merged all 3 agents' task 001 into one array
- `total_tasks` showed 5 (governance-depth's count, not the others)
- Actions log isolation worked correctly (separate `agent-*-actions.jsonl` files)

## Research Questions

### Consumers of sr_dev_workflow.json
- Who reads it? (`/kernel/complete`, `/kernel/anchor`, run-task.sh, autonomous cycling, session-start)
- Who writes it? (same commands + hooks)
- Which fields are per-task vs per-session vs per-agent?
- What breaks if each agent has its own copy?

### Isolation Strategies
- **Per-agent workflow files** (`agent-{id}-workflow.json`) — same pattern as actions log fix. Each agent reads/writes its own. Parent merges on completion.
- **Locking** (file lock or advisory lock) — agents take turns writing. Adds latency, risk of deadlock.
- **Carry-and-merge** — each agent carries workflow state in its prompt context, writes back only on completion. Parent merges completed_tasks arrays.
- **Redesign cycling state** — separate cycling state from workflow state. Cycling becomes per-task-folder, workflow stays per-session.
- **Scoped fields** — some fields are global (anchored, anchor_timestamp), some are per-agent (completed_tasks, current_task, task_folder). Split the file by scope.

### Integration with Execute Pipeline
- If execute-pipeline absorbs spawn-agent-swarm (parallel dispatch), how does the parent aggregate results?
- Does the parent need to merge N workflow files into one report?
- What happens if one agent fails mid-flight and its workflow file is partial?

## Requirements
- Map every consumer of sr_dev_workflow.json (command, hook, script)
- Classify each field as global vs per-agent
- Evaluate each isolation strategy (pros, cons, complexity, risk)
- Produce a concrete recommendation with implementation sketch
- Consider interaction with the execute-pipeline parallel dispatch merge

## References
- Backlog 153 (done): `docs/backlog/done/153-kernel-build-state-isolation-for-parallel-agents.md` — actions log isolation (shipped)
- Backlog 146 (done): state isolation and CI solutions research
- Test evidence: 2026-06-24 parallel run (150/151/152)
- `sr_dev_workflow.json` schema in `.claude/state/`
- Lesson: `multi-agent-orchestration.md` — per-agent state isolation principle

## Task Builder Input
- **Deliverable:** Research report with concrete isolation strategy recommendation and implementation sketch
- **Location:** subproject:workflow-state-isolation-research
- **Scope:** RESEARCH
- **Constraints:** Must be compatible with existing actions log isolation (backlog 153). Must not break single-agent (sequential) execution. Solution must work before parallel dispatch gets merged into execute-pipeline.
