# Step 3: Spawn Agents in Parallel

Spawn one background agent per backlog number. All agents spawn immediately and run in parallel.

## Prerequisites

Before spawning, each backlog must already have its task folder built (by execute-pipeline or task-builder). The swarm spawns `run-task.sh` against existing task folders — it does not build tasks.

## Pattern

For each backlog number, use the **Bash tool with `run_in_background: true`**:

```bash
env -u CLAUDECODE bash run-task.sh [REPO_ROOT] [MAX_ITERATIONS] [TASK_SUBFOLDER]
```

**Example:**
```bash
env -u CLAUDECODE bash "D:/my_ai_projects/project_test_repos/sr_dev_workspace/run-task.sh" "D:/my_ai_projects/project_test_repos/sr_dev_workspace" 6 "kernel-minimalize"
```

**Arguments:**
- `REPO_ROOT` — absolute path to the workspace (must contain CLAUDE.md)
- `MAX_ITERATIONS` — task count + 2 buffer (e.g., 4 tasks → 6 iterations)
- `TASK_SUBFOLDER` — folder name under `tasks/` (NOT the full path)

**Why this pattern:**
- `env -u CLAUDECODE` — unsets blocking env var so nested `claude -p` works
- `run-task.sh` — proven task execution with session resume, state isolation, and kernel governance
- `run_in_background: true` on Bash tool — returns immediately with a background task ID
- Each agent gets `agent_id` derived from TASK_SUBFOLDER (per-agent state isolation from backlog 153)
- Actions log routes to `agent-{subfolder}-actions.jsonl` instead of shared `actions.jsonl`

**WRONG patterns (do NOT use):**
- `claude -p "Execute /kernel/execute-pipeline..."` — bypasses run-task.sh, no state isolation
- `Agent(prompt: "env -u CLAUDECODE bash -c '...'"` — unnecessary Agent wrapper
- Passing full task folder path as first arg — run-task.sh expects repo root first

## Execution

1. **For each backlog number N in the list:**
   - Resolve task subfolder name (e.g., `kernel-minimalize`, `governance-depth-research`)
   - Count tasks in folder to set MAX_ITERATIONS = task_count + 2
   - Invoke Bash tool with `run_in_background: true`
   - Capture background task ID
   - Continue to next agent (no waiting)

2. **Spawn ALL agents in a single message** — use parallel Bash tool calls, one per agent

3. **After all spawned:**
   - Report: "Spawned N agents in parallel" with task IDs

## Per-Agent State Isolation

Each spawned agent automatically gets state isolation (backlog 153):
- `agent_id` set from TASK_SUBFOLDER in `run-task.sh`
- Actions logged to `.claude/state/agent-{subfolder}-actions.jsonl`
- Session state `actions_log` array NOT updated (prevents contention)
- Shared `session_state.json` and `sr_dev_workflow.json` safe from concurrent writes

## Error Handling

**Spawn failures are rare but possible:**

| Error | Action |
|-------|--------|
| "Not a kernel repo (no CLAUDE.md)" | Wrong first argument — must be repo root, not task folder |
| Command syntax error | Fail immediately, show error |
| Process creation fails | Fail immediately, check system resources |

## Non-Blocking Guarantee

This step returns immediately. By design:
- All agents spawn in parallel via Bash `run_in_background`
- Parent gets background task IDs instantly
- No waiting for agent execution
- Parent can proceed to monitoring

## Next Step

After spawning, immediately proceed to Step 4 (Monitor). Do NOT delay or add pauses.
