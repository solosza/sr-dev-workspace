# Task 004: L2 - Fixture Portability + Semantics
**Type:** TEST (L2) | **Gates:** SE-04
## Action
ONE script: fixture scope check; no hardcoded creds; PYTHONPATH=framework + DATABASE_URL + service URL documented/configurable (grep the test); confirm the suite can be invoked from a different cwd without a relative-path DB error (the 222 nit).
## Acceptance
Portable fixtures verified, exit 0. Red: fix then /kernel/learn.
