# Write conftest.py with parameterized harness_root

## Context
The conftest.py must accept `--harness-root` as a pytest CLI option so the same test suite can evaluate any harness, not just kernel-minimal. This replaces the hardcoded `HARNESS_ROOT` path.

## Type
BUILD

## Execution
inline

## Dependencies
- None

## Requirements
- Write to `D:/my_ai_projects/project_test_repos/platform-deepeval/tests/conftest.py`
- Add `pytest_addoption` hook that registers `--harness-root` CLI option (required=True, help text)
- `harness_root` fixture reads from `request.config.getoption("--harness_root")` and returns a `Path`
- Add `sys.path.insert` for `framework/` directory (relative to repo root: `Path(__file__).parent.parent / "framework"`)
- Include all fixtures from source conftest: `harness_commands`, `harness_hooks`, `harness_skills`, `harness_claudemd`, `harness_settings`, `harness_manifest`, `eval_config`
- Remove `golden_harness` fixture (not used)
- The `harness_root` fixture must use `request` fixture parameter for `config.getoption`

## Acceptance Criteria
- [ ] `D:/my_ai_projects/project_test_repos/platform-deepeval/tests/conftest.py` exists
- [ ] File contains `def pytest_addoption` with `--harness-root`
- [ ] File contains `def harness_root` fixture using `request.config.getoption`
- [ ] File contains `harness_commands`, `harness_hooks`, `harness_skills`, `harness_claudemd`, `harness_settings`, `harness_manifest` fixtures

## Gates Satisfied
- BUILD-05, FUNC-03

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
