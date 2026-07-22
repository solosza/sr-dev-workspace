# 5-Layer Reference Checklist

Extracted from platform-deepeval `framework/` — the compliance baseline for auditing SSH platform.

## Layer 1: Interface (`interfaces/`)

### Required Patterns
- Single file: `deepeval_interface.py`
- Single class: `DeepEvalInterface`
- Constructor: `__init__(self, config: dict, logger: logging.Logger)`
- Imports DeepEval SDK directly: `from deepeval import evaluate, assert_test`, `from deepeval.test_case import LLMTestCase`, `from deepeval.metrics import ...`
- All DeepEval SDK imports concentrated here — no other layer imports `deepeval` directly (except L2 for `GEval` and `LLMTestCaseParams`)
- Methods expose SDK operations: `create_test_case()`, `create_metric()`, `create_custom_metric()`, `measure_metric()`, `run_evaluation()`, `load_dataset()`, `assert_test()`
- Retry logic lives here (`max_retries`, exponential backoff)
- Result persistence lives here (`save_results()`, `_save_failure_report()`)

### Banned Patterns
- No business logic (metric criteria, dimension definitions)
- No orchestration (looping over experiments, discovering harness components)

## Layer 2: Metrics (`metrics/`)

### Required Patterns
- One file per metric domain: `ab_metrics.py`, `harness_metrics.py`
- Each file has a Metric Object class: `ABMetrics`, `HarnessMetrics`
- Module-level criteria constants: `METRIC_CRITERIA` dict, `METRIC_THRESHOLDS` dict (or `DIMENSION_CRITERIA`, `DIMENSION_THRESHOLDS`)
- Criteria are natural-language strings for GEval
- Class has: `evaluate()` (returns self for fluent chaining), `is_above_threshold()`, `get_score()`, `get_detail()`
- Internal state: `_scores: dict`, `_details: dict`, `_interface` (optional DeepEvalInterface), `_thresholds`
- GEval metric construction: `GEval(name=..., criteria=..., evaluation_params=[...], threshold=...)`
- Imports: `from deepeval.metrics import GEval` and `from deepeval.test_case import LLMTestCase, LLMTestCaseParams` — these are the ONLY allowed DeepEval imports outside L1
- Optional: factory function `make_geval_metric()` for dimension-based construction

### Banned Patterns
- No direct `from deepeval import evaluate` or `from deepeval.metrics import FaithfulnessMetric` — those belong in L1
- No orchestration logic (looping over experiments)
- No file I/O or harness discovery

## Layer 3: Tasks (`tasks/`)

### Required Patterns
- One file per eval task: `run_ab_eval.py`, `run_harness_eval.py`
- Each file has a single function (not a class): `run_ab_eval()`, `run_harness_eval()`
- Function composes L2 metrics: creates Metric Object, calls `.evaluate()`, attaches results to test case
- Returns `None` — results accessed via `test_case._eval_results`
- Import pattern: `from metrics.<module> import <MetricClass>` (relative to `framework/` PYTHONPATH)
- Parameters: `deepeval_interface` (L1), `test_case` (LLMTestCase), domain-specific args (dimension, thresholds)

### Banned Patterns
- No class definitions (tasks are functions)
- No direct DeepEval SDK imports
- No file I/O or harness discovery
- No result formatting or reporting

## Layer 4: Roles (`roles/`)

### Required Patterns
- One file per evaluator role: `ab_evaluator.py`, `harness_evaluator.py`
- Each file has a single class: `ABEvaluator`, `HarnessEvaluator`
- Constructor: `__init__(self, deepeval_interface)` — receives L1 interface
- Main method orchestrates: discovers content, builds test cases (via L1 `create_test_case()`), calls L3 task functions, collects results
- Import pattern: `from tasks.<module> import <task_function>` (L3 only)
- May also import L2 constants: `from metrics.<module> import DIMENSION_CRITERIA`
- Returns structured result dict: `{ "test_cases": ..., "count": ..., "eval_type": "..." }`
- File I/O and harness discovery lives here (e.g., `discover_harness()` reads `.claude/` directories)

### Banned Patterns
- No direct DeepEval SDK imports
- No metric construction (that's L2)
- No metric measurement (that's L1 via L2)

## Layer 5: Tests (`tests/`)

### Required Patterns
- `conftest.py` provides fixtures: `deepeval_interface` fixture creates DeepEvalInterface with config + logger
- Import from L1: `from interfaces.deepeval_interface import DeepEvalInterface`
- Test files: one per eval domain (`test_ab_eval.py`)
- Test classes use descriptive names: `TestABMetricScoring`, `TestABMetricsEvaluateContract`, `TestABMetricsAccessors`
- Tests import L2 metrics: `from metrics.ab_metrics import ABMetrics, METRIC_CRITERIA`
- AAA pattern: Arrange / Act / Assert with comments
- `@pytest.mark.parametrize` for dimension/metric iteration
- Method naming: `test_<what>_REQ_<layer>` (e.g., `test_ab_metric_scores_REQ_L2`)
- Assertions use metric object methods: `metrics.is_above_threshold()`, `metrics.get_score()`, `metrics.get_detail()`
- Mock LLM judge by populating `metrics._scores` directly (no real API calls in unit tests)

### Banned Patterns
- No direct DeepEval SDK imports (only via L1 fixtures or L2 classes)
- No file I/O in tests (fixtures provide all data)
- No `from deepeval.metrics import ...` in test files

## Import Direction (Critical)

```
L5 (tests) → imports → L2 (metrics), L1 (via fixtures)
L4 (roles) → imports → L3 (tasks), L2 (constants)
L3 (tasks) → imports → L2 (metrics)
L2 (metrics) → imports → deepeval.metrics.GEval, deepeval.test_case (ONLY these)
L1 (interface) → imports → deepeval SDK (all imports)
```

**Direction rule:** Higher layers import lower layers. Never: L1→L2, L2→L3, L3→L4, etc.

**PYTHONPATH rule:** All imports are relative to `framework/` directory. Use `from metrics.ab_metrics import ...` NOT `from framework.metrics.ab_metrics import ...`.
