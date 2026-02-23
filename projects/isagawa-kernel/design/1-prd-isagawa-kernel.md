# PRD: Isagawa Kernel

**Version:** 1.0
**Created:** 2026-02-06
**Status:** Draft
**Design Doc:** `0-design-isagawa-kernel.md`

---

## 1. Introduction/Overview

The Isagawa Kernel is a **self-building, self-improving, safety-first agent** implemented as a CLAUDE.md that teaches Claude Code how to:

1. Analyze any domain it enters
2. Build protocols (how work must be done)
3. Self-create slash commands for enforcement
4. Operate within self-built structure
5. Improve and extend over time

**Problem:** AI agents drift as context grows. External guardrails are rigid. No mechanism exists for agents to create and enforce their own professional standards dynamically.

**Solution:** A kernel that teaches the agent to author its own constraints via slash commands, then invoke them to stay anchored.

---

## 2. Goals

| Goal | Measurable Outcome |
|------|-------------------|
| Agent self-builds defense in depth | Creates protocols + slash commands for any domain |
| Agent stays anchored | Invokes own commands, doesn't drift |
| Agent self-improves | Creates new commands when encountering friction |
| Preserves autonomy | Agent is author of constraints, not constrained externally |
| Self-builds test harness | Agent creates its own validation infrastructure |

---

## 3. User Stories

**Primary User:** Developer testing the kernel concept (this weekend)

| Story | Description |
|-------|-------------|
| US-1 | As a developer, I want to point the kernel at the QA domain and see it self-build protocols that match my existing FRAMEWORK.md patterns |
| US-2 | As a developer, I want to see the kernel create slash commands in `.claude/commands/` that enforce its protocols |
| US-3 | As a developer, I want to see the kernel invoke its own commands to stay anchored during work |
| US-4 | As a developer, I want to compare Agent A (HITL) vs Agent B (pure autonomy) behavior |
| US-5 | As a developer, I want the kernel to self-build a test harness that validates its own behavior |

---

## 4. Functional Requirements

### 4.1 Kernel CLAUDE.md

| ID | Requirement |
|----|-------------|
| FR-1 | Kernel MUST contain meta-instructions for analyzing any domain |
| FR-2 | Kernel MUST instruct agent to build protocols before working |
| FR-3 | Kernel MUST instruct agent to create slash commands for enforcement BEFORE doing domain work (safety-first) |
| FR-4 | Kernel MUST instruct agent to invoke its commands regularly to stay anchored |
| FR-5 | Kernel MUST instruct agent to create new commands when encountering friction (self-improvement) |

### 4.2 Agent A Variant (HITL)

| ID | Requirement |
|----|-------------|
| FR-6 | Agent A MUST present protocols to human for approval before proceeding |
| FR-7 | Agent A MUST present slash commands it creates for approval before using them |
| FR-8 | Agent A MUST ask human before adding new commands (self-improvement with approval) |

### 4.3 Agent B Variant (Pure Autonomy)

| ID | Requirement |
|----|-------------|
| FR-9 | Agent B MUST build protocols without waiting for approval |
| FR-10 | Agent B MUST create and use slash commands autonomously |
| FR-11 | Agent B MUST self-improve without human intervention |

### 4.4 Self-Built Test Harness

| ID | Requirement |
|----|-------------|
| FR-12 | Kernel MUST instruct agent to create a test harness for validating its own behavior |
| FR-13 | Test harness SHOULD include commands to verify protocols are followed |
| FR-14 | Test harness SHOULD include commands to detect drift |
| FR-15 | Test harness SHOULD be created as slash commands the agent can invoke |

### 4.5 Slash Command Structure

| ID | Requirement |
|----|-------------|
| FR-16 | Slash commands MUST be created in `.claude/commands/` directory |
| FR-17 | Each command MUST be a standalone `.md` file |
| FR-18 | Command names SHOULD reflect their purpose (e.g., `validate-architecture.md`) |
| FR-19 | Commands MUST re-anchor agent to specific protocols when invoked |

---

## 5. Non-Goals (Out of Scope)

| Non-Goal | Reason |
|----------|--------|
| Multiple domains | Weekend scope — QA only |
| Domain packs | Kernel should work without accelerators first |
| Production polish | This is concept validation |
| Static hooks | Using self-created slash commands instead |
| MCP enforcement tools | Using Claude Code native mechanisms |
| UI/Dashboard | Terminal-first, developer-focused |

---

## 6. Technical Considerations

### 6.1 Architecture

