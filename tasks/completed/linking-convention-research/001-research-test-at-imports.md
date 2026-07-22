# Test @path Import Behavior Outside CLAUDE.md

## Context
Claude Code supports `@path/to/file` in CLAUDE.md for auto-reading files. Test whether this works in skill files, design docs, and other markdown files. This determines if @imports are a viable linking convention beyond CLAUDE.md.

## Type
RESEARCH

## Execution
inline

## Dependencies
- None

## Requirements
- Create a test file that uses `@path` syntax pointing to a known file
- Place it in a skill directory and a design doc directory
- Check Claude Code documentation for @import scope
- Document: does `@path` trigger auto-read in skill files? In design docs? Only in CLAUDE.md?
- Write results to `tasks/linking-convention-research/at-import-test-results.md`

## Acceptance Criteria
- [ ] Test results document exists at `tasks/linking-convention-research/at-import-test-results.md`
- [ ] Documents whether @path works in: CLAUDE.md, skill files, design docs
- [ ] Clear yes/no answer for each context

## Gates Satisfied
- BUILD-01

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
