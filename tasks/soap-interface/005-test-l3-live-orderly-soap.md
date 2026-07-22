# Task 005: L3 - Live vs Orderly SOAP (GATE)
**Type:** TEST (L3) - GATE TASK: skip never waives (lesson #39).
**Gates:** SI4-06
## Target
The 220 Orderly SOAP service (boot harness/orderly/main.py which mounts SOAP at /soap, seeded DB). Unreachable => L3-BLOCKED and STOP.
## Action
ONE script: seed DB; boot the app (SOAP at /soap?wsdl) on a documented port; construct SoapInterface with that WSDL URL; call_operation('GetCustomer', customer_id=1) -> assert name/email match DB; call_operation('GetOrderStatus', order_id=1) -> assert status matches DB; create_object builds a valid request type without error; teardown the service.
## Acceptance
Live SOAP calls via the interface match DB, exit 0. Red: fix then /kernel/learn.
