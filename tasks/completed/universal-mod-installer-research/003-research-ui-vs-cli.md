# Task 003: Research UI vs CLI

## Type
RESEARCH

## Objective
Determine the right interface for a mod installer — CLI-only (Claude Code terminal), web UI, desktop app, or hybrid. Consider the target audience (gamers, not developers).

## Steps
1. Analyze target user:
   - Gamers modding their games — technical comfort level varies widely
   - FM community specifically — many non-technical users follow YouTube guides
   - Skyrim/Bethesda community — more technical, comfortable with MO2/Vortex
2. Evaluate interface options:
   - **CLI only (current):** Claude Code terminal. Powerful but intimidating for non-devs.
   - **Web UI:** Dashboard showing installed mods, one-click install. Needs backend.
   - **Desktop app (Electron/Tauri):** Native feel, file system access. Heavy to build.
   - **Hybrid:** CLI backend + simple web dashboard for status/browsing.
3. For each option assess:
   - Development effort
   - User experience for target audience
   - Maintenance burden
   - Distribution method (npm, exe installer, web app)
4. Research how existing mod managers handle UI:
   - Vortex: Electron app
   - MO2: Qt/C++ native
   - r2modman: Electron
   - Wabbajack: WPF/.NET
5. Recommend interface approach with rationale

## Deliverable
`projects/universal-mod-installer-research/03-ui-vs-cli.md`

## Acceptance Criteria
- At least 3 interface options evaluated
- Target audience analysis
- Clear recommendation with effort estimate
