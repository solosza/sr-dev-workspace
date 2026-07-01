# Write step-03-contract.json

## Context
Layer 5 contract for Step 3 (Copy Artifact). Validates that the artifact was isolated correctly — all references resolve, no broken wikilinks, contract JSONs parse.

## Type
BUILD

## Execution
inline

## Dependencies
- None

## Requirements
- File: `.claude/skills/eval/contracts/step-03-contract.json`
- Must be valid JSON
- Must contain:
  - `step`: "03-copy-artifact"
  - `success_criteria`: ["All SKILL.md file index entries exist in test repo", "All step file references resolve", "All contract JSONs parse as valid JSON", "No broken wikilinks in copied markdown"]
  - `expected_artifacts`: ["target artifact's SKILL.md in test repo", "all step files", "all reference files", "all contract files"]
  - `soft_validation_rules`: rules for isolation quality (e.g., "No references to source repo paths remain", "Artifact is fully self-contained")
  - `verification_commands`: bash commands to verify file existence and JSON parsing
- Must parse as valid JSON

## Acceptance Criteria
- [ ] File exists at `.claude/skills/eval/contracts/step-03-contract.json`
- [ ] `python -c "import json; json.load(open('.claude/skills/eval/contracts/step-03-contract.json'))"` exits 0
- [ ] `grep -q "wikilink" .claude/skills/eval/contracts/step-03-contract.json` OR `grep -q "self-contained" .claude/skills/eval/contracts/step-03-contract.json` passes

## Gates Satisfied
BUILD-20, FUNC-01 (partial)

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
