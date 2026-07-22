# Selenium Click-Fault Root Cause Report

Backlog 235. Diagnostic-only research into chromedriver post-navigation click delivery failure on this machine.

## Timeline

**Last boot:** 2026-07-12 22:30:01 (source: `Win32_OperatingSystem.LastBootUpTime` — notes-timeline.md)
**Fault onset:** 2026-07-14 ~18:00 (source: backlog 235 evidence block — pipelines 203/204 live click flows passed earlier that day)
**Machine rebooted since onset?** No — uptime spans the entire fault window (notes-timeline.md)

Key events on 2026-07-14, in order:

| Time | Event | Source |
|------|-------|--------|
| 11:07 AM | KB5120102 staged, Windows Modules Installer toggled | notes-timeline.md (Setup log) |
| 15:07 | DRIVERS registry hive reorganized (6750208 → 6729728 bytes) | notes-timeline.md (Kernel-General event 15) |
| 15:07–15:31 | WindowsAppRuntime ActivationStore.dat cleared (multiple packages) | notes-timeline.md |
| 16:03–17:42 | Multiple sleep/wake cycles (InputHid); 17:42 wake is closest to onset | notes-timeline.md (power state transitions) |
| 17:36 | Chrome SetupMetrics folder modified | notes-timeline.md |
| 17:58 | Chrome RLZ ping + DCOM permission error | notes-timeline.md |
| ~18:00 | First observed click delivery failure | backlog 235 evidence block |

**Pending reboot confirmed:** Both `RebootRequired` and `RebootPending` registry keys present. KB5101650 (security update, staged 2026-07-15 03:42 AM) explicitly requires reboot to install (notes-timeline.md, Setup log: "A reboot is necessary before package KB5101650 can be changed to the Installed state").

No driver installs/uninstalls found in System log for July 14. No display adapter changes detected (notes-timeline.md).

## Pipeline Diff

Chromedriver issues three CDP `Input.dispatchMouseEvent` commands per click (notes-pipeline-diff.md):

1. `mouseMoved` — position pointer (button: "none", clickCount: 0)
2. `mousePressed` — press left button (button: "left", clickCount: 1)
3. `mouseReleased` — release button (button: "left", clickCount: 1)

**Pre-navigation vs post-navigation comparison:** No protocol-level difference. Structurally identical — same 3-event sequence, same session ID and target attachment, same parameter structure, same empty success response `{}`. Only coordinates differ based on element position (notes-pipeline-diff.md, CDP log excerpts commands 85-87 vs 176-178).

