# Research: Read Superpowers Systematic Debugging Skill

## Context
The Superpowers package includes a 4-phase systematic debugging skill using Root Cause Analysis with component boundary logging. Need to read it and document the methodology.

## Type
RESEARCH

## Execution
inline

## Dependencies
- 001-kernel-build-create-project-dir.md

## Phase Gate
- [ ] `projects/debugging-skill-research/` exists

## Requirements
- WebFetch `https://github.com/obra/superpowers` — find and read the systematic debugging skill
- Document the 4 phases of the methodology
- Document what "component boundary logging" means in practice
- Document how RCA (Root Cause Analysis) is applied
- Note any claims about time savings (15-30 min vs 2-3 hours)
- Write to `projects/debugging-skill-research/skill-summary.md`

## Acceptance Criteria
- [ ] `projects/debugging-skill-research/skill-summary.md` exists
- [ ] File documents the 4 phases
- [ ] File explains component boundary logging
- [ ] File covers RCA application

## Gates Satisfied
- DOC-02, DOC-03

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
