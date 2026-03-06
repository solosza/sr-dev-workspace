# Kernel Spec Design

## What the Kernel Spec Produces

When domain-setup reads the kernel spec, it must produce every Category 1 file from the 017 audit. The kernel spec ships **reference copies** of these files that domain-setup copies into the target workspace.

### Files Produced (from 017 audit — all Category 1)

| File | Source in Spec | Notes |
|------|---------------|-------|
| `CLAUDE.md` | `_reference/CLAUDE.md` | Kernel rules, loop, commands reference |
| `.claude/commands/kernel/session-start.md` | `_reference/commands/kernel/session-start.md` | Check state, resume |
| `.claude/commands/kernel/anchor.md` | `_reference/commands/kernel/anchor.md` | Re-read protocol, review work |
| `.claude/commands/kernel/learn.md` | `_reference/commands/kernel/learn.md` | Record lesson after failure |
| `.claude/commands/kernel/complete.md` | `_reference/commands/kernel/complete.md` | Final gate |
| `.claude/commands/kernel/fix.md` | `_reference/commands/kernel/fix.md` | Impact assessment |
| `.claude/commands/kernel/reset.md` | `_reference/commands/kernel/reset.md` | Dev tool: fresh state |
| `.claude/commands/kernel/domain-setup.md` | `_reference/commands/kernel/domain-setup.md` | Entry point for domain-setup |
| `.claude/commands/kernel/autonomous-cycle.md` | `_reference/commands/kernel/autonomous-cycle.md` | Entry point for cycling |
| `.claude/hooks/universal-gate-enforcer.py` | `_reference/hooks/universal-gate-enforcer.py` | PreToolUse gate |
| `.claude/hooks/test-failure-detector.py` | `_reference/hooks/test-failure-detector.py` | PostToolUse test failure detection |
| `.claude/settings.local.json` | `_reference/settings.local.json` | Hook registration + base permissions |
| `.claude/skills/kernel-domain-setup/SKILL.md` | `_reference/skills/kernel-domain-setup/SKILL.md` | Domain-setup skill identity |
| `.claude/skills/kernel-domain-setup/references/step-01 through step-11` | `_reference/skills/kernel-domain-setup/references/*.md` | 11 domain-setup steps |
| `.claude/skills/autonomous-cycling/SKILL.md` | `_reference/skills/autonomous-cycling/SKILL.md` | Cycling skill identity |
| `.claude/skills/autonomous-cycling/workflow.md` | `_reference/skills/autonomous-cycling/workflow.md` | Cycling loop behavior |
| `.gitignore` | `_reference/.gitignore` | Git ignore rules |

**Total: 28 files produced** (CLAUDE.md + 8 commands + 2 hooks + 1 settings + 14 skill files + 1 gitignore + 1 state template)

### Files NOT Produced (domain-setup handles these)
- `.claude/protocols/[domain]-protocol.md` — domain-setup creates from spec
- `.claude/lessons/lessons.md` — domain-setup initializes
- `.claude/state/*` — domain-setup and session-start initialize

## Workflow Steps

The kernel spec's "workflow" is the build sequence. Unlike QA specs (which have discovery/construction/execution), the kernel spec has a simpler copy-and-configure flow.

### Step 1: Workspace Validation
- **Input:** Target workspace path
- **Check:** Is there an existing kernel? (`CLAUDE.md` with kernel markers)
- **If existing kernel:** STOP — kernel already installed. Use domain specs to add capabilities.
- **If clean workspace:** Proceed
- **Output:** `{workspace_clean: true}`

