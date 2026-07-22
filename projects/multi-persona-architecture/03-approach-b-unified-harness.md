# Approach B: Unified Harness Architecture

**Task:** 003-research-approach-b-unified-harness
**Date:** 2026-07-07

---

## Architecture Diagram

```
┌──────────────────────────────────────────────────────────────────┐
│                    UNIFIED HARNESS REPO                          │
│                    sr_dev_workspace/                             │
│                                                                  │
│  ┌────────────────────────────────────────────────────────────┐  │
│  │                  SHARED KERNEL LAYER                       │  │
│  │                                                            │  │
│  │  .claude/protocols/sr_dev-protocol.md (indexed, shared)    │  │
│  │  .claude/hooks/universal-gate-enforcer.py                  │  │
│  │  .claude/hooks/actions-log-appender.py                     │  │
│  │  .claude/hooks/test-failure-detector.py                    │  │
│  │  .claude/commands/kernel/ (session-start, anchor, etc.)    │  │
│  │  .claude/lessons/lessons.md (shared cheat sheet)           │  │
│  │  .claude/state/session_state.json                          │  │
│  │  run-task.sh                                               │  │
│  └────────────────────────┬───────────────────────────────────┘  │
│                           │                                      │
│                  ┌────────▼────────┐                             │
│                  │ PERSONA ROUTER  │                             │
│                  │                 │                             │
│                  │ Reads:          │                             │
│                  │ - backlog tag   │                             │
│                  │ - explicit flag │                             │
│                  │ - command prefix│                             │
│                  └────────┬────────┘                             │
│                           │                                      │
│       ┌───────────┬───────┼───────┬───────────┐                 │
│       ▼           ▼       ▼       ▼           ▼                 │
│  ┌─────────┐ ┌────────┐ ┌────┐ ┌───────┐ ┌─────────┐          │
│  │Developer│ │  QA    │ │ PM │ │ Sales │ │Marketing│          │
│  │ Mode    │ │ Mode   │ │Mode│ │ Mode  │ │  Mode   │          │
│  ├─────────┤ ├────────┤ ├────┤ ├───────┤ ├─────────┤          │
│  │commands/│ │commands/│ │cmd/│ │ cmd/  │ │  cmd/   │          │
│  │ kernel/ │ │ qa/    │ │pm/ │ │sales/ │ │ mktg/   │          │
│  │skills/  │ │skills/ │ │sk/ │ │ sk/   │ │  sk/    │          │
│  │hooks/   │ │hooks/  │ │hk/ │ │ hk/   │ │  hk/    │          │
│  │lessons/ │ │lessons/│ │ls/ │ │ ls/   │ │  ls/    │          │
│  │ dev/    │ │ qa/    │ │pm/ │ │sales/ │ │ mktg/   │          │
│  └─────────┘ └────────┘ └────┘ └───────┘ └─────────┘          │
│                                                                  │
│  .claude/state/                                                  │
│  ├── sr_dev_workflow.json        (shared kernel state)          │
│  ├── persona-active.json         (which persona is active)      │
│  ├── persona/                                                    │
│  │   ├── dev_workflow.json       (dev-specific state)           │
│  │   ├── qa_workflow.json        (qa-specific state)            │
│  │   ├── pm_workflow.json        (pm-specific state)            │
│  │   ├── sales_workflow.json     (sales-specific state)         │
│  │   └── mktg_workflow.json      (mktg-specific state)         │
│  └── persona/                                                    │
│      ├── dev_lessons.md                                          │
│      ├── qa_lessons.md                                           │
│      ├── pm_lessons.md                                           │
│      ├── sales_lessons.md                                        │
│      └── mktg_lessons.md                                         │
└──────────────────────────────────────────────────────────────────┘
```

Each persona is a **workflow mode** within the same repo. The shared kernel layer (session-start, anchor, complete, learn, fix, hooks) runs identically regardless of persona. Persona-specific commands, skills, hooks, and lessons live in namespaced directories.

---

## Command Namespace Design

### Namespace Convention

Commands are namespaced by persona prefix under `.claude/commands/`:

