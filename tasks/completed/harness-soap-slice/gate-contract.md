# Gate Contract - 220 Orderly SOAP Slice (V4)

| Gate | Check | Method | Task | Pass |
|------|-------|--------|------|------|
| SO-01 | Branch build/220-qa-build-harness-soap-slice from platform main | run_code | 001 | merge-base == main HEAD |
| SO-02 | SOAP deps installed + pinned (spyne + zeep + lxml) in the harness requirements/env | run_code | 002 | import spyne, zeep OK |
| SO-03 | harness/orderly/soap_service.py: spyne Application exposing GetCustomer(customer_id)->customer fields and GetOrderStatus(order_id)->status, reading via the SAME db layer (db.py / SQLAlchemy Core) as the web routes; generic commerce vocab | file_exists + grep + AST | 003 | both operations defined; uses db layer; no invented vocab |
| SO-04 | WSDL served + reachable: SOAP app mounted (WSGI mount on the FastAPI app OR standalone wsgiref server on a documented port); GET ...?wsdl returns valid WSDL XML | run_test | 004 | wsdl 200 + parses |
| SO-05 | L1: files exist on branch; extended vocab lexicon 0 hits; py_compile | run_test | 005 | clean |
| SO-06 | L2: WSDL defines both operations with correct message types; wsdl parses via zeep client construction (no network call yet) | run_test | 006 | zeep.Client(wsdl) builds, lists both ops |
| SO-07 | L3 GATE (skip never waives, lesson #39): live - boot the SOAP service against the seeded orderly DB, zeep client calls GetCustomer(1) and GetOrderStatus(1), assert returned values match direct DB query; teardown | run_test | 007 | live values match DB |

## Rules
- READ harness-app.md + db.py + main.py before building (RULE ZERO)
- spyne serves SOAP; zeep is the test client. WSDL must be stable for zeep (SO-06/07).
- Only database orderly. Boot on an ephemeral or documented non-conflicting port.
- Any red: fix then /kernel/learn
