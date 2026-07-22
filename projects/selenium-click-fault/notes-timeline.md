# Machine Timeline vs Fault Onset

Research output for backlog 235, task 001.

## Timeline

### Boot & Reboot Status

**Last boot:** Sunday, July 12, 2026 10:30:01 PM
**Fault onset:** Monday, July 14, 2026 ~6:00 PM
**Machine rebooted since onset?** NO — uptime spans the entire fault window.

**Pending reboot?** YES — both registry keys present:
- `HKLM:\SOFTWARE\Microsoft\Windows\CurrentVersion\WindowsUpdate\Auto Update\RebootRequired` — EXISTS
- `HKLM:\SOFTWARE\Microsoft\Windows\CurrentVersion\Component Based Servicing\RebootPending` — EXISTS

**Verdict:** "Reboot fixes it" is NOT disproven — the machine has never rebooted since the fault began. A pending reboot is actively flagged by Windows.

```
Command: (Get-CimInstance Win32_OperatingSystem).LastBootUpTime
Output:  Sunday, July 12, 2026 10:30:01 PM
```

### Windows Updates Around Onset

| KB | Type | Date Staged | Date Installed | Reboot Required? |
|----|------|------------|----------------|-----------------|
| KB5120102 | Security Update | July 14 11:07 AM | July 15 3:36 AM | No (installed OK) |
| KB5101650 | Security Update | July 15 3:36 AM | July 15 3:42 AM (staged) | **YES — pending reboot** |
| KB5100998 | (unknown) | July 15 3:13 AM | July 15 3:14 AM | Unknown |

KB5101650 was staged at 3:42 AM on July 15 and the Setup log explicitly states: "A reboot is necessary before package KB5101650 can be changed to the Installed state."

```
Command: Get-WinEvent -FilterHashtable @{LogName='Setup'; StartTime='2026-07-13'; EndTime='2026-07-16'}
Output (key lines):
  7/15/2026 3:50:27 AM - A reboot is necessary before package KB5101650 can be changed to the Installed state.
  7/14/2026 11:07:27 AM - Package KB5120102 was successfully changed to the Staged state.
```

### Chrome & Chromedriver

- **Chrome version:** 150.0.7871.115 (installed July 13 2:21 PM, chrome.dll built July 7)
- **SetupMetrics folder:** Last modified July 14 5:36 PM — activity around onset
- **Selenium version:** 4.39.0
- **chromedriver-autoinstaller:** Not installed (chromedriver managed externally)
- **chromedriver binary:** Not found in PATH or project dir at time of check

```
Command: Get-ChildItem "${env:ProgramFiles}\Google\Chrome\Application" -Directory
Output:
  150.0.7871.115  7/13/2026 2:21:20 PM
  SetupMetrics    7/14/2026 5:36:57 PM
```

### Notable System Events on July 14

**3:07 PM — DRIVERS hive reorganized:**
The system DRIVERS registry hive was reorganized (6750208 → 6729728 bytes). This is a compaction event but indicates driver-related registry activity the same day as fault onset.

```
Event 15, Microsoft-Windows-Kernel-General:
  Hive \SystemRoot\System32\config\DRIVERS was reorganized
  with starting size 6750208 bytes and ending size 6729728 bytes.
```

**11:07 AM — Windows Modules Installer toggled:**
Service Control Manager changed Windows Modules Installer from demand→auto→demand start. This is Windows Update staging KB5120102.

**3:07-3:31 PM — WindowsAppRuntime ActivationStore updates:**
Multiple AppRuntime packages (1.8, 2.x) had ActivationStore.dat cleared. Timing correlates with DRIVERS hive reorg.

**5:36 PM — Chrome SetupMetrics updated:**
Chrome's setup metrics folder was modified 24 minutes before estimated fault onset. Could indicate a Chrome background update check or telemetry operation.

**5:58 PM — Chrome RLZ ping:**
Chrome sent an RLZ telemetry ping. Normal periodic activity.

**5:58 PM — DCOM permission error:**
Local Activation permission error for COM Server {2593F8B9-4EAF-457C-B68A-50F6B8EA6B54}. Recurring issue (also at 10:56 AM).

**Power state transitions (InputHid):**
Multiple sleep/wake cycles on July 14. Key transitions:
- 4:03 PM — wake from InputAccelerometer
- 4:26 PM — wake from InputHid
- 5:08 PM — wake from InputHid
- 5:42 PM — wake from InputHid ← closest to fault onset
- 7:29 PM — wake from InputHid
- 8:44 PM — wake from InputHid

The machine went through at least 6 sleep/wake cycles on July 14. The 5:42 PM wake is nearest to the estimated fault onset (~6 PM).

**No driver install/uninstall events found** in the System log for July 14. The DRIVERS hive reorg is a compaction, not a driver installation.

**No display adapter changes** found in System events.

### Summary of Findings

1. **Machine has NOT rebooted since July 12** — the entire fault window is within one boot session
2. **Pending reboot is active** — KB5101650 (security update) requires reboot, has not been applied
3. **Chrome 150.0.7871.115** was installed July 13 (day before onset) — could be a contributing factor if chromedriver version mismatch exists
4. **DRIVERS hive reorganized** at 3:07 PM on July 14 — same day as onset but 3 hours before estimated time
5. **Multiple sleep/wake cycles** on July 14, with the 5:42 PM wake closest to onset
6. **No explicit driver installs** found in event logs for July 14
7. **Windows Update staging** (KB5120102) happened at 11:07 AM on July 14; KB5101650/KB5100998 staged overnight July 14→15

### Recommendation

The strongest single remediation candidate is **rebooting the machine**:
- Pending reboot is confirmed flagged by Windows
- Machine has been up since July 12 with security updates pending
- The fault appeared mid-session on July 14 without any explicit trigger
- Sleep/wake cycling may have left compositor or input subsystem in a degraded state that only a full reboot can reset
