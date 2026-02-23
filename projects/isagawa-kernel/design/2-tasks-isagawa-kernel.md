# Tasks: Isagawa Kernel

**PRD:** `1-prd-isagawa-kernel.md`
**Created:** 2026-02-06
**Status:** Ready for execution

---

## Relevant Files

### New Repo (D:\my_ai_projects\isagawa-kernel)

| File | Description |
|------|-------------|
| `CLAUDE.md` | Kernel meta-instructions (or separate A/B variants) |
| `README.md` | Project overview |
| `.claude/commands/` | Directory for agent-created slash commands |
| `docs/design/0-design-isagawa-kernel.md` | Design doc (moved from QA repo) |
| `docs/design/1-prd-isagawa-kernel.md` | PRD (moved from QA repo) |
| `docs/test-logs/` | Session logs from testing |
| `docs/comparison.md` | A vs B analysis |

### This Repo (py_sel_framework_mcp)

| File | Description |
|------|-------------|
| `docs/projects/isagawa-kernel/` | Keep as reference/pointer to new repo |

---

## Tasks

### 1.0 Create and initialize isagawa-kernel repo [GLUE]

- [ ] 1.1 Create directory `D:\my_ai_projects\isagawa-kernel`
- [ ] 1.2 Initialize git repo (`git init`)
- [ ] 1.3 Create basic structure:
  ```
  isagawa-kernel/
  ├── .claude/
  │   └── commands/        ← Agent will create files here
  ├── docs/
  │   ├── design/          ← Design docs
  │   └── test-logs/       ← Test session logs
  ├── CLAUDE.md            ← Kernel (or kernel-a.md, kernel-b.md)
  ├── README.md
  └── .gitignore
  ```
- [ ] 1.4 Create README.md with project overview
- [ ] 1.5 Create .gitignore (standard Python/Node ignores)
- [ ] 1.6 Copy design docs from this repo to new repo:
  - `0-design-isagawa-kernel.md`
  - `1-prd-isagawa-kernel.md`
  - `2-tasks-isagawa-kernel.md`
- [ ] 1.7 Update this repo's design doc folder with pointer to new repo
- [ ] 1.8 Initial commit: `chore: Initialize isagawa-kernel repo`

**Done when:** Repo exists with structure, design docs moved, pointer left in QA repo

---

### 2.0 Write Kernel CLAUDE.md (both variants) [CORE]

- [ ] 2.1 Write core kernel instructions (shared by both variants):
  - Section: Identity (what this kernel is)
  - Section: Domain Analysis (how to analyze any domain)
  - Section: Protocol Building (how to create protocols)
  - Section: Self-Create Enforcement (create slash commands BEFORE working)
  - Section: Re-Anchoring (invoke commands to stay anchored)
  - Section: Self-Improvement (create new commands when friction)
  - Section: Safety-First Pattern (enforcement before execution)
- [ ] 2.2 Write Agent A variant additions:
  - HITL checkpoint: Present protocols for approval
  - HITL checkpoint: Present commands for approval
  - HITL checkpoint: Approval before self-improvement
- [ ] 2.3 Write Agent B variant additions:
  - No HITL: Proceed directly with self-build
  - No HITL: Create and use commands autonomously
  - No HITL: Self-improve without asking
- [ ] 2.4 Decide structure: One file with sections OR two separate files
- [ ] 2.5 Write self-built test harness instructions:
  - Instruct agent to create validation commands for itself
  - Include example patterns (e.g., `/validate`, `/audit`, `/check-drift`)
- [ ] 2.6 Review against PRD requirements (FR-1 through FR-19)
- [ ] 2.7 Commit: `feat: Add kernel CLAUDE.md with A/B variants`

**Done when:** Kernel CLAUDE.md exists with all meta-instructions, both variants defined

---

### 3.0 Test Kernel on QA domain [CORE]

