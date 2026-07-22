# Task 003: Write SQL Server Schema

**Type:** BUILD | **Gates:** DB-03

## Action
Write `D:/my_ai_projects/project_test_repos/hmsa-qa-platform/harness/orderly/db_sqlserver_schema.sql` (ONE file).

## Spec
READ `D:/my_ai_projects/project_test_repos/hmsa-qa-platform/harness/orderly/db.py` first (RULE ZERO) — mirror the exact SQLite schema in T-SQL:
- `customers` (id INT IDENTITY PK, name NVARCHAR, email NVARCHAR)
- `orders` (id INT IDENTITY PK, customer_id FK->customers, status NVARCHAR(20), total DECIMAL(10,2), created_at DATETIME2)
- `order_items` (id INT IDENTITY PK, order_id FK->orders, product_name NVARCHAR, qty INT, price DECIMAL(10,2))
- Idempotent: guard each CREATE with IF NOT EXISTS (OBJECT_ID check)
- Generic commerce vocab only.

## Acceptance
Greps per DB-03; script re-runnable.
