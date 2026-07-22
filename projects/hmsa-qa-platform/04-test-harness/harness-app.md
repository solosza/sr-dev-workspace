# Harness App ("Orderly" demo) — Design Doc

## Constraint (user-set, 2026-07-14)

Generic commerce demo — **no HMSA, no healthcare** vocabulary anywhere. Neutral name: **Orderly**.

## Decision

One app, grown vertically — each vertical adds the door its interface needs. Demo-grade on purpose: the harness is a test target, not a product.

**Stack:** FastAPI + Jinja2 templates (plain HTML, no JS framework) + SQLAlchemy Core over SQLite (V1) / SQL Server (V3+). Run: `uvicorn`, single process; Docker-composed at V5 (Phase 4.3, designed then — catalogs on demand).

## Slices per vertical

| Vertical | Slice | Adds |
|----------|-------|------|
| V1 | harness-ui | CRUD screens: customer list/create, order list/create/edit, order detail with status change. Login page (two users: clerk, manager) |
| V2 | harness-api | REST endpoints over the same services: /api/customers, /api/orders (CRUD + /process) |
| V3 | harness-db | SQL Server (Docker) replaces SQLite, same schema + `process_pending_orders` stored procedure (SP-as-subject target) |
| V4 | harness-soap | SOAP facade (spyne or equivalent): GetCustomer, GetOrderStatus operations over the same services |
| V5 | harness-compose | docker-compose wiring app + DB (Phase 4.3 design doc written at V5 start) |

## Testability conventions (contract-aligned)

- **`data-testid` on every interactive element** — platform-selenium's locator convention; page-object locators bind to these, never to CSS classes
- Grid-shaped order list (table with headers/rows) — the GridComponent flagship gets a real target
- One modal (delete confirmation) — the ModalComponent lead exemplar gets a real target
- Login as identity seam — credentials fixture's clerk/manager users are Orderly users
- Seed script: deterministic demo data (fixed IDs) so scenario JSON in `data/` is stable

## What the harness is NOT

- Not production code — no auth beyond demo login, no validation rigor, no styling investment
- Not covered by the 5-layer contract (it's the system under test, not the framework)
- Not a client deliverable — lives in the target repo under `harness/`, excluded from platform packaging
