# Gate Contract - 223 _reference SOAP Test (V4 Exit Gate)

Deliverable: framework/_reference/tests/ SOAP test exemplar per tests-soap.md - typed assertion + pytest.raises fault test. GREEN live = V4 exit gate.

| Gate | Check | Method | Task | Pass |
|------|-------|--------|------|------|
| SE-01 | Branch from platform main (incl. 222) | run_code | 001 | merge-base == main HEAD |
| SE-02 | Test exemplar per tests-soap.md: typed assertions (pydantic result fields, not raw zeep); a pytest.raises fault test (bad op/arg raises through the chain); conftest fixture wiring that boots/points-at the Orderly SOAP service; PYTHONPATH=framework documented in the test (lesson #47 - state PYTHONPATH explicitly) | AST + grep | 002 | typed + raises + documented env |
| SE-03 | L1: structure per doc; lexicon 0 hits; single-root imports; py_compile | run_test | 003 | clean |
| SE-04 | L2: fixture scope correct; no hardcoded creds; test IDs meaningful; env (PYTHONPATH=framework, service URL, DB) documented so the suite is portable (avoid the 222 fixture-env-sensitivity nit) | run_test | 004 | portable fixtures |
| SE-05 | L3 EXIT GATE (skip never waives lesson #39): full SOAP suite GREEN live via pytest against the booted Orderly SOAP service - typed assertion passes + fault test passes; report explicitly 'V4 SOAP SLICE EXIT GATE: PASS' | run_test | 005 | suite green live, gate confirmed |

## Rules
- READ tests-soap.md + 5-layer-contract.md + merged 220/221/222 deliverables FIRST (RULE ZERO)
- This is the vertical's exit gate - red here means the WHOLE V4 SOAP slice is not done
- Fixture MUST be portable: state PYTHONPATH=framework + the DATABASE_URL + SOAP service URL explicitly (222 residue: env-sensitive fixture)
- L3 unreachable => L3-BLOCKED and STOP. Only orderly DB.
- Any red: fix then /kernel/learn