- [ ] 3.1 Test Agent A variant:
  - [ ] 3.1.1 Start fresh Claude Code session in isagawa-kernel repo
  - [ ] 3.1.2 Load kernel CLAUDE.md (Agent A)
  - [ ] 3.1.3 Prompt: "I need QA test automation for a web application"
  - [ ] 3.1.4 Observe: Does agent analyze domain?
  - [ ] 3.1.5 Observe: Does agent build protocols?
  - [ ] 3.1.6 Observe: Does agent create slash commands BEFORE working?
  - [ ] 3.1.7 Observe: Does agent ask for approval (HITL)?
  - [ ] 3.1.8 Observe: Does agent create test harness for itself?
  - [ ] 3.1.9 Give task: "Create a login test"
  - [ ] 3.1.10 Observe: Does agent invoke its commands?
  - [ ] 3.1.11 Observe: Does agent stay anchored?
  - [ ] 3.1.12 Save session log to `docs/test-logs/agent-a-session.md`
- [ ] 3.2 Test Agent B variant:
  - [ ] 3.2.1 Start fresh Claude Code session
  - [ ] 3.2.2 Load kernel CLAUDE.md (Agent B)
  - [ ] 3.2.3 Same prompt: "I need QA test automation for a web application"
  - [ ] 3.2.4 Observe: Same checkpoints as Agent A
  - [ ] 3.2.5 Observe: Does it proceed without asking?
  - [ ] 3.2.6 Give task: "Create a login test"
  - [ ] 3.2.7 Observe: Anchoring and drift behavior
  - [ ] 3.2.8 Save session log to `docs/test-logs/agent-b-session.md`
- [ ] 3.3 Verify acceptance tests (from PRD):
  - [ ] AT-1: Agent produces protocol document
  - [ ] AT-2: Agent creates ≥1 slash command before working
  - [ ] AT-3: Agent invokes at least one command during work
  - [ ] AT-4: Agent proposes new command on friction (if occurs)
  - [ ] AT-5: Agent A asks for approval
  - [ ] AT-6: Agent B proceeds without asking
  - [ ] AT-7: Test harness commands exist

**Done when:** Both variants tested, session logs saved, acceptance tests verified

---

### 4.0 Document findings and compare variants [GLUE]

- [ ] 4.1 Create `docs/comparison.md` with:
  - What Agent A did vs Agent B
  - Commands each created (list them)
  - HITL friction in Agent A (too much? too little?)
  - Drift observed in Agent B (yes/no, how much)
  - Which variant felt more effective
- [ ] 4.2 Compare agent-created commands to FRAMEWORK.md patterns:
  - Do commands reflect similar architecture rules?
  - What did agent capture that we have?
  - What did agent miss?
- [ ] 4.3 Document test-and-learn findings:
  - Minimum commands: What did agent create naturally?
  - Re-anchoring: When did agent invoke commands?
  - Session persistence: Did commands survive?
  - Test harness: How complete was it?
- [ ] 4.4 List improvements for next iteration
- [ ] 4.5 Update design doc with learnings
- [ ] 4.6 Commit: `docs: Add test findings and variant comparison`

**Done when:** Comparison doc complete, learnings captured, next steps identified

---

## Weekend Schedule (Suggested)

| Block | Task | Duration |
|-------|------|----------|
| Sat AM | 1.0 Repo setup | 30 min |
| Sat AM-PM | 2.0 Write kernel | 2-3 hours |
| Sat PM | 3.1 Test Agent A | 1-2 hours |
| Sun AM | 3.2 Test Agent B | 1-2 hours |
| Sun PM | 4.0 Document findings | 1 hour |

---

## Success Criteria

| Criteria | Target |
|----------|--------|
| Repo created | ✓ |
| Kernel CLAUDE.md written | ✓ |
| Both variants tested | ✓ |
| Commands created by agent | ≥3 |
| Agent invokes own commands | ≥1 time |
| Comparison documented | ✓ |

---

*Status: Tasks ready for execution.*