```
CLAUDE.md (Kernel)
├── Meta-instructions for self-build
├── Safety-first pattern (create enforcement before working)
├── Re-anchoring pattern (invoke commands)
└── Self-improvement pattern (create new commands)

.claude/commands/ (Agent-Created)
├── [domain]-validate.md
├── [domain]-audit.md
├── [domain]-check.md
├── test-harness.md
└── ... (whatever agent decides to create)
```

### 6.2 Dependencies

| Dependency | Purpose |
|------------|---------|
| Claude Code | Runtime environment |
| .claude/commands/ | Slash command storage |
| Existing QA framework | Reference for validation |

### 6.3 Two Variants

| Variant | CLAUDE.md Difference |
|---------|---------------------|
| Agent A | Includes HITL checkpoints: "Present to human and await approval before..." |
| Agent B | No HITL checkpoints: "Proceed directly..." |

---

## 7. Success Metrics

| Metric | Target | How to Measure |
|--------|--------|----------------|
| Commands created | ≥3 | Count files in .claude/commands/ after run |
| Pattern match | Recognizable | Compare to FRAMEWORK.md patterns manually |
| Stays anchored | No major drift | Observe if agent invokes its commands |
| Self-built harness | Exists | Agent creates test/validation commands |
| Both variants run | Complete | Both A and B finish QA domain test |

---

## 8. Test Protocol

### 8.1 Test Domain

QA test automation (existing framework as reference)

### 8.2 Test Steps

```
1. Start fresh Claude Code session
2. Load kernel CLAUDE.md
3. Give prompt: "I need QA test automation for a web application"
4. Observe:
   - Does agent analyze the domain?
   - Does agent build protocols?
   - Does agent create slash commands BEFORE working?
   - Does agent create a test harness for itself?
5. Let agent work on a simple task (e.g., "create a login test")
6. Observe:
   - Does agent invoke its commands?
   - Does it stay anchored to its protocols?
7. Repeat with Agent B variant
8. Compare outputs
```

### 8.3 Acceptance Tests

| ID | Given | When | Then |
|----|-------|------|------|
| AT-1 | Kernel loaded, QA domain prompt given | Agent analyzes domain | Agent produces protocol document |
| AT-2 | Agent has protocols | Agent prepares to work | Agent creates ≥1 slash command first |
| AT-3 | Agent has commands | Agent works on task | Agent invokes at least one command |
| AT-4 | Agent encounters friction | Agent identifies issue | Agent proposes new command |
| AT-5 | Agent A variant | Any structural creation | Agent asks human for approval |
| AT-6 | Agent B variant | Any structural creation | Agent proceeds without asking |
| AT-7 | Kernel instructs self-test | Agent builds harness | Test harness commands exist |

---

## 9. Test-and-Learn Items

Items to explore during implementation (from design):

| Question | Hypothesis | Observe |
|----------|------------|---------|
| Minimum commands before working? | Agent decides | What does it create naturally? |
| Re-anchoring triggers? | Agent decides | When does it invoke commands? |
| Session persistence? | Commands persist as files | Do commands survive restart? |
| HITL granularity? | Approve structure, not each command | Is Agent A too slow? |
| Command naming? | Agent chooses | What patterns emerge? |
| Test harness scope? | Agent decides | How complete is self-built harness? |

---

## 10. Deliverables

| Deliverable | Location | Description |
|-------------|----------|-------------|
| Kernel CLAUDE.md (A) | `.claude/kernel-a.md` or similar | HITL variant |
| Kernel CLAUDE.md (B) | `.claude/kernel-b.md` or similar | Pure autonomy variant |
| Test session logs | `docs/projects/isagawa-kernel/test-logs/` | What happened during test |
| Comparison notes | `docs/projects/isagawa-kernel/comparison.md` | A vs B analysis |
| Agent-created commands | `.claude/commands/` | Whatever agent builds |
| Agent-created harness | `.claude/commands/` or docs | Self-validation infrastructure |

---

## 11. Open Questions

| Question | Resolution Path |
|----------|-----------------|
| Best location for kernel CLAUDE.md? | Test both: root vs .claude/ |
| Should kernel replace or augment existing CLAUDE.md? | Start with separate file, merge later if needed |
| How to switch between Agent A and B? | Separate CLAUDE.md files or sections |

---

## 12. Definition of Ready

- [x] Design doc complete
- [x] PRD complete
- [x] Success metrics defined
- [x] Test protocol defined
- [x] Acceptance tests defined
- [ ] Proceed to task generation

---

*Status: PRD complete. Ready for Phase 3 (Divide).*
