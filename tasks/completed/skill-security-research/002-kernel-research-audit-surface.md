# Research: Define the Audit Surface

## Context
Before designing static analysis checks, need to understand what a skill consists of — all the attack surfaces that a malicious or poorly-written skill could exploit.

## Type
RESEARCH

## Execution
inline

## Dependencies
- 001-kernel-build-create-project-dir.md

## Phase Gate
- [ ] `projects/skill-security-research/` exists

## Requirements
- Read `.claude/skills/task-builder/SKILL.md` — document its structure as an example of a well-formed skill
- Read `.claude/agents/` if it exists, or describe the expected YAML frontmatter format for named agents
- Map all attack surfaces: tool invocations, file paths, bash commands embedded in markdown, network calls, state file access, model routing
- For each surface: what's the worst-case exploit? (e.g., SKILL.md that runs `rm -rf` via Bash, agent that exfiltrates via WebFetch, skill that rewrites kernel state files)
- Assess: which surfaces are detectable by static analysis (reading the markdown/YAML) vs only detectable at runtime?
- Write to `projects/skill-security-research/audit-surface-analysis.md`

## Acceptance Criteria
- [ ] `projects/skill-security-research/audit-surface-analysis.md` exists
- [ ] File documents skill formats (SKILL.md and agent YAML)
- [ ] File maps attack surfaces with worst-case exploits
- [ ] File distinguishes static-detectable vs runtime-only risks

## Gates Satisfied
- DOC-02, DOC-03

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
