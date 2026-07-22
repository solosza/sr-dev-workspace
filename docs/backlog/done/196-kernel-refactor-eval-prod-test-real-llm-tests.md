# Refactor Eval Test Suite for Prod-Test — Real LLM Test Cases

## Status
Open

## Priority
High — 9/15 eval tests fail due to mock agent, not skill quality; real tests needed to validate prod-test command

## Summary
The current `test_eval_prod_test.py` uses a simplistic `mock_prod_test_agent` that returns identical generic output for every scenario, causing 9/15 GEval tests to fail (all 8 StepSequencing + GateCompliance). Replace the mock with real deepeval LLMTestCase patterns where `actual_output` is the skill text itself (SKILL.md, step files, gate-contract.md) fed directly to GEval as the artifact being evaluated. GEval judges the quality of the written instructions — the artifact text IS the actual_output.

## Requirements
- Remove `mock_prod_test_agent` function from conftest.py and test file
- For each StepSequencing test: load the corresponding step file (e.g., `steps/step-01-parse.md`) as `actual_output`
- For GateCompliance test: load `gate-contract.md` as `actual_output`
- Golden fixture `expected_output` fields describe what correct behavior looks like — GEval compares skill documentation against those expectations
- Keep the 6 passing tests (InfraDerivation, Isolation x2, DockerRequired, VerdictAccuracy, PipelineCoverage) unchanged — they already work correctly
- Update conftest.py to add a fixture that loads skill files by step number
- Re-run `deepeval test run` after refactor and verify improved scores
- All 15 tests should target >= 0.70 threshold

## References
- `evals/eval-prod-test/eval-report.md` — current 6/15 PASS with root cause analysis
- `evals/eval-prod-test/tests/test_eval_prod_test.py` — current test file with mock
- `evals/eval-prod-test/tests/conftest.py` — current conftest with mock function
- `evals/eval-prod-test/.claude/skills/prod-test/` — skill files to use as actual_output
- `eval/results/score-history.json` — score history (first entry: 6/15)

## Task Builder Input
- **Deliverable:** Refactored test_eval_prod_test.py and conftest.py with real LLM test cases, re-run deepeval showing improved scores
- **Location:** `workspace:evals/eval-prod-test/tests/`
- **Scope:** REFACTOR
- **Constraints:** Must preserve golden fixture format (golden_prod_test.json), must use existing _reference/ metric patterns, OPENAI_API_KEY must be set for GEval
