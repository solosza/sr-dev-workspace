# Research: Machine Selenium/Chromedriver Click-Delivery Fault

## Status
Open

## Priority
High — blocks 208 (V1 E2E exit gate) and every selenium suite on this machine; the QA platform's product IS selenium tests

## Summary
Since 2026-07-14 ~6PM, native clicks issued through chromedriver are dropped after the first page navigation of a session — intermittently (~1 delivered in 16 attempts on 2026-07-16). JS clicks and Playwright are always fine; the fault is isolated to the chromedriver-session input path. Find the root cause on THIS machine and a reliable fix.

## Evidence Already Gathered (do not re-derive — build on it)
- Reproduces with bare selenium on a bare page (framework-free); Chrome 150 installed + CfT 150/140 pinned; selenium 4.39 and 4.25; headless=new AND headed
- First-document clicks always deliver (even delayed 8s); post-navigation clicks drop ~15/16
- Click-to-check delays 0.5/2/5s don't help; 20s poll after click → never lands (dropped, not delayed)
- Raw CDP Input.dispatchMouseEvent THROUGH the chromedriver session also drops; Playwright (own browser + CDP client) never drops
- Zero DOM events at document level (capture-phase listener) on failed clicks
- GPU flags, occlusion-disable flags, backgrounding flags: no effect. No Chrome enterprise policies in registry
- ONE success today (headed, ~2s waits) — intermittent, not deterministic
- Full history: lessons #41/#42 in .claude/lessons/lessons.md; probes in scratchpad debug_modal*.py

## Requirements
- Establish whether the machine restarted since onset (Windows event log: `systeminfo` boot time, update history around 2026-07-14 18:00) — if a reboot already happened and the fault persists, eliminate "pending update" theory
- Hunt the input pipeline: chromedriver verbose logs (`--verbose --log-path`) on a failing click; Chrome `chrome://histograms`/`--enable-logging` around input; compare a passing Playwright click's CDP traffic vs chromedriver's (both are Input.dispatchMouseEvent — what differs: target attachment? frame id? coordinates space?)
- Check machine-level suspects with evidence, not guesses: Windows pointer/precision settings changed ~07-14, accessibility filters, antivirus/EDR injecting into Chrome, display driver update, DPI/scaling change
- Deliver: root cause (or best-evidence candidate), the FIX (config change, version pin, driver flag), and a regression probe script to keep in the workspace (`tools/selenium-click-probe.py`) so future breakage is detected in seconds
- If fix requires reboot/OS action: state it as a finding with the evidence, don't just recommend blind

## References
- .claude/lessons/lessons.md — lessons #41, #42
- Scratchpad probes: debug_modal*.py, timing matrix + 20s flush test (2026-07-16 session)
- Playwright comparison baseline: works via mcp and direct

## Task Builder Input
- **Deliverable:** projects/selenium-click-fault/root-cause-report.md (cause + fix + evidence) and workspace:tools/selenium-click-probe.py (reusable probe)
- **Location:** subproject:selenium-click-fault
- **Scope:** RESEARCH
- **Constraints:** Diagnostic-only on machine state — no registry/system changes without reporting first (report the fix, let the user apply anything system-level). May install/run diagnostic tooling in scratchpad. Do not kill user processes. The one sanctioned code deliverable outside projects/ is tools/selenium-click-probe.py.
