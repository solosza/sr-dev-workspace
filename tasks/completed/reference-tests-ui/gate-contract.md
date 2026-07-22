# Gate Contract — 208 _reference UI Tests

Deliverable: framework/_reference/tests/ UI test exemplar on branch build/208-qa-build-reference-tests-ui, GREEN against live Orderly via the framework's own selenium stack. This test passing IS the V1 exit gate.

| Gate | Check | Method |
|------|-------|--------|
| UT-01 | Branch from main (8a23917+); main untouched | run_code |
| UT-02 | Exemplar per tests-ui.md canonical (READ IT — swept 2026-07-21): COPY-FIRST from platform-selenium, AAA, highest-applicable-layer (Task for single-Task, ROLE for multi-user clerk+manager), same-instance page-object asserts, failure messages, degenerate dual assertion (page state carries evidence), pre-conftest interim wiring per doc | run_test AST + read |
| UT-03 | CONTRACT SEMANTICS: AST docstring-excluded fn.body-scoped decorator-aware (lessons #38/#39/#43); no try/except outside pytest.raises; no screenshots/waits/locators/Interface-acts in test bodies; extended lexicon clean (lesson #45) | run_test AST |
| UT-04 | THE EXIT SIGNAL: bare-selenium click probe green at execution time (lessons #41/#42, L3-BLOCKED protocol), then suite GREEN via pytest against live Orderly (fresh seed; port from harness docs; --rootdir=target repo; PYTHONPATH=framework only per DEF-014); zero skips; cleanup asserted | run_test |
| UT-05 | Commit on branch; porcelain clean; no merge to main | run_code |

## Rules
- Lessons #39/#43 for AST scripts; lesson #40 (read route handlers before URL/status assertions); lesson #46 env preflight
- Tests are L5 — they consume Tasks/Roles; no locators, no interface calls to act
- The pipeline reports green/red honestly — L3-BLOCKED if env broken, never fake a pass; a skipped GATE task never waives the gate (orchestrator validates)
