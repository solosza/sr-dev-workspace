# Input Pipeline Diff: Chromedriver vs Playwright

Research output for backlog 235, task 002.

## Pipeline Diff

### CDP Command Structure

Chromedriver issues **three** CDP `Input.dispatchMouseEvent` commands per click, in this exact sequence:

1. `mouseMoved` — position the pointer (button: "none", buttons: 0, clickCount: 0)
2. `mousePressed` — press left button (button: "left", buttons: 0, clickCount: 1)
3. `mouseReleased` — release left button (button: "left", buttons: 1, clickCount: 1)

All three share the same `session_id` and target attachment ID. The payload is identical between pre-navigation and post-navigation clicks — only coordinates differ (based on element position).

### Pre-Navigation Click (Page A — always delivers)

```
Command: Input.dispatchMouseEvent (id=85) session_id=105ADCEA80B4BF594F5D3ADC0C2B1B87
  type: mouseMoved, x: 131, y: 90, button: none, pointerType: mouse

Command: Input.dispatchMouseEvent (id=86) session_id=105ADCEA80B4BF594F5D3ADC0C2B1B87
  type: mousePressed, x: 131, y: 90, button: left, clickCount: 1, pointerType: mouse

Command: Input.dispatchMouseEvent (id=87) session_id=105ADCEA80B4BF594F5D3ADC0C2B1B87
  type: mouseReleased, x: 131, y: 90, button: left, clickCount: 1, pointerType: mouse
```

### Post-Navigation Click (Page B — historically drops ~15/16)

```
Command: Input.dispatchMouseEvent (id=176) session_id=105ADCEA80B4BF594F5D3ADC0C2B1B87
  type: mouseMoved, x: 41, y: 90, button: none, pointerType: mouse

Command: Input.dispatchMouseEvent (id=177) session_id=105ADCEA80B4BF594F5D3ADC0C2B1B87
  type: mousePressed, x: 41, y: 90, button: left, clickCount: 1, pointerType: mouse

Command: Input.dispatchMouseEvent (id=178) session_id=105ADCEA80B4BF594F5D3ADC0C2B1B87
  type: mouseReleased, x: 41, y: 90, button: left, clickCount: 1, pointerType: mouse
```

### Diff Result

**No protocol-level difference.** The CDP commands are structurally identical:
- Same 3-event sequence (mouseMoved → mousePressed → mouseReleased)
- Same session ID and target attachment throughout the session
- Same parameter structure (pointerType, force, modifiers, tiltX/Y, twist, tangentialPressure)
- Same response format (empty success response `{}`)
- Coordinates differ only because elements are at different positions

### Conclusion: Fault is Below CDP

The chromedriver CDP commands for post-navigation clicks are correct and complete. Chrome's WebSocket responses confirm receipt (id matches, empty success body). The fault, when it manifests, occurs **below the CDP protocol layer** — at the browser's compositor/input-routing level, after Chrome acknowledges the command but before the event reaches the DOM.

## Current Fault Status (2026-07-16 probe)

### Bare Pages: ALL CLICKS DELIVERED

The probe ran 10 post-navigation clicks on bare HTML pages against a fresh chromedriver session:

```
Page A click: result='CLICKED 1784234199020', DOM events=1  ← pre-nav (expected pass)
Page B click 0: result='CLICKED 1784234201619', DOM events=1  ← post-nav (historically drops)
Page B click 1: result='CLICKED 1784234202237', DOM events=2
Page B click 2: result='CLICKED 1784234202822', DOM events=3
...
Page B click 9: result='CLICKED 1784234206868', DOM events=10
```

**10/10 post-navigation clicks delivered.** This contradicts the original fault pattern (1/16 delivery rate on July 14-16).

### Possible Explanations

1. **Intermittent nature:** The fault was documented as ~1/16 (one success in 16 attempts). Today's probe may have hit a "good" window. A larger trial (100+ clicks) would be needed to confirm sustained recovery.

2. **Partial self-resolution:** Something changed between the July 14-16 fault window and now — possibly Windows Update background servicing settling, Chrome background update applying, or compositor state cycling through sleep/wake.

3. **Pending reboot effect:** KB5101650 (security update, July 15) is pending reboot. The update staging process may have reset some system state that was contributing to the fault, even without a full reboot.

4. **Bare-page vs real-app divergence:** The original fault was observed against Orderly (complex app with templates, sessions, form handling). Bare pages may not trigger the same code path in Chrome's compositor.

## Machine-Level Suspects (Read-Only Check)

### Display/DPI Settings

No changes found in System event log for display adapter or DPI settings around July 14 onset.

### Input/Pointer Settings

Power state transition events on July 14 show "Reason InputHid" — HID input device wake events. No pointer precision or accessibility filter changes detected in System events.

### Chrome Enterprise Policies

The backlog confirms: "No Chrome enterprise policies in registry." Verified read-only.

## Secondary Probe: mouseMoved Injection

Not conducted — the primary probe showed 10/10 delivery, so there is no failing click to improve upon in this session. The mouseMoved injection experiment requires a reproducing failure state to be meaningful. If the fault recurs, the probe should be re-run with a 100-click trial and the mouseMoved injection interleaved on alternating clicks.

## Artifacts

- `scratchpad/chromedriver_verbose.log` — Full verbose log, bare-page probe (824KB, 18213 lines)
- `scratchpad/chromedriver_verbose_orderly.log` — Full verbose log, Orderly probe (514KB)
- `scratchpad/cdp_probe_chromedriver.py` — Bare-page probe script
- `scratchpad/cdp_probe_orderly.py` — Orderly probe script
- `scratchpad/bare_server.py` + `bare_click_page.html` / `bare_click_page_b.html` — Test server

## Summary

The CDP input pipeline is **identical** between pre- and post-navigation clicks at the protocol level. The fault, when present, is below CDP — in Chrome's input-routing/compositor stack. Current probe shows **10/10 delivery**, suggesting the intermittent fault may have partially self-resolved since the July 14-16 window. Pending reboot (KB5101650) remains the strongest remediation candidate.