### Step 2: Copy CLAUDE.md
- **Input:** `_reference/CLAUDE.md`
- **Action:** Copy to workspace root
- **If existing CLAUDE.md:** Merge kernel sections (append, don't overwrite user content)
- **Output:** `CLAUDE.md` in workspace root

### Step 3: Copy Kernel Commands
- **Input:** `_reference/commands/kernel/*.md` (8 files)
- **Action:** Create `.claude/commands/kernel/` and copy all command files
- **Output:** 8 command files in `.claude/commands/kernel/`

### Step 4: Copy Hooks
- **Input:** `_reference/hooks/*.py` (2 files)
- **Action:** Create `.claude/hooks/` and copy hook files
- **Output:** 2 hook files in `.claude/hooks/`

### Step 5: Copy Skills
- **Input:** `_reference/skills/` (kernel-domain-setup + autonomous-cycling)
- **Action:** Create `.claude/skills/` and copy skill directories
- **Output:** 14 skill files across 2 skill directories

### Step 6: Configure Settings
- **Input:** `_reference/settings.local.json`
- **Action:** Create or merge `.claude/settings.local.json`
- **If existing settings:** Merge hook registrations (append hooks, merge permissions)
- **If clean:** Copy reference settings
- **Output:** `.claude/settings.local.json` with hooks registered

### Step 7: Initialize State
- **Action:** Create `.claude/state/` directory
- **Action:** Initialize `session_state.json` with `{session_started: false}`
- **Output:** State directory ready

### Step 8: Verify + Restart
- **Verify:** All 28 files exist in expected locations
- **Set:** `needs_restart: true` (hooks load on restart)
- **Report:** List all files created, prompt user to restart Claude Code

## Bootstrap Sequence

```
1. User has empty workspace (or existing project)
2. Install kernel spec → domain-setup reads it → copies 28 kernel files
3. RESTART Claude Code (hooks load)
4. Kernel is now active: hooks enforce, commands work, anchor blocks until invoked
5. Install domain spec → domain-setup reads it → builds domain governance on top
6. RESTART Claude Code (domain hooks load)
7. Governed workspace: kernel + domain spec active
```

**Key insight:** domain-setup EXISTS before step 2. It's the constant primitive. The kernel spec is just the first spec it processes. But the kernel spec is special — it installs domain-setup itself (as one of the skills it copies). This means:

- **First-ever install:** domain-setup must be bootstrapped somehow (can't use domain-setup to install itself)
- **Subsequent installs:** domain-setup already exists, reads domain specs normally

**Bootstrap resolution:** The kernel spec repo includes a simple `install.md` (or the spec's SKILL.md itself instructs domain-setup to copy files). Since domain-setup step-01 checks for prerequisites and step-03 reads reference code, the kernel spec's `_reference/` directory IS the reference code domain-setup reads and copies.

## File Structure for kernel-spec Repo

```
kernel-spec/
├── .claude/
│   ├── skills/
│   │   └── kernel-governance/                ← The kernel spec skill
│   │       ├── SKILL.md                      ← Identity, philosophy, steps overview
│   │       ├── workflow.md                   ← Build flow (copy + configure)
│   │       ├── gate-contract.md              ← Kernel governance responsibilities
│   │       ├── steps/
│   │       │   ├── step-01.md                ← Workspace validation
│   │       │   ├── step-02.md                ← Copy CLAUDE.md
│   │       │   ├── step-03.md                ← Copy kernel commands
│   │       │   ├── step-04.md                ← Copy hooks
│   │       │   ├── step-05.md                ← Copy skills
│   │       │   ├── step-06.md                ← Configure settings
│   │       │   ├── step-07.md                ← Initialize state
│   │       │   └── step-08.md                ← Verify + restart
│   │       └── checkpoints/
│   │           ├── pre-install.md            ← Check workspace clean
│   │           └── post-install.md           ← Verify all files
│   │
│   ├── commands/                             ← (none — kernel spec uses domain-setup command)
│   │
│   └── lessons/
│       ├── lessons.md                        ← Index
│       ├── bootstrap/
│       │   └── install-patterns.md           ← Bootstrap lessons
│       ├── kernel/
│       │   └── common-mistakes.md            ← Hook bypass, quick anchor, etc.
│       └── architecture/
│           └── layering.md                   ← Three-layer architecture
│
├── _reference/                               ← Files that get copied to target workspace
│   ├── CLAUDE.md
│   ├── .gitignore
│   ├── commands/
│   │   └── kernel/
│   │       ├── session-start.md
│   │       ├── anchor.md
│   │       ├── learn.md
│   │       ├── complete.md
│   │       ├── fix.md
│   │       ├── reset.md
│   │       ├── domain-setup.md
│   │       └── autonomous-cycle.md
│   ├── hooks/
│   │   ├── universal-gate-enforcer.py
│   │   └── test-failure-detector.py
│   ├── settings.local.json
│   └── skills/
│       ├── kernel-domain-setup/
│       │   ├── SKILL.md
│       │   └── references/
│       │       ├── step-01-prerequisites.md
│       │       ├── step-02-discover.md
│       │       ├── step-03-read.md
│       │       ├── step-04-extract.md
│       │       ├── step-05-enforcement.md
│       │       ├── step-06-workflow.md
│       │       ├── step-07-roadmap.md
│       │       ├── step-08-protocol.md
│       │       ├── step-09-commands.md
│       │       ├── step-10-state.md
│       │       └── step-11-report.md
│       └── autonomous-cycling/
│           ├── SKILL.md
│           └── workflow.md
│
├── README.md
├── FRAMEWORK.md
├── CONTRIBUTING.md
└── LICENSE
```

## Reference Code Strategy

The kernel spec ships actual kernel files in `_reference/`. These are **exact copies** from the canonical kernel repo (`isagawa-co/isagawa-kernel`).

- **Source of truth:** canonical kernel repo
- **Sync rule:** when kernel changes, update `_reference/` in kernel-spec
- **domain-setup reads `_reference/`** during step-03 (Read reference code) and copies files to target workspace during step-04 (Extract patterns) or via a custom build step

The kernel spec's workflow steps explicitly instruct domain-setup to copy each file from `_reference/` to its target location. This is different from QA specs (which teach the agent patterns to BUILD code). The kernel spec teaches domain-setup to INSTALL files.

## Open Questions

1. **settings.local.json merge strategy** — When a domain spec installs on top of an existing kernel, how should permissions merge? Union of allow lists? Append hooks? Need to handle in task 025-026 (rerunability).

2. **CLAUDE.md merge strategy** — Domain specs may need to add sections to CLAUDE.md. How does domain-setup merge without overwriting kernel sections? Options: append-only, section markers, separate includes file.

3. **Hook customization** — Are hooks always identical across all domains, or should domain specs be able to add custom hooks? Current design: hooks are constant (kernel-level), domain enforcement is via protocol (soft gate).

4. **First-install bootstrap** — If domain-setup doesn't exist yet, how does the kernel spec get processed? Options:
   - User manually copies files (defeats the purpose)
   - A simple shell script (`install.sh`) that copies files
   - domain-setup ships as a standalone CLI that works without CLAUDE.md
   - The kernel-spec repo IS the installable artifact (clone → CLAUDE.md already there)

   **Recommended:** Option 4 — the kernel-spec repo IS the starting point. User clones it, CLAUDE.md is already there with domain-setup skill included. They run `/kernel/domain-setup` to finalize (register hooks, init state). This sidesteps the bootstrap problem entirely.
