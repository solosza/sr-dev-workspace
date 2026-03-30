# Build Domain Spec for Kernel Integration

## Type
BUILD

## Context
Create the SSH management layer domain spec so the kernel can discover, enforce, and cycle through SSH testing workflows.

## Dependencies
- 002 (scaffolding — .claude/skills/ directory must exist)

## Phase Gate
- [ ] `.claude/skills/ssh-management-layer/` directory exists

## Requirements
- Create `SKILL.md` — identity, vocabulary, rules, file index
- Create `workflow.md` — 5-step pipeline (input → preflight → plan → execute → report)
- Create `gate-contract.md` — quality gates per workflow step
- Create step files in `references/`:
  - `step-01.md` — User input (target host IP, image variant, test scope)
  - `step-02.md` — Preflight (verify SSH connectivity, check paramiko, validate config)
  - `step-03.md` — Plan (select validators based on image variant, set thresholds)
  - `step-04.md` — Execute (run test suite via SSHBatchExecutor)
  - `step-05.md` — Report (compile results, flag failures, recommend fixes)

## Acceptance Criteria
- [ ] `.claude/skills/ssh-management-layer/SKILL.md` exists
- [ ] `.claude/skills/ssh-management-layer/workflow.md` exists
- [ ] `.claude/skills/ssh-management-layer/gate-contract.md` exists
- [ ] At least 5 step files in `references/`
- [ ] SKILL.md has step table with wikilinks to references

## Gates Satisfied
BUILD-18, BUILD-19, BUILD-20

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
