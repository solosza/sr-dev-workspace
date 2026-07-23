# Task 002: Fixture-Portability Linter
**Type:** BUILD | **Gates:** GI-02
## Action
Add a helper that lints live test tasks/fixtures for portability violations (relative DATABASE_URL, missing explicit PYTHONPATH).
## Spec
Scan a test task/fixture file for: (1) a relative or hardcoded-cwd-dependent DATABASE_URL (must be absolute or env-driven — lesson #47, the 222 relative-URL class); (2) missing an explicit PYTHONPATH declaration where the test imports package roots. Flag violations with the file + line. Encode 223's already-portable pattern (absolute DATABASE_URL, explicit PYTHONPATH, configurable host/port) as the PASS standard. Read-only linter — reports, does not modify.
## Acceptance
Linter flags relative/cwd-dependent DATABASE_URL + missing PYTHONPATH; a 223-style portable fixture passes clean.
