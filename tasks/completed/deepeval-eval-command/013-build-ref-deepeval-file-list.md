# Write step-02/deepeval-file-list.md

## Context
Layer 4 reference payload for Step 2 (Compile Harness). Lists the exact files and directories to copy from platform-deepeval into the test repo.

## Type
BUILD

## Execution
inline

## Dependencies
- None

## Requirements
- File: `.claude/skills/eval/references/step-02/deepeval-file-list.md`
- Must list the exact files/directories to copy from platform-deepeval (`D:\my_ai_projects\project_test_repos\platform-deepeval`):
  - `.claude/skills/deepeval-management-layer/` — full skill (SKILL.md, workflow.md, gate-contract.md, steps/, references/)
  - `framework/interfaces/deepeval_interface.py` — DeepEval interface
  - `framework/_reference/` — all reference implementations (metrics/, tests/, tasks/, roles/, fixtures/)
  - `framework/resources/` — any shared resources
  - `FRAMEWORK.md` — framework documentation
- Source material: `docs/backlog/157-kernel-build-deepeval-command-testing/harness-compilation.md` (From Platform-DeepEval section)
- Must be under 200 lines

## Acceptance Criteria
- [ ] File exists at `.claude/skills/eval/references/step-02/deepeval-file-list.md`
- [ ] `grep -q "deepeval-management-layer" .claude/skills/eval/references/step-02/deepeval-file-list.md` passes
- [ ] `grep -q "_reference" .claude/skills/eval/references/step-02/deepeval-file-list.md` passes
- [ ] `grep -q "deepeval_interface" .claude/skills/eval/references/step-02/deepeval-file-list.md` passes
- [ ] File is under 200 lines

## Gates Satisfied
BUILD-13

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
