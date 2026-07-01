# Build Workflow State Isolation (Scoped Write Guard)

## Status
Open

## Priority
High — blocking reliable parallel pipeline execution. Research complete (backlog 154), implementation sketch ready.

## Summary
Implement Strategy E from backlog 154 research. When `agent_id` is set in session_state.json, route per-agent workflow fields (completed_tasks, current_task, task_folder, cycling, anchored, etc.) to `agent-{id}-workflow.json`. Global fields (domain, setup_complete, lessons) stay in shared `sr_dev_workflow.json`. Same routing pattern as the actions-log-appender fix from backlog 153.

## Requirements
- Change 1: `/kernel/complete` — add routing guard. When agent_id set, write per-agent fields to agent-{id}-workflow.json
- Change 2: `universal-gate-enforcer.py` — read anchored/actions_since_anchor/actions_limit from agent-specific file when agent_id set. Write counter increment to correct file.
- Change 3: `/kernel/anchor` — write anchor fields (anchored, anchor_timestamp, actions_since_anchor reset) to agent-specific file when agent_id set
- Change 4: `run-task.sh` + `lib/common.sh` — read completed_tasks, skipped_tasks, current_task from agent-specific workflow file when AGENT_ID is set
- Change 5: Agent workflow file seeding — when agent-{id}-workflow.json doesn't exist, create it with per-agent fields only (empty completed_tasks, cycling false, etc.)
- Change 6: Execute-pipeline step 5 / spawn-agent-swarm step 5 — read each agent-{id}-workflow.json to aggregate results for final report
- Test: re-run 150/151/152 parallel, verify each agent completes ALL its tasks with no cross-agent confusion

## References
- Backlog 154 (research): `docs/backlog/154-kernel-research-workflow-state-isolation.md`
- Implementation sketch: `projects/workflow-state-isolation-research/recommendation.md`
- Field classification: `projects/workflow-state-isolation-research/field-classification.md`
- Consumer map: `projects/workflow-state-isolation-research/consumer-map.md`
- Backlog 153 (done): actions log isolation (the pattern to follow)

## Task Builder Input
- **Deliverable:** Scoped write guard in 4 files (complete.md, universal-gate-enforcer.py, anchor.md, run-task.sh/lib/common.sh) plus seeding logic and parent merge
- **Location:** workspace
- **Scope:** BUILD
- **Constraints:** Must not change behavior for single-agent (sequential) execution. Must follow the routing pattern from backlog 153 (actions-log-appender). Per-agent fields defined in projects/workflow-state-isolation-research/field-classification.md.
