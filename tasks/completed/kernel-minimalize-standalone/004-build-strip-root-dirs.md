# Strip Non-Core Root Directories

## Type
BUILD

## Phase Gate
Task 001 must be complete.

## Deliverable
Non-core root directories removed from the kernel repo.

## Instructions
Working in `D:\my_ai_projects\project_test_repos\kernel-minimal`:

**Remove these directories:**
- `delegation/` (cross-repo delegation engine)
- `scanner/` (bookmark scanner)
- `backlog/` (backlog items)
- `tests/` (extension tests)
- `docs/` (extension docs)

**Keep these:**
- `.claude/` (commands, hooks, skills, lessons, settings)
- `lib/` (will be stripped in next task)
- `CLAUDE.md`, `README.md`, `LICENSE`, `CONTRIBUTING.md`
- `run-task.sh`
- `kernel-manifest.json`, `kernel-sync.sh`
- `.gitignore`

## Verification
- `delegation/` does not exist
- `scanner/` does not exist
