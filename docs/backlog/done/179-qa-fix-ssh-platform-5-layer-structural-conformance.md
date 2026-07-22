# Fix SSH Platform 5-Layer Structural Conformance

## Status
Open

## Priority
Medium — Style and structural violations that don't affect functionality but diverge from platform-deepeval conventions. 11 violations (5 medium, 6 low).

## Summary
Remediate the structural and style violations (R5-R8) found in the SSH platform 5-layer compliance audit. These are non-critical conformance issues: interface in wrong directory, constructor signatures not matching L1 pattern, missing result persistence, and test style conventions (AAA comments, parametrize, naming).

## Requirements
- **R5: Move interface to standard directory** — Move `ssh_interface.py` to `framework/_reference/interfaces/ssh_interface.py`. Update all imports.
- **R6: Fix constructor signatures** — Add `logger` parameter to SSHInterface. Rename `hc` → `config`, add type hints. Update SSHBatchExecutor constructor.
- **R7: Add result persistence** — Add `save_results()` and `_save_failure_report()` to SSHInterface.
- **R8: Add test conventions** — Add AAA comments, `@pytest.mark.parametrize`, and `test_<what>_REQ_<layer>` naming.
- **Remove sys.path hacks** — Centralize in conftest.py.

## Violations Addressed

| ID | File | Violation | Severity |
|----|------|-----------|----------|
| L1-V1 | `ssh_interface.py` | Wrong directory | LOW |
| L1-V2 | `ssh_interface.py:5` | Constructor signature | MEDIUM |
| L1-V3 | `ssh_interface.py` | Missing persistence | LOW |
| L1-V4 | `tests/conftest.py` | No L1 import in fixture | MEDIUM |
| L3-V2 | `run_ssh_command.py:3` | Returns result not None | MEDIUM |
| L4-V2 | `ssh_batch_executor.py` | Wrong constructor | MEDIUM |
| L5-V2 | `test_stig_validator.py:62` | Direct L1 import | MEDIUM |
| L5-V3 | `test_stig_validator.py:7` | sys.path.insert | LOW |
| L5-V4 | test files | No AAA comments | LOW |
| L5-V5 | test files | No parametrize | LOW |
| L5-V6 | test files | No _REQ_ naming | LOW |

## References
- Compliance report: `projects/ssh-5-layer-audit/compliance-report.md`
- SSH platform: `D:/my_ai_projects/project_test_repos/isagawa-qa/platform-ssh/`
- Backlog 178: Critical architecture fixes (must complete first)

## Task Builder Input
- **Deliverable:** SSH platform with standard directory layout, signatures, persistence, and test conventions
- **Location:** `new-repo:D:/my_ai_projects/project_test_repos/isagawa-qa/platform-ssh`
- **Scope:** REFACTOR
- **Constraints:** Depends on backlog 178 completing first. Style changes only — no functional logic changes.
