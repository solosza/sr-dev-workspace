# Commit the Contract Fix

## Context
Fix verified — commit on the SAME 203 branch so the branch history shows build → orchestrator catch → fix.

## Type
BUILD
## Execution
inline
## Dependencies
- 003
## Phase Gate
- [ ] FIX-03 passing (both tiers green incl. propagation assertion)

## Requirements
- `git -C <target> add -A`; commit: `fix(203): contract compliance — re-raise on all SDK failures, screenshot machinery removed (orchestrator-found)`
- Stay on build/203-qa-build-browser-interface; main untouched

## Acceptance Criteria
- [ ] Commit on the branch; porcelain empty; main unchanged

## Gates Satisfied
- FIX-04

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
