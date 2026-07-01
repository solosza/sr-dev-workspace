# Kernel Feature Freeze Policy

**Effective:** 2026-06-23
**References:** Backlogs 147, 150

---

## Purpose

The Isagawa Kernel is a governance layer. It governs. It does not build, test, deploy, or orchestrate. This policy freezes the kernel's feature set: no new commands, hooks, or skills will be added to the kernel. All new features go to workspace extensions.

## What Constitutes "Kernel"

The kernel is the governance loop plus enforcement:

```
session-start → anchor → WORK → complete
                              ↓ (on failure)
                            fix → learn
```

If a component is not part of this loop or its enforcement, it is not kernel.

## Core Governance Components

### Commands (7)

| Command | Purpose |
|---------|---------|
| `session-start` | Check state, resume if needed |
| `anchor` | Re-read protocol, review inter-anchor work |
| `learn` | Record lesson after failure, update protocol |
| `complete` | Final gate before marking done |
| `fix` | Impact assessment before any fix |
| `domain-setup` | Create protocol + hooks for a new domain |
| `reset` | Dev tool: fresh state for testing |

### Hooks (4)

| Hook | Purpose |
|------|---------|
| `universal-gate-enforcer.py` | Enforce anchor, learn gates, protocol hash |
| `actions-log-appender.py` | Append every action to actions.jsonl |
| `test-failure-detector.py` | Set `needs_learn` on test failure |
| `auto-approve-claude-writes.py` | Auto-approve writes to `.claude/` state files |

### Skills (2)

| Skill | Purpose |
|-------|---------|
| `kernel-domain-setup/` | Modular steps for domain-setup command |
| `autonomous-cycling/` | Loop behavior for cycling through tasks |

### Scripts (3)

| Script | Purpose |
|--------|---------|
| `CLAUDE.md` | Kernel instructions (governance loop only) |
| `run-task.sh` | One-shot task executor |
| `common.sh` | Shared shell utilities |

## The Freeze Rule

**No new commands, hooks, or skills will be added to the kernel.**

- No new commands in `.claude/commands/kernel/`
- No new hooks in `.claude/hooks/`
- No new skills in `.claude/skills/` (kernel namespace)
- No new scripts at the kernel root

Improvements to existing core components (bug fixes, enforcement tightening) are permitted. New features are not.

## The Extension Path

All new capabilities go to workspace extensions, not the kernel:

- **Current extensions:** execute-pipeline, task-builder, prod-test, spawn-agent-swarm, audit-workflow, backlog, attest, scan-bookmarks, elegant, grill, clone, spawn-subagent
- **Future features:** Any new command, skill, or hook that is not part of the governance loop goes to the workspace or a separate extensions repo
- Extensions are workspace-local — they are not synced to the kernel repo

## Principles

1. **Fewer files = easier sync.** The kernel syncs across repos (sr_dev_workspace, isagawa-kernel, hmsa-healthcare-qa). Every file added to the kernel is another file to keep in sync.
2. **Fewer files = easier adoption.** A new user clones the kernel and gets governance. They don't get a build system, a task manager, or a test orchestrator unless they choose to add extensions.
3. **Fewer files = easier reasoning.** The agent re-reads the kernel at every anchor. A smaller kernel means faster, more focused re-centering.
4. **Extensions exist for power users.** The kernel exists for everyone.
