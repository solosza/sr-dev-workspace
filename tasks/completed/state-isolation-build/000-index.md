# State Isolation for Parallel Agents — Task Index

## Goal

Implement per-agent state isolation so parallel background agents stop overwriting shared state files. Based on research from backlog 146 and proposal at projects/production-readiness-solutions/state-isolation-proposal.md.

## Tasks

| # | Task | Type | Dependencies | Status |
|---|------|------|-------------|--------|
| 001 | [[001-kernel-build-actions-log-routing]] | BUILD | none | pending |
| 002 | [[002-kernel-build-agent-state-write-guard]] | BUILD | 001 | pending |
| 003 | [[003-kernel-build-run-task-agent-id]] | BUILD | none | pending |
| 004 | [[004-kernel-build-anchor-per-agent-cleanup]] | BUILD | 001 | pending |
| 005 | [[005-kernel-test-state-isolation]] | TEST | 001, 002, 003, 004 | pending |

## Gate Contract

→ [[gate-contract.md]]

## Deliverables

When complete:
- actions-log-appender.py routes to per-agent log files when agent_id is set
- universal-gate-enforcer.py blocks agent writes to parent session_state.json context
- run-task.sh passes agent_id in pre_init_state
- Anchor ceremony cleans up per-agent state files
- All changes backward-compatible (no agent_id = existing behavior)
