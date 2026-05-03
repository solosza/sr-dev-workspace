# Refactor: Sync All Domain Specs to Master Kernel

## Status
Open

## Priority
High — kernel drift across 18 repos means governance gaps, stale hooks, missing commands, and inconsistent behavior

## Summary
All domain specs across isagawa-co repos need to be refactored to match this workspace's kernel (sr_dev_workspace). This kernel is the master. Every repo with a `.claude/` directory gets audited: commands diffed, skills diffed, hooks diffed. Missing features get added. Outdated versions get replaced with the master's version. Domain-specific commands/skills are preserved; kernel-level infrastructure is synchronized.

## Master Kernel Feature Inventory (sr_dev_workspace)

### Commands (15)
| Command | Purpose |
|---------|---------|
| `anchor.md` | Re-read protocol + check work quality |
| `attest.md` | Sigstore/Rekor attestation pipeline |
| `audit-workflow.md` | Scan for gaps + auto-fix |
| `autonomous-cycle.md` | Loop through tasks autonomously |
| `backlog.md` | Create backlog items |
| `complete.md` | Final gate before done |
| `domain-setup.md` | Create protocol + hooks |
| `execute-pipeline.md` | Backlog to tasks to run-task.sh |
| `fix.md` | Impact assessment before fixes |
| `learn.md` | Update protocol + hooks after failure |
| `prod-test.md` | Production test a deliverable |
| `reset.md` | Dev tool: fresh state |
| `scan-bookmarks.md` | X bookmark scanner |
| `session-start.md` | Check state and resume |
| `task-builder.md` | Decompose goals into tasks |

### Skills (7)
| Skill | Purpose |
|-------|---------|
| `audit-workflow/` | Gap scanning + auto-fix |
| `autonomous-cycling/` | Task loop behavior spec |
| `execute-pipeline/` | Full autonomous pipeline |
| `kernel-domain-setup/` | Protocol + hook creation |
| `prod-test/` | Production testing framework |
| `task-builder/` | Goal decomposition + execution |
| `website-cloner/` | Playwright-based site extraction |

### Hooks (6)
| Hook | Purpose |
|------|---------|
| `actions-log-appender.py` | Append-only action ledger |
| `agent-inline-execution-blocker.py` | Block inline agent execution |
| `auto-approve-claude-writes.py` | Auto-approve .claude/ writes |
| `[domain]-gate-enforcer.py` | Domain-specific gate enforcement |
| `test-failure-detector.py` | Detect test failures, set needs_learn |
| `universal-gate-enforcer.py` | Session/anchor/learn gates |

### Supporting Infrastructure
| File | Purpose |
|------|---------|
| `run-task.sh` | One-shot task execution with resume |
| `lib/common.sh` | Shared shell helpers |
| `lib/attestation/intent.py` | Intent chain recording |
| `.claude/state/` | Session + workflow state |
| `.claude/lessons/lessons.md` | Actionable lessons cheat sheet |
| `.claude/protocols/[domain]-protocol.md` | Domain protocol |

## Design Documents

| Document | Purpose |
|----------|---------|
| [[057-kernel-refactor-sync-all-domain-specs/repo-inventory]] | All 18 repos with current kernel features |
| [[057-kernel-refactor-sync-all-domain-specs/diff-strategy]] | How to diff and sync each feature category |
| [[057-kernel-refactor-sync-all-domain-specs/preservation-rules]] | What to keep (domain-specific) vs replace (kernel infrastructure) |

## Repos to Sync (18)

| Repo | Location | Kernel Age |
|------|----------|------------|
| cognitive-agent | project_test_repos | Old (2 hooks, no core commands) |
| domain-spec-factory | project_test_repos | Recent (has execute-pipeline, task-builder) |
| game-dev | project_test_repos | Medium (5 hooks, 1 skill) |
| game-engine-master | project_test_repos | Medium (5 hooks, 1 skill) |
| healthcare-qa-spec-master | project_test_repos | Medium (5 hooks, 1 skill) |
| hmsa-healthcare-qa | project_test_repos | Recent (has execute-pipeline, task-builder) |
| isagawa-qa-zentyant | project_test_repos | Old (2 hooks, no core commands) |
| platform-deepeval | project_test_repos | Medium (4 hooks, some skills) |
| platform-playwright | project_test_repos | Old (2 hooks, no core commands) |
| platform-selenium | project_test_repos | Old (2 hooks, no core commands) |
| test-content-production | project_test_repos | Old (2 hooks, no CLAUDE.md) |
| test-kernel-bootstrap | project_test_repos | Old (2 hooks, mixed commands) |
| test-platform-deepeval | project_test_repos | Old (2 hooks, no commands) |
| isagawa-kernel | top-level | Minimal (2 hooks, 2 skills) |
| isagawa-kernel-a | top-level | Legacy (playwright enforcer) |
| isagawa-kernel-b | top-level | Legacy (playwright enforcer) |
| py_sel_framework_mcp | top-level | Legacy (old qa-gate-enforcer) |
| qa_kernel_test | top-level | Legacy (old qa-gate-enforcer) |

## Requirements
- Inventory master kernel features (done above)
- For each repo: diff commands, skills, hooks against master
- Replace outdated kernel infrastructure with master versions
- Preserve domain-specific commands/skills (e.g., `qa-workflow.md`, `game-build.md`)
- Update CLAUDE.md in each repo to reflect new command set
- Update protocols to reference new commands/skills
- Test: each synced repo should pass `bash -n` on hooks, and commands should be parseable

## Dependencies
- **Backlog 061** (sync sr_dev_workspace → isagawa-kernel) — MUST complete first. The master repo is currently behind sr_dev_workspace. 061 updates the master, then 057 fans it out to all 18 repos.
- **Backlog 058** (done) — artifact versioning research. Manifest schema ready to stamp during sync.

## References
- Master kernel: `D:\my_ai_projects\isagawa-kernel` (source of truth AFTER 061 completes)
- Working kernel: `D:\my_ai_projects\project_test_repos\sr_dev_workspace\.claude\`
- All repos listed in inventory above

## Task Builder Input
- **Deliverable:** All 18 repos synced to master kernel, with diffs documented and domain-specific content preserved
- **Location:** `workspace` (orchestration from here, edits in each target repo)
- **Scope:** REFACTOR
- **Constraints:** Must preserve domain-specific commands/skills. Must not break existing protocols. Each repo is a separate git repo. Backlog 061 must complete first (master must be current). Stamp kernel-manifest.json in each repo during sync.
