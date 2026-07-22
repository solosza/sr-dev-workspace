# Step 3: Spawn Agents in Parallel

Spawn one background agent per backlog number. All agents spawn immediately and run in parallel.

## Prerequisites

Each backlog must have a task folder before spawning. If the folder doesn't exist, build it inline:

1. **Check:** Does `tasks/[subfolder]/` exist with `.md` task files?
2. **If YES:** Proceed to spawn
3. **If NO:** Run execute-pipeline steps 1-3 inline (backlog → task-builder → write task files). This creates the task folder WITHOUT executing tasks. Then proceed to spawn.

**CRITICAL:** The swarm NEVER uses raw `claude -p` to bypass this. Every agent goes through `run-task.sh` for state isolation. Execute-pipeline is the inner loop that converts backlogs into task folders.

## Pattern — Scope-Routed Isolation

Each backlog is routed by scope to the correct isolation mechanism:

| Scope | Tool | Why |
|-------|------|-----|
| BUILD / REFACTOR | `Agent(isolation: "worktree", run_in_background: true)` | Code changes isolated until merge |
| RESEARCH / TEST | `Bash(run_in_background: true)` with unique subfolder | No code to merge, just needs lock isolation |

### BUILD / REFACTOR — Worktree Mode

```
Agent(
  description: "Pipeline: [backlog title]",
  prompt: "Run: env -u CLAUDECODE bash \"[repo]/run-task.sh\" \"[repo]\" [N] \"[subfolder]\" \"[backlog]\"
           Return full output including final status banner.",
  isolation: "worktree",
  run_in_background: true
)
```

On completion: feature branch enters `/kernel/review-queue` for merge.

### RESEARCH / TEST — Subfolder Mode

```bash
Bash(
  command: 'env -u CLAUDECODE bash "[repo]/run-task.sh" "[repo]" [N] "[subfolder]" "[backlog]"',
  run_in_background: true
)
```

**CRITICAL: Always use unique subfolder per backlog.** Never pass empty `""` — causes lock contention.

### Arguments

- `REPO_ROOT` — absolute path to the workspace (must contain CLAUDE.md)
- `MAX_ITERATIONS` — task count + 2 buffer (e.g., 4 tasks → 6 iterations)
- `TASK_SUBFOLDER` — folder name under `tasks/` (NOT the full path, ALWAYS unique per backlog)
- `BACKLOG_PATH` — relative path to the backlog `.md` file (enables automatic move-to-done)

**WRONG patterns (do NOT use):**
- `claude -p "[any task]"` — bypasses run-task.sh, no state isolation
- Empty subfolder `""` with concurrent spawns — lock contention
- Passing full task folder path as first arg — run-task.sh expects repo root first

## Execution — Wave-Scoped Dispatch

1. **Read the manifest** from `.claude/state/agent-swarm.json`
2. **Get current wave:** Read `current_wave` field from manifest (0 for initial dispatch)
3. **Filter agents to current wave only:** From the manifest's `active_agents`, dispatch ONLY agents where `wave_id == current_wave`
4. **For each agent in the current wave:**
   - Resolve task subfolder name (e.g., `kernel-minimalize`, `governance-depth-research`)
   - Resolve backlog path (e.g., `docs/backlog/150-kernel-refactor-minimalize-kernel.md`)
   - Count tasks in folder to set MAX_ITERATIONS = task_count + 2
   - Invoke Bash tool with `run_in_background: true`, passing backlog path as 4th arg
   - Capture background task ID
   - Continue to next agent (no waiting)

5. **Spawn ONLY the current wave's agents in a single message** — use parallel Bash tool calls, one per agent

6. **After all spawned:**
   - Report: "Spawned N agents from wave {current_wave} in parallel" with task IDs and wave info
   - Include message: "Barrier will dispatch wave {current_wave+1} when wave {current_wave} completes"

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
