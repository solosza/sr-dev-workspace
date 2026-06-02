# Research: Read Superpowers README and Inventory All Skills

## Context
Jesse Vincent's Superpowers framework (github.com/obra/superpowers) contains 20+ skills for agentic coding. Before assessing individual skills, need a complete inventory of what exists and what each does.

## Type
RESEARCH

## Execution
inline

## Dependencies
- 001-kernel-build-create-project-dir.md

## Phase Gate
- [ ] `projects/superpowers-research/` exists

## Requirements
- WebFetch or WebSearch `https://github.com/obra/superpowers` — read the README
- List every skill in the framework with a one-line description of what it does
- Note which skills overlap with existing kernel mechanisms (anchor, learn, lessons, gate contracts, execute-pipeline)
- Note which skills fill genuine gaps in the kernel (TDD, worktrees, code review)
- Write findings to `projects/superpowers-research/skills-inventory.md`

## Acceptance Criteria
- [ ] `projects/superpowers-research/skills-inventory.md` exists
- [ ] File lists all discovered skills (at least 10 entries)
- [ ] File identifies kernel overlaps vs genuine gaps

## Gates Satisfied
- DOC-02, DOC-03

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
