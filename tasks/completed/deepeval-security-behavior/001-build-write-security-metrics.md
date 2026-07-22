# 001 — Write SecurityMetrics L2 class

**Type:** BUILD
**Deliverable:** `D:/my_ai_projects/project_test_repos/platform-deepeval/framework/_reference/metrics/security_metrics.py`

## Action
Write `security_metrics.py` following the existing Metric Object pattern (see `safety_metrics.py`). Uses GEval for: PromptInjectionResistance, HookBypassResistance, UnauthorizedAction. Threshold: 0.9 (strict). Pattern: `__init__`, `evaluate`, `is_above_threshold`, `get_score`, `get_detail`.

## Acceptance Criteria
- [ ] File exists at target path
- [ ] Class follows Metric Object pattern with GEval metrics
- [ ] Threshold constants defined at 0.9
