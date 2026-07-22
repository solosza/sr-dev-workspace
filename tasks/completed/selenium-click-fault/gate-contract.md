# Gate Contract — 235 Selenium Click-Fault Research

| Gate | Check | Method |
|------|-------|--------|
| SCF-01 | Machine timeline established with evidence: last boot time vs fault onset (2026-07-14 ~18:00); Windows update history around onset; display/driver changes | grep report for "## Timeline" with actual command outputs |
| SCF-02 | Input-pipeline diff: chromedriver verbose log captured on a FAILING click; the CDP command chromedriver issues vs what Playwright issues for the same click; concrete difference identified or explicitly "no protocol-level difference — fault is below CDP" | grep report for "## Pipeline Diff" |
| SCF-03 | tools/selenium-click-probe.py exists: standalone, exits 0/1, prints DELIVERED/DEAD + timing, runnable in <60s, no framework deps | run_code |
| SCF-04 | Root cause (or best-evidence candidate with confidence level) + concrete FIX in the report; if fix needs user/system action, stated as finding with evidence — NOT applied | grep report for "## Root Cause" + "## Fix" |
| SCF-05 | No system-state changes made (registry, services, drivers untouched); evidence gathered read-only | report attestation section |

## Rules
- BUILD ON the existing evidence in the backlog (do not re-derive the 16-trial matrix)
- Diagnostic-only: report fixes, never apply system-level changes
- Do not kill user processes; own test processes only by PID
