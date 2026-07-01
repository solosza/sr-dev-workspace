# Build Command Entry Point

## Context
Create the user-facing command file that wires `/kernel/human-check` to the skill.

## Type
BUILD

## Execution
inline

## Dependencies
- 002-build-skill-and-steps

## Phase Gate
- [ ] `.claude/skills/human-check/SKILL.md` exists

## Requirements
- Create `.claude/commands/kernel/human-check.md`
- Usage: `/kernel/human-check [file-path]` or `/kernel/human-check [inline text]`
- Input modes: file path (scans file), inline text (scans provided text)
- Examples showing both modes
- Route to skill: "Read and follow `.claude/skills/human-check/SKILL.md`"
- Update CLAUDE.md Commands section to include human-check

## Acceptance Criteria
- [ ] File exists: `.claude/commands/kernel/human-check.md`
- [ ] Usage section with both input modes
- [ ] Examples section
- [ ] Routes to SKILL.md

## Gates Satisfied
- BUILD-03

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
