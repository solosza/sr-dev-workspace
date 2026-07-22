# Spawn Agent Swarm — Skill

**Type:** Orchestration
**Style:** Indexed — SKILL.md + references/

## What

Spawns multiple background agents in parallel, monitors their progress in real-time using isolated per-agent state files, and reports completion. Uses a shared agent manifest (`agent-swarm.json`) for aggregated view plus per-agent state files to prevent contention.

**Wave-Based Execution (DAG Support):**
If backlogs or their task folders declare dependencies (`depends_on`), the swarm automatically produces execution waves and coordinates dispatch via a notification-driven barrier. Partial dispatch on failure: only downstream dependents are blocked, independent agents proceed. See → `[[references/wave-engine]]`

## Usage

```
/spawn-agent-swarm 128 131 132
/spawn-agent-swarm 125 126 127 129
/spawn-agent-swarm backlog-list.txt
```

**Arguments:**
- Backlog numbers (space-separated) → spawns one agent per backlog
- File path → reads backlog numbers from file (one per line)

## Steps

| Step | Action | Reference |
|------|--------|-----------|
| 1 | Parse input (detect backlog numbers, extract waves if dependencies declared) | → `[[references/step-01-parse-input]]` |
| 2 | Create manifest + per-agent state files (with wave plan) | → `[[references/step-02-create-manifest]]` |
| 3 | Spawn agents in current wave only | → `[[references/step-03-spawn-agents]]` |
| 4 | Monitor wave completion, apply failure semantics, dispatch next wave | → `[[references/step-04-monitor]]` |
| 5 | Report final status (all waves) | → `[[references/step-05-report]]` |

## Execution

1. **Parse input** to extract backlog numbers
2. **Create manifest** in `.claude/state/agent-swarm.json` (shared, aggregated view)
3. **Create per-agent state files** in `.claude/state/agent-{N}-state.json` (isolated per agent)
4. **For each backlog, ensure task folder exists:**
   - Check if `tasks/[subfolder]/` already exists with task files
   - **If YES:** proceed directly to spawn (step 5)
   - **If NO:** run execute-pipeline inline (steps 1-3 only: backlog → task-builder → write tasks). This builds the task folder WITHOUT executing tasks. Then proceed to spawn.
5. **Spawn all agents** — scope-routed: BUILD/REFACTOR via `Agent(isolation: "worktree")`, RESEARCH/TEST via `Bash(run_in_background: true)` with unique subfolder per backlog — all in parallel, returns immediately
6. **Start continuous monitor** that polls per-agent state files every 10 seconds
7. **Report results** when all agents complete or timeout reached

**Execute-pipeline as inner loop (CRITICAL):**
- The swarm NEVER spawns raw `claude -p` for any reason
- Every agent MUST go through `run-task.sh` for state isolation
- If a backlog has no task folder, the swarm builds it first via execute-pipeline steps 1-3 (task-builder), then spawns `run-task.sh` against the built folder
- This is what makes the swarm composable: backlog number in → isolated agent out

**run-task.sh invocation:** `run-task.sh [REPO_ROOT] [MAX_ITERATIONS] [TASK_SUBFOLDER] [BACKLOG_PATH]`
- First arg = repo root (must have CLAUDE.md), NOT the task folder path
- Second arg = task count + 2 buffer
- Third arg = subfolder name under `tasks/` (just the name)
- Fourth arg = backlog file path (e.g., `docs/backlog/128-market-research-pulsia.md`) — enables automatic move-to-done on completion

## Key Principles

- **Parallel execution** — all agents spawn simultaneously, no sequential wait
- **Non-blocking spawn** — returns after agents are spawned, doesn't wait for completion
- **Per-agent state isolation** — each agent writes to `agent-{N}-state.json`, preventing contention
- **Automatic monitoring** — monitor reads per-agent files, updates manifest in real-time
- **Generic tracking** — works with any number of agents (1 to N)
- **Real-time visibility** — user sees progress updates without manual checking
- **Eventual completion** — monitor detects completion via per-agent state files + backlog archive status
- **Composable** — can be chained or called standalone

## Agent Manifest (Shared)

File: `.claude/state/agent-swarm.json`

```json
{
  "active_agents": [
    {
      "backlog": 128,
      "spawned_at": "2026-06-15T01:00:00Z",
      "status": "complete | running | failed",
      "progress": "N/M tasks",
      "last_update": "ISO timestamp",
      "completed_at": "ISO timestamp",
      "deliverable": "human-readable description"
    }
  ]
}
```

**Status values:**
- `running` — agent spawned, tasks executing
- `complete` — all tasks done, backlog archived
- `failed` — agent errored out (detected after timeout)

## Per-Agent State Files (CRITICAL)

Files: `.claude/state/agent-{N}-state.json` (one per agent)

```json
{
  "backlog": 128,
  "backlog_path": "docs/backlog/128-market-research-pulsia.md",
  "spawned_at": "2026-06-15T01:00:00Z",
  "status": "running | complete | failed",
  "progress": "N/M tasks",
  "total_tasks": M,
  "completed_tasks": ["001-task.md", "002-task.md"],
  "last_update": "ISO timestamp",
  "task_folder": "tasks/project-name/",
  "deliverable": "description"
}
```

**Why per-agent files:**
- Prevents state overwrites when multiple agents run concurrently
- Each agent updates only its own file, no contention
- Monitor reads all files independently
- Preserves execution visibility even if other agents complete/crash
- Solves state contention issue from lesson 2026-06-14

## Monitor Behavior

Runs for max 30 polls (5 minutes with 10-second intervals):

- **Every 10 seconds:** Poll per-agent state files
- **Detection method:** Read `agent-{N}-state.json`, check `completed_tasks` count vs `total_tasks`
- **Real-time output:** Prints progress as agents complete
- **Stops early:** If all agents done OR no updates for 2+ polls

**CRITICAL: Read per-agent files, NOT shared state files**
- Monitor uses `agent-{N}-state.json` as source of truth
- Never reads `session_state.json` or `sr_dev_workflow.json` for agent status
- This prevents visibility loss from state file overwrites

## Outcome

After completion:
- `agent-swarm.json` updated with final status for all agents (aggregated)
- Per-agent state files show independent completion for each agent
- All spawned agents completed their pipelines
- User notified with final report (deliverables per agent)
- Backlog items moved to done/ as each agent finishes
