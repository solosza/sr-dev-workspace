# Task 007: L3 - Live zeep Smoke (GATE)
**Type:** TEST (L3) - GATE TASK: skip never waives (lesson #39).
**Gates:** SO-07
## Target
Seeded orderly DB (SQLite is fine for the harness smoke, or native SQL Server if wired) + booted SOAP service. Only orderly.
## Action
ONE script: ensure orderly seeded; boot the SOAP service (background); zeep.Client -> call GetCustomer(1) and GetOrderStatus(1); assert the returned values equal a direct DB query for customer 1 and order 1; teardown the service.
## Acceptance
Live SOAP calls return DB-matching values, exit 0. Red: fix then /kernel/learn.
