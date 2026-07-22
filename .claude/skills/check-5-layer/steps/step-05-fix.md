# Step 5: Fix

## Purpose

Apply fixes with user approval. Only runs if user requests after seeing the report.

## Input

- Findings list from Step 3 (FAIL findings only, unless user requests WARN fixes)

## Trigger

**Only runs if user requests.** After Step 4 report, user must explicitly ask for fixes.

## Procedure

### 1. Present Each Finding

```
Finding 1/N: [FAIL] login_page.py:30
Rule: Layer 2, Structural Rule #2 — No decorators on any methods
Found: @automation_logger("POM") on method click_log_in
Proposed fix: Remove the decorator

[approve / modify / skip / approve all / stop]
```

### 2. Process User Response

| Response | Action |
|----------|--------|
| `approve` | Apply proposed fix via Edit tool |
| `modify` | User provides alternative fix, apply that |
| `skip` | Move to next finding |
| `approve all` | Apply all remaining fixes without asking |
| `stop` | Exit fix mode |

### 3. Apply Fix

- Use the Edit tool to modify the file at the exact line
- Verify the edit addresses the finding
- Move to next finding

### 4. Report Fixes Applied

```
FIXES APPLIED: 4/6
  Applied: findings 1, 2, 3, 5
  Skipped: findings 4, 6

Re-run /check-5-layer to verify fixes.
```

## Rules

1. **FAIL findings only by default.** WARN and INFO do not enter fix queue unless user explicitly requests.
2. **Never apply without approval.** Even "approve all" requires one explicit user action.
3. **One finding at a time.** Present sequentially unless user says "approve all".
4. **Suggest re-run after fixes.** Always end with "Re-run /check-5-layer to verify fixes."
