# Build Kernel Spec Commands

## Context
Build the commands that ship with the kernel spec. These are entry points the user invokes after installing the kernel spec. Also build the reference kernel files — the actual CLAUDE.md template, command templates, hook templates that domain-setup copies into the workspace.

## Dependencies
- **021** — skill files must exist (commands reference the workflow)
- **020** — repo exists

## Phase Gate
- [ ] `kernel-spec/.claude/skills/kernel-build-guidance/SKILL.md` exists
- [ ] `kernel-spec/.claude/skills/kernel-build-guidance/workflow.md` exists

## Requirements

### Build into: `D:\my_ai_projects\project_test_repos\specs\kernel-spec\`

### Commands (`.claude/commands/`)
Read commands from the chosen template spec (docker-spec or playwright-spec) and adapt:
- `kernel-build.md` — main build workflow (production mode, HITL)
- `kernel-build-dev.md` — dev mode (relaxed HITL)
- `kernel-on-failure.md` — failure triage during build
- `kernel-pre-build-check.md` — verify workspace before building

Each command must include:
- YAML frontmatter
- Kernel Loop Integration (anchor every 10 actions, learn on failure)
- Mandatory file reads before execution
- Production vs dev mode differences

### Reference files (`reference/`)
These are the actual kernel files that domain-setup copies into the target workspace:
- `reference/CLAUDE.md` — the kernel's CLAUDE.md (copy from `D:\my_ai_projects\isagawa-kernel\CLAUDE.md`)
- `reference/commands/` — all kernel commands (copy from isagawa-kernel `.claude/commands/kernel/`)
- `reference/hooks/` — gate enforcer and hook scripts (copy from isagawa-kernel `.claude/hooks/`)
- `reference/skills/kernel-domain-setup/` — the domain-setup skill (copy from isagawa-kernel)
- `reference/skills/autonomous-cycling/` — the cycling skill (copy from isagawa-kernel)
- `reference/settings-local.json` — hook registration template

**IMPORTANT:** Copy these from the canonical kernel repo (`D:\my_ai_projects\isagawa-kernel`), not from cognitive-agent or sr_dev_test. The canonical repo is the source of truth.

## Output
- Commands in `kernel-spec/.claude/commands/`
- Reference files in `kernel-spec/reference/`

## Validation
- [ ] All command files exist with YAML frontmatter and Kernel Loop Integration
- [ ] `reference/CLAUDE.md` exists and matches canonical kernel
- [ ] `reference/commands/` contains all kernel commands
- [ ] `reference/hooks/` contains gate enforcer and hook scripts
- [ ] `reference/skills/` contains kernel-domain-setup and autonomous-cycling
- [ ] `reference/settings-local.json` exists
- [ ] All reference files sourced from canonical kernel (`D:\my_ai_projects\isagawa-kernel`), NOT other repos

## Completion Signal
When ALL validation checks pass, invoke `/kernel/complete`.
