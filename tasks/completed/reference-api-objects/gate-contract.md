# Gate Contract — 211 _reference API Objects

Deliverables on branch build/211-qa-build-reference-api-objects: `framework/_reference/api_objects/models/*.py` (pydantic), `orders_api_object.py`, SOAP object exemplar per api-objects.md.

| Gate | Check | Method |
|------|-------|--------|
| AO-01 | Branch from main (d212801+); main untouched | run_code |
| AO-02 | Pydantic models bind Orderly's ACTUAL JSON shapes (209's docstrings + live responses are the source — read routes_api_*.py; field-exact) | run_test |
| AO-03 | OrdersApiObject per design doc canonical: constructor takes ApiInterface via DI (never constructs it); endpoint paths owned HERE (slash-canonical per 209 flag); last_response convention exactly as the design doc specifies; methods return self or models per doc | run_test — AST + execution |
| AO-04 | CONTRACT SEMANTICS (lessons #38/#39/#43): no try/except outside documented state-checks; no screenshot machinery; DI-only; AST body-scoped/decorator-aware; string-grep BANNED | run_test |
| AO-05 | SOAP object exemplar: shape per design doc, imports clean, L1/L2 only — its live e2e is EXPLICITLY deferred to V4 (documented in the file's docstring) | run_test import + AST |
| AO-06 | L3 live vs Orderly: OrdersApiObject drives create→process→verify→delete through ApiInterface; pydantic models validate real responses; L3-BLOCKED honestly if env broken | run_test |
| AO-07 | No healthcare vocab; commit on branch; porcelain clean | grep + run_code |

## Test-Script Requirements (lessons #39/#43 — MANDATORY)
AST-based, docstrings excluded, fn.body per-statement walks (decorator-aware). RULE ZERO for the builder: READ api-objects.md's canonical example + the ACTUAL routes_api_*.py response shapes before writing models — do not invent fields.

## Port Rule
Live tests: Orderly on PORT 8018.
