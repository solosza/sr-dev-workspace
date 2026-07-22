# Phase 5: Fix framework/ Roles and Tasks

## Status
NEW

## Location
`platform-deepeval/framework/`

## What To Fix

`framework/` mirrors `_reference/` — same violations, same fixes. Fix AFTER `_reference/` is correct.

### Roles To Fix

| File | Current Violation | Fix |
|------|-------------------|-----|
| `roles/harness_evaluator.py:127` | `evaluate_harness()` returns dict | Return `None`, add `self.metrics` + state methods |
| `roles/harness_evaluator.py:33` | `discover_harness()` hardcoded to `.claude/commands/kernel/` | Generalize path (accept as parameter or scan) |
| `roles/harness_evaluator.py:123-124` | Reads `_eval_results` from test cases | Read from `self.metrics` instead |
| `roles/ab_evaluator.py:50` | `evaluate_experiment()` returns dict | Return `None`, add `self.metrics` + state methods |

### Tasks To Fix

| File | Violation | Fix |
|------|-----------|-----|
| `tasks/run_harness_eval.py:21` | `test_case._eval_results = {dimension: metrics}` | Use `metrics_out` parameter, remove `_eval_results` |
| `tasks/run_ab_eval.py` | Same `_eval_results` pattern | Same fix |

### Tests To Fix

| File | Violation | Fix |
|------|-----------|-----|
| `tests/` | Assert on return values or `_scores` direct access | Assert on role state methods (`is_dimension_passing`, `get_score`) |

### discover_harness() Fix

```python
# BEFORE (hardcoded)
def discover_harness(self):
    path = Path(".claude/commands/kernel/")  # Kernel-specific

# AFTER (parameterized)
def discover_harness(self, harness_root=None):
    """Discover harness from given root or auto-detect."""
    if harness_root:
        path = Path(harness_root)
    else:
        # Auto-detect: scan for .claude/commands/*/eval.md
        path = self._auto_detect_harness_root()
```

### Acceptance Criteria
- [ ] `harness_evaluator.py` returns `None`, has `self.metrics` + state methods
- [ ] `ab_evaluator.py` returns `None`, has `self.metrics` + state methods
- [ ] `discover_harness()` accepts path parameter, not hardcoded to kernel
- [ ] No `_eval_results` in any task
- [ ] Tests assert on role/metric state methods, not return values
- [ ] All changes mirror the corrected `_reference/` pattern
