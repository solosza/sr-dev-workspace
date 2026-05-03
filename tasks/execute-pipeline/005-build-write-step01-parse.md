# Write step-01-parse-input.md

## Context
Step 1 of execute-pipeline: detect whether input is an existing backlog file path or natural language. If file path, use directly. If natural language, pass through to step 2.

## Type
BUILD

## Execution
inline

## Dependencies
- 003 (references directory must exist)

## Requirements
- Write `.claude/skills/execute-pipeline/references/step-01-parse-input.md`
- Detection logic: if argument ends in `.md` AND file exists at that path → use as backlog item (set `backlog_path` in state, skip step 2)
- Otherwise → treat as natural language goal (proceed to step 2)
- Also accept shorthand: if argument is a number (e.g., "031"), resolve to `docs/backlog/031-*.md` by glob
- Output: report whether using existing backlog or creating new one
- Set `pipeline_state` in session_state.json with `input_mode` and `backlog_path` (if known)

## Acceptance Criteria
- [ ] `test -f .claude/skills/execute-pipeline/references/step-01-parse-input.md` exits 0
- [ ] File documents both input modes (existing backlog file, natural language)
- [ ] File documents shorthand number resolution

## Gates Satisfied
- BUILD-05

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
