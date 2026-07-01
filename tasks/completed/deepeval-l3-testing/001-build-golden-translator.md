# Build Golden Dataset Translator

## Type
BUILD

## Phase Gate
None (first task, no dependencies).

## Deliverable
`framework/golden_dataset_translator.py`

## Instructions
1. Read the golden-dataset-translator design doc: `docs/backlog/154-kernel-build-deepeval-l3-testing/golden-dataset-translator.md`
2. Read the platform-deepeval framework to understand golden dataset format: `D:\my_ai_projects\project_test_repos\platform-deepeval\FRAMEWORK.md`
3. Create `framework/golden_dataset_translator.py` implementing:
   - `translate_contract(contract_path)` — reads a contract JSON, returns DeepEval golden dataset JSON
   - Extract `soft_validation_rules` and `success_criteria` from contract
   - Generate positive goldens (rule passes) and negative goldens (rule violated) for each rule
   - Each golden has: `input`, `expected_output`, `context` (rule descriptions), `metadata` (rule_ids, step, contract_id)
   - Minimum 20 goldens per contract (generate variations if under 20)
   - `translate_all_contracts(contracts_dir)` — batch translate all contracts in a directory
4. Output format must match DeepEval's `EvaluationDataset` schema

## Verification
- File exists at `framework/golden_dataset_translator.py`
- Contains `translate_contract` and `translate_all_contracts` functions
- Parses without syntax errors
