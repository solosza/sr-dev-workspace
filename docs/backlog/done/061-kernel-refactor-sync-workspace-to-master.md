# Refactor: Sync sr_dev_workspace Kernel to isagawa-kernel Master Repo

## Status
Open

## Priority
High — isagawa-kernel (the published master) is far behind sr_dev_workspace (the working kernel). Must complete before 057 (sync master to all 18 repos).

## Summary
The sr_dev_workspace has the latest kernel: 15 commands, 7 skills, 6 hooks, full infrastructure. The isagawa-kernel master repo has only 9 commands (8 differ), 2 skills (both differ), 2 hooks (both differ significantly), and is missing all infrastructure (lib/, run-task.sh, lessons/, attestation/, settings). This backlog syncs sr_dev_workspace → isagawa-kernel so the master repo is current before 057 fans it out to all 18 repos.

## Design Documents

| Document | Purpose |
|----------|---------|
| [[061-kernel-refactor-sync-workspace-to-master/commands-diff]] | 15 commands: 8 differ, 6 missing, 1 identical, plus 3 top-level |
| [[061-kernel-refactor-sync-workspace-to-master/skills-diff]] | 7 skills: 2 differ (7 files), 5 missing (47 files) |
| [[061-kernel-refactor-sync-workspace-to-master/hooks-diff]] | 6 hooks: 2 differ (296 diff lines), 4 missing, settings registration |
| [[061-kernel-refactor-sync-workspace-to-master/infrastructure-diff]] | lib/, run-task.sh, lessons/, CLAUDE.md, settings |
| [[061-kernel-refactor-sync-workspace-to-master/preservation-rules]] | Master-only content to preserve: scanner/, delegation/, tests/, README, LICENSE |

## Sync Summary

| Category | sr_dev | Master | Action |
|----------|--------|--------|--------|
| Kernel commands | 15 | 9 (8 differ) | Replace 8, add 6 |
| Top-level commands | 3 | 0 | Add 3 |
| Skills | 7 (47 files) | 2 (14 files) | Replace 7 files, add 5 folders |
| Hooks | 6 | 2 (both differ) | Replace 2, add 4 |
| lib/ | 8 files | 0 | Add all |
| Shell scripts | 2 | 0 | Add both |
| Lessons | 17 files | 0 | Add all |
| CLAUDE.md | Current | 72 lines behind | Replace |
| Settings | Full | 2 hooks only | Update |

## Requirements
- Diff every shared file, replace with sr_dev version where they differ
- Copy all files missing from master
- Preserve master-only content (scanner/, delegation/, lessons/ Python, tests/, README, LICENSE, CONTRIBUTING)
- Update settings.local.json to register all 6 hooks
- Replace CLAUDE.md with current version
- Copy domain gate enforcer as a template file
- Stamp `kernel-manifest.json` (from 058 research) as first versioned artifact
- Git commit the sync with clear message

## References
- Master kernel: `D:\my_ai_projects\isagawa-kernel`
- Source of truth: `D:\my_ai_projects\project_test_repos\sr_dev_workspace\.claude\`
- Backlog 057: sync master to all 18 repos (depends on this completing first)
- Backlog 058 (done): artifact versioning research — manifest schema ready

## Task Builder Input
- **Deliverable:** isagawa-kernel master repo fully synced with sr_dev_workspace kernel
- **Location:** `workspace` (orchestrated from here, target is `D:\my_ai_projects\isagawa-kernel`)
- **Scope:** REFACTOR
- **Constraints:** Additive + replace only, never delete master-only content. Must commit result. 057 depends on this.
