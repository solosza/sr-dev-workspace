# Step 3: Invoke Background Task via Bash

## Purpose

Spawn the background agent using the **Bash tool with `run_in_background: true`**. This is the proven pattern for all background task execution.

## The Working Pattern

**Use this pattern for all background agent spawning:**

```bash
Bash(
  command: 'env -u CLAUDECODE bash "D:/path/to/run-task.sh" "D:/path/to/repo" [max_iterations] "[task_subfolder]"',
  run_in_background: true,
  description: "Pipeline: [task description]"
)
```

**For ad-hoc tasks (no task folder):**
```bash
Bash(
  command: 'env -u CLAUDECODE claude -p "[task description]" --cwd "D:/path/to/repo"',
  run_in_background: true,
  description: "Subagent: [task description]"
)
```

## run-task.sh Invocation (Primary Pattern)

**Arguments:** `run-task.sh [REPO_ROOT] [MAX_ITERATIONS] [TASK_SUBFOLDER]`

```bash
env -u CLAUDECODE bash "D:/my_ai_projects/project_test_repos/sr_dev_workspace/run-task.sh" "D:/my_ai_projects/project_test_repos/sr_dev_workspace" 6 "kernel-minimalize"
```

| Argument | What | Example |
|----------|------|---------|
| 1st | Repo root (must have CLAUDE.md) | `D:/my_ai_projects/project_test_repos/sr_dev_workspace` |
| 2nd | Max iterations (tasks + 2 buffer) | `6` |
| 3rd | Subfolder name under `tasks/` | `kernel-minimalize` |

**WRONG:** Passing full task folder path as first arg. run-task.sh checks for CLAUDE.md in the first arg.

## Why Bash Tool (Not Agent Tool)

The Agent tool wrapping was an earlier pattern that added unnecessary complexity:

| Pattern | Status | Why |
|---------|--------|-----|
| `Bash(run_in_background: true)` | Correct | Direct, proven, returns background task ID |
| `Agent(prompt: "env -u CLAUDECODE bash -c '...'")` | Wrong | Unnecessary wrapper, Agent tool is for LLM prompts not shell commands |
| `claude -p` directly | Wrong | Bypasses run-task.sh state isolation, no kernel governance per task |

## Per-Agent State Isolation

When run-task.sh spawns with a TASK_SUBFOLDER, each agent gets:
- `agent_id` derived from the subfolder name
- Actions logged to `.claude/state/agent-{subfolder}-actions.jsonl`
- No writes to shared `session_state.json` actions_log array
- Full isolation from concurrent agents

## Implementation

1. Resolve the task subfolder from Step 1's parsed description
2. Count tasks in the folder to compute MAX_ITERATIONS
3. Construct the command with absolute paths
4. Call Bash tool with `run_in_background: true`
5. Capture the background task ID from the response
6. Return task ID to Step 4

## Non-Blocking Guarantee

**CRITICAL:** This pattern returns control immediately.

- Bash `run_in_background: true` returns a task ID instantly
- Background process runs independently
- User can spawn multiple agents in parallel (parallel Bash calls)
- Use `TaskOutput(task_id, block: false)` to check progress

**Wrong behavior:**
- Waiting for agent output
- Polling task status in a loop
- Blocking on completion
- Using `wait` command

## Response Format

Return to user immediately with:

```
Task spawned: [task_id]
Subfolder: tasks/[subfolder]/
Output: [output file path from Bash response]

Background agent is running. You'll be notified on completion.
```

## Error Cases

| Error | Cause | Fix |
|-------|-------|-----|
| "Not a kernel repo (no CLAUDE.md)" | First arg is task folder, not repo root | Use repo root as first arg |
| "No tasks found" | Task folder empty or wrong subfolder name | Check `tasks/[subfolder]/` exists |
| Hook blocks | `anchored: false` in shared state | Agent handles its own anchoring via one_shot mode |

## Related Documentation

- → `run-task.sh` — Task execution script (lines 1-30 for usage)
- → `.claude/lessons/lessons.md` RULE ZERO: "USE BACKGROUND AGENT + env -u CLAUDECODE FOR RUN-TASK.SH"
- → `.claude/hooks/actions-log-appender.py` — Per-agent log routing
