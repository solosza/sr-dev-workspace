# Task 004: L2 - Contract Semantics

**Type:** TEST (L2) | **Gates:** DT-04

## Action
ONE script (AST body-scoped, docstring-excluded): except-blocks-reraise classification; zero literal SP/table names in the tasks file (grep 'process_pending_orders|FROM orders|UPDATE orders' etc = 0 outside comments); imports audit (no mssql_python/interface imports - Data Object only); run/verify separation (no verify logic inside run methods - assert distinct method sets).

## Acceptance
All compliant, exit 0. Red: fix then /kernel/learn.
