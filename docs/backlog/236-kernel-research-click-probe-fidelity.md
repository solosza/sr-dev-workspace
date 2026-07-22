# Iterate 235: Click-Probe Fidelity — Find the Discriminator

## Status
Open

## Priority
High when active — the probe is the sentinel lesson #41's preflight relies on; a false-negative sentinel is worse than none. SEQUENCING: run AFTER the user reboots (the pending-reboot fix may clear the fault entirely; if post-reboot probe AND Orderly repro both stay green over a few days, downgrade this to Low/close).

parent_backlog: 235

## Summary
235's probe delivers 8/8 on its bare pages while the Orderly repro is DEAD in the same minutes — the fault is page/flow-dependent and the probe misses it. Find the single discriminating feature by bisection and upgrade `tools/selenium-click-probe.py` to include one Orderly-shaped trial.

## Requirements
- Bisect the differences between probe flow and Orderly repro, ONE variable at a time, N≥4 trials each, both variants in the same minutes (the fault drifts — always run the control alongside):
  1. Navigation type: link-click nav (probe) vs driver.get() nav (repro) on identical pages
  2. Prior POST-redirect chain (login form 303) before the tested navigation
  3. Server: python http.server vs uvicorn/FastAPI serving identical bytes
  4. Page weight/structure: serve the ACTUAL orders.html bytes from the bare server
  5. Session cookies present vs absent
- Evidence already ruled out (do NOT retest): full-viewport fixed display:none overlay (4/4 delivered with it, 2026-07-16); click-to-check delay 0.5-20s; headless-vs-headed; Chrome 140 vs 150; selenium 4.25 vs 4.39
- Upgrade tools/selenium-click-probe.py: add a trial mode replicating the discriminating condition; verdict line must go DEAD whenever the Orderly repro would
- Update projects/selenium-click-fault/root-cause-report.md with a Discriminator addendum

## References
- docs/backlog/done/235-kernel-research-selenium-click-fault.md (parent — full evidence base)
- projects/selenium-click-fault/ (report + notes)
- review-status entry 235 (orchestrator gap notes, 2026-07-16)

## Task Builder Input
- **Deliverable:** Discriminator identified with bisection evidence; upgraded probe that reproduces the fault; report addendum
- **Location:** subproject:selenium-click-fault
- **Scope:** RESEARCH
- **Constraints:** HOLD until post-reboot re-measure (see Priority). Diagnostic-only; ports: use ephemeral or 8019+; always run control+variant in the same window; no system changes.
