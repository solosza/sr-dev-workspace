# Audit SSH Platform for 5-Layer Eval Framework Compliance

## Status
Open

## Priority
High — SSH platform is a shipped deliverable; non-compliance with the 5-layer framework means inconsistent testing architecture across all platforms

## Summary
Audit all test files in the SSH platform (platform-ssh) against the platform-deepeval 5-layer architecture (L1 DeepEvalInterface, L2 Metrics, L3 EvalTasks, L4 EvalRoles, L5 Tests). Identify direct deepeval SDK imports, tests not going through the interface layer, metrics not using the standard evaluate/is_above_threshold pattern, and any structural violations. Produce a compliance report with specific file:line violations and remediation steps.

## Requirements
- Scan all Python files in `D:/my_ai_projects/project_test_repos/isagawa-qa/platform-ssh/` for:
  - Direct `from deepeval` or `import deepeval` imports (should go through DeepEvalInterface at L1)
  - Test files not following L5 pattern (pytest, AAA, parametrize)
  - Metric classes not using L2 pattern (evaluate, is_above_threshold, get_score)
  - Tasks not following L3 pattern (compose metrics, return None)
  - Roles not following L4 pattern (orchestrate tasks)
- Check import direction: must be strictly downward (L5→L4→L3→L2→L1→SDK)
- Check for banned patterns from step-06-atomize.md (interface in _reference/, tests only in _reference/tests/)
- Produce compliance report with:
  - Per-file violation list (file:line, violation type, current code, required pattern)
  - Summary counts (compliant vs non-compliant files)
  - Remediation steps for each violation type
  - Priority ordering (critical violations first)

## References
- SSH platform: `D:/my_ai_projects/project_test_repos/isagawa-qa/platform-ssh/`
- 5-layer architecture reference: `D:/my_ai_projects/project_test_repos/platform-deepeval/framework/`
- L1 reference: `framework/interfaces/deepeval_interface.py`
- L2 reference: `framework/metrics/` (ab_metrics.py, harness_metrics.py)
- L3 reference: `framework/tasks/`
- L4 reference: `framework/roles/`
- L5 reference: `framework/tests/`
- Prior refactoring: pipelines 172 (A/B 5-layer) and 173 (harness eval 5-layer)

## Task Builder Input
- **Deliverable:** Compliance report with per-file violations and remediation steps
- **Location:** `subproject:ssh-5-layer-audit`
- **Scope:** TEST
- **Constraints:** Read-only audit — do not modify SSH platform files. Only produce the report. Remediation is a separate backlog item if violations found.
