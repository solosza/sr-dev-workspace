# Write step-02-create-backlog.md

## Context
Step 2 of execute-pipeline: create backlog item from natural language input. SKIP if step 1 detected an existing backlog file.

## Type
BUILD

## Execution
inline

## Dependencies
- 003 (references directory must exist)

## Requirements
- Write `.claude/skills/execute-pipeline/references/step-02-create-backlog.md`
- Skip condition: if `pipeline_state.backlog_path` already set in session_state.json, skip this step
- Otherwise: invoke `/kernel/backlog` inline with the user's natural language input
- Capture the created backlog file path into `pipeline_state.backlog_path`
- All user context passes through verbatim to the backlog command — never summarize

## Acceptance Criteria
- [ ] `test -f .claude/skills/execute-pipeline/references/step-02-create-backlog.md` exits 0
- [ ] File documents skip condition
- [ ] File documents inline invocation of /kernel/backlog

## Gates Satisfied
- BUILD-06

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
