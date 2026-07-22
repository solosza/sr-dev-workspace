# Research: Machine Timeline vs Fault Onset

## Context
Backlog 235. Onset 2026-07-14 ~18:00. Establish what changed on the machine — with command evidence, not guesses.

## Type
RESEARCH
## Execution
inline
## Dependencies
- None

## Requirements
- Last boot: `powershell "(Get-CimInstance Win32_OperatingSystem).LastBootUpTime"` — did the machine reboot since onset? (Decides whether "reboot fixes it" is already disproven)
- Update history: `powershell "Get-HotFix | Sort-Object InstalledOn -Descending | Select-Object -First 10"` + Windows Update log around 07-14; Chrome version install dates in `%ProgramFiles%/Google/Chrome` metadata
- Display/driver/UI changes around onset: `powershell "Get-WinEvent -FilterHashtable @{LogName='System'; StartTime='2026-07-14'} -MaxEvents 200"` filtered for driver/display/input service events
- Write findings to `projects/selenium-click-fault/notes-timeline.md` — every claim with the command + output excerpt

## Acceptance Criteria
- [ ] notes-timeline.md: boot time verdict, update list, notable events around onset

## Gates Satisfied
- SCF-01, SCF-05

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
