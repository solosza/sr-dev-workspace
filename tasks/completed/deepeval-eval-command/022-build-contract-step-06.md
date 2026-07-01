# Write step-06-contract.json

## Context
Layer 5 contract for Step 6 (Run and Score). Validates that the scored report was produced correctly — all metrics scored, report file exists, score history updated.

## Type
BUILD

## Execution
inline

## Dependencies
- None

## Requirements
- File: `.claude/skills/eval/contracts/step-06-contract.json`
- Must be valid JSON
- Must contain:
  - `step`: "06-run-and-score"
  - `success_criteria`: ["Scored report produced", "All metrics have numeric scores (0-1)", "Overall pass/fail determined", "Score history updated in source repo"]
  - `expected_artifacts`: ["eval report (console output or file)", "score-history.json entry in source repo's eval/results/"]
  - `soft_validation_rules`: rules for scoring quality (e.g., "Regression detected if score drops > 0.1", "Failing metrics include triage recommendations", "New components documented")
  - `verification_commands`: bash commands to verify score-history.json exists and parses as valid JSON
- Must parse as valid JSON

## Acceptance Criteria
- [ ] File exists at `.claude/skills/eval/contracts/step-06-contract.json`
- [ ] `python -c "import json; json.load(open('.claude/skills/eval/contracts/step-06-contract.json'))"` exits 0
- [ ] `grep -q "score-history" .claude/skills/eval/contracts/step-06-contract.json` passes

## Gates Satisfied
BUILD-22, FUNC-01 (partial)

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
