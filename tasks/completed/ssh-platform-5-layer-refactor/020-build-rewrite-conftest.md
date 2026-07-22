# 020 — Rewrite conftest.py

**Type:** BUILD
**Phase:** 5 — Tests
**Depends on:** 019

## What

Rewrite `conftest.py` with proper test fixtures for Layer 5 compliance.

## Target

`D:\my_ai_projects\project_test_repos\platform-ssh\framework\_reference\tests\conftest.py`

## Contract Rules (5-layer-contract.md)

**Layer 5 — Test (fixtures):**
- `@pytest.fixture(autouse=True) def setup` wires dependencies (Interface, config, test data)
- Setup fixture creates Component instances on `self` for assertions

## Requirements

- Keep MockSSH class but enhance: add type hints, proper docstrings
- MockSSH should return configurable responses (pass/fail scenarios)
- `mock_ssh_interface` fixture returns MockSSH wrapped as SSHInterface-compatible
- `sample_host_config` fixture (keep existing)
- `sample_stig_rules` fixture with test rule data
- sys.path setup for imports

## Acceptance Criteria

- [ ] MockSSH class has docstrings and type hints
- [ ] `mock_ssh_interface` fixture exists
- [ ] `sample_host_config` fixture exists
- [ ] `sample_stig_rules` fixture exists
- [ ] sys.path insert for `_reference/` directory
