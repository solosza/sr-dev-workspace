# Create kernel-sync.sh Script

## Context
Syncs core kernel files from a workspace back to isagawa-kernel. Only files listed in kernel-manifest.json get synced. Dry-run by default.

## Type
BUILD

## Execution
inline

## Dependencies
- 002-kernel-build-kernel-manifest

## Phase Gate
- [ ] `D:/my_ai_projects/isagawa-kernel/kernel-manifest.json` exists and is valid JSON

## Requirements
- Create `D:/my_ai_projects/isagawa-kernel/kernel-sync.sh`
- Script takes two args: workspace path, kernel repo path
- Reads kernel-manifest.json to know which files to sync
- Dry-run mode by default (show diff, don't copy)
- Flag `--apply` to actually copy files
- Creates a feature branch (never pushes to main directly)
- Shows diff of each file before copying
- Use spec from docs/backlog/147-kernel-refactor-define-kernel-boundary/sync-mechanism.md

## Acceptance Criteria
- [ ] File exists: `D:/my_ai_projects/isagawa-kernel/kernel-sync.sh`
- [ ] Script is executable (has shebang line)
- [ ] Reads kernel-manifest.json for file list
- [ ] Dry-run by default (no --apply = show diff only)
- [ ] Never syncs files not in manifest

## Gates Satisfied
- BUILD-02

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
