# Research: Read Anthropic Frontend Design Skill

## Context
Anthropic published a frontend-design skill at github.com/anthropics/skills/tree/main/skills/frontend-design. Need to read it and document exactly what it instructs Claude to do before writing any CSS/HTML.

## Type
RESEARCH

## Execution
inline

## Dependencies
- 001-kernel-build-create-project-dir.md

## Phase Gate
- [ ] `projects/frontend-design-research/` exists

## Requirements
- WebFetch `https://github.com/anthropics/skills/tree/main/skills/frontend-design` — read the skill file(s)
- Document: what does the skill instruct Claude to do? What aesthetic options does it present? How does it enforce aesthetic direction before code?
- Note: is this designed for claude.ai artifact-based development or file-based HTML/CSS development?
- Note: what specific aesthetic systems does it reference (Brutalism, Minimalism, Retro-futurism, etc.)?
- Write to `projects/frontend-design-research/skill-summary.md`

## Acceptance Criteria
- [ ] `projects/frontend-design-research/skill-summary.md` exists
- [ ] File describes what the skill instructs Claude to do
- [ ] File covers aesthetic selection mechanism
- [ ] File addresses artifact-based vs file-based applicability

## Gates Satisfied
- DOC-02, DOC-03

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
