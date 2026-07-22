# Workflow

## Phases

### Phase 1: Analysis (Read-Only)
- Steps: 1, 2, 3, 4
- Gate: All files loaded, corpus type detected, checks complete, report presented
- Rule: No file modifications allowed in this phase

### Phase 2: Fix (Write)
- Steps: 5
- Gate: User has seen the report and explicitly entered fix mode
- Rule: Each fix requires user approval (unless `approve all`)

## State Persistence

**None.** `/gap` is stateless. Each run is a fresh scan. No state file is written or read.

Rationale: Gap analysis is idempotent. Running it twice with no changes produces the same report. There is no multi-session workflow to resume.

## HITL Stops

| After Step | Why | User Options |
|-----------|-----|-------------|
| 4 (Report) | User reviews findings before any modifications | `fix` (enter fix mode), `fix all` (batch), or done |
| 5 (per-finding) | Each fix requires approval | `approve`, `modify`, `skip`, `approve all`, `stop` |

## Outer/Inner Loop Support

**Outer loop (standalone):**
```
user -> /gap [target]
  -> reads files, detects type
  -> applies checks
  -> reports gaps
  -> optional fix mode
```

**Inner loop (called by other commands):**
```
/build-command Step 8 -> /gap [skill folder]
/create-test-artifacts Step 7 -> /gap [onboard-run folder]
/verify-sit-xlsx -> /gap [sit artifacts]
```

When called as inner loop, fix mode is typically skipped — the caller handles remediation.
