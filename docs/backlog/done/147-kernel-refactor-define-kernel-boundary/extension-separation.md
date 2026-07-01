# Extension Separation

## Status
NEW

## What
Move extensions out of the kernel namespace so they're clearly separate from core. Define how extensions are installed, updated, and discovered.

## Extensions to Separate

| Extension | Type | Files |
|-----------|------|-------|
| task-builder | Skill + Command | `.claude/skills/task-builder/`, `.claude/commands/kernel/task-builder.md` |
| execute-pipeline | Skill + Command | `.claude/skills/execute-pipeline/`, `.claude/commands/kernel/execute-pipeline.md` |
| prod-test | Skill + Command | `.claude/skills/prod-test/`, `.claude/commands/kernel/prod-test.md` |
| spawn-agent-swarm | Skill + Command | `.claude/skills/spawn-agent-swarm/`, `.claude/commands/kernel/spawn-agent-swarm.md` |
| audit-workflow | Skill + Command | `.claude/skills/audit-workflow/`, `.claude/commands/kernel/audit-workflow.md` |
| backlog | Command | `.claude/commands/kernel/backlog.md` |
| attest | Command + Lib | `.claude/commands/kernel/attest.md`, `lib/attestation/` |
| scan-bookmarks | Command | `.claude/commands/kernel/scan-bookmarks.md` |
| spawn-subagent | Skill + Command | `.claude/skills/spawn-subagent/`, `.claude/commands/spawn-subagent.md` |
| elegant | Command | `.claude/commands/elegant.md` |
| grill | Command | `.claude/commands/grill.md` |
| clone/website-cloner | Skill + Command | `.claude/skills/website-cloner/`, `.claude/commands/clone.md` |

## Options

### Option A: Extensions repo (`isagawa-co/isagawa-extensions`)
- Separate repo with all extensions
- domain-setup can optionally install extensions from this repo
- Pro: clean separation, versioned independently
- Con: another repo to manage, sync complexity

### Option B: Extensions stay workspace-local
- Extensions live in whatever workspace developed them
- domain-setup only installs kernel, user manually copies extensions they want
- Pro: simplest, no new repo
- Con: no sharing between workspaces without manual copy

### Option C: Kernel repo with `extensions/` directory
- isagawa-kernel has `core/` and `extensions/` at top level
- domain-setup installs core always, extensions optionally
- Pro: single repo, clear boundary
- Con: kernel repo isn't truly minimal anymore (just organized)

## Decision needed
User should pick Option A, B, or C before implementation.

## Dependencies
- kernel-manifest.md (defines what's core, everything else is extension)
