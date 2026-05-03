# L1: Verify Site Structure

## Context
Level 1 structural test. Verify all required HTML elements and CSS classes exist without opening a browser.

## Type
TEST

## Execution
agent

## Dependencies
- 020-test-phase-boundary

## Phase Gate
- [ ] Phase boundary test passed

## Requirements
- Run grep checks against `D:\my_ai_projects\isagawa-portfolio-site\index.html`:
  - `grep -q "conversational agent factory"` — hero copy
  - `grep -q 'id="seed"'` — seed section
  - `grep -q 'id="growth"'` — growth section
  - `grep -q 'id="self-extension"'` — self-extension section
  - `grep -q 'id="this-page"'` — this page section
  - `grep -q 'id="provenance"'` — provenance section
  - `grep -q 'attestation-bundle-1'` — first bundle embedded
  - `grep -q 'attestation-bundle-2'` — second bundle embedded
  - `grep -qi 'rekor'` — Rekor verification JS
  - `grep -q '<footer'` — footer element
  - `grep -q 'menu-toggle'` — mobile nav JS
- Run grep checks against `D:\my_ai_projects\isagawa-portfolio-site\styles.css`:
  - `grep -q 'scroll-behavior'` — smooth scroll
  - `grep -q '@media'` — responsive rules

## Acceptance Criteria
- [ ] All 13 grep checks exit 0
- [ ] No grep check returns non-zero

## Gates Satisfied
- BUILD-01 through BUILD-17 (structural verification)

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
