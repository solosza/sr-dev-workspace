# Kernel File List — Step 2 Reference

Exact files and directories to copy from the kernel workspace into the test repo during harness compilation. Step 2 reads this before copying — do not guess, follow this list.

## Source

The kernel source is the current workspace (sr_dev_workspace) or a golden master. All paths are relative to the kernel root.

## Directories (recursive copy)

### `.claude/commands/kernel/`

All kernel commands. Copy the entire directory:

- `session-start.md`
- `anchor.md`
- `complete.md`
- `learn.md`
- `fix.md`
- `reset.md`
- `domain-setup.md`
- `autonomous-cycle.md`
- `execute-pipeline.md`
- `task-builder.md`
- `audit-workflow.md`
- `prod-test.md`
- `backlog.md`
- `attest.md`
- `eval.md`
- `human-check.md`
- `scan-bookmarks.md`

### `.claude/protocols/`

Protocol template or active protocol. Copy entire directory.

### `.claude/hooks/`

All hook enforcement scripts:

- `universal-gate-enforcer.py` — core gate enforcement (anchor, learn blocks)
- `sr_dev-gate-enforcer.py` — domain-specific gate enforcer
- `actions-log-appender.py` — auto-increments action counter
- `test-failure-detector.py` — sets `needs_learn` on test failure
- `auto-approve-claude-writes.py` — auto-approve for headless execution
- `agent-inline-execution-blocker.py` — blocks inline agent execution

### `.claude/skills/kernel-domain-setup/`

Full domain-setup skill (required for compilation). Copy entire directory recursively.

### `.claude/skills/autonomous-cycling/`

Autonomous cycling skill for task execution. Copy entire directory recursively.

### `.claude/lessons/`

- `lessons.md` — RULE ZERO template + accumulated lessons

### `.claude/state/`

Fresh state files (overwritten by domain-setup, but needed as templates):

- `session_state.json`
- `sr_dev_workflow.json` (or domain-appropriate workflow JSON)

### `.claude/settings.local.json`

Hook registrations. Maps hook scripts to Claude Code events.

## Root Files

### `run-task.sh`

Task execution script — spawns one-shot agents for task files.

### `lib/common.sh`

Shared shell utilities used by `run-task.sh`.

### `CLAUDE.md`

Kernel CLAUDE.md — top-level agent instructions.

## Copy Rules

1. Preserve directory structure exactly
2. Create parent directories before copying (`mkdir -p`)
3. Overwrite any existing files in the test repo
4. Do NOT copy `.claude/state/actions.jsonl` or agent-specific state files
5. Do NOT copy project-specific files (tasks/, docs/, projects/)

## Verification

After copying, verify key files exist in the test repo:

```bash
test -f "<test-repo>/CLAUDE.md"
test -f "<test-repo>/run-task.sh"
test -f "<test-repo>/.claude/hooks/universal-gate-enforcer.py"
test -f "<test-repo>/.claude/hooks/actions-log-appender.py"
test -f "<test-repo>/.claude/settings.local.json"
test -f "<test-repo>/.claude/skills/kernel-domain-setup/SKILL.md"
test -f "<test-repo>/.claude/lessons/lessons.md"
```

All must pass before proceeding to Phase 2 (platform-deepeval copy).
