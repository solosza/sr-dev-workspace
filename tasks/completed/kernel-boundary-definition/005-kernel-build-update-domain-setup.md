# Update domain-setup to Use Kernel Manifest

## Context
domain-setup currently copies the entire .claude/ directory. It should read kernel-manifest.json and copy only listed files.

## Type
BUILD

## Execution
inline

## Dependencies
- 002-kernel-build-kernel-manifest

## Phase Gate
- [ ] `D:/my_ai_projects/isagawa-kernel/kernel-manifest.json` exists

## Requirements
- Read current domain-setup command: `D:/my_ai_projects/isagawa-kernel/.claude/commands/kernel/domain-setup.md`
- Read domain-setup skill: `D:/my_ai_projects/isagawa-kernel/.claude/skills/kernel-domain-setup/SKILL.md`
- Add instruction that domain-setup should reference kernel-manifest.json for what to copy
- The manifest becomes the authoritative list of files domain-setup installs
- Do not break existing domain-setup behavior for repos that already have the kernel

## Acceptance Criteria
- [ ] domain-setup command or skill references kernel-manifest.json
- [ ] grep "kernel-manifest" returns match in domain-setup files

## Gates Satisfied
- BUILD-04

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
