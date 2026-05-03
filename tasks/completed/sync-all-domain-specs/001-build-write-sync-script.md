# Task 001: Write Kernel Sync Script

## Objective
Write a bash script that syncs all kernel files from the master repo (isagawa-kernel) to a target repo.

## Instructions

Write `tasks/sync-all-domain-specs/sync-kernel.sh` with the following behavior:

```bash
#!/usr/bin/env bash
# Usage: bash sync-kernel.sh <target-repo-path>
# Syncs kernel infrastructure from isagawa-kernel master to target repo.
# Preserves domain-specific content (commands, skills, protocols, state).
```

The script must:

1. **Accept one argument:** absolute path to target repo
2. **Validate:** target has `.claude/` directory
3. **Copy kernel commands:**
   - `mkdir -p "$TARGET/.claude/commands/kernel/"`
   - Copy all 15 `.md` files from `D:/my_ai_projects/isagawa-kernel/.claude/commands/kernel/`
4. **Copy kernel skills (7 folders):**
   - For each: `audit-workflow`, `autonomous-cycling`, `execute-pipeline`, `kernel-domain-setup`, `prod-test`, `task-builder`, `website-cloner`
   - `rm -rf "$TARGET/.claude/skills/$skill/"` then `cp -r` from master
5. **Copy kernel hooks (6 files):**
   - Copy: `actions-log-appender.py`, `agent-inline-execution-blocker.py`, `auto-approve-claude-writes.py`, `domain-gate-enforcer.template.py`, `test-failure-detector.py`, `universal-gate-enforcer.py`
6. **Copy infrastructure:**
   - `run-task.sh` and `run-task-batch.sh` to target root (if they don't conflict with domain scripts)
   - `mkdir -p "$TARGET/lib/attestation/"` then copy `lib/common.sh` and `lib/attestation/*.py`
   - Copy `.claude/lessons/lessons.md` (index only, not topic files — those are domain-specific)
7. **Merge settings.local.json:**
   - If exists, read and merge hook registrations
   - If doesn't exist, create with standard kernel hook registrations
   - Preserve any existing `permissions` and domain-specific settings
8. **Report:** Print summary of what was copied

The script must use absolute paths for the source (`D:/my_ai_projects/isagawa-kernel`). It must NOT use `cd`. It must NOT touch `.claude/state/`, `.claude/protocols/`, or domain-specific commands/skills.

## Acceptance Criteria
- `tasks/sync-all-domain-specs/sync-kernel.sh` exists
- Script is executable and passes `bash -n` (syntax check)

## Gate
BUILD-01
