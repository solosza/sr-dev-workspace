# Gap Check Findings — 26 Findings

## Source
Gap check run against `platform-deepeval/framework/` on 2026-07-07.

## Summary
16 errors, 10 warnings across `_reference/` and `framework/`.

## Errors (16)

### E01-E04: _reference/ roles return dicts
| # | File | Line | Finding |
|---|------|------|---------|
| E01 | `_reference/roles/rag_evaluator.py` | 40 | `evaluate_pipeline()` returns `{"test_cases": ...}` |
| E02 | `_reference/roles/agent_evaluator.py` | 40 | `evaluate_pipeline()` returns dict |
| E03 | `_reference/roles/security_evaluator.py` | 50 | `evaluate_pipeline()` returns dict |
| E04 | `_reference/roles/compliance_evaluator.py` | 44 | `evaluate_pipeline()` returns dict |

### E05-E06: framework/ roles return dicts
| # | File | Line | Finding |
|---|------|------|---------|
| E05 | `roles/harness_evaluator.py` | 127 | `evaluate_harness()` returns dict |
| E06 | `roles/ab_evaluator.py` | 50 | `evaluate_experiment()` returns dict |

### E07-E13: tasks use test_case._eval_results
| # | File | Line | Finding |
|---|------|------|---------|
| E07 | `_reference/tasks/run_rag_eval.py` | 25 | `test_case._eval_results = {...}` |
| E08 | `_reference/tasks/run_agent_eval.py` | ~ | Same |
| E09 | `_reference/tasks/run_security_eval.py` | ~ | Same |
| E10 | `_reference/tasks/run_compliance_eval.py` | ~ | Same |
| E11 | `_reference/tasks/run_hook_bypass_eval.py` | ~ | Same |
| E12 | `_reference/tasks/run_tool_boundary_eval.py` | ~ | Same |
| E13 | `_reference/tasks/run_protocol_eval.py` | ~ | Same |

### E14: framework/ task uses _eval_results
| # | File | Line | Finding |
|---|------|------|---------|
| E14 | `tasks/run_harness_eval.py` | 21 | `test_case._eval_results = {dimension: metrics}` |

### E15-E16: tests bypass evaluate()
| # | File | Line | Finding |
|---|------|------|---------|
| E15 | `_reference/tests/test_prompt_injection.py` | 27 | `metrics._scores["..."] = 0.95` |
| E16 | `_reference/tests/test_prompt_injection.py` | 61 | `metrics._scores["..."] = 0.95` |

## Warnings (10)

### W01-W05: Hardcoded Kernel-specific GEval criteria
| # | File | Line | Finding |
|---|------|------|---------|
| W01 | `_reference/metrics/security_metrics.py` | 47 | HookBypassResistance criteria references `/kernel/anchor`, `/kernel/learn` |
| W02 | `_reference/metrics/security_metrics.py` | 63 | UnauthorizedAction criteria references `prod-test/run-task.sh` |
| W03 | `_reference/metrics/security_metrics.py` | 37 | PromptInjectionResistance criteria mentions "documented protocol rules" (generic, but could be more parameterizable) |
| W04 | Behavior metrics (if exist) | ~ | Same hardcoded pattern |
| W05 | Compliance metrics (if exist) | ~ | Same hardcoded pattern |

### W06: discover_harness() hardcoded path
| # | File | Line | Finding |
|---|------|------|---------|
| W06 | `roles/harness_evaluator.py` | 33 | Hardcoded to `.claude/commands/kernel/` |

### W07-W08: Roles missing state-check methods
| # | File | Line | Finding |
|---|------|------|---------|
| W07 | All `_reference/roles/` | ~ | No `is_dimension_passing()`, `get_score()`, `get_count()` methods |
| W08 | `roles/harness_evaluator.py` | ~ | No state-check boolean methods |

### W09-W10: _eval_results reads in framework
| # | File | Line | Finding |
|---|------|------|---------|
| W09 | `roles/harness_evaluator.py` | 123-124 | Reads `_eval_results` from test cases |
| W10 | `roles/ab_evaluator.py` | ~ | May read `_eval_results` |

## Fix Order

```
Phase 1: _reference/ roles (E01-E04, W07) — golden pattern
Phase 2: _reference/ tasks (E07-E13) — remove _eval_results
Phase 3: _reference/ tests (E15-E16) — call evaluate()
Phase 4: Parameterize metrics (W01-W05) — generic criteria
Phase 5: framework/ roles + tasks (E05-E06, E14, W06, W08-W10) — mirror _reference/
```
