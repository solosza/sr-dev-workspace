# 004 — Edit Batch Executor: Framework-Aware Reporting

**Type:** BUILD
**Depends on:** 001

## Target
`D:\my_ai_projects\project_test_repos\isagawa-qa\platform-ssh-test\framework\_reference\roles\ssh_batch_executor.py`

## Requirements
Enhance SSHBatchExecutor to produce framework-grouped results. Update `get_results()` to include a `by_framework` breakdown when results contain the `framework` field (from ComplianceValidator).

Enhanced summary format:
```json
{
  "total": 45,
  "passed": 42,
  "failed": 3,
  "by_framework": {
    "DISA STIG": {"total": 15, "passed": 14, "failed": 1},
    "CIS L1": {"total": 12, "passed": 12, "failed": 0}
  },
  "details": [...]
}
```

Must remain backward compatible: if results don't have `framework` field (old-style validators), `by_framework` is empty or omitted.

## Acceptance Criteria
- [ ] `ssh_batch_executor.py` contains `by_framework`
- [ ] `get_results()` still returns `total`, `passed`, `failed`, `details`

## Gates
BUILD-08
