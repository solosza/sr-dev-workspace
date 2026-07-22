# Task 002: Write Pydantic Row Models

**Type:** BUILD | **Gates:** DO-02

## Action
Write D:/my_ai_projects/project_test_repos/hmsa-qa-platform/framework/_reference/data_objects/row_models.py (ONE file; exact filename per data-objects.md - READ it first and follow ITS naming if different).

## Spec
READ FIRST (RULE ZERO): D:/my_ai_projects/project_test_repos/sr_dev_workspace/projects/hmsa-qa-platform/02-reference-patterns/data-objects.md AND the real schema (D:/my_ai_projects/project_test_repos/hmsa-qa-platform/harness/orderly/db_sqlserver_schema.sql + db.py). Pydantic models: CustomerRow, OrderRow, OrderItemRow - fields exactly mirror columns/types (INT->int, NVARCHAR->str, DECIMAL->Decimal, DATETIME2->datetime). Generic commerce vocab only.

## Acceptance
py_compile; model fields == schema columns; no invented fields.
