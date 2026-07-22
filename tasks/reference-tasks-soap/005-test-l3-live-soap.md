# Task 005: L3 - Live vs Orderly SOAP (GATE)
**Type:** TEST (L3) - GATE TASK: skip never waives (lesson #39).
**Gates:** ST-05
## Target
The 220 Orderly SOAP service (boot harness/orderly/main.py, SOAP at /soap?wsdl, seeded DB) + 221 SoapInterface. Unreachable => L3-BLOCKED and STOP. PERSIST this as a pytest under framework/_reference/tests/.
## Action
ONE pytest: seed DB; boot the app (SOAP at /soap on a documented port); construct zeep.Client -> SoapInterface -> the SOAP task; assert a task method returns a TYPED result matching DB (order 1 status eligibility); assert a SOAP fault (bad operation/arg) PROPAGATES through the task to the caller; teardown.
## Acceptance
Live typed result + fault propagation, exit 0, service torn down. Red: fix then /kernel/learn.
