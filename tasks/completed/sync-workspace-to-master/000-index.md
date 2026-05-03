# Sync Workspace to Master — Task Index

## Source
docs/backlog/061-kernel-refactor-sync-workspace-to-master.md

## Deliverable
isagawa-kernel master repo fully synced with sr_dev_workspace kernel.

## Location
workspace (orchestrated from here, target: D:\my_ai_projects\isagawa-kernel)

## Tasks

| # | Task | Type | Description |
|---|------|------|-------------|
| 001 | build-sync-kernel-commands | BUILD | Copy 14 differing/missing kernel commands to master |
| 002 | build-sync-top-level-commands | BUILD | Copy 3 top-level commands (clone, elegant, grill) |
| 003 | build-sync-skill-autonomous-cycling | BUILD | Replace 2 differing files in autonomous-cycling |
| 004 | build-sync-skill-domain-setup | BUILD | Replace 5 differing reference files in kernel-domain-setup |
| 005 | build-sync-missing-skills | BUILD | Copy 5 missing skill folders to master |
| 006 | build-sync-hooks | BUILD | Replace 2 differing hooks + copy 4 missing hooks |
| 007 | build-sync-settings | BUILD | Update settings.local.json with all 6 hook registrations |
| 008 | build-sync-lib | BUILD | Copy lib/ directory (common.sh + attestation/) |
| 009 | build-sync-shell-scripts | BUILD | Copy run-task.sh and run-task-batch.sh |
| 010 | build-sync-lessons | BUILD | Copy .claude/lessons/ (17 files) |
| 011 | build-sync-claude-md | BUILD | Replace CLAUDE.md with current version |
| 012 | build-stamp-manifest | BUILD | Generate and write kernel-manifest.json with hashes |
| 013 | test-l1-verify-file-counts | TEST | Verify all expected files exist in master |
| 014 | test-l2-verify-content-match | TEST | Diff sr_dev vs master — zero differences for synced files |
| 015 | test-l3-verify-preservation | TEST | Verify master-only content preserved (scanner/, tests/, etc.) |
