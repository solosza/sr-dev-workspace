# Step 6: Generate Contracts

## Purpose

Create Layer 5 validation contract JSON files from the design doc's contract definitions. Only generate contracts for steps that specify validation rules.

## Input

- Design doc contract definitions (if specified)
- Input contract checklist: > `.claude/docs/design/build-command/references/input-contract.md`
- Template: > `.claude/docs/design/build-command/references/layer-templates-supporting.md#Contract JSON`

## Output

- `.claude/skills/[name]/contracts/step-NN-contract.json` (one per step with contracts)

## Acceptance Criteria

- [ ] Contract JSON is valid (parseable by `json.load`)
- [ ] Has `contract_metadata` with contract_id, version, artifact_type
- [ ] Has `validations` array (soft gate rules)
- [ ] Has `mechanical_validations` array (hard gate rules, may be empty)
- [ ] `canonical_reference.path` points to design doc references

## References

- > `.claude/docs/design/build-command/references/layer-templates-supporting.md`
- > `.claude/docs/design/build-command/references/input-contract.md`

## Procedure

1. For each step with contract definitions in the design doc:
   - Read the step's validation spec
   - Write `contracts/step-NN-contract.json` with contract_metadata + validations
2. If no contract definitions specified > skip Layer 5 entirely

## Verification

- Each JSON file passes `python -c "import json; json.load(open(...))"`
- contract_metadata fields are populated

## Failure Recovery

If contract definitions are missing from design doc, skip Layer 5 with warning.
