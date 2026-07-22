# Refactor Docker Platform to 5-Layer Compliance

## Status
Open

## Priority
Medium — 3 layers non-compliant (L1, L2, L5), but architecture is structurally sound

## Summary
The `/check-5-layer` audit on platform-docker found 3 FAIL layers and 2 WARN layers across 6 framework files. The Interface layer needs logging, error handling, and constructor fixes. Component docstrings need structural rule bullets. Tests need decorators, marks, setup fixtures, and Role-layer routing. Task and Role layers are functionally correct but use free functions instead of the contract's class-based pattern.

## Audit Results (2026-07-09)

| Layer | Files | Status | Key Issues |
|-------|-------|--------|------------|
| L1 Interface | 1 | FAIL | No logging, no error handling, returns `self`, missing logger param |
| L2 Component | 2 | FAIL | Class docstrings are one-liners (need structural rule bullets) |
| L3 Task | 1 | PASS (warn) | Free functions instead of class, no fluent chaining used |
| L4 Role | 1 | PASS (warn) | Free functions instead of class, `run_full_compliance_audit` wraps only 1 Task |
| L5 Test | 1 | FAIL | No @automation_logger, no @pytest.mark, no setup fixture, bypasses Role layer |

## Requirements

### Critical (FAIL findings)
- Rewrite `image_interface.py` constructor: add `logger` and `config` parameters
- Add `self.logger` calls on every operation in Interface
- Add try/except around subprocess calls: catch `CalledProcessError`, log, re-raise
- Change lifecycle methods (`pull_image`, `start_container`, `stop_container`, `remove_container`) to return `None` instead of `self`
- Expand class docstrings on Interface + both Components to list structural rules as bullets
- Add `@automation_logger("Test")` to all 6 test methods
- Add `@pytest.mark` tags to all test methods
- Add `@pytest.fixture(autouse=True) def setup` to test class
- Route tests through Role layer (stop calling Interface/Component directly)

### Moderate (WARN findings)
- Convert Task functions to class-based `PackageValidationTasks` with `__init__(self, interface)`
- Convert Role functions to class-based `SecurityAuditor` with `__init__(self, interface, config)`
- Use fluent Component chaining in Task methods
- Change section headers from `# -- Category --` to `# === CATEGORY ===`
- Either compose multiple Tasks in `run_full_compliance_audit` or move it to Task layer

## References
- 5-layer contract: `.claude/docs/design/check-5-layer/references/5-layer-contract.md`
- Audit report: generated 2026-07-09 via `/check-5-layer`
- Platform repo: `D:\my_ai_projects\project_test_repos\platform-docker`
- Related: backlog 192 (SSH platform refactor — same pattern)

## Task Builder Input
- **Deliverable:** All 6 framework files refactored to pass `/check-5-layer` with 0 FAIL
- **Location:** `new-repo:D:\my_ai_projects\project_test_repos\platform-docker`
- **Scope:** REFACTOR
- **Constraints:** Must not break existing test assertions. Run `/check-5-layer` after to verify compliance. Use platform-selenium as reference for correct patterns.
