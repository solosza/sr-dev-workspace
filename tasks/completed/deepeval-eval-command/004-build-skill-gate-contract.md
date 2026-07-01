# Write Skill gate-contract.md (Eval Quality Gates)

## Context
Layer 2 companion defining quality gates for the eval command's own behavior. These gates validate the eval loop itself — not the target artifact being tested. Each gate maps to a step's expected output.

## Type
BUILD

## Execution
inline

## Dependencies
- None

## Requirements
- File: `.claude/skills/eval/gate-contract.md`
- Must contain gates for each step:
  - **Step 1 gates**: test repo directory exists, git initialized
  - **Step 2 gates**: protocol file exists in test repo, hooks wired in settings.local.json, state files initialized
  - **Step 3 gates**: artifact SKILL.md (or equivalent) exists in test repo, all file index references resolve, no broken wikilinks
  - **Step 4 gates**: component check completed, decision log produced (what was reused vs created)
  - **Step 5 gates**: conftest.py exists, at least one test file exists, fixtures loadable, metrics selected
  - **Step 6 gates**: scored report file exists, all metrics have numeric scores, score-history.json updated
- Format: table with ID, Check, Method, Pass Criteria, Fail Action
- Must be under 200 lines

## Acceptance Criteria
- [ ] File exists at `.claude/skills/eval/gate-contract.md`
- [ ] `grep -q "Step 1" .claude/skills/eval/gate-contract.md` OR `grep -q "step-01" .claude/skills/eval/gate-contract.md` passes
- [ ] `grep -q "Step 6" .claude/skills/eval/gate-contract.md` OR `grep -q "step-06" .claude/skills/eval/gate-contract.md` passes
- [ ] File is under 200 lines

## Gates Satisfied
BUILD-04

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
