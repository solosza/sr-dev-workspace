# Task 004: Write OrdersDataObject

**Type:** BUILD | **Gates:** DO-04

## Action
Write D:/my_ai_projects/project_test_repos/hmsa-qa-platform/framework/_reference/data_objects/orders_data_object.py (ONE file; follow data-objects.md naming).

## Spec
READ data-objects.md + tasks-db.md (ratified refinement) FIRST. Requirements:
- Constructor receives a SqlServerInterface instance (dependency injection - constructs nothing internally per contract)
- Methods load sql/ files, execute via the interface, return typed row models
- Variant-to-identifier maps as CLASS CONSTANTS (variant name -> SP name / table name) per the ratified refinement - includes process_pending_orders
- catch-log-reraise; no direct driver imports; single-root imports (from _reference....)

## Acceptance
py_compile; AST shows delegation-only + constant maps; no driver imports.
