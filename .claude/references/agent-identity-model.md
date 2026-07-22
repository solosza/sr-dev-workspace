# Agent Identity Model

Canonical reference for how the kernel identifies agents and derives state filenames. Every state file maps to exactly one ID kind. Mixing ID kinds is a bug.

## ID Kinds

| ID Kind | Source | Example | Scope |
|---------|--------|---------|-------|
| **Swarm Run ID** | Timestamp or sequential, assigned by execute-pipeline | `run-20260721-1610` | One execute-pipeline invocation (multiple workers) |
| **Backlog Item ID** | Backlog number from `docs/backlog/NNN-*.md` | `244` | One pipeline's goal (maps 1:1 to a task folder) |
| **Worker ID** | Task subfolder name under `tasks/` | `agent-state-isolation` | One run-task.sh process working a task folder |
| **Task ID** | Individual task filename | `001-build-write-identity-model-doc.md` | One claude -p invocation within a worker |
| **Worktree ID** | Git worktree branch suffix | `agent-a7560104f65d9033f` | One isolated git worktree for a pipeline |

## State Filename Derivations

All per-agent state files derive from **Worker ID** (the task subfolder name). This is the only ID kind used in filenames.

| State File | Pattern | ID Kind | Example |
|------------|---------|---------|---------|
| Per-agent workflow | `agent-{worker}-workflow.json` | Worker ID | `agent-agent-state-isolation-workflow.json` |
| Per-agent session state | `agent-{worker}-session-state.json` | Worker ID | `agent-agent-state-isolation-session-state.json` |
| Per-agent actions log | `agent-{worker}-actions.jsonl` | Worker ID | `agent-agent-state-isolation-actions.jsonl` |
| Lock file | `{worker}_run-task.lock` | Worker ID | `agent-state-isolation_run-task.lock` |
| Iteration logs | `{worker}_iteration_N.log` | Worker ID | `agent-state-isolation_iteration_1.log` |
| Parent session state | `session_state.json` | — (no prefix) | Single shared file, parent only |
| Parent workflow | `{domain}_workflow.json` | — (domain, not agent) | `sr_dev_workflow.json` |
| Parent actions log | `actions.jsonl` | — (no prefix) | Single shared file, parent only |

## Routing Rule

When `KERNEL_AGENT_ID` env var is set (exported by run-task.sh):
- Hooks resolve session state to `agent-{KERNEL_AGENT_ID}-session-state.json`
- Hooks resolve actions log to `agent-{KERNEL_AGENT_ID}-actions.jsonl`
- Parent `session_state.json` and `actions.jsonl` are never touched

When `KERNEL_AGENT_ID` is NOT set (interactive session, single-agent):
- All hooks use `session_state.json` and `actions.jsonl` as today
- Backward compatible — no behavior change for non-swarm runs

## Live Bug This Fixes (2026-07-21)

**Symptom:** Swarm monitor reported 0/5 tasks complete forever, despite run-task.sh completing tasks normally.

**Root cause:** ID kind mismatch. The swarm monitor tracked progress by reading `agent-{backlog-id}-state.json` (e.g., `agent-237-state.json`), keyed by **Backlog Item ID**. But run-task.sh wrote its state files keyed by **Worker ID** (task subfolder name, e.g., `agent-kernel-minimalize-workflow.json`). The monitor looked for files that never existed.

**Fix:** This model establishes that ALL per-agent state files derive from Worker ID. The swarm monitor must map Backlog Item ID → Worker ID (via the backlog's `task_folder` or the pipeline state) to find the correct files. One mapping table, one source of truth, no more ID kind confusion.

## Secondary Bug: Session State Clobber (2026-07-21)

One-shot agents spawned by run-task.sh read and write the shared `session_state.json`. Their session-start/exit writes (`session_started: false`, stale `agent_id`, `one_shot` leakage) clobber the parent orchestrator's state, requiring full recovery-anchor cycles. Four clobber events observed in a single session on 2026-07-21.

**Fix:** With `KERNEL_AGENT_ID` routing, each one-shot agent writes `agent-{worker}-session-state.json`. The parent's `session_state.json` is never opened by agents.
