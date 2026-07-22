# Orderly Harness — UI Slice [V1 first]

## Status
Open

## Priority
High — every V1 L2 identifier binds to this DOM

## Summary
Build the Orderly demo app UI slice per the harness design docs: FastAPI + Jinja2 + SQLite, CRUD screens for customers/orders, order detail with status change, demo login (clerk/manager), data-testid on every interactive element, deterministic seed script. GENERIC COMMERCE — no healthcare.

## Requirements
- Implement per 04-test-harness/harness-app.md V1 slice + data-model.md entities
- data-testid convention on all interactive elements; order list as a real table (grid target); one delete-confirmation modal (modal target)
- Seed script with fixed IDs; runnable via uvicorn with documented port
- Lives under harness/ in target repo — excluded from platform packaging

## References
- projects/hmsa-qa-platform/04-test-harness/harness-app.md
- projects/hmsa-qa-platform/04-test-harness/data-model.md

## Task Builder Input
- **Deliverable:** harness/ app in target repo: runnable Orderly UI on SQLite with seed data, smoke-tested (starts + pages render)
- **Location:** new-repo:D:\my_ai_projects\project_test_repos\hmsa-qa-platform
- **Scope:** BUILD
- **Constraints:** V1 Browser — blocked until ALL V-BASE items (199-201) accepted via /kernel/review-queue. STRICT vertical order within the slice — each item waits on the previous item's acceptance. Write ONLY on target-repo feature branch build/202-qa-build-harness-ui-slice; merge via /kernel/review-queue accept, never direct to main. Clean-room: v2 legacy is anti-pattern/architecture reference only. DEMO DOMAIN IS GENERIC COMMERCE (Orderly orders app) — NO HMSA/healthcare vocabulary in any shipped code. Plan L1/L2/L3 test tasks during atomization.
