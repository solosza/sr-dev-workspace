# Component Decision Table

Determines whether to reuse existing `_reference/` components or create new ones.

## Decision Matrix

| Component Needed | Detection Path | Exists? | Action |
|------------------|---------------|---------|--------|
| Agent metrics (ToolCorrectness, TaskCompletion) | `_reference/metrics/agent_metrics.py` | Yes | Copy to test repo `framework/` as-is |
| GEval for custom contract rules | `_reference/metrics/custom_metrics.py` | Yes | Copy template, generate criteria from target's contracts |
| Faithfulness / contextual metrics | `_reference/metrics/faithfulness_metrics.py` | Yes | Copy if target has retrieval/context components |
| Agent eval task | `_reference/tasks/run_agent_eval.py` | Yes | Copy as pattern, adapt for target's pipeline type |
| RAG eval task | `_reference/tasks/run_rag_eval.py` | Yes | Copy if target is RAG-type pipeline |
| Test file pattern | `_reference/tests/test_rag_pipeline.py` | Yes | Copy structure, adapt assertions for target |
| Conftest / fixtures | `_reference/tests/conftest.py` | Yes | Copy fixture loading pattern |
| Kernel-specific metrics | `_reference/metrics/kernel_*.py` | Maybe | If missing: create following `agent_metrics.py` pattern |
| Kernel eval task | `_reference/tasks/run_kernel_eval.py` | Maybe | If missing: create following `run_agent_eval.py` pattern |
| Kernel test file | `_reference/tests/test_kernel_*.py` | Maybe | If missing: create following `test_rag_pipeline.py` pattern |
| Harness metrics (GEval) | `_reference/metrics/harness_metrics.py` | Maybe | If missing: create with GEval criteria per harness dimension |
| Harness eval task | `_reference/tasks/run_harness_eval.py` | Maybe | If missing: create following `run_agent_eval.py` pattern |
| Harness test file | `_reference/tests/test_harness_eval.py` | Maybe | If missing: create with parametrized GEval + structural checks |
| Harness golden dataset | `_reference/fixtures/golden_harness.json` | Maybe | If missing: generate from harness component inventory |

## Pipeline Type Mapping

| Pipeline Type | Required Metrics | Required Task Runner |
|---------------|-----------------|---------------------|
| **Agent** (uses tools, follows protocols) | ToolCorrectness, TaskCompletion, GEval per contract rule | `run_agent_eval.py` pattern |
| **RAG** (retrieves and generates) | Faithfulness, ContextualRelevancy, AnswerRelevancy | `run_rag_eval.py` pattern |
| **Hybrid** (agent + retrieval) | All agent metrics + faithfulness metrics | Combine both patterns |
| **Harness** (whole repo as system) | GEval per dimension + structural assertions | `run_harness_eval.py` (new, pattern: `run_agent_eval.py`) |

## Creation Rules

When creating a new component:

1. Read the closest `_reference/` implementation first — it IS the pattern
2. Follow the same class structure, naming, return patterns
3. `DeepEvalInterface` methods first — check what the interface provides
4. Metric Objects return `self`, Tasks return `None`
5. Golden datasets are fixtures (loaded from JSON), never hardcoded
6. Thresholds are configurable with sensible defaults (0.7 for most metrics)
7. Place new components in test repo's `framework/`, NOT in master platform-deepeval
8. Document what was created in the eval report (component name, source pattern, adaptations)

## Pattern Adherence Checklist

Before committing any new component, verify:

- [ ] `DeepEvalInterface` methods checked first — reuse interface methods before writing custom logic
- [ ] Metric Objects return `self` (not raw values, not dicts)
- [ ] Tasks return `None` (side effects only — write files, update state)
- [ ] Golden datasets loaded from fixture files (JSON), never hardcoded in test or metric code
- [ ] Thresholds are constructor parameters with defaults, not magic numbers in method bodies
- [ ] Class/method naming matches `_reference/` conventions (e.g., `KernelProtocolFaithfulness` not `check_protocol`)
- [ ] Imports follow `_reference/` patterns (DeepEval SDK imports, then interface, then local)
