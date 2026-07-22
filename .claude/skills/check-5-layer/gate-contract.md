# Gate Contract — check-5-layer

## Per-Step Gates

### Step 1: Resolve Target

| Check | Type | Failure Action |
|-------|------|---------------|
| `target-path` exists | hard | Stop with error |
| `framework/` directory found | hard | Stop with error |
| Interface file found in `framework/interfaces/` | hard | Stop with error |
| SDK import detected in Interface | hard | Stop — cannot determine platform type |
| Platform type resolved | hard | Stop — unknown SDK |

### Step 2: Classify Files

| Check | Type | Failure Action |
|-------|------|---------------|
| At least 1 `.py` file found | hard | Stop — empty framework |
| Every file assigned a layer or flagged | soft | INFO finding for unclassifiable files |
| Layer 2 directory detected | soft | WARN — no Layer 2 dir found, check manually |

### Step 3: Check Compliance

| Check | Type | Failure Action |
|-------|------|---------------|
| Contract file loaded | hard | Stop — cannot check without contract |
| AST parse succeeds for each file | soft | WARN — syntax error, skip file |
| At least 1 check ran per file | soft | INFO — file had no applicable rules |

### Step 4: Report

| Check | Type | Failure Action |
|-------|------|---------------|
| Report contains scorecard | hard | Regenerate — scorecard is mandatory |
| All findings have file:line reference | hard | Regenerate — vague findings not allowed |
| All findings reference a contract rule | hard | Regenerate — unlinked findings not allowed |

### Step 5: Fix

| Check | Type | Failure Action |
|-------|------|---------------|
| User approval received before edit | hard | Never apply without approval |
| Edit targets correct file:line | soft | Verify location before applying |
| Fix addresses the finding | soft | Review fix matches proposed solution |

## Severity Classification

| Level | Meaning | Fix Mode |
|-------|---------|----------|
| FAIL | Mechanically verifiable contract violation | Enters fix queue |
| WARN | Likely non-compliant, needs judgment | Report only (user can request fix) |
| INFO | Compliant but worth noting | Report only |
