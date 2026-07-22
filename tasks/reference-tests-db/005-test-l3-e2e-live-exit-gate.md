# Task 005: L3 - E2E Live (V3 EXIT GATE)

**Type:** TEST (L3) - GATE TASK: skip never waives (lesson #39). THIS IS THE V3 VERTICAL EXIT GATE.
**Gates:** DE-05

## Target
Native SQL Server, database orderly, full chain. Unreachable => L3-BLOCKED and STOP.

## Action
Run the full exemplar suite live via pytest against orderly. Assert: 100% pass (this suite itself, not a platform-wide claim), same-instance recount pattern proven (pre/post query via one fixture), typed outcomes correct. Reseed via init_sqlserver.py at session end. Report explicitly: "V3 DB SLICE EXIT GATE: PASS" or the specific failure.

## Acceptance
Suite green live, DB reseeded, exit gate explicitly confirmed in output. Red: fix then /kernel/learn.
