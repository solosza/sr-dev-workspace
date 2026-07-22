# Phase 2: Fix _reference/ Tasks

## Status
NEW

## Location
`platform-deepeval/framework/_reference/tasks/`

## What To Fix

All 7 tasks stuff results onto `test_case._eval_results` — wrong state holder. Metrics already store state internally via `evaluate()` returning `self`. Tasks should store metric references on the role (via callback or return to role), NOT on test_case.

### Current Violation Pattern

```python
# WRONG — test_case is not the state holder
def run_rag_eval(deepeval_interface, test_case, thresholds=None) -> None:
    faithfulness = FaithfulnessMetrics(thresholds).evaluate(test_case)
    retrieval = RetrievalMetrics(thresholds).evaluate(test_case)
    relevancy = RelevancyMetrics(thresholds).evaluate(test_case)
    test_case._eval_results = {  # VIOLATION: wrong state holder
        "faithfulness": faithfulness,
        "retrieval": retrieval,
        "relevancy": relevancy,
    }
```

### Canonical Pattern (platform-selenium tasks)

```python
# Tasks operate on state holders (page objects), return None
def login(self, login_url, email, password) -> None:
    (self.login_page
        .navigate(login_url)
        .wait_for_login_button_visible()
        .click_log_in()...)
# State lives on self.login_page — the page object IS the state holder
```

### Target Pattern (after fix)

```python
def run_rag_eval(deepeval_interface, test_case, thresholds=None,
                 metrics_out: dict = None) -> None:
    """Run RAG evaluation. Returns None.
    Metrics store state internally. Role passes metrics_out dict to collect references."""
    faithfulness = FaithfulnessMetrics(thresholds).evaluate(test_case)
    retrieval = RetrievalMetrics(thresholds).evaluate(test_case)
    relevancy = RelevancyMetrics(thresholds).evaluate(test_case)
    if metrics_out is not None:
        metrics_out["faithfulness"] = faithfulness
        metrics_out["retrieval"] = retrieval
        metrics_out["relevancy"] = relevancy
    # NO test_case._eval_results
    return None
```

The role then calls: `run_rag_eval(self.deepeval_interface, test_case, thresholds, self.metrics)`

### Files To Fix

| File | Lines | Fix |
|------|-------|-----|
| `run_rag_eval.py:25-29` | Remove `test_case._eval_results`, use `metrics_out` |
| `run_agent_eval.py` | Same pattern |
| `run_security_eval.py` | Same pattern |
| `run_compliance_eval.py` | Same pattern |
| `run_hook_bypass_eval.py` | Same pattern |
| `run_tool_boundary_eval.py` | Same pattern |
| `run_protocol_eval.py` | Same pattern |

### Acceptance Criteria
- [ ] No task writes to `test_case._eval_results`
- [ ] All tasks accept `metrics_out: dict = None` parameter
- [ ] All tasks return `None` with `-> None` type hint
- [ ] Metric objects store state internally (already do — `evaluate()` returns `self`)
- [ ] Role passes `self.metrics` dict to tasks for metric collection
