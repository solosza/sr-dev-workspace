# retry.py Utility — Task Index

## Goal
Ship retry.py per the 2.5.3 design doc into the target repo on feature branch build/200-qa-build-retry-utility.

## Tasks

| # | Task | Type | Dependencies | Status |
|---|------|------|-------------|--------|
| 001 | [[001-build-create-feature-branch]] | BUILD | none | pending |
| 002 | [[002-build-write-retry-py]] | BUILD | 001 | pending |
| 003 | [[003-test-transient-retry-succeeds]] | TEST | 002 | pending |
| 004 | [[004-test-exhaustion-reraises]] | TEST | 002 | pending |
| 005 | [[005-build-commit-branch]] | BUILD | 002, 003, 004 | pending |

## Gate Contract
→ [[gate-contract.md]]

## Deliverables
- `framework/resources/utilities/retry.py` on branch build/200-qa-build-retry-utility, tested, committed
