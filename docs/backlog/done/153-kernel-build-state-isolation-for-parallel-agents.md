# Build State Isolation for Parallel Agents

## Status
Open

## Priority
High — Parallel pipelines lose deliverables due to shared mutable state. Demonstrated in pipelines 148/149 this session.

## Summary

Implement per-agent state isolation so parallel background agents stop overwriting each other's state. The solution was fully designed in backlog 146 research (projects/production-readiness-solutions/state-isolation-proposal.md). This backlog implements the 3-phase migration: (1) add agent_id to run-task.sh pre_init_state, (2) route actions log by agent_id in hook, (3) update execute-pipeline to pass agent identity when spawning.

## Requirements

### Change 1: Hook — Route actions log by agent_id
- Modify universal-gate-enforcer.py (or actions-log-appender.py)
- If session_state has `agent_id`, write to `agent-{id}-actions.jsonl` instead of shared `actions.jsonl`
- Parent (no agent_id) continues writing to shared `actions.jsonl`

### Change 2: Hook — Protect parent state from agent writes
- When `agent_id` is set in session_state, block writes to `session_state.json` context field
- Agents write ONLY to `agent-{id}-state.json`
- Parent orchestrator owns shared state files exclusively

### Change 3: run-task.sh — Pass agent_id
- Add `agent_id` to pre_init_state (use backlog number or task folder name as ID)
- Format: `pre_init_state "session_started=True,one_shot=True,agent_id={id}"`

### Change 4: execute-pipeline — Spawn with agent identity
- When spawning background agents via Agent tool, include agent_id in the command
- Format: `AGENT_ID={id} env -u CLAUDECODE bash run-task.sh ...`

### Change 5: Anchor ceremony — Archive per-agent logs
- During anchor log archival, also archive and clear `agent-*-actions.jsonl` files
- Clear `agent-*-state.json` files at pipeline start

## References
- Research: `projects/production-readiness-solutions/state-isolation-proposal.md`
- Backlog 146: `docs/backlog/done/146-kernel-research-state-isolation-and-ci-solutions.md`
- Existing per-agent design: `.claude/skills/spawn-agent-swarm/references/step-02-create-manifest.md`
- State contention lesson: `.claude/lessons/lessons.md` (MULTI-AGENT STATE ISOLATION entry)
- universal-gate-enforcer.py: `.claude/hooks/universal-gate-enforcer.py`
- actions-log-appender.py: `.claude/hooks/actions-log-appender.py`
- run-task.sh: `run-task.sh`

## Task Builder Input
- **Deliverable:** Per-agent state isolation implemented across hooks, run-task.sh, and execute-pipeline
- **Location:** workspace
- **Scope:** BUILD
- **Constraints:** No external runtime dependencies. Must work on Windows (Git Bash) and Unix. Must be backward-compatible (agents without agent_id use existing shared state). Must not break one_shot guard or existing lock file mechanism.