```
.claude/commands/
├── kernel/                    # Shared kernel commands (all personas)
│   ├── session-start.md
│   ├── anchor.md
│   ├── complete.md
│   ├── learn.md
│   ├── fix.md
│   └── execute-pipeline.md
├── dev/                       # Developer-specific
│   ├── build.md               →  /dev/build
│   ├── design.md              →  /dev/design
│   └── backlog.md             →  /dev/backlog
├── qa/                        # QA-specific
│   ├── run.md                 →  /qa/run
│   ├── schedule.md            →  /qa/schedule
│   └── report.md              →  /qa/report
├── pm/                        # PM-specific
│   ├── prioritize.md          →  /pm/prioritize
│   ├── roadmap.md             →  /pm/roadmap
│   └── status-report.md       →  /pm/status-report
├── sales/                     # Sales-specific
│   ├── apply.md               →  /sales/apply
│   ├── outreach.md            →  /sales/outreach
│   └── follow-up.md           →  /sales/follow-up
└── mktg/                      # Marketing-specific
    ├── publish.md              →  /mktg/publish
    ├── campaign.md             →  /mktg/campaign
    └── analytics.md            →  /mktg/analytics
```

### Invocation Pattern

```
/kernel/session-start          ← always (shared)
/kernel/anchor                 ← always (shared)
/qa/run                        ← persona-specific
/kernel/complete               ← always (shared)
```

The kernel commands (`/kernel/*`) are persona-agnostic. The persona prefix (`/qa/*`, `/pm/*`, etc.) determines which workflow mode is active. When a persona command is invoked, the router sets `active_persona` in state before execution.

### Skills Namespace

```
.claude/skills/
├── kernel-domain-setup/       # Shared
├── task-builder/              # Shared (used by dev + pm)
├── autonomous-cycling/        # Shared
├── execute-pipeline/          # Shared
├── spawn-subagent/            # Shared
├── spawn-agent-swarm/         # Shared
├── qa-prod-test/              # QA-specific
├── qa-gap-check/              # QA-specific
├── qa-eval/                   # QA-specific
├── qa-audit-workflow/         # QA-specific
├── pm-velocity-tracker/       # PM-specific
├── pm-dependency-graph/       # PM-specific
├── sales-pipeline-tracker/    # Sales-specific
├── sales-interview-prep/      # Sales-specific
├── mktg-content-gen/          # Marketing-specific
└── mktg-seo-optimizer/        # Marketing-specific
```

Skills are prefixed with their persona name. Shared skills (task-builder, execute-pipeline) have no persona prefix. This prevents name collisions and makes ownership clear from the directory listing.

---

## Persona Routing

### How the System Switches Between Personas

Three mechanisms, checked in priority order:

1. **Explicit command prefix** — invoking `/qa/run` sets persona to `qa`
2. **Backlog tag** — `186-kernel-research-*` maps to `dev`, `175-qa-audit-*` maps to `qa`
3. **Workflow state** — `persona-active.json` remembers last active persona for `continue`

### Router Implementation

The persona router is a lightweight function, not a separate harness:

```python
# In sr_dev-gate-enforcer.py (added to existing hook)
PERSONA_MAP = {
    "kernel": "dev",    # kernel/* commands → dev persona
    "dev": "dev",
    "qa": "qa",
    "pm": "pm",
    "sales": "sales",
    "mktg": "mktg"
}

def route_persona(command_prefix):
    """Set active persona from command prefix."""
    persona = PERSONA_MAP.get(command_prefix, "dev")  # default to dev
    write_persona_state(persona)
    return persona
```

### Persona Activation Flow

```
User invokes: /qa/run
  │
  ├─ Hook detects command prefix "qa"
  ├─ Sets persona-active.json: { "active": "qa" }
  ├─ Protocol router loads qa-specific references:
  │   - .claude/skills/qa-*/
  │   - .claude/lessons/qa_lessons.md (if exists)
  │   - .claude/state/persona/qa_workflow.json
  └─ Executes qa/run.md command
```

### Protocol Handling

The shared protocol (`sr_dev-protocol.md`) uses a **references section per persona**:

