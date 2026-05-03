# Production Test: Step-11 Validation Against Mock Spec

## Context
Level 3 production test: run the rebuilt step-11 validation flow against a minimal mock spec to prove the sub-references work as a validation engine. This tests the PROCESS, not just the files — create workspace, copy spec, generate gate tasks, run gates, compile report.

## Type
TEST

## Dependencies
- 035

## Phase Gate
- [ ] step-11.md rewritten as thin index (task 035)
- [ ] All 10 sub-reference files exist in `C:/Users/solos/my_ai_projects/domain-spec-factory/.claude/skills/spec-factory/references/validation/`

## Requirements
- Create a minimal mock spec:
  - `mock-spec/.claude/skills/mock-domain/SKILL.md` — 10-line identity file
  - `mock-spec/.claude/skills/mock-domain/workflow.md` — 5-line workflow
  - `mock-spec/gate-contract.md` — 3 structural gates (file_exists for SKILL.md, workflow.md, README.md)
  - `mock-spec/README.md` — 3-line readme
- Create temp workspace for validation
- Follow the step-11 sub-references IN ORDER:
  1. `setup-workspace.md` — copy mock spec + kernel into workspace
  2. `install-dependencies.md` — skip (mock spec has no deps)
  3. `generate-gate-tasks.md` — parse gate-contract.md, generate 3 task files
  4. `verify-gates.md` — run the 3 structural gates directly (test -f for each)
  5. `coverage-report.md` — calculate coverage (expect 100% for 3/3)
  6. `validation-report-schema.md` — compile validation-report.json
- Read the produced validation-report.json
- Verify it has: total_gates=3, passed=3 (or 2 if README missing), valid JSON

## Acceptance Criteria
- [ ] Mock spec created with 3 structural gates (verify: file_exists for gate-contract.md)
- [ ] Gate tasks generated — 3 task files (verify: `ls tasks/gate-verification/*.md | wc -l` = 3)
- [ ] All 3 gates verified directly (verify: per-gate pass/fail logged)
- [ ] `validation-report.json` produced (verify: file_exists)
- [ ] `validation-report.json` is valid JSON with `total_gates` field (verify: `python -c "import json; d=json.load(open(...)); assert 'total_gates' in d"`)

## Gates Satisfied
PROD-07

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
