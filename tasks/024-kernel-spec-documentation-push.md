# Kernel Spec Documentation and Push

## Context
Final task for the kernel spec. Write docs, verify all files, commit, push to GitHub.

## Dependencies
- **020** — repo exists
- **021** — skill files built
- **022** — commands + reference files built
- **023** — lessons built

## Phase Gate
- [ ] `kernel-spec/.claude/skills/kernel-build-guidance/SKILL.md` exists
- [ ] `kernel-spec/.claude/commands/` has command files
- [ ] `kernel-spec/reference/CLAUDE.md` exists
- [ ] `kernel-spec/.claude/lessons/lessons.md` exists

## Requirements

### Build into: `D:\my_ai_projects\project_test_repos\specs\kernel-spec\`

### README.md
- Overview: What this spec is — a bootstrap spec that builds the Isagawa Kernel
- Install flow: domain-setup reads this spec → builds kernel → restart → kernel active
- What gets built: CLAUDE.md, commands, hooks, skills, state
- Prerequisites: Claude Code, domain-setup skill installed
- Directory structure tree
- After install: how to add a domain spec on top

### FRAMEWORK.md
- Bootstrap architecture: domain-setup → kernel spec → kernel
- File mapping: which reference file becomes which workspace file
- Sequence diagram: fresh workspace → kernel → domain spec → governed workspace
- Layer model: domain-setup (constant) → kernel spec (Layer 2) → kernel (Layer 1) → domain spec (Layer 2) → domain governance (Layer 3)

### Commit and push
- `git add` all files in kernel-spec repo
- Commit message: `feat: complete kernel spec — bootstrap the Isagawa Kernel from a skill`
- Push to `isagawa-co/kernel-spec` main branch

## Output
- `kernel-spec/README.md`
- `kernel-spec/FRAMEWORK.md`
- All files committed and pushed

## Validation
- [ ] README.md exists with all sections
- [ ] FRAMEWORK.md exists with all sections
- [ ] `git status` shows no uncommitted files
- [ ] Push succeeded

## Completion Signal
When ALL validation checks pass, invoke `/kernel/complete`.
