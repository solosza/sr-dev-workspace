# Gate Contract - 222 _reference SOAP Tasks (V4)

Deliverable: framework/_reference/tasks/ SOAP task exemplar over SoapInterface (order status eligibility domain flow).

| Gate | Check | Method | Task | Pass |
|------|-------|--------|------|------|
| ST-01 | Branch from platform main (incl. 221 SoapInterface) | run_code | 001 | merge-base == main HEAD |
| ST-02 | SOAP tasks class per tasks-soap.md: DI constructor (SoapInterface injected, constructs nothing); task methods call operations via the interface (call_operation), return TYPED results (not raw zeep objects); order-status-eligibility flow per doc | AST | 002 | structure per doc |
| ST-03 | L1: canonical structure; extended lexicon 0 hits; single-root imports; py_compile | run_test | 003 | clean |
| ST-04 | L2 contract semantics (AST body-scoped, docstring-excluded): except-blocks reraise (fault propagation - a SOAP fault surfaces, not swallowed); no interface/zeep imports at Task layer (SoapInterface only); typed returns | run_test | 004 | compliant |
| ST-05 | L3 GATE (skip never waives lesson #39): live vs Orderly SOAP - boot the 220 service; construct SoapInterface (221) + the SOAP task; task method returns typed result matching DB (e.g. order status eligibility for order 1); a SOAP fault (bad op/arg) propagates through the task to caller; teardown | run_test | 005 | live typed result + fault propagation |

## Rules
- READ tasks-soap.md + 5-layer-contract.md + merged soap_interface.py (221) FIRST (RULE ZERO)
- Layer 3 consumes the SoapInterface (Layer 1) - no direct zeep at Task layer
- L3 unreachable => L3-BLOCKED and STOP
- Note (221 residue): create_object has a spyne-namespace quirk; prefer call_operation for the task flow, or use the namespace-qualified type name if create_object is needed
- Any red: fix then /kernel/learn
