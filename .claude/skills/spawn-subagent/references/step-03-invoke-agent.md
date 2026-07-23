# Step 3: Invoke Background Agent — Scope-Routed Isolation

## Purpose

Spawn the background agent with the correct isolation level based on backlog scope. BUILD/REFACTOR scope gets worktree isolation. RESEARCH scope gets subfolder-level isolation via run-task.sh.

## Scope Routing (CRITICAL)

Read the backlog file's `Scope` field to determine isolation mode:

| Scope | Isolation | Mechanism | Why |
|-------|-----------|-----------|-----|
| BUILD | Worktree | `Agent(isolation: "worktree", run_in_background: true)` | Code changes isolated until reviewed + merged |
| REFACTOR | Worktree | `Agent(isolation: "worktree", run_in_background: true)` | Code changes isolated until reviewed + merged |
| RESEARCH | Subfolder | `Bash(run_in_background: true)` + unique subfolder | No code to merge, but needs lock isolation |
| TEST | Subfolder | `Bash(run_in_background: true)` + unique subfolder | Tests don't change main, just produce reports |

## Launcher-Death: Spawned Agent Must Block on Its Own Pipeline (CRITICAL)

The `run_in_background: true` on the outer `Agent(...)`/`Bash(...)` call below is what makes the CALLER non-blocking — that's correct and required. It does NOT license the SPAWNED agent to detach the pipeline it runs inside its own turn.

Once the spawned agent is executing, `run-task.sh` / `run-spec-factory.sh` / `prod-test` MUST run in that agent's FOREGROUND — the agent blocks on it and does not end its turn until the pipeline finishes or definitively fails. The spawned agent must NOT nest another `run_in_background: true`, background the pipeline with a shell `&`, or otherwise detach-then-return inside its own session. A detached child does not outlive the sub-agent session that spawned it — if the spawned agent ends its turn while the pipeline runs detached, the pipeline dies silently with no error. This is why Pattern A's prompt below says "Wait for completion" — that instruction is mandatory, not optional framing.

## Pattern A: Worktree Mode (BUILD / REFACTOR)

Use the Agent tool with `isolation: "worktree"`:

```
Agent(
  description: "Pipeline: [backlog title]",
  prompt: "Run this command and return full output:
    env -u CLAUDECODE bash \"[repo_path]/run-task.sh\" \"[repo_path]\" [count+2] \"[subfolder]\" \"[backlog_path]\"
    Wait for completion. Return the full output including final status banner.
    Do NOT background this command and end your turn — run it in your foreground and block until it completes or definitively fails (launcher-death).",
  isolation: "worktree",
  run_in_background: true
)
```

**What happens:**
1. Agent tool creates a temporary git worktree with a new branch from HEAD
2. Agent runs inside the worktree — all edits happen on the feature branch
3. `.claude/state/` is naturally isolated (separate working directory)
4. No lock contention — each worktree has its own lock file
5. On completion:
   - If no changes → worktree auto-cleaned
   - If changes → worktree path + branch name returned in result
6. Feature branch enters review queue for merge via `/kernel/review-queue accept`

**Result handling:** When the Agent completes, extract:
- `worktree_branch` — the feature branch name
- `worktree_path` — path to the worktree directory

Record in `pipeline_state` (session_state.json):
```json
{
  "pipeline_state": {
    "worktree_mode": true,
    "worktree_branch": "worktree/pipeline-NNN-...",
    "worktree_path": ".claude/worktrees/pipeline-NNN",
    "merge_status": "pending_review"
  }
}
```

Register in `review-status.json`:
```json
{
  "NNN": {
    "status": "unreviewed",
    "worktree_branch": "worktree/pipeline-NNN-...",
    "worktree_path": ".claude/worktrees/pipeline-NNN",
    "merge_status": "pending_review",
    "scope": "BUILD"
  }
}
```

## Pattern B: Subfolder Mode (RESEARCH / TEST)

Use Bash tool with a **unique subfolder per backlog** (prevents lock contention):

```bash
Bash(
  command: 'env -u CLAUDECODE bash "[repo_path]/run-task.sh" "[repo_path]" [count+2] "[subfolder]" "[backlog_path]"',
  run_in_background: true,
  description: "Pipeline: [backlog title]"
)
```

**CRITICAL: Always use a unique subfolder.** Derive from backlog filename:
- Backlog `188-kernel-research-llm-market-shift-analysis.md` → subfolder `llm-market-shift-research`
- Backlog `189-kernel-research-curiosity-harness.md` → subfolder `curiosity-harness-research`

**NEVER pass empty string `""` as subfolder when spawning concurrent agents.** Empty subfolder → `default_run-task.lock` → lock contention between concurrent spawns.

## run-task.sh Arguments

| Argument | What | Example |
|----------|------|---------|
| 1st | Repo root (must have CLAUDE.md) | `D:/my_ai_projects/project_test_repos/sr_dev_workspace` |
| 2nd | Max iterations (tasks + 2 buffer) | `6` |
| 3rd | Subfolder name under `tasks/` | `llm-market-shift-research` |
| 4th | Backlog file path (enables move-to-done) | `docs/backlog/188-kernel-research-llm-market-shift-analysis.md` |

**WRONG:** Passing full task folder path as first arg. run-task.sh checks for CLAUDE.md in the first arg.

## Per-Agent State Isolation

**Worktree mode (BUILD/REFACTOR):**
- Separate working directory = separate `.claude/state/` files
- No shared mutable state between agents
- Feature branch preserves all changes until merge

**Subfolder mode (RESEARCH/TEST):**
- `agent_id` derived from the subfolder name
- Actions logged to `.claude/state/agent-{subfolder}-actions.jsonl`
- Unique lock file per subfolder: `{subfolder}_run-task.lock`
- Concurrent spawns safe as long as subfolders are unique

## Implementation

1. Read the backlog file → extract `Scope` field
2. Resolve task subfolder from backlog filename (ALWAYS unique, NEVER empty)
3. Resolve backlog path for the 4th arg
4. Count tasks in the folder to compute MAX_ITERATIONS
5. **Route by scope:**
   - BUILD/REFACTOR → Agent tool with `isolation: "worktree"`, `run_in_background: true`
   - RESEARCH/TEST → Bash tool with `run_in_background: true`
6. Capture the task ID from the response
7. If worktree mode: register in review-status.json
8. Return task ID to Step 4

## Non-Blocking Guarantee

**CRITICAL:** Both patterns return control immediately.

- Agent/Bash `run_in_background: true` returns a task ID instantly
- Background process runs independently
- User can spawn multiple agents in parallel
- Use `TaskOutput(task_id, block: false)` to check progress

## Error Cases

| Error | Cause | Fix |
|-------|-------|-----|
| "Not a kernel repo (no CLAUDE.md)" | First arg is task folder, not repo root | Use repo root as first arg |
| "No tasks found" | Task folder empty or wrong subfolder | Check `tasks/[subfolder]/` exists |
| Lock contention | Empty subfolder, concurrent spawns | Always use unique subfolder per backlog |
| "Another run-task.sh already running" | Same subfolder used twice | Derive unique subfolder from backlog filename |
| Hook blocks | `anchored: false` in shared state | Agent handles via one_shot mode |

## Related Documentation

- → `run-task.sh` — Task execution script (lines 1-30 for usage)
- → `projects/worktree-research/` — Full worktree isolation research + design
- → `.claude/lessons/lessons.md` RULE ZERO: "USE BACKGROUND AGENT + env -u CLAUDECODE FOR RUN-TASK.SH"
- → `.claude/hooks/actions-log-appender.py` — Per-agent log routing
