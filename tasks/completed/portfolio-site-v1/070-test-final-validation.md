# Test Final Validation

## Context
Final validation task that checks all gate contract items. Runs structural checks on HTML section IDs and CSS variables, then produces a pass/fail summary for every gate.

## Type
TEST

## Execution
inline

## Dependencies
- 069-test-anchor-links

## Requirements
- Verify all BUILD gates (BUILD-01 through BUILD-20) from gate-contract.md
- Verify all FUNC gates (FUNC-01 through FUNC-02) from gate-contract.md
- Verify all TEST gates (TEST-01 through TEST-03) were satisfied by prior tasks
- Run structural checks: all 9 sections have correct IDs in index.html
- Run structural checks: CSS has all required variables (--bg-primary, --font-heading, --space-section)
- Run structural checks: CSS has @media queries
- Produce summary table with pass/fail for each gate ID

## Acceptance Criteria
- [ ] All BUILD gates checked and results recorded
- [ ] All FUNC gates checked and results recorded
- [ ] All TEST gates confirmed from prior task results
- [ ] Summary table produced showing gate ID, status (pass/fail), and notes
- [ ] Zero critical failures (BUILD-01 through BUILD-14 all pass)
- [ ] HTML parses without error (FUNC-01)
- [ ] CSS reads without error (FUNC-02)

## Gates Satisfied
FUNC-01, FUNC-02

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
