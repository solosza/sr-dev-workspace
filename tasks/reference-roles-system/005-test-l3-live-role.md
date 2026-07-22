# Task 005: L3 - Live Role Execution (GATE)

**Type:** TEST (L3) - GATE TASK: skip never waives (lesson #39).
**Gates:** SR-05

## Target
Native SQL Server, database orderly, full chain. Unreachable => L3-BLOCKED and STOP.

## Action
ONE pytest file under framework/_reference/tests/roles/: construct the real chain (interface -> data object -> task modules -> role); seed a known scenario (set order 1 PENDING); run the role's batch validation; assert the typed outcome reflects reality (counts, transitions); negative sub-case (impossible expectation surfaces as a failed validation result, not an exception swallow); reseed via init_sqlserver.py at session finish.

## Acceptance
All live asserts PASS, exit 0, DB reseeded. Red: fix then /kernel/learn.