```markdown
## Persona References

### Developer (default)
| Reference | File |
|-----------|------|
| Build Command | `.claude/skills/build-command/SKILL.md` |
| Design Command | `.claude/skills/design-command/SKILL.md` |

### QA
| Reference | File |
|-----------|------|
| Prod Test | `.claude/skills/qa-prod-test/SKILL.md` |
| Gap Check | `.claude/skills/qa-gap-check/SKILL.md` |

### PM
| Reference | File |
|-----------|------|
| Velocity Tracker | `.claude/skills/pm-velocity-tracker/SKILL.md` |
```

During `/kernel/anchor`, the agent reads the shared protocol AND the active persona's reference section. It only internalizes the relevant persona's skills and rules.

---

## State Isolation Strategy

### Scoped State Files

State isolation within the shared repo uses a **per-persona state directory**:

```
.claude/state/
├── session_state.json              # Shared: session lifecycle, anchor token, etc.
├── sr_dev_workflow.json            # Shared: kernel workflow (anchored, actions_since_anchor)
├── persona-active.json             # Router: { "active": "qa", "timestamp": "..." }
└── persona/
    ├── dev_workflow.json           # Dev: completed_tasks, cycling state, etc.
    ├── qa_workflow.json            # QA: test results, coverage, audit state
    ├── pm_workflow.json            # PM: roadmap state, velocity metrics
    ├── sales_workflow.json         # Sales: pipeline state, application tracking
    └── mktg_workflow.json          # Mktg: content queue, SEO scores
```

### What's Shared vs. Scoped

| State | Scope | File | Rationale |
|-------|-------|------|-----------|
| Session lifecycle | Shared | `session_state.json` | One session, one agent, one lifecycle |
| Anchor counter | Shared | `sr_dev_workflow.json` | Anchoring is a kernel behavior, not persona-specific |
| Protocol hash | Shared | `session_state.json` | One protocol file, one hash |
| Completed tasks | Per-persona | `persona/{name}_workflow.json` | Each persona has its own task queue |
| Cycling state | Per-persona | `persona/{name}_workflow.json` | Cycling is per-task-folder, per-persona |
| Lessons | Per-persona | `persona/{name}_lessons.md` OR shared `lessons.md` | See Lessons Strategy below |
| Metrics | Per-persona | `persona/{name}_metrics.json` | Each persona tracks its own outcomes |

### Lessons Strategy: Hybrid

Two lesson tiers:

1. **Shared lessons** (`lessons.md`) — kernel-level rules that apply to ALL personas (RULE ZERO, anchor discipline, cd prohibition, etc.). These are read during every anchor regardless of persona.

2. **Persona lessons** (`persona/{name}_lessons.md`) — persona-specific failures and fixes. QA learns about test flakiness. Sales learns about form-filling edge cases. These are read during anchor only when that persona is active.

During `/kernel/anchor`:
```
Read: .claude/lessons/lessons.md              ← always
Read: .claude/state/persona/{active}_lessons.md  ← if active persona has lessons
```

During `/kernel/learn`:
```
If failure is kernel-level → write to lessons.md
If failure is persona-specific → write to persona/{active}_lessons.md
```

### Concurrent Execution

For concurrent persona execution (e.g., QA running while Developer works):

- Each concurrent agent gets its own `agent_id` (existing pattern)
- Agent state routes to `agent-{id}-workflow.json` (existing pattern)
- Persona state routes to `persona/{name}_workflow.json`
- No shared mutable state contention — each persona writes its own files

The existing `agent-{id}-workflow.json` pattern already solves this. Unified harness inherits the solution without additional work.

---

## Autonomous Nightly Operation Flow

