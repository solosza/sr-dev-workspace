# Test: data-testid Coverage Audit

## Context
Backlog 202: the locator convention is load-bearing — V1 page objects bind ONLY to data-testid. One missed element = one invented selector later.

## Type
TEST
## Execution
inline
## Dependencies
- 005, 007, 009, 010
## Phase Gate
- [ ] All templates exist on the branch

## Requirements
- Run a python audit over `harness/orderly/templates/*.html`: parse each `<a>`, `<button>`, `<input>`, `<select>`, `<form>` tag; every one must carry data-testid; print any misses with file+line; exit non-zero on any miss
- Also run the healthcare-vocabulary grep (HUI-06): `grep -riE "hmsa|claim|member|patient|provider|healthcare"` over harness/ must return zero matches

## Acceptance Criteria
- [ ] Audit exits 0 (full coverage); vocabulary grep clean

## Gates Satisfied
- HUI-04, HUI-06

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