**Conclusion:** The fault is **below the CDP protocol layer** — Chrome acknowledges the commands successfully, but the events do not reach the DOM. Zero DOM events at document level via capture-phase listener on failed clicks (backlog 235 evidence block). Playwright (own browser + own CDP client) never drops clicks in the same scenario (backlog 235 evidence block; lesson #42 in lessons.md).

## Root Cause

**Best-evidence candidate: Compositor/input-routing state corruption in Chrome's chromedriver session, triggered by Windows Update staging + sleep/wake cycling during the same boot session.**

**Confidence: Medium-high (convergent evidence, no single smoking gun).**

Evidence chain:

1. **The fault is specific to chromedriver's Chrome session** — Playwright launches its own browser and is unaffected (backlog 235; notes-pipeline-diff.md). This eliminates machine-wide input subsystem failure.

2. **The fault is below CDP** — CDP commands are protocol-identical between working and failing clicks; Chrome acknowledges receipt. The drop occurs in Chrome's internal input-routing/compositor between CDP acknowledgment and DOM event dispatch (notes-pipeline-diff.md).

3. **The fault appeared mid-session without explicit trigger** — no driver installs, no Chrome update applied, no display changes on July 14 (notes-timeline.md). But: DRIVERS hive reorganization at 15:07, Chrome SetupMetrics activity at 17:36, and 6+ sleep/wake cycles throughout the day.

4. **The fault is intermittent** — ~1/16 delivery rate during the July 14-16 window (backlog 235), but 10/10 delivery on the probe run during task 002 research (notes-pipeline-diff.md). The intermittent recovery without reboot suggests compositor state cycling, not a permanent configuration change.

5. **Pending reboot is confirmed** — KB5101650 requires reboot; the machine has been up since July 12. Windows Update staging modifies system state (service configurations, runtime packages) that may affect Chrome's compositor when not finalized by reboot (notes-timeline.md).

**Mechanism hypothesis:** Chrome's compositor maintains per-session input routing state that can enter a degraded mode when the Windows input subsystem is perturbed (sleep/wake cycles, HID device reconnection, background update staging). In this state, `Input.dispatchMouseEvent` CDP commands are acknowledged at the protocol layer but silently dropped at the compositor's page-target routing after navigation creates a new render frame. Playwright avoids this because it launches a fresh browser instance with its own compositor state, while chromedriver sessions inherit the degraded state from the running Chrome process context.

## Fix

**Primary fix: Reboot the machine.**

| Action | Type | Evidence |
|--------|------|----------|
| Reboot | User action (system-level) | Pending reboot confirmed via registry keys; KB5101650 requires reboot; machine has been up since July 12 spanning the entire fault window; no reboot has been attempted since onset (notes-timeline.md). The fault appeared without any applied change, suggesting accumulated system state degradation that only a full reboot can reset. |
| Re-run probe after reboot | Verification | `python tools/selenium-click-probe.py --trials 16` — if all 16 deliver, the fix is confirmed. If the fault persists post-reboot, the cause is Chrome 150-specific and requires Chrome version pinning investigation. |

**Secondary fix (if reboot does not resolve):** Pin Chrome to a known-good version. Chrome 150.0.7871.115 was installed July 13 (notes-timeline.md), one day before onset. If rebooting clears the fault, Chrome 150 is exonerated. If the fault persists post-reboot, the chromedriver/Chrome 150 combination is the suspect and downgrading Chrome or pinning chromedriver to a compatible version is the next diagnostic step.

**Not applied:** All fixes are system-level actions (reboot, Chrome version management). Per backlog 235 constraints: diagnostic-only, no system changes applied.

## Attestation

No system state was modified during this research:

- No registry keys written, deleted, or modified
- No services started, stopped, or reconfigured
- No drivers installed or uninstalled
- No Chrome settings or policies changed
- No user processes killed
- All probes used read-only system queries (`Get-CimInstance`, `Get-WinEvent`, `Get-ChildItem`, registry reads) and self-contained test servers/browsers that were cleanly shut down

Probe scripts and test pages created in `scratchpad/` (disposable) and `tools/` (permanent probe). Chromedriver verbose logs captured to `scratchpad/` for analysis.

## Probe

Run the regression probe to check current click delivery status:

```bash
python tools/selenium-click-probe.py --trials 16
```

**What it does:**
- Starts a local HTTP server on a random port serving two bare HTML pages
- Page 1: link to page 2 (tests navigation click)
- Page 2: button with onclick DOM flag (tests post-navigation click delivery)
- Launches headless Chrome via selenium, clicks through both pages per trial
- Reports per-trial verdict (DELIVERED/DEAD) with step timing
- Overall verdict: DELIVERED (all trials pass, exit 0) or DEAD (any trial fails, exit 1)

**Usage:**
- Default: `python tools/selenium-click-probe.py` (3 trials)
- Extended: `python tools/selenium-click-probe.py --trials 100` (rate measurement)
- CI preflight: exit code 0/1 is machine-readable

**Dependencies:** Python 3, selenium (pip). No framework imports.

**When to run:**
- Before any selenium E2E test suite (env-sanity preflight per lesson #41)
- After machine reboot (verify fix)
- After Chrome or chromedriver version changes
- When selenium tests start failing with click-not-delivered symptoms
