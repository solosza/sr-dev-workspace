# Build Tests + Fixtures (Layer 5)

## Type
BUILD

## Context
Layer 5 validates all layers via pytest. Golden fixtures define host configs and expected outputs for CIQ image variants.

## Dependencies
- 004 (validators), 005 (tasks + roles)

## Phase Gate
- [ ] All validator files exist and import
- [ ] Task and role files exist and import

## Requirements
- Create `framework/_reference/tests/conftest.py`:
  - Fixture for SSHInterface (mock for unit tests)
  - Fixture loading host_configs.json
  - Parametrize helpers
- Create `framework/_reference/tests/test_ssh_batch.py`:
  - Tests using `@pytest.mark.parametrize` over host configs
  - AAA pattern: Arrange (executor + config), Act (execute_suite), Assert (validator.is_valid())
  - Test per validator type: package, kernel, service, config
- Create `framework/_reference/fixtures/host_configs.json`:
  - CIQ image configs with expected values from research (task 001)
  - At least 2 variants: RLC Pro base, RLC Pro AI (with GPU packages)
  - Include expected packages, kernel version, services per variant
- Tests must use mock SSH interface for unit testing (real SSH is task 008)

## Acceptance Criteria
- [ ] `framework/_reference/tests/test_ssh_batch.py` exists
- [ ] `framework/_reference/tests/conftest.py` exists
- [ ] `framework/_reference/fixtures/host_configs.json` exists and is valid JSON
- [ ] Tests use `@pytest.mark.parametrize`
- [ ] Fixtures have at least 2 CIQ image variants with realistic data
- [ ] `pytest framework/_reference/tests/ -v` exits 0 (with mock SSH)

## Gates Satisfied
BUILD-15, BUILD-16, BUILD-17, FUNC-05, TEST-01

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
