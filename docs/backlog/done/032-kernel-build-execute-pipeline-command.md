# Build /kernel/execute-pipeline Command

## Status
Open

## Priority
High — user does backlog → task-builder → run-task.sh manually every time, this automates the full chain

## Summary
Create `/kernel/execute-pipeline` — a fully autonomous orchestration command that chains `/kernel/backlog` → `/kernel/task-builder` → `run-task.sh` in one invocation. User describes what they want, the command creates the backlog item, decomposes into tasks, and executes them via run-task.sh — all under kernel governance. Follows the same outer-agent pattern as `/kernel/prod-test`: the command runs in the current kernel-enabled workspace, spawns sub-agents and run-task.sh as needed, tasks use absolute paths to operate on any target.

## Requirements

### Command + Skill
- Command: `.claude/commands/kernel/execute-pipeline.md`
- Skill: `.claude/skills/execute-pipeline/SKILL.md` + `references/` (wikilink tiered indexing)
- Follow prod-test as structural reference (command → skill → step references)

### Pipeline Steps
1. Parse input — detect mode:
   - If argument is an existing `.md` file path → use as backlog item (skip step 2)
   - Otherwise → treat as natural language goal (proceed to step 2)
2. Create backlog item (SKIP if existing backlog provided) — invoke `/kernel/backlog` inline, capture file path
3. Decompose into tasks — invoke `/kernel/task-builder` with backlog file path, `--skip-review` flag (skip step 7), `--no-execute` flag (stop after step 8)
4. Execute tasks — spawn `run-task.sh` against the task folder in current repo
5. Validate + report — read results, report pass/fail

### Task-Builder Modifications (3 gaps to close)
- **`--skip-review` flag**: When set, task-builder skips step 7 (plan review) and goes straight to step 8. Standalone task-builder unchanged.
- **`--no-execute` flag**: When set, task-builder stops after step 8 (write tasks). Does not start cycling in step 9. Hands task folder back to caller.
- **Backlog file input**: When argument is a backlog file path, task-builder reads the Task Builder Input section as its goal. Convention: if argument ends in `.md` and file exists, read it.

### Execution Model
- Outer agent is kernel-governed (session-start, anchor, full loop)
- run-task.sh runs OUTSIDE the inner loop — spawned as subprocess from outer agent
- Tasks in sr_dev_workspace use absolute paths to operate on target repos/directories
- Sub-agents spawned for steps that need isolated claude -p sessions (e.g., domain-setup in another repo triggers restart, next run-task.sh iteration picks up fresh)
- Fully autonomous — no pause points, no user approval

### Key Principles
- All user context passes through verbatim: natural language → backlog → task-builder input
- Composable — callable standalone or by other commands
- Runs in any kernel-enabled workspace (not workspace-specific)
- Same outer-agent pattern as prod-test

## References
- Prod-test command (structural reference): `.claude/commands/kernel/prod-test.md`
- Prod-test skill: `.claude/skills/prod-test/SKILL.md`
- Task-builder skill: `.claude/skills/task-builder/SKILL.md`
- Backlog command: `.claude/commands/kernel/backlog.md`
- run-task.sh: `run-task.sh`, `run-task-batch.sh`
- Backlog 031 (first use case): `docs/backlog/031-domain-build-hmsa-healthcare-qa-workspace.md`

## Task Builder Input
- **Deliverable:** `/kernel/execute-pipeline` command + skill installed in sr_dev_workspace, task-builder modified with --skip-review and --no-execute flags and backlog file input, tested end-to-end by executing backlog 031
- **Scope:** BUILD
- **Constraints:** Task-builder modifications must not break standalone usage. Skill follows wikilink tiered indexing (SKILL.md + references/). First real test is backlog 031 (hmsa-healthcare-qa workspace).
