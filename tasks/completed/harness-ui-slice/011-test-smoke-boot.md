# Test: Smoke — App Boots and Pages Render

## Context
Backlog 202: L2/L3 — the app actually starts and serves. This app becomes V1's E2E target; a dead harness blocks the whole vertical.

## Type
TEST
## Execution
inline
## Dependencies
- 003, 005, 007, 009, 010
## Phase Gate
- [ ] All app files + seed exist on the branch

## Requirements
- Install deps if needed (fastapi, uvicorn, jinja2, sqlalchemy, python-multipart, itsdangerous — pip install, note versions in output)
- Run seed; start `uvicorn harness.orderly.main:app --port 8017` as a background process; poll GET /login until 200 (≤15s); perform demo login (clerk); GET /customers and /orders expecting 200 + page markers; then TERMINATE the server process cleanly
- Non-zero exit = failure → fix → /kernel/learn

## Acceptance Criteria
- [ ] Script exits 0; server not left running

## Gates Satisfied
- HUI-02, HUI-03

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