```
CRON (2:00 AM)
  │
  ▼
UNIFIED HARNESS boots (single repo)
  │
  ├─ Read persona-active.json → set to "orchestrator" mode
  ├─ Read schedules.json → find nightly triggers
  │
  ├─ For each scheduled persona:
  │   │
  │   ├─ Set persona-active.json → { "active": "qa" }
  │   ├─ Spawn agent:
  │   │   env -u CLAUDECODE claude -p \
  │   │     --cwd sr_dev_workspace/ \
  │   │     "Read CLAUDE.md. Active persona: qa. Run /qa/run"
  │   ├─ Agent reads CLAUDE.md (same repo)
  │   ├─ Agent runs session-start → anchor (reads qa lessons) → /qa/run
  │   ├─ Agent writes results to persona/qa_metrics.json
  │   ├─ Agent runs /kernel/complete
  │   │
  │   ├─ Set persona-active.json → { "active": "pm" }
  │   ├─ Spawn agent for PM status-report
  │   │   (same pattern)
  │   │
  │   └─ Set persona-active.json → { "active": "dev" }
  │       Spawn agent for Developer audit-workflow
  │       (same pattern)
  │
  ├─ Read all persona/{name}_metrics.json
  ├─ Compile aggregate nightly report
  ├─ If follow_up items exist → create backlog items with persona tag
  │
  ▼
DONE (reports/nightly/YYYY-MM-DD.md)
```

Key difference from Approach A: all agents spawn in the **same repo**. No context envelope needed — the agent reads the same CLAUDE.md, same protocol, same shared lessons. Persona-specific context is loaded via the persona routing mechanism.

---

## Hook Enforcement for Multiple Personas

### Can hooks differentiate between personas?

Yes. The existing hook architecture supports this with two strategies:

**Strategy 1: Shared hooks with persona-aware logic**

```python
# sr_dev-gate-enforcer.py — existing hook, extended
def check_persona_rules(tool_name, tool_input):
    active = read_persona_state()  # reads persona-active.json

    if active == "qa":
        # QA-specific enforcement
        if tool_name == "Write" and not tool_input["path"].startswith("projects/"):
            return block("QA persona can only write to projects/ and tests/")

    if active == "sales":
        # Sales-specific enforcement
        if tool_name == "Bash" and "git push" in tool_input["command"]:
            return block("Sales persona cannot push to git")

    # Shared rules apply regardless of persona
    return check_shared_rules(tool_name, tool_input)
```

**Strategy 2: Per-persona hook files loaded conditionally**

```
.claude/hooks/
├── universal-gate-enforcer.py       # Always active
├── sr_dev-gate-enforcer.py          # Always active (shared rules)
├── qa-gate-enforcer.py              # Active only when persona=qa
├── sales-gate-enforcer.py           # Active only when persona=sales
└── mktg-gate-enforcer.py            # Active only when persona=mktg
```

**Limitation:** Claude Code loads hooks from `settings.local.json` at startup. Hooks cannot be dynamically loaded/unloaded per-persona without restarting. This means:

- **Strategy 1 is the practical choice** — one hook file with persona-aware branching
- **Strategy 2 requires all hooks to be registered** in settings.local.json at startup, with each hook checking `persona-active.json` and early-returning if it's not the active persona

Both work. Strategy 1 is simpler. Strategy 2 is cleaner for large persona-specific rule sets.

---

## Pros and Cons

### Pros

| # | Pro | Technical Rationale |
|---|-----|-------------------|
| 1 | **Zero kernel duplication** | One copy of session-start, anchor, complete, learn, fix, hooks. Kernel updates apply to all personas instantly. No sync burden, no drift. The sync problem from Approach A (75 files across 5 repos) doesn't exist. |
| 2 | **Shared infrastructure** | task-builder, execute-pipeline, run-task.sh, spawn-subagent — all shared. QA persona calls the same task-builder as Developer. No duplication, no version mismatch. |
| 3 | **Single protocol, single truth** | One `sr_dev-protocol.md` with persona-specific sections. `/kernel/anchor` reads one file. Lessons that apply everywhere are in one place. No risk of QA's protocol diverging from Developer's. |
| 4 | **Lower operational overhead** | One repo, one git history, one CI pipeline. No orchestrator repo. No context envelopes. No dispatch serialization. Persona switching is a state file update, not a repo checkout. |
| 5 | **Warm context between personas** | When QA finds a bug and creates a follow-up for Developer, the Developer agent inherits the same repo context — same file history, same lessons, same state. No lossy envelope serialization. The full investigation context is in the git log and project files. |
| 6 | **Incremental adoption** | Adding a persona = adding a command directory (`commands/pm/`), a skills directory (`skills/pm-*/`), and a state file (`persona/pm_workflow.json`). No new repo, no domain-setup, no hook registration. 10 minutes vs. 2 hours. |
| 7 | **Existing pattern match** | The sr_dev_workspace already has QA skills (prod-test, gap-check, eval), PM skills (task-builder, backlog), and Developer skills (build, design) — all in the same repo. This approach formalizes what already exists without restructuring. |
| 8 | **Cross-persona learning** | A shared `lessons.md` means a QA failure that reveals a kernel bug gets learned by ALL personas. In Approach A, the QA harness learns it but Developer doesn't — until the kernel-sync propagates (if it does). |

