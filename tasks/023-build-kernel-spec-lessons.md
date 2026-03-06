# Build Kernel Spec Seeded Lessons

## Context
Build seeded lessons for the kernel spec — expert knowledge that gets installed so the agent avoids common kernel building mistakes from day one.

## Dependencies
- **020** — repo exists
- **021** — skill files exist

## Phase Gate
- [ ] `kernel-spec` repo exists at expected path
- [ ] Skill files exist in `kernel-spec/.claude/skills/kernel-build-guidance/`

## Requirements

### Build into: `D:\my_ai_projects\project_test_repos\specs\kernel-spec\.claude\lessons\`

### lessons.md (index)
Standard index format with How This Works header:
- Index points to payload files
- 200-line threshold rule
- Seeded knowledge vs learned knowledge explained

### Topic folders and payload files

**kernel/bootstrap.md**
- Hook registration is mandatory — unregistered hooks are dead code
- `settings.local.json` must list every hook file
- Restart required after hook creation — hooks load at Claude Code startup
- CLAUDE.md must reference all kernel commands accurately

**kernel/common-mistakes.md**
- Never bypass hooks by editing state directly
- Never skip re-reading during anchor ("quick anchor" is an anti-pattern)
- Every action between anchors must be logged
- "Lesson recorded" means written to disk — words are not actions
- Protocol = index (point to files, never duplicate content)
- 200-line threshold — split files when exceeded

**architecture/layering.md**
- domain-setup is the constant primitive — never rebuilt by specs
- Kernel spec = Layer 2 input that produces Layer 1 (kernel)
- Domain spec = Layer 2 input that produces Layer 3 (domain governance)
- One project = one domain = one protocol

### Source
Pull lessons from:
- `D:\my_ai_projects\project_test_repos\sr_dev_test\.claude\lessons\` (sr_dev lessons — real failures)
- `D:\my_ai_projects\isagawa-kernel` CLAUDE.md (kernel rules)
- Memory file lessons (kernel lessons section)

## Output
- `kernel-spec/.claude/lessons/lessons.md` (index)
- `kernel-spec/.claude/lessons/kernel/bootstrap.md`
- `kernel-spec/.claude/lessons/kernel/common-mistakes.md`
- `kernel-spec/.claude/lessons/architecture/layering.md`

## Validation
- [ ] `lessons.md` index exists with How This Works header
- [ ] All topic folders and payload files exist
- [ ] Index points to all payload files
- [ ] No payload content duplicated in the index
- [ ] Lessons sourced from real failures (sr_dev lessons), not invented

## Completion Signal
When ALL validation checks pass, invoke `/kernel/complete`.
