# Batch Executor Framework-Aware Reporting

## Status
EXISTS — needs enhancement

## Location
`framework/_reference/roles/ssh_batch_executor.py`

## Current Behavior
Takes a list of validators, runs them all, aggregates flat results.

## Enhanced Behavior
- Read `frameworks` from host config
- Auto-select compliance validators based on framework list
- Group results by framework in the summary
- Produce per-framework pass rates

## Enhanced Summary Format
```json
{
  "total": 45,
  "passed": 42,
  "failed": 3,
  "by_framework": {
    "DISA STIG": {"total": 15, "passed": 14, "failed": 1},
    "CIS L1": {"total": 12, "passed": 12, "failed": 0},
    "FIPS 140-3": {"total": 8, "passed": 7, "failed": 1}
  },
  "details": [...]
}
```

## Dependencies
- Host config update (reads `frameworks` field)
- Base ComplianceValidator (validators to select from)
