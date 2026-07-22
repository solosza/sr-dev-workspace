# Write App Entry + Login Wiring (main.py)

## Context
Backlog 202: FastAPI app with Jinja2 templates, session-cookie demo login (clerk/manager from seed), route registration. Login is the identity seam the credentials fixture binds to later.

## Type
BUILD
## Execution
inline
## Dependencies
- 002
## Phase Gate
- [ ] db.py exists on the branch

## Requirements
- Write `harness/orderly/main.py`: FastAPI app, Jinja2Templates, session middleware (demo-grade), GET/POST /login (validates against seeded users), logout, auth guard redirecting to /login, includes customer + order routers (tasks 006/008)
- Runnable: `uvicorn harness.orderly.main:app --port 8017` documented in module docstring

## Acceptance Criteria
- [ ] File exists; app importable; login/logout routes defined; port 8017 documented

## Gates Satisfied
- (feeds HUI-02/03)

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
