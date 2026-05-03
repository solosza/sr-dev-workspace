# 001 — Audit Current Fix State

## Type
RESEARCH

## Description
Read `run-task.sh` and `lib/common.sh` and compare against each backlog requirement. Determine what's already fixed and what remains.

## Requirements
- Read `run-task.sh` (full file)
- Read `lib/common.sh` (full file)
- Read `docs/backlog/050-kernel-fix-run-task-zombie-processes.md`
- For each requirement in the backlog, check if the current code addresses it:
  1. Output capture: does `run_claude()` use file-based capture instead of `$()`?
  2. Process cleanup: does `kill_process_tree()` use `taskkill //F //T` on Windows?
  3. Loop exit: is there a pre-iteration guard checking workflow state?
  4. Log namespacing: does `LOG_PREFIX` prevent cross-pipeline overwrites?
  5. Linux compatibility: are there platform-specific code paths?
- Write findings as a comment block at the top of the next task file (inline notes, not a separate file)
- Report which requirements are DONE, PARTIAL, or OPEN

## Acceptance Criteria
- [ ] All 5 requirements assessed with DONE/PARTIAL/OPEN status

## Gates
FUNC-01
