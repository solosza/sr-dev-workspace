# Test Golden Dataset Translator

## Type
TEST

## Phase Gate
Task 001 must be complete.

## Deliverable
Test verification output.

## Instructions
1. Verify `framework/golden_dataset_translator.py` exists and parses:
   `python -c "import ast; ast.parse(open('framework/golden_dataset_translator.py').read()); print('Syntax OK')"`
2. Verify required functions exist:
   `python -c "import ast; t=ast.parse(open('framework/golden_dataset_translator.py').read()); fns=[n.name for n in ast.walk(t) if isinstance(n, ast.FunctionDef)]; assert 'translate_contract' in fns, f'Missing translate_contract, found {fns}'; print('Functions OK:', fns)"`
3. If example contract JSONs exist at `D:\my_ai_projects\project_test_repos\hmsa-healthcare-qa\.claude\skills\check-data\contracts\`, run translator against one:
   `python -c "import sys; sys.path.insert(0, '.'); from framework.golden_dataset_translator import translate_contract; result = translate_contract('path/to/contract.json'); print(f'Goldens generated: {len(result.get(\"goldens\", []))}')"`
4. Verify output has required fields: input, expected_output, context, metadata

## Verification
- Syntax check passes (exit 0)
- Required functions present
- If contract available: goldens generated with correct schema
