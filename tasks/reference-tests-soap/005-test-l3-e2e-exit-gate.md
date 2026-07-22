# Task 005: L3 - E2E Live (V4 EXIT GATE)
**Type:** TEST (L3) - GATE TASK: skip never waives (lesson #39). THIS IS THE V4 SOAP SLICE EXIT GATE.
**Gates:** SE-05
## Target
Booted Orderly SOAP service (harness/orderly/main.py, SOAP at /soap?wsdl, seeded DB) + the full chain (SoapInterface -> OrderStatusTasks). Unreachable => L3-BLOCKED and STOP.
## Action
Run the exemplar suite live via pytest (state PYTHONPATH=framework + DATABASE_URL explicitly). Assert: typed assertion passes (order/customer match seeded DB); pytest.raises fault test passes (fault propagates). Reseed if mutated. Report explicitly: "V4 SOAP SLICE EXIT GATE: PASS" or the specific failure.
## Acceptance
Suite green live, exit gate explicitly confirmed. Red: fix then /kernel/learn.
