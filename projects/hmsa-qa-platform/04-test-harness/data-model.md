# Harness Data Model — Design Doc

## Constraint (user-set, 2026-07-14)

The demo product is **generic commerce — NOT HMSA, NOT healthcare**. No claims, members, providers, or client vocabulary anywhere in the harness or in built `_reference/` exemplars. Healthcare appears only in workspace design-doc dry-run narratives (grounding), never in shipped code.

## Decision

An **orders domain** — deliberately matching the vocabulary the Phase 2 canonical examples already use (`OrdersDataObject`, `OrderRow`, `find_eligible_order`, status pipelines). The built exemplars and the harness share one vocabulary with zero adaptation.

## Entities (minimal on purpose — a target, not a product)

| Entity | Fields | Notes |
|--------|--------|-------|
| Customer | id, name, email | |
| Order | id, customer_id, status, total, created_at | status: PENDING → PROCESSING → COMPLETE; CANCELLED terminal |
| OrderItem | id, order_id, product_name, qty, price | order.total derives from items |

## Why this shape works as a test target

- **Discovery patterns:** "find eligible order" (status + total filters) — exercises broad-query→filter→pick→validate exactly like the DiscoveryTasks exemplar
- **Pipeline patterns:** status transitions give run→verify shapes (V3 adds a `process_pending_orders` stored procedure to exercise SP-as-subject testing)
- **Hybrid flows (V5):** DB seed → UI edit → API process → DB verify, all on one data model
- **Multi-persona:** clerk creates, manager approves/cancels — two identities, one workflow (roles-ui multi-user pattern)

## Storage per vertical

V1: SQLite (fastest to a clickable target) → V3: SQL Server in Docker, same schema (the swap itself dry-tests schema portability). App accesses storage via SQLAlchemy Core so the swap is config, not rewrite. Tests hit SQL Server directly — the app's ORM is an app detail, invisible to the framework.
