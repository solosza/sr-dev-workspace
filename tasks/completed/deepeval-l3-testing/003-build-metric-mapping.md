# Build Metric Mapping

## Type
BUILD

## Phase Gate
None (no dependencies).

## Deliverable
`framework/metric_mapping.py`

## Instructions
1. Read the metric-mapping design doc: `docs/backlog/154-kernel-build-deepeval-l3-testing/metric-mapping.md`
2. Create `framework/metric_mapping.py` implementing:
   - `select_metrics(pipeline_type)` — returns auto-selected metrics for pipeline type (Agent: ToolCorrectness, TaskCompletion)
   - `generate_geval_criteria(contract)` — reads contract's `soft_validation_rules`, generates GEval criterion per rule with name, criteria text, evaluation_params, threshold
   - `generate_geval_from_success_criteria(contract)` — generates GEval from `success_criteria` for TaskCompletion scoring
   - `get_optional_metrics(contract)` — returns additional metrics based on contract signals (Faithfulness if context refs, Hallucination if xlsx/DB reads)
   - Threshold constants: minimum_viable=0.5, acceptable=0.7, production_ready=0.85, target=0.95
3. GEval criteria must include `evaluation_params: ["input", "actual_output", "expected_output"]`

## Verification
- File exists at `framework/metric_mapping.py`
- Contains `select_metrics`, `generate_geval_criteria` functions
