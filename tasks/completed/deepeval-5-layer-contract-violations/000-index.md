# Fix Platform-DeepEval 5-Layer Contract Violations

## Backlog
`docs/backlog/191-qa-refactor-deepeval-5-layer-contract-violations.md`

## Target Repo
`D:/my_ai_projects/project_test_repos/platform-deepeval`

## Canonical Reference
`D:/my_ai_projects/project_test_repos/platform-selenium`

## Task Order
1. `001-fix-reference-roles.md` — Fix 4 _reference/ roles: return None, add self.metrics, state methods
2. `002-fix-reference-tasks.md` — Fix 7 _reference/ tasks: remove _eval_results, use metrics_out
3. `003-fix-reference-tests.md` — Fix _reference/ tests: call evaluate() instead of setting _scores
4. `004-parameterize-metrics.md` — Parameterize security/behavior metrics: accept protocol rules as config
5. `005-fix-framework-roles-tasks.md` — Fix framework/ roles + tasks to mirror corrected _reference/
6. `006-import-validation.md` — Validate all imports and test suite passes
