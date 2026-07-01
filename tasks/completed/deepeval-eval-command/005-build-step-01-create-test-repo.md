# Write step-01-create-test-repo.md

## Context
Layer 3 step file for the eval loop's first step. Defines how to create the disposable test repo at `D:\my_ai_projects\project_test_repos\eval-[target]-test\`. The repo is recreated each run — if it exists, it is deleted and recreated.

## Type
BUILD

## Execution
inline

## Dependencies
- None

## Requirements
- File: `.claude/skills/eval/steps/step-01-create-test-repo.md`
- Must contain:
  - **What to do**: create `D:\my_ai_projects\project_test_repos\eval-[target]-test\`, initialize git
  - **Pre-generation checkpoint**: verify source-repo exists and target artifact is identifiable
  - **What to produce**: empty git-initialized directory
  - **Verification**: directory exists, `.git/` exists
  - **Error handling**: if source-repo doesn't exist, abort with clear message; if target not found in source-repo, abort with available artifacts list
  - **Cleanup**: if test repo already exists from prior run, remove it first
- Must be under 200 lines

## Acceptance Criteria
- [ ] File exists at `.claude/skills/eval/steps/step-01-create-test-repo.md`
- [ ] `grep -q "eval-" .claude/skills/eval/steps/step-01-create-test-repo.md` passes (repo naming pattern)
- [ ] `grep -q "git init" .claude/skills/eval/steps/step-01-create-test-repo.md` passes
- [ ] File is under 200 lines

## Gates Satisfied
BUILD-05

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