### Cons

| # | Con | Technical Rationale |
|---|-----|-------------------|
| 1 | **Growing command surface** | 5 personas x ~5 commands each = 25+ commands in one repo. The `commands/` directory becomes large. Tab completion and discoverability suffer. Mitigated by namespace prefixing but still a larger surface than any single-persona repo. |
| 2 | **Protocol complexity** | One protocol must serve 5 personas. Persona-specific sections grow the file. During anchor, the agent reads rules that don't apply to its current persona. Mitigated by the indexed protocol pattern (agent reads only its persona's references), but the index itself grows. |
| 3 | **Shared lessons pollution** | If lesson boundaries aren't well-maintained, QA lessons leak into the shared file and Developer reads irrelevant rules during anchor. Requires discipline: kernel-level → shared, persona-level → scoped file. The hybrid strategy mitigates this but relies on correct categorization. |
| 4 | **Hook complexity** | One gate-enforcer hook must handle rules for all personas with conditional branching. The hook file grows with each persona. Testing becomes harder — a change for QA enforcement might accidentally affect Developer. Strategy 2 (per-persona hook files) mitigates this but all hooks load at startup. |
| 5 | **Blast radius** | A bad hook change affects ALL personas. In Approach A, a broken QA hook only breaks QA. Here, a syntax error in the shared gate-enforcer blocks Developer, PM, Sales, and Marketing too. Mitigated by per-persona hook files (Strategy 2), but shared hooks remain a single point of failure. |
| 6 | **State file contention (concurrent)** | If two personas run concurrently (QA + Developer), they share `session_state.json` and `sr_dev_workflow.json`. The existing `agent-{id}-workflow.json` pattern handles per-agent state, but `session_state.json` fields (anchor_token, protocol_hash) are still shared. Mitigated by the existing one-shot pattern but not fully eliminated. |
| 7 | **Identity ambiguity** | One CLAUDE.md must describe multiple personas or dynamically adjust. The agent's identity ("You are a QA engineer" vs. "You are a developer") depends on runtime state, not a static file. This could cause identity bleed — the agent applies Developer instincts during QA work. Mitigated by persona-specific protocol sections but less clean than Approach A's per-repo CLAUDE.md. |

---

## Risk Assessment

| Risk | Severity | Mitigation |
|------|----------|------------|
| Command namespace collisions | LOW | Strict prefix convention (`/qa/*`, `/pm/*`). Lint hook validates prefix uniqueness. |
| Protocol file grows too large | MEDIUM | Indexed protocol pattern already in use. Persona sections are reference tables (3-5 lines each), not inline content. Extract to `references/persona-{name}.md` if sections exceed 20 lines. |
| Shared lessons become noisy | MEDIUM | Hybrid strategy: shared lessons for kernel rules, per-persona files for domain-specific lessons. `/kernel/learn` routes automatically based on active persona. |
| Hook regression across personas | HIGH | Per-persona hook files (Strategy 2) + hook unit tests. Each persona's hook is tested in isolation. Shared hook changes require regression test across all personas. |
| Concurrent persona state contention | MEDIUM | Existing `agent-{id}-workflow.json` pattern handles per-agent state. Persona-scoped state files (`persona/{name}_workflow.json`) prevent cross-persona contention. Only `session_state.json` remains shared — acceptable for session-level fields. |
| Identity bleed between personas | LOW | Persona-specific protocol sections loaded during anchor. Clear persona activation in session state. Agent told "Active persona: qa" at dispatch time. |
