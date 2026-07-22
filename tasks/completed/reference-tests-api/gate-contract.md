# Gate Contract — 213 _reference API Tests

Deliverable: framework/_reference/tests/ API test exemplar on branch build/213-qa-build-reference-tests-api. GREEN against live Orderly = the V2 exit signal (merge still orchestrator-held for 208).

| Gate | Check | Method |
|------|-------|--------|
| AT-01 | Branch from main (94f87f9+); main untouched | run_code |
| AT-02 | Test exemplar per tests-api.md canonical (READ IT): AAA structure, highest-applicable-layer rule (drives via OrderManagementTasks, not raw objects/interface, except where the doc's canonical says otherwise), DUAL ASSERTION per doc, asserted cleanup (ensure_order_absent + verify gone) | run_test AST + read |
| AT-03 | CONTRACT SEMANTICS: no try/except in tests outside doc-sanctioned pytest.raises; fixtures/DI per doc (given conftest doesn't exist until 229, the doc's interim wiring pattern governs — READ what it says about pre-conftest instantiation); extended lexicon clean (lesson #45) | run_test AST |
| AT-04 | THE EXIT SIGNAL: suite runs GREEN via pytest against live Orderly (PORT 8018, fresh seed, --rootdir=target repo per cross-repo pytest lesson); dual assertions genuinely executed (not skipped); cleanup asserted | run_test |
| AT-05 | Commit on branch; porcelain clean | run_code |

## Rules
- Lessons #39/#43 for AST scripts; lesson #40 (read route handlers before URL/status assertions)
- Tests are L5 — they consume Tasks; no locators, no interface calls except where the doc's canonical explicitly demonstrates a lower-layer assertion
- The pipeline reports green/red honestly — L3-BLOCKED if env broken, never fake
