# Refactor Playwright Platform to 5-Layer Compliance

## Status
Open

## Priority
Low — architecture is structurally sound, only JSDoc/docstring gaps

## Summary
The `/check-5-layer` audit on platform-playwright found 12 FAIL files, all due to missing JSDoc docstrings on methods and classes (Global Rules #2 and #3). The architecture is correct — composition patterns, import boundaries, return conventions, and decorator usage are all compliant. Fixing JSDoc alone brings the platform to near-full compliance. Two structural limitations exist (can't decorate Playwright test callbacks with @autologger) that are acceptable exceptions.

## Audit Results (2026-07-09)

| Layer | Files | Status | Key Issues |
|-------|-------|--------|------------|
| L1 Interface | 2 | FAIL | Missing JSDoc on methods |
| L2 Component | 4 | FAIL | Missing JSDoc on methods and classes |
| L3 Task | 2 | FAIL | Missing JSDoc on methods |
| L4 Role | 2 | FAIL | Missing JSDoc on methods |
| L5 Test | 2 | FAIL | Missing JSDoc on methods |

All 12 FAILs are the same root cause: JSDoc docstring gaps.

## Requirements

### Critical (FAIL findings)
- Add JSDoc docstrings to every class across all 12 framework files
- Add JSDoc docstrings to every method across all 12 framework files
- Follow the contract format: class docstrings list structural rules as bullets, method docstrings describe purpose + params + return

### Acceptable Exceptions
- Playwright test callbacks cannot be decorated with `@autologger` — this is a framework limitation, not a compliance gap
- Document this exception in test file docstrings

## References
- 5-layer contract: `.claude/docs/design/check-5-layer/references/5-layer-contract.md`
- Audit report: generated 2026-07-09 via `/check-5-layer`
- Platform repo: `D:\my_ai_projects\project_test_repos\platform-playwright`
- Related: backlog 192 (SSH), backlog 193 (Docker) — same audit cycle

## Task Builder Input
- **Deliverable:** All 12 framework files with JSDoc docstrings passing `/check-5-layer` with 0 FAIL
- **Location:** `new-repo:D:\my_ai_projects\project_test_repos\platform-playwright`
- **Scope:** REFACTOR
- **Constraints:** Do not change any logic, imports, or structure — docstrings only. Run `/check-5-layer` after to verify compliance.
