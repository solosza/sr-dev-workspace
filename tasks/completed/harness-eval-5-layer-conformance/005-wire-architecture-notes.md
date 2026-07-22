# Task 005: Wire architecture_notes.py into Test Cases

## Action
Connect the orphaned `architecture_notes.py` so harness eval tests pass architectural context to the GEval judge via `LLMTestCase.context`.

## Steps

1. Read `D:/my_ai_projects/project_test_repos/platform-deepeval/framework/metrics/architecture_notes.py` — has `get_notes(dimension)` and `ARCHITECTURE_NOTES` dict
2. Read `D:/my_ai_projects/project_test_repos/platform-deepeval/framework/metrics/harness_metrics.py` — `make_geval_metric()` already supports `use_context=True`
3. Update HarnessMetrics.evaluate() to:
   - Call `get_notes(dimension)` from architecture_notes.py
   - If notes exist for the dimension, pass them as `context` on the LLMTestCase
   - Set `use_context=True` when calling `make_geval_metric()`
4. Update test_eval_harness.py test functions to pass context when creating test cases:
   ```python
   from framework.metrics.architecture_notes import get_notes
   notes = get_notes("command_quality")
   test_case = deepeval_interface.create_test_case(
       input=..., actual_output=..., context=notes
   )
   ```
5. This completes the architecture_notes → harness_metrics → test pipeline that was designed but never wired

## Acceptance Criteria
- `architecture_notes.get_notes()` is called during harness eval
- Dimensions with notes (command_quality, loop_integrity) pass context to the judge
- Dimensions without notes (skill_completeness, etc.) work without context
- `make_geval_metric(dimension, use_context=True)` is used when context exists
