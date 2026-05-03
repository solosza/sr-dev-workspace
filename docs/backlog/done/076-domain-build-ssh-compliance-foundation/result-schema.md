# Enhanced Result Schema

## Status
NEW

## Location
`framework/_reference/validators/` — affects all validator output

## What It Does
Defines the compliance-ready result format that all framework validators produce.

## Current Format
```json
{"check": "config_sshd_config", "passed": true, "evidence": "pattern in file"}
```

## Required Format
```json
{
  "rule_id": "STIG-001",
  "framework": "DISA STIG",
  "severity": "high",
  "check": "PermitRootLogin must be no",
  "passed": false,
  "expected": "no",
  "actual": "yes",
  "evidence": "PermitRootLogin yes",
  "remediation": "Set PermitRootLogin no in /etc/ssh/sshd_config"
}
```

## Fields Added
| Field | Type | Purpose |
|-------|------|---------|
| `rule_id` | string | Framework-specific rule identifier |
| `framework` | string | Which compliance framework |
| `severity` | string | `critical`, `high`, `medium`, `low` |
| `expected` | string | What the check expects |
| `actual` | string | What was found |
| `remediation` | string | How to fix a failure |

## Backward Compatibility
Existing 4 validators (Package, Kernel, Service, Config) should continue working with the old format. The new fields are additions, not replacements. The base `ComplianceValidator` class produces the enhanced format; generic validators keep the simple format.

## Dependencies
None — this is the first thing to build.
