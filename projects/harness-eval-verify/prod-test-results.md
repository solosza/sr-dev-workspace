# Prod Test Results — platform-deepeval

**Date:** 2026-07-07
**Target:** `D:/my_ai_projects/project_test_repos/platform-deepeval`

## Import Verification

All framework layers import correctly:

| Module | Class/Export | Status |
|--------|-------------|--------|
| `interfaces.deepeval_interface` | `DeepEvalInterface` | PASS |
| `metrics.harness_metrics` | `HarnessMetrics` | PASS |
| `metrics.ab_metrics` | `ABMetrics` | PASS |
| `metrics.architecture_notes` | `ARCHITECTURE_NOTES` | PASS |
| `ab_testing.experiment_config` | `ExperimentConfig` | PASS |
| `ab_testing.runner` | `ABRunner` | PASS |
| `ab_testing.scorer` | `ABScorer` | PASS |
| `ab_testing.reporter` | `ABReporter` | PASS |
| `ab_testing.variant_generator` | `VariantGenerator` | PASS |

## Test Results

### Framework Tests (L2 — structural)
- **34 passed, 0 failed** (0.34s)
- Test files: `test_ab_eval.py`, `test_harness_eval.py`
- Covers: metric scoring, threshold validation, evaluate contract, accessors, dimensions

### Reference Tests (L2 — behavioral)
- **321 passed, 0 failed** (0.63s)
- Test files: `test_command_sequence.py`, `test_cycling_behavior.py`, `test_data_leakage.py`, `test_hook_bypass.py`, `test_prompt_injection.py`, `test_protocol_adherence.py`, `test_rag_pipeline.py`, `test_state_management.py`, `test_tool_boundaries.py`
- Covers: command sequence compliance, cycling behavior, data leakage detection, hook bypass prevention, prompt injection resistance, protocol adherence, RAG pipeline correctness, state management, tool boundary enforcement

### Kernel Integration Tests (L3 — GEval)
- **Skipped** — requires `--harness-root` flag and valid `OPENAI_API_KEY`
- These are LLM-as-judge evaluations that test a specific kernel harness target
- Not runnable in isolation without a harness target and API credentials

## Summary

| Level | Tests | Passed | Failed | Skipped |
|-------|-------|--------|--------|---------|
| L2 Framework | 34 | 34 | 0 | 0 |
| L2 Reference | 321 | 321 | 0 | 0 |
| L3 GEval | — | — | — | skipped (requires harness + API key) |
| **Total** | **355** | **355** | **0** | **0** |

All layers import correctly. All existing tests pass. Harness eval platform verified operational.
