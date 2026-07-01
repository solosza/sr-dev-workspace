# Verify Kernel Boundary — Only Governance Files in Manifest

## Context
Final verification that the manifest contains only governance files and no extensions leaked in.

## Type
TEST

## Execution
agent

## Dependencies
- 003-kernel-build-sync-script
- 004-kernel-refactor-strip-extensions
- 005-kernel-build-update-domain-setup

## Phase Gate
- [ ] `D:/my_ai_projects/isagawa-kernel/kernel-manifest.json` exists
- [ ] `D:/my_ai_projects/isagawa-kernel/kernel-sync.sh` exists
- [ ] `projects/kernel-boundary/extension-list.md` exists

## Requirements
- Parse kernel-manifest.json and verify every listed file exists in isagawa-kernel
- Verify NO extension files are in the manifest (no execute-pipeline, task-builder, prod-test, backlog, attest, scan-bookmarks, elegant, grill, clone, spawn-subagent, spawn-agent-swarm, audit-workflow)
- Verify manifest only contains: loop commands, hooks, scripts, kernel skills, lessons template
- Report pass/fail for each check

## Acceptance Criteria
- [ ] All files in manifest exist on disk in isagawa-kernel
- [ ] Zero extension files found in manifest
- [ ] All governance files are present in manifest (nothing missing)

## Gates Satisfied
- TEST-01

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
