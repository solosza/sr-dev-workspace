# Fix SSH Platform 5-Layer Critical Architecture

## Status
Open

## Priority
High — SSH platform has no L2 metrics layer, causing skip-layer violations across L3/L4/L5. 10 critical violations identified in compliance audit (backlog 175).

## Summary
Remediate the critical architecture violations (R1-R4) found in the SSH platform 5-layer compliance audit. The SSH platform is missing the entire L2 metrics layer — existing `validators/` use a non-standard API (`validate()` → `List[Dict]`) instead of the required L2 pattern (`evaluate()`, `is_above_threshold()`, `get_score()`). This absence cascades: L3 tasks call L1 directly (skip-layer), L4 roles orchestrate validators instead of L3 tasks, and L5 tests import from the non-standard `validators/` layer.

## Requirements
- **R1: Create L2 metrics layer** — Create `framework/_reference/metrics/` with metric wrapper classes around existing validators. Expose `evaluate()`, `is_above_threshold()`, `get_score()`, `get_detail()` API. Define `METRIC_CRITERIA` and `METRIC_THRESHOLDS` constants.
- **R2: Refactor L3 to compose L2 metrics** — Rewrite `run_ssh_command.py` to import from `metrics/`, compose L2 metric objects instead of calling L1 directly. Accept `test_case` parameter, return `None`.
- **R3: Refactor L4 to import L3 tasks** — Update `ssh_batch_executor.py` to import L3 task functions. Orchestrate via L3 tasks instead of directly calling validators. Accept L1 interface in constructor.
- **R4: Fix L5 imports** — Replace `from validators.*` imports with L4 role or L2 metric imports. Move `SSHInterface` import to conftest fixture. Remove `sys.path.insert` from test files.
- **Import direction:** After all changes, verify strict L5→L4→L3→L2→L1→SDK
- **Tests pass:** All existing tests must pass after refactoring

## Violations Addressed

| ID | File | Violation | Severity |
|----|------|-----------|----------|
| L2-V1 | — | No `metrics/` directory exists | HIGH |
| L2-V2 | `validators/*.py` | Wrong API (`validate()` not `evaluate()`) | HIGH |
| L3-V1 | `run_ssh_command.py:2` | No L2 composition, calls L1 directly | HIGH |
| L3-V4 | `run_ssh_command.py:2` | Skip-layer L3→L1 | HIGH |
| L4-V1 | `ssh_batch_executor.py` | No L3 imports, DI validators directly | HIGH |
| L4-V3 | `ssh_batch_executor.py` | Orchestrates validators, not L3 tasks | HIGH |
| L5-V1 | `test_ssh_batch.py`, `test_stig_validator.py` | Import from non-standard `validators/` | HIGH |
| V-ID-001 | L3→L1 | Skip-layer | HIGH |
| V-ID-002 | L4→validators | Skip-layer | HIGH |
| V-ID-003 | L5→validators | Skip-layer | HIGH |

## References
- Compliance report: `projects/ssh-5-layer-audit/compliance-report.md`
- SSH platform: `D:/my_ai_projects/project_test_repos/isagawa-qa/platform-ssh/`
- 5-layer reference: `D:/my_ai_projects/project_test_repos/platform-deepeval/framework/`
- Backlog 175: SSH 5-layer audit (source audit)

## Task Builder Input
- **Deliverable:** SSH platform with compliant L2 metrics layer and correct import direction across all layers
- **Location:** `new-repo:D:/my_ai_projects/project_test_repos/isagawa-qa/platform-ssh`
- **Scope:** REFACTOR
- **Constraints:** Must preserve existing validator logic (wrap, don't rewrite). Must not break existing tests during migration. Execute R1→R2→R3→R4 in order (L2 must exist before L3 can compose it).
