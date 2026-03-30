# Production test: full coverage pipeline end-to-end

## Context
L3: run scan, report, generate, check in sequence. Verify real outputs.

## Type
TEST

## Execution
agent

## Dependencies
- 006, 011, 012

## Phase Gate
- [ ] CLI exists (006), scan verified (011), generate verified (012)

## Requirements
- Run full pipeline via CLI in C:/Users/solos/my_ai_projects/py-selenium-framework-mcp/:
- `python -m framework.coverage.cli scan` — verify output
- `python -m framework.coverage.cli report` — verify markdown report
- `python -m framework.coverage.cli check --threshold 50` — verify exits 0 (7/12 > 50%)
- `python -m framework.coverage.cli check --threshold 90` — verify exits 1 (7/12 < 90%)

## Acceptance Criteria
- [ ] All 4 CLI commands produce expected results (verify: agent report)

## Gates Satisfied
PROD-01

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
