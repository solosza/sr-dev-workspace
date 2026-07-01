# Kernel Core vs Extension Classification

**Effective:** 2026-06-24
**References:** Feature Freeze Policy, Kernel Manifest (backlog 147)

---

## Classification Rule

If a component is part of the governance loop (`session-start → anchor → WORK → complete`, with `fix → learn` on failure) or its enforcement, it is **core**. Everything else is an **extension**.

---

## Commands

| Component | Classification | Rationale |
|-----------|---------------|-----------|
| `session-start.md` | Core | Entry point — checks state, resumes session |
| `anchor.md` | Core | Re-reads protocol, reviews inter-anchor work |
| `learn.md` | Core | Records lesson after failure, updates protocol |
| `complete.md` | Core | Final gate before marking task done |
| `fix.md` | Core | Impact assessment before any fix |
| `domain-setup.md` | Core | Creates protocol + hooks for a new domain |
| `reset.md` | Core | Dev tool — fresh state for testing |
| `execute-pipeline.md` | Extension | Backlog → tasks → run-task.sh orchestration |
| `task-builder.md` | Extension | Decomposes goals into atomic tasks |
| `autonomous-cycle.md` | Extension | Loops through tasks autonomously |
| `prod-test.md` | Extension | Production testing orchestration |
| `audit-workflow.md` | Extension | Scans kernel infrastructure for gaps |
| `backlog.md` | Extension | Creates backlog items in standard format |
| `attest.md` | Extension | Attestation workflow |
| `scan-bookmarks.md` | Extension | X bookmark scanning |
| `human-check.md` | Extension | Human-in-the-loop check workflow |

## Hooks

| Component | Classification | Rationale |
|-----------|---------------|-----------|
| `universal-gate-enforcer.py` | Core | Enforces anchor, learn gates |
| `actions-log-appender.py` | Core | Appends every action to actions.jsonl |
| `test-failure-detector.py` | Core | Sets `needs_learn` on test failure |
| `auto-approve-claude-writes.py` | Core | Auto-approves writes to `.claude/` state files |
| `sr_dev-gate-enforcer.py` | Extension | Domain-specific gate enforcement (sr_dev workspace only) |
| `agent-inline-execution-blocker.py` | Extension | Blocks inline execution in workspace |

## Skills

| Component | Classification | Rationale |
|-----------|---------------|-----------|
| `kernel-domain-setup/` | Core | Modular steps for domain-setup command |
| `autonomous-cycling/` | Core | Loop behavior spec for task cycling |
| `task-builder/` | Extension | Goal decomposition into atomic tasks |
| `execute-pipeline/` | Extension | Full pipeline orchestration skill |
| `prod-test/` | Extension | Production testing skill |
| `audit-workflow/` | Extension | Infrastructure gap scanning |
| `spawn-agent-swarm/` | Extension | Multi-agent swarm orchestration |
| `spawn-subagent/` | Extension | Single subagent spawning |
| `human-check/` | Extension | Human-in-the-loop check skill |
| `website-cloner/` | Extension | Website cloning via Playwright |

## Scripts

| Component | Classification | Rationale |
|-----------|---------------|-----------|
| `CLAUDE.md` | Core | Kernel instructions (governance loop) |
| `run-task.sh` | Core | One-shot task executor |
| `lib/common.sh` | Core | Shared shell utilities |

## Summary

| Category | Core | Extension | Total |
|----------|------|-----------|-------|
| Commands | 7 | 9 | 16 |
| Hooks | 4 | 2 | 6 |
| Skills | 2 | 8 | 10 |
| Scripts | 3 | 0 | 3 |
| **Total** | **16** | **19** | **35** |
