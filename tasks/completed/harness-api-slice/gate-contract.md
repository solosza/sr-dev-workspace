# Gate Contract — 209 Orderly API Slice

Deliverable: REST slice in target repo `harness/orderly/` on branch build/209-qa-build-harness-api-slice.

| Gate | Check | Method |
|------|-------|--------|
| API-01 | Feature branch from main; main untouched | run_code |
| API-02 | /api/customers: GET list, GET /{id}, POST create — JSON over the SAME tables/services the UI uses (no parallel data layer) | run_test |
| API-03 | /api/orders: GET list (+status filter), GET /{id} (incl. items), POST create, POST /{id}/status, DELETE /{id}, POST /{id}/process | run_test |
| API-04 | /process semantics per data-model.md: PENDING→PROCESSING→COMPLETE transition rules enforced; invalid transition → 4xx JSON error (never 500) | run_test |
| API-05 | JSON shapes STABLE + documented (field names/types listed in a docstring or api README section) — V2 framework's pydantic models will bind to these | run_test + grep |
| API-06 | L3 live: fresh seed → requests session drives create-customer → create-order → process → status transitions asserted → delete → 404 on re-GET. UI slice unaffected: / login page and /orders still render 200 | run_test |
| API-07 | No healthcare/HMSA vocabulary anywhere (generic commerce only); commit on branch, porcelain clean | grep + run_code |

## Rules

- Harness code is the SYSTEM UNDER TEST — 5-layer contract does NOT apply here (no @trace, plain FastAPI style matching existing routes_*.py files). Read the existing routes files FIRST and match their idiom (RULE ZERO)
- Same services/tables as UI — API handlers may share helpers with UI routes; extract shared logic only if trivially clean, never fork the data access
- Auth: same demo session model as UI is NOT required for API (per harness-app.md "no auth beyond demo login" — API endpoints may be open; document the choice)
- Deterministic seed data unchanged — scenario JSON stability depends on fixed IDs
