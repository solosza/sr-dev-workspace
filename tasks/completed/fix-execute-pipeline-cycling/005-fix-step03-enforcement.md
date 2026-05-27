# Fix step-03 — Atomic Flag-Clear Enforcement

## Context
execute-pipeline step 3 sets `no_execute: true` so task-builder stops before cycling. After task-builder returns, the flag must be cleared and step 4 must run immediately. But the agent reports status and stops instead of continuing. The flag-clear and step-4 invocation must be made atomic and non-optional.

## Type
BUILD

## Execution
inline

## Dependencies
None

## Requirements
- In `.claude/skills/execute-pipeline/references/step-03-run-task-builder.md`:
  - Add a prominent enforcement block after the "Clear pipeline mode flags" section
  - Make it explicit that clearing flags + proceeding to step 4 is MECHANICAL — the agent MUST NOT stop, report, or wait for user input between clearing flags and starting step 4
  - Add language like: "MUST NOT STOP between clearing pipeline_mode and executing step 4. This transition is atomic."

## Acceptance Criteria
- [ ] `grep -qi 'MUST NOT STOP\|atomic\|MECHANICAL' .claude/skills/execute-pipeline/references/step-03-run-task-builder.md` exits 0

## Gates Satisfied
BUILD-05

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
