# SSH Platform File Map

**Source:** `D:/my_ai_projects/project_test_repos/isagawa-qa/platform-ssh/`
**Scanned:** 2026-07-05

## Python Files by Layer

### L1 — Interface
| File | Path |
|------|------|
| ssh_interface.py | `framework/_reference/ssh_interface.py` |

**Note:** Located at `_reference/` root, not in an `interfaces/` subdirectory (deviation from deepeval pattern).

### L2 — Metrics
No files found. No `metrics/` directory exists in the SSH platform.

### L3 — Tasks
| File | Path |
|------|------|
| run_ssh_command.py | `framework/_reference/tasks/run_ssh_command.py` |

### L4 — Roles
| File | Path |
|------|------|
| ssh_batch_executor.py | `framework/_reference/roles/ssh_batch_executor.py` |

### L5 — Tests
| File | Path |
|------|------|
| conftest.py | `framework/_reference/tests/conftest.py` |
| test_ssh_batch.py | `framework/_reference/tests/test_ssh_batch.py` |
| test_stig_validator.py | `framework/_reference/tests/test_stig_validator.py` |

### Unknown / Non-Standard Layer
| File | Path | Notes |
|------|------|-------|
| compliance_validator.py | `framework/_reference/validators/compliance_validator.py` | `validators/` not in 5-layer model |
| config_validator.py | `framework/_reference/validators/config_validator.py` | `validators/` not in 5-layer model |
| kernel_validator.py | `framework/_reference/validators/kernel_validator.py` | `validators/` not in 5-layer model |
| package_validator.py | `framework/_reference/validators/package_validator.py` | `validators/` not in 5-layer model |
| service_validator.py | `framework/_reference/validators/service_validator.py` | `validators/` not in 5-layer model |
| stig_validator.py | `framework/_reference/validators/stig_validator.py` | `validators/` not in 5-layer model |
| eval_config.py | `framework/resources/eval_config.py` | `resources/` not in 5-layer model |

## Summary

| Layer | Count | Status |
|-------|-------|--------|
| L1 (Interface) | 1 | Present (wrong directory location) |
| L2 (Metrics) | 0 | **Missing entirely** |
| L3 (Tasks) | 1 | Present |
| L4 (Roles) | 1 | Present |
| L5 (Tests) | 3 | Present |
| Unknown | 7 | `validators/` (6) + `resources/` (1) |

**Total Python files:** 13
