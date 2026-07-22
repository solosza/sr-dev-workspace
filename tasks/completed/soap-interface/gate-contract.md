# Gate Contract - 221 SoapInterface (V4 Layer 1)

Deliverable: framework/interfaces/soap_interface.py from scratch wrapping zeep.Client.

| Gate | Check | Method | Task | Pass |
|------|-------|--------|------|------|
| SI4-01 | Branch build/221-qa-build-soap-interface from platform main (incl. 220 SOAP service) | run_code | 001 | merge-base == main HEAD |
| SI4-02 | Interface per soap-interface.md: call_operation + create_object; wraps zeep.Client; WSDL/binding via config (constructor/config, not hardcoded); imports zeep, NOT raw suds/requests-SOAP | file_exists + AST | 002 | methods present; zeep-based; config-driven |
| SI4-03 | Faults: catch-log-RERAISE on all call paths (every except logs then raises; only documented bool state-checks may return); no domain vocabulary at L1 | AST (body-scoped, docstring-excluded, lessons #39/#44) | 004 | all except blocks classified compliant |
| SI4-04 | Clean-room: v2 legacy never mirrored; extended vocab lexicon 0 hits | run_test + grep | 003 | lexicon clean |
| SI4-05 | Negative path: injected SOAP fault (bad operation / unreachable WSDL) PROPAGATES to caller after logging | run_test | 004 | exception surfaces + log line |
| SI4-06 | L3 live vs Orderly SOAP (GATE, skip never waives lesson #39): boot the 220 SOAP service; SoapInterface.call_operation('GetCustomer', customer_id=1) and GetOrderStatus(order_id=1) return values matching the DB; create_object builds a valid request type; teardown | run_test | 005 | live calls match DB |

## Rules
- READ soap-interface.md + 5-layer-contract.md + the merged harness/orderly/soap_service.py FIRST (RULE ZERO)
- Wrap zeep.Client; WSDL URL via config (e.g. http://127.0.0.1:<port>/soap?wsdl)
- catch-log-reraise on faults; no domain vocab at Layer 1
- L3 unreachable => L3-BLOCKED and STOP. Read one sibling interface (sql_server_interface.py / api_interface.py) for idiom only.
- Any red: fix then /kernel/learn
