# Spawn Subagent — Skill Specification

## Identity

**Skill:** spawn-subagent
**Purpose:** Spawn an autonomous agent to execute a task in the background without blocking the user
**Input:** Task description (string)
**Output:** Task ID + non-blocking control return
**Platform:** Bash subprocess with `env -u CLAUDECODE bash run-task.sh` (via execute-pipeline)
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
| `references/step-03-invoke-agent.md` | Scope-routed isolation: worktree (BUILD) or subfolder (RESEARCH) |
| `references/step-04-return-task-id.md` | Capture task ID and return immediately (non-blocking) |
| `references/error-handling.md` | Error cases and recovery strategies |

---

## Overview

This skill transforms `/spawn-subagent [description]` into a background agent via execute-pipeline. All spawns go through: backlog → task-builder → run-task.sh. No raw `claude -p` — every agent gets state isolation.

**Steps:**
1. Parse the task description provided by user
2. Validate it's suitable for background execution (not requiring immediate results)
3. Route by scope: BUILD/REFACTOR → `Agent(isolation: "worktree")`, RESEARCH/TEST → `Bash`
4. Capture the background task ID from the response
5. If worktree mode: register feature branch in review-status.json
6. Return task ID to user immediately (non-blocking)
7. User gets notified on completion, or checks with `TaskOutput(task_id, block: false)`

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
Agent: Parse description → create backlog → build tasks
  ↓
Agent: Read backlog scope
  ↓
BUILD/REFACTOR?                    RESEARCH/TEST?
  ↓                                  ↓
Agent(isolation: "worktree",       Bash(run_in_background: true):
  run_in_background: true)           env -u CLAUDECODE bash run-task.sh
  ↓                                  [unique subfolder per backlog]
Worktree + feature branch            ↓
  ↓                                Subfolder isolation (unique lock)
Register in review-status.json       ↓
  ↓                                Return task ID
Return task ID                       ↓
  ↓                                User continues working
User continues working
  ↓
On completion: /kernel/review-queue accept → merge to main
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

## Working Implementation Pattern — Scope-Routed Isolation

Spawns are routed by backlog scope to the correct isolation mechanism.

→ See `references/step-03-invoke-agent.md` for full implementation details.

### Scope Routing Table

| Scope | Isolation | Tool | Merge Gate |
|-------|-----------|------|------------|
| BUILD | Worktree | `Agent(isolation: "worktree")` | Yes — `/kernel/review-queue accept` merges |
| REFACTOR | Worktree | `Agent(isolation: "worktree")` | Yes — `/kernel/review-queue accept` merges |
| RESEARCH | Subfolder | `Bash(run_in_background: true)` | No — output lands directly |
| TEST | Subfolder | `Bash(run_in_background: true)` | No — reports only |

### Common Requirements

- All spawns go through `run-task.sh` — kernel governance, session resume, per-agent state isolation
- `env -u CLAUDECODE` — unsets blocking env var for nested claude invocation
- **Always use unique subfolder per backlog** — NEVER pass empty `""` for concurrent spawns

**WRONG patterns (do NOT use):**
- `claude -p "[task description]"` — bypasses run-task.sh, no state isolation
- Empty subfolder `""` with concurrent spawns — lock contention
- Passing task folder as first arg — causes "Not a kernel repo" error

---

**Key principle:** Scope determines isolation. BUILD/REFACTOR get worktree + merge gate. RESEARCH/TEST get unique subfolder. Every spawn goes through run-task.sh.
