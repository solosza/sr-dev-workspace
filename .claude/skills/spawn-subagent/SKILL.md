# Spawn Subagent — Skill Specification

## Identity

**Skill:** spawn-subagent
**Purpose:** Spawn an autonomous agent to execute a task in the background without blocking the user
**Input:** Task description (string)
**Output:** Task ID + non-blocking control return
**Platform:** Bash subprocess with `env -u CLAUDECODE claude -p`
**Blocking:** No — returns immediately, user can continue working

---

## Philosophy

This skill enables **parallel work**:
- User invokes `/spawn-subagent [task description]`
- Agent spawns a background process running the task
- Control returns immediately (non-blocking)
- User can continue working on other things
- Background task runs to completion
- User can check results by reading the log file
- User can check progress via task ID

**Key principle:** Non-blocking == user never waits for the spawned agent to complete

---

## Critical Requirement: env -u CLAUDECODE

**For interactive sessions (normal usage), the background agent MUST use `env -u CLAUDECODE` to operate independently.**

Without this environment variable unset:
- ✗ Background agent inherits parent session's CLAUDECODE=1
- ✗ Nested Claude Code invocations are blocked
- ✗ Agent cannot use hooks, bash, or kernel operations
- ✗ Agent gets stuck on hook enforcement blocks

With `env -u CLAUDECODE`:
- ✓ Background agent runs in a clean subprocess
- ✓ Hooks work normally (agent has its own state)
- ✓ Bash commands execute without parent session interference
- ✓ Full autonomy and parallel execution

**This is non-negotiable for spawn-subagent to work reliably.**

→ See `references/step-03-invoke-agent.md` for implementation details.

---

## File Index

| File | Purpose |
|------|---------|
| `SKILL.md` | This file. Skill identity, philosophy, overview |
| `references/step-01-parse-description.md` | Parse and validate the task description |
| `references/step-02-validate-background-safe.md` | Ensure task is appropriate for background execution |
| `references/step-03-invoke-agent.md` | Invoke bash subprocess with env -u CLAUDECODE |
| `references/step-04-return-task-id.md` | Capture task ID and return immediately (non-blocking) |
| `references/error-handling.md` | Error cases and recovery strategies |

---

## Overview

This skill transforms `/spawn-subagent [description]` into a background Bash subprocess running `env -u CLAUDECODE bash run-task.sh` (for task folders) or `env -u CLAUDECODE claude -p` (for ad-hoc tasks).

**Steps:**
1. Parse the task description provided by user
2. Validate it's suitable for background execution (not requiring immediate results)
3. Invoke Bash tool with `run_in_background: true` and `env -u CLAUDECODE`
4. Capture the background task ID from the Bash response
5. Return task ID to user immediately (non-blocking)
6. User gets notified on completion, or checks with `TaskOutput(task_id, block: false)`

---

## Input Specification

**User provides:**
```
/spawn-subagent [task description]
```

**Example:**
```
/spawn-subagent Build H3 adventure pack with 50 monsters
/spawn-subagent Test all selenium harness commands
/spawn-subagent Clean up the backlog - remove duplicates
/spawn-subagent Research harness marketplace opportunities
```

**Validation:**
- Description must be non-empty (length > 10 characters)
- Description should not request immediate feedback or user input
- Description should not require result before continuing

---

## Output Specification

**Agent returns:**
```
Task spawned: [task-id]

You can check progress:
  tail -f /tmp/[task-name]-[timestamp].log

Background agent is running — you can continue working.
```

**Technical return (to user):**
- Task ID (unique identifier for the background process)
- Log file path (where agent logs all output)
- User can continue immediately (non-blocking)

---

## Execution Flow

```
User: /spawn-subagent [description]
  ↓
Agent: Parse description (resolve task subfolder if applicable)
  ↓
Agent: Validate background-safe
  ↓
Agent: Bash(run_in_background: true):
       env -u CLAUDECODE bash run-task.sh [repo] [iterations] [subfolder]
  ↓
Agent: Capture background task ID from Bash response
  ↓
Agent: Return task ID immediately (non-blocking)
  ↓
User: Can immediately start new work
  ↓
[Background agent runs in parallel with per-agent state isolation]
```

---

## Non-Blocking Guarantee

The skill MUST return control immediately after invoking the bash subprocess.

**Violation patterns:**
- ✗ Waiting for agent output
- ✗ Polling task status
- ✗ Pausing until completion
- ✗ Blocking user from next action

**Correct pattern:**
- ✓ Return task ID immediately
- ✓ User can work on other things
- ✓ Agent runs in background
- ✓ User checks log file anytime

---

## When to Use

→ See `references/step-02-validate-background-safe.md` for full decision tree

**Good candidates:**
- Multi-hour builds (adventure packs, harness specs, pipelines)
- Comprehensive tests (test suites, prod-test, cycling)
- Parallel research (spawn 2+ agents, work on something else)
- Any task that doesn't need immediate feedback

**Not suitable:**
- Tasks requiring user confirmation mid-execution
- Tasks producing results needed for next immediate step
- Interactive work requiring console I/O
- Anything blocking downstream work

---

## Error Handling

→ See `references/error-handling.md` for detailed error cases

**Common failures:**
| Error | Recovery |
|-------|----------|
| Description empty | Fail with message, ask user to provide description |
| Description too vague | Warn but proceed (let background agent fail gracefully) |
| Bash invocation fails | Fail immediately, show error output |
| Missing `env -u CLAUDECODE` | Agent will be blocked by hooks; check log file |

---

## Related Skills

- → `autonomous-cycling` — Execute multiple tasks sequentially
- → `execute-pipeline` — Run full pipeline (task-builder → run-task.sh)
- → `prod-test` — Production testing (uses spawn internally)

---

## Protocol Integration

**Soft enforcement:** Agent follows skill instructions and validates background-safe conditions.

**Hard enforcement:** Hook prevents spawning for interactive/blocking tasks.

---

## Working Implementation Pattern

**For task-folder execution (primary):**
```bash
Bash(
  command: 'env -u CLAUDECODE bash "D:/path/run-task.sh" "D:/path/repo" [iterations] "[subfolder]"',
  run_in_background: true
)
```

**For ad-hoc tasks (no task folder):**
```bash
Bash(
  command: 'env -u CLAUDECODE claude -p "[task description]" --cwd "D:/path/repo"',
  run_in_background: true
)
```

**Why this pattern:**
- `Bash` tool with `run_in_background: true` — returns background task ID instantly
- `env -u CLAUDECODE` — unsets blocking env var for nested claude invocation
- `run-task.sh` — kernel governance, session resume, per-agent state isolation
- Each agent gets `agent_id` from subfolder name (backlog 153)
- Actions route to isolated `agent-{id}-actions.jsonl`, no shared state contention

**run-task.sh arguments:** `[REPO_ROOT] [MAX_ITERATIONS] [TASK_SUBFOLDER]`
- First arg = repo root with CLAUDE.md (NOT the task folder path)
- Second arg = task count + 2 buffer
- Third arg = subfolder name under `tasks/` (just the name, not full path)

**WRONG patterns (do NOT use):**
- `Agent(prompt: "env -u CLAUDECODE bash -c '...'")` — unnecessary Agent wrapper
- Passing task folder as first arg to run-task.sh — causes "Not a kernel repo" error

---

**Key principle:** Non-blocking background execution with independent environment (env -u CLAUDECODE) and per-agent state isolation enables true parallel work.
