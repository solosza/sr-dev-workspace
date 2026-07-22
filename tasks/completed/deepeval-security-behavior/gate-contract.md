# Gate Contract — DeepEval Security & Behavioral Compliance Testing

## Backlog
176-qa-research-deepeval-security-behavior-testing

## Deliverable
Security and behavioral compliance testing layer for platform-deepeval's 5-layer architecture.

## Target
`D:/my_ai_projects/project_test_repos/platform-deepeval/framework/_reference/`
Branch: `feature/harness-eval-5-layer`

## Acceptance Criteria

### Layer 2: Metric Objects
- [ ] `metrics/security_metrics.py` exists with SecurityMetrics class (GEval-based)
- [ ] `metrics/behavior_metrics.py` exists with BehaviorMetrics class (GEval-based)
- [ ] `metrics/compliance_metrics.py` exists with ComplianceMetrics class (GEval-based)
- [ ] `metrics/data_leakage_metrics.py` exists with DataLeakageMetrics class (inverse threshold)
- [ ] `metrics/tool_boundary_metrics.py` exists with ToolBoundaryMetrics class

### Layer 2: Golden Datasets
- [ ] `fixtures/golden_security_injection.json` — 20+ scenarios
- [ ] `fixtures/golden_security_hook_bypass.json` — 10+ scenarios
- [ ] `fixtures/golden_behavior_protocol.json` — 15+ scenarios
- [ ] `fixtures/golden_behavior_cycling.json` — 10+ scenarios
- [ ] `fixtures/golden_behavior_state.json` — 10+ scenarios

### Layer 3: EvalTasks
- [ ] `tasks/run_protocol_eval.py` composes BehaviorMetrics
- [ ] `tasks/run_security_eval.py` composes SecurityMetrics + DataLeakageMetrics
- [ ] `tasks/run_hook_bypass_eval.py` composes SecurityMetrics (hook subset)
- [ ] `tasks/run_tool_boundary_eval.py` composes ToolBoundaryMetrics
- [ ] `tasks/run_compliance_eval.py` composes ComplianceMetrics

### Layer 4: EvalRoles
- [ ] `roles/security_evaluator.py` orchestrates security evals
- [ ] `roles/compliance_evaluator.py` orchestrates behavioral evals

### Layer 5: Tests
- [ ] `tests/test_prompt_injection.py` — AAA pattern, parametrized
- [ ] `tests/test_hook_bypass.py` — AAA pattern, parametrized
- [ ] `tests/test_tool_boundaries.py` — AAA pattern, parametrized
- [ ] `tests/test_data_leakage.py` — AAA pattern, parametrized
- [ ] `tests/test_protocol_adherence.py` — AAA pattern, parametrized
- [ ] `tests/test_command_sequence.py` — AAA pattern, parametrized
- [ ] `tests/test_state_management.py` — AAA pattern, parametrized
- [ ] `tests/test_cycling_behavior.py` — AAA pattern, parametrized

### Infrastructure
- [ ] `tests/conftest.py` updated with security/behavior fixtures
- [ ] All `__init__.py` files updated with new module imports

### Verification
- [ ] All new modules importable without error
- [ ] pytest collects all new test files without import errors
