# Test: Copy Is Byte-Identical

## Context
Backlog 201 (V-BASE): a contract copy that drifted during copying is worse than no copy.

## Type
TEST

## Execution
inline

## Dependencies
- 002

## Phase Gate
- [ ] Target contract file exists (CON-02)

## Requirements
- Run python: sha256 of workspace source == sha256 of target copy; exit non-zero on mismatch
- Non-zero exit = failure → re-copy → /kernel/learn

## Acceptance Criteria
- [ ] Hashes match (CON-03)

## Gates Satisfied
- CON-03

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
