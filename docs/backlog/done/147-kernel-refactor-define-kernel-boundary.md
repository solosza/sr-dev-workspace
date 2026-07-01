# Define Kernel Boundary — Separate Core from Extensions

## Status
Open

## Priority
High — prerequisite for state isolation (Phase 1) and CI (Phase 2-4). Three repos have diverged with no sync mechanism. Adding more features to a bloated kernel makes the problem worse.

## Summary

The kernel repo (isagawa-kernel) was designed to be minimalistic — the loop (session-start → anchor → work → complete → learn) plus domain-setup. But workspace-specific tools (execute-pipeline, task-builder, prod-test, spawn-agent-swarm) have accumulated in the kernel namespace. Three repos now have diverged copies: sr_dev_workspace (latest), isagawa-kernel (behind), hmsa-healthcare-qa (independently evolved). There's no manifest defining what's kernel vs extension, and no sync mechanism.

## Design Documents

| Document | Purpose |
|----------|---------|
| [[147-kernel-refactor-define-kernel-boundary/kernel-manifest]] | Define exactly what files are core kernel, create manifest.json |
| [[147-kernel-refactor-define-kernel-boundary/extension-separation]] | Move extensions out of kernel namespace, define extension architecture |
| [[147-kernel-refactor-define-kernel-boundary/sync-mechanism]] | Workspace → kernel repo sync for core items only |
| [[147-kernel-refactor-define-kernel-boundary/three-way-resolve]] | Resolve divergence between sr_dev_workspace, isagawa-kernel, hmsa-healthcare-qa |

## Current State (from diff analysis)

### Three-way divergence:
- **sr_dev_workspace** — latest kernel + 12 extensions + domain-specific tools
- **isagawa-kernel** — stale kernel, task-builder has old 8-step numbering (workspace has 10)
- **hmsa-healthcare-qa** — independently evolved, has execute-pipeline + spawn-agent-swarm but different versions, plus domain skills (healthcare-qa, create-sit-xlsx, test-pipeline, validate-tc)

### Proposed boundary:

**CORE KERNEL** (isagawa-kernel):
- Commands: `session-start`, `anchor`, `learn`, `complete`, `fix`, `domain-setup`, `reset`
- Hooks: `universal-gate-enforcer.py`, `actions-log-appender.py`, `test-failure-detector.py`, `auto-approve-claude-writes.py`
- Scripts: `CLAUDE.md`, `run-task.sh`, `common.sh`
- Skills: `kernel-domain-setup/`, `autonomous-cycling/`
- Lessons: `lessons.md` (template with RULE ZERO only)

**EXTENSIONS** (NOT kernel — workspace-level):
- `execute-pipeline`, `task-builder`, `prod-test`, `spawn-agent-swarm`, `audit-workflow`
- `backlog`, `attest`, `scan-bookmarks`
- `elegant`, `grill`, `clone`, `spawn-subagent`

**DOMAIN-GENERATED** (per-repo, never synced back):
- `{domain}-gate-enforcer.py`, `protocols/`, `references/`, domain lessons, domain skills

## Requirements
- Create `kernel-manifest.json` listing every core kernel file (path + hash)
- domain-setup copies only manifest items into new repos
- Sync script: diff workspace kernel files against manifest, push core-only changes to isagawa-kernel
- Extensions either get their own repo (`isagawa-extensions`?) or stay workspace-local with clear separation
- Resolve the three-way drift — pick a winner per file, sync all three repos

## References
- Diff output: sr_dev_workspace vs isagawa-kernel (this session)
- Diff output: sr_dev_workspace vs hmsa-healthcare-qa (this session)
- `projects/production-readiness-solutions/summary-report.md` — Phase 1-4 depends on this
- Backlog 146 research (state isolation + CI proposals)
- Backlog 145 research (production readiness critiques)

## Task Builder Input
- **Deliverable:** Kernel manifest, sync mechanism, resolved three-way drift, clean kernel repo
- **Location:** workspace
- **Scope:** REFACTOR
- **Constraints:** Must not break existing domain repos (hmsa, sr_dev). Extensions must still work after separation. Kernel repo must remain usable standalone (clone → domain-setup → working repo).
