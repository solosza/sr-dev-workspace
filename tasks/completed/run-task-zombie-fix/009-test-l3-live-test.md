# 009 — L3 Live Test with Simple Task Folder

## Type
TEST

## Description
Run `run-task.sh` against a minimal test task folder and verify no zombie processes, proper log capture, and clean exit.

## Requirements
- Create a minimal test task folder `tasks/zombie-test/` with:
  - `000-index.md` (simple index)
  - `001-build-write-hello.md` (write a hello.txt file)
  - `gate-contract.md` (single structural gate)
- Run: `env -u CLAUDECODE bash run-task.sh "$(pwd)" 3 zombie-test`
- After completion, verify:
  - `iteration_1.log` (or `zombie-test_iteration_1.log`) contains valid JSON
  - `hello.txt` exists (task was executed)
  - No orphaned `claude` processes remain (check `tasklist | grep claude` on Windows)
  - Exit code is 0
- Clean up: remove `tasks/zombie-test/` and `hello.txt`

## Acceptance Criteria
- [ ] Log file contains valid JSON output
- [ ] Task deliverable was produced
- [ ] No orphaned processes after exit

## Gates
FUNC-03
