# Task 006: Import Validation

## What
Validate all imports work and no existing functionality is broken after the refactor.

## Validation Commands

Run from `D:/my_ai_projects/project_test_repos/platform-deepeval/`:

```bash
# 1. Import check — all reference modules
python -c "
from _reference.roles.rag_evaluator import RAGEvaluator
from _reference.roles.agent_evaluator import AgentEvaluator
from _reference.roles.security_evaluator import SecurityEvaluator
from _reference.roles.compliance_evaluator import ComplianceEvaluator
from _reference.tasks.run_rag_eval import run_rag_eval
from _reference.tasks.run_security_eval import run_security_eval
from _reference.metrics.security_metrics import SecurityMetrics
print('All _reference/ imports OK')
"

# 2. Import check — framework modules
python -c "
from roles.harness_evaluator import HarnessEvaluator
from roles.ab_evaluator import ABEvaluator
from tasks.run_harness_eval import run_harness_eval
print('All framework/ imports OK')
"

# 3. Contract check — no return values
grep -r "return {" framework/_reference/roles/ framework/roles/ && echo "FAIL: dict returns found" || echo "PASS: no dict returns"

# 4. Contract check — no _eval_results
grep -r "_eval_results" framework/ && echo "FAIL: _eval_results found" || echo "PASS: no _eval_results"

# 5. Contract check — no hardcoded kernel references in metrics
grep -ri "kernel" framework/_reference/metrics/security_metrics.py && echo "FAIL: kernel refs found" || echo "PASS: no kernel refs"

# 6. Test collection
python -m pytest framework/_reference/tests/ --collect-only
```

## Gate
- [ ] All imports succeed
- [ ] No `return {` in roles
- [ ] No `_eval_results` anywhere in framework
- [ ] No kernel-specific references in metric criteria
- [ ] Test collection succeeds (no import errors)

## Gate Contract
This is the FINAL task. All 26 findings from the gap check must be resolved.
