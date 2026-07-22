# Fix Platform-DeepEval 5-Layer Contract Violations

## Status
Open

## Priority
High — the `_reference/` folder is the golden pattern that `/kernel/eval` reads to generate test suites. Every violation in `_reference/` propagates to every generated harness. Platform-selenium already has the correct contract (explicit `-> None`, "NO return values" comments). DeepEval must match.

## Summary

Gap check found 26 findings (16 errors, 10 warnings) across `platform-deepeval/framework/`. All 6 roles return dicts instead of `None`. All 9 tasks stuff results onto `test_case._eval_results` instead of letting metrics hold state. Security/behavior metrics have hardcoded Kernel-specific GEval criteria instead of accepting protocol rules as configuration. Fix order: `_reference/` first (golden pattern), then `framework/` follows.

## Design Documents

| Document | Purpose |
|----------|---------|
| [[191-qa-refactor-deepeval-5-layer-contract-violations/phase-1-reference-roles]] | Fix 4 `_reference/` roles: return None, add self.metrics, add state methods |
| [[191-qa-refactor-deepeval-5-layer-contract-violations/phase-2-reference-tasks]] | Fix 7 `_reference/` tasks: remove test_case._eval_results, metrics store state internally |
| [[191-qa-refactor-deepeval-5-layer-contract-violations/phase-3-reference-tests]] | Fix `_reference/` tests: call evaluate() instead of setting _scores directly |
| [[191-qa-refactor-deepeval-5-layer-contract-violations/phase-4-parameterize-metrics]] | Parameterize security/behavior metrics to accept protocol rules as config |
| [[191-qa-refactor-deepeval-5-layer-contract-violations/phase-5-framework-roles-tasks]] | Fix framework/ roles (harness_evaluator, ab_evaluator) and tasks to match corrected _reference/ |
| [[191-qa-refactor-deepeval-5-layer-contract-violations/gap-check-findings]] | Full 26-finding gap check report with file:line locations |

## Architecture

```
Phase 1: Fix _reference/ roles (golden pattern)
  ├─ rag_evaluator.py — return None, add self.metrics + state methods
  ├─ agent_evaluator.py — same
  ├─ security_evaluator.py — same
  └─ compliance_evaluator.py — same
         ↓
Phase 2: Fix _reference/ tasks
  ├─ run_rag_eval.py — remove test_case._eval_results
  ├─ run_agent_eval.py — same
  ├─ run_security_eval.py — same
  ├─ run_compliance_eval.py — same
  ├─ run_hook_bypass_eval.py — same
  ├─ run_tool_boundary_eval.py — same
  └─ run_protocol_eval.py — same
         ↓
Phase 3: Fix _reference/ tests
  ├─ test_rag_pipeline.py — call evaluate(), not _scores =
  ├─ test_prompt_injection.py — same
  └─ test_hook_bypass.py — same
         ↓
Phase 4: Parameterize metrics
  ├─ security_metrics.py — accept protocol rules as config
  ├─ behavior_metrics.py — same
  ├─ compliance_metrics.py — same
  ├─ tool_boundary_metrics.py — same
  └─ data_leakage_metrics.py — same
         ↓
Phase 5: Fix framework/ (mirrors _reference/)
  ├─ roles/harness_evaluator.py — return None, self.metrics, state methods
  ├─ roles/ab_evaluator.py — same
  ├─ tasks/run_harness_eval.py — remove _eval_results
  ├─ tasks/run_ab_eval.py — same
  └─ tests/ — assert on role state, not return values
```

## Requirements
- All roles return `None` with explicit `-> None` type hint and "NO return values" docstring comment (matching platform-selenium)
- All roles store state on `self.metrics` dict and expose boolean state-check methods
- All tasks remove `test_case._eval_results` — metrics hold state via `evaluate()` returning `self`
- Security/behavior metrics accept protocol rules as constructor config, not hardcoded GEval criteria
- `discover_harness()` generalized beyond `.claude/commands/kernel/` path
- All tests assert on metric/role state methods, not return values or `_scores` direct access
- Platform-selenium `_reference/` is the canonical contract reference

## References
- **Platform-deepeval:** `D:/my_ai_projects/project_test_repos/platform-deepeval`
- **Platform-selenium (canonical contract):** `D:/my_ai_projects/project_test_repos/platform-selenium`
- **Selenium role pattern:** `platform-selenium/framework/_reference/roles/employee_manager.py` — "NO return values" comment
- **Selenium task pattern:** `platform-selenium/framework/_reference/tasks/employee_management_tasks.py` — `-> None`
- **Selenium test pattern:** `platform-selenium/framework/_reference/tests/test_e2e_create_employee_and_assign_task.py` — assert on page object state
- **Gap check source:** Discussion in sr_dev_workspace session 2026-07-07
- **Related:** Backlog 176 (DeepEval security/behavior testing — iterated, needs this fix first)

## Task Builder Input
- **Deliverable:** Corrected `_reference/` and `framework/` files in platform-deepeval matching platform-selenium's 5-layer contract
- **Location:** `new-repo:D:/my_ai_projects/project_test_repos/platform-deepeval`
- **Scope:** REFACTOR
- **Constraints:** Must not break existing test imports. Fix `_reference/` first — it's the golden pattern. Platform-selenium is the canonical reference for the contract. Must read platform-selenium roles/tasks/tests before modifying deepeval equivalents.
