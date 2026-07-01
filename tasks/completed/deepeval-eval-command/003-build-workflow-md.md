# Write workflow.md (Eval Loop Behavior)

## Context
Layer 2 companion to SKILL.md. Defines the eval loop's state machine, loop behavior, error handling, and resume support. This is where the 6-step loop is described in operational detail — how state transitions work, what happens on failure, how to resume a partial run.

## Type
BUILD

## Execution
inline

## Dependencies
- None

## Requirements
- File: `.claude/skills/eval/workflow.md`
- Must contain:
  - **State Machine**: states (init, creating_repo, compiling_harness, copying_artifact, checking_components, generating_tests, running_scoring, complete, failed)
  - **Loop Behavior**: 6-step sequential execution, each step has entry condition and exit condition
  - **Error Handling**: what to do when each step fails (Step 2 harness compilation failure, Step 3 missing dependencies, Step 4 _reference/ not found, Step 5 test generation failure, Step 6 deepeval execution failure)
  - **Resume Support**: how to resume from a failed step using session_state.json `resume_step`
  - **Composability**: standalone invocation vs callable by another loop
  - **Input Parsing**: how target and source-repo are resolved
- Source material: `docs/backlog/157-kernel-build-deepeval-command-testing/eval-loop.md`
- Must be under 200 lines

## Acceptance Criteria
- [ ] File exists at `.claude/skills/eval/workflow.md`
- [ ] `grep -q "resume" .claude/skills/eval/workflow.md` passes (resume support)
- [ ] `grep -q "error" .claude/skills/eval/workflow.md` passes (error handling, case-insensitive match acceptable)
- [ ] `grep -q "composab" .claude/skills/eval/workflow.md` passes (composability)
- [ ] File is under 200 lines

## Gates Satisfied
BUILD-03

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
