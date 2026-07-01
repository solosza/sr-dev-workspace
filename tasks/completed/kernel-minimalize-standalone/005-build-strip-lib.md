# Strip Non-Core Lib Files

## Type
BUILD

## Phase Gate
Task 001 must be complete.

## Deliverable
Only core lib files remain.

## Instructions
Working in `D:\my_ai_projects\project_test_repos\kernel-minimal`:

**Keep in `lib/`:**
- `common.sh` (shared bash helpers for run-task.sh)
- `__init__.py` (if needed)

**Remove from `lib/`:**
- `attestation/` (entire directory)
- `validators/` (entire directory)
- `skill_extraction.py`
- Any `__pycache__/` directories

## Verification
- `lib/attestation/` does not exist
- `lib/validators/` does not exist
