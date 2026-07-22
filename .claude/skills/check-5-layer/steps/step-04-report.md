# Step 4: Report

## Purpose

Present findings in a scannable per-layer compliance report with scorecard.

## Input

- Findings list from Step 3 (severity, location, rule, description, fix)
- Platform type from Step 1
- File count from Step 2

## Output Format

```
COMPLIANCE REPORT: [target-path]
Platform type: [detected type]
Contract: 5-layer-contract.md v1.0
Files checked: N
Scope: [full | layer N | single file]

LAYER 1 — Interface (N files)
  FAIL  browser_interface.py:45 — [Global #3] Missing docstring on method `click`
        Fix: Add docstring describing click behavior
  WARN  browser_interface.py:12 — [Layer 1 #3] Config default not constructor-driven
        Fix: Move timeout default to constructor parameter

LAYER 2 — Component (N files)
  FAIL  login_page.py:30 — [Layer 2 #2] Decorator found on atomic method
        Fix: Remove @automation_logger — Layer 2 methods have no decorators
  INFO  employees_page.py — All 7 structural rules pass

...

SCORECARD
─────────────────────────────────────────
Layer 1 (Interface):   2 files —  2 PASS, 0 FAIL
Layer 2 (Component):  12 files — 10 PASS, 1 FAIL, 1 WARN
Layer 3 (Task):        7 files —  7 PASS
Layer 4 (Role):        3 files —  2 PASS, 1 FAIL
Layer 5 (Test):       10 files —  8 PASS, 1 FAIL, 1 INFO
─────────────────────────────────────────
Total: 34 files — 29 PASS, 3 FAIL, 1 WARN, 1 INFO
```

## Rules

1. **Group by layer** — Layer 1 first, Layer 5 last
2. **Sort by severity within layer** — FAIL first, then WARN, then INFO
3. **Files with all rules passing** — show as single INFO line: "All N rules pass"
4. **Scorecard always present** — even if checking one file, show the scorecard
5. **If fully compliant:**

```
COMPLIANCE REPORT: [target-path]
Platform type: [type]
Contract: 5-layer-contract.md v1.0
Files checked: N

All files compliant. Clean.
```

## Scoring Logic

- A file with any FAIL finding = FAIL in scorecard
- A file with WARN but no FAIL = WARN in scorecard
- A file with only INFO or no findings = PASS in scorecard
