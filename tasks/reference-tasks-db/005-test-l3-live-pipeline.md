# Task 005: L3 - Live Pipeline (GATE)

**Type:** TEST (L3) - GATE TASK: skip never waives (lesson #39).
**Gates:** DT-05

## Target
Native SQL Server, database orderly, via the REAL chain (Task -> OrdersDataObject -> SqlServerInterface). Unreachable => L3-BLOCKED and STOP. Only orderly/orderly_v3.

## Action
ONE script: construct the full chain; set order 1 PENDING directly; call the run method with variant 'process_pending'; call the verify method(s) - assert PENDING count 0 and transitions verified through the Task layer's own API; typed result accessible; then reseed (init_sqlserver.py) and confirm baseline.

## Acceptance
Live asserts PASS, exit 0, DB reseeded. Red: fix then /kernel/learn.
