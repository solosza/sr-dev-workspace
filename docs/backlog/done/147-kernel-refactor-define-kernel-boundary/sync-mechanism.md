# Sync Mechanism

## Status
NEW

## What
Create a script or command that syncs core kernel files from a workspace back to isagawa-kernel. Only files in `kernel-manifest.json` get synced.

## Proposed: `kernel-sync.sh`

```bash
#!/bin/bash
# Usage: kernel-sync.sh <workspace-path> <kernel-repo-path>
# Reads kernel-manifest.json, copies listed files from workspace to kernel repo

WORKSPACE="$1"
KERNEL_REPO="$2"
MANIFEST="$KERNEL_REPO/kernel-manifest.json"

# For each file in manifest.core.*
# Copy from WORKSPACE to KERNEL_REPO
# Show diff before copying (dry-run mode)
# Commit with message: "sync: update from <workspace>"
```

## Workflow
1. Developer evolves kernel files in workspace (sr_dev_workspace)
2. Run `kernel-sync.sh` to see diff of what changed
3. Review diff — confirm only kernel files are being synced
4. Script copies and commits to isagawa-kernel feature branch
5. Developer reviews and merges

## Safety
- Never syncs domain-specific files (protocols, references, domain lessons)
- Never syncs extensions (even if they're in `.claude/commands/kernel/`)
- Dry-run mode by default — shows diff without copying
- Creates feature branch, never pushes to main directly

## Dependencies
- kernel-manifest.md (defines what to sync)
- extension-separation.md (extensions must be identified to exclude them)
