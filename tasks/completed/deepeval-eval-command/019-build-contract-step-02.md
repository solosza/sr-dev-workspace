# Write step-02-contract.json

## Context
Layer 5 contract for Step 2 (Compile Harness). Validates that the harness was compiled correctly — protocol exists, hooks are wired, state is initialized. These contracts validate the eval command's OWN behavior.

## Type
BUILD

## Execution
inline

## Dependencies
- None

## Requirements
- File: `.claude/skills/eval/contracts/step-02-contract.json`
- Must be valid JSON
- Must contain:
  - `step`: "02-compile-harness"
  - `success_criteria`: ["Protocol file exists in test repo", "Hooks wired in settings.local.json", "State files initialized (session_state.json exists)", "Domain-setup completed without error"]
  - `expected_artifacts`: ["protocol file", "settings.local.json with hook entries", "session_state.json"]
  - `soft_validation_rules`: rules for harness quality (e.g., "All kernel commands accessible", "DeepEval skill discoverable by domain-setup")
  - `verification_commands`: bash commands to verify each criterion
- Must parse as valid JSON (`python -c "import json; json.load(open(f))"`)

## Acceptance Criteria
- [ ] File exists at `.claude/skills/eval/contracts/step-02-contract.json`
- [ ] `python -c "import json; json.load(open('.claude/skills/eval/contracts/step-02-contract.json'))"` exits 0
- [ ] `grep -q "protocol" .claude/skills/eval/contracts/step-02-contract.json` passes

## Gates Satisfied
BUILD-19, FUNC-01 (partial)

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
