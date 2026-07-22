# 004 — Write DataLeakageMetrics L2 class

**Type:** BUILD
**Deliverable:** `D:/my_ai_projects/project_test_repos/platform-deepeval/framework/_reference/metrics/data_leakage_metrics.py`

## Action
Write `data_leakage_metrics.py` following Metric Object pattern. Inverse threshold (lower=better). Uses GEval for: PIILeakage, CanaryTokenCheck, CredentialExposure. Threshold: 0.1 (inverse).

## Acceptance Criteria
- [ ] File exists at target path
- [ ] Class follows inverse Metric Object pattern (like safety_metrics.py)
- [ ] Threshold constants defined at 0.1 (inverse)
