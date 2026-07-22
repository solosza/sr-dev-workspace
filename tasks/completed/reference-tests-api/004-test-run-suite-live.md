# Test: Run the Suite Live — THE V2 EXIT SIGNAL

## Type
TEST
## Execution
inline
## Dependencies
- 003

## Requirements
- Fresh seed + boot Orderly on PORT 8018 (cwd = target repo)
- `python -m pytest framework/_reference/tests/ --rootdir=D:/my_ai_projects/project_test_repos/hmsa-qa-platform -v` (cross-repo pytest lesson) — capture full output
- ALL tests green; zero skips; assert the cleanup left no test orders behind (GET list shows only the 8 seeded)
- Cleanup server in finally; env problem → L3-BLOCKED honestly; any red → fix → /kernel/learn (never weaken an assertion to pass)

## Acceptance Criteria
- [x] pytest exit 0, output captured, no residue orders

## Orchestrator Validation (2026-07-20)
Pipeline SKIPPED this gate (0-byte iteration log — suite never executed). Orchestrator ran it per lesson #39 (skipped GATE never waived): fresh seed, Orderly on 8018, `pytest framework/_reference/tests/ --rootdir=<repo> -v` with PYTHONPATH = `framework` + `framework/_reference` (dual import roots — lesson #46). Result: **exit 0, 1 passed, 0 skipped**; dual assertions + asserted cleanup executed live; residue check clean (exactly the 8 seeded orders remain). AST + extended-lexicon checks: NONE flagged. AT-04 SATISFIED. Merge still HELD for 208 per compensating condition.

## Gates Satisfied
- AT-04

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
