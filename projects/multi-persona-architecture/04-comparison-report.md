# Multi-Persona Architecture — Comparison Report

**Task:** 004-build-comparison-report
**Date:** 2026-07-07
**Sources:** 01-existing-infrastructure.md, 02-approach-a-multi-harness.md, 03-approach-b-unified-harness.md

---

## Side-by-Side Comparison Matrix

| Dimension | Approach A: Multi-Harness | Approach B: Unified Harness | Winner |
|-----------|--------------------------|----------------------------|--------|
| **State isolation** | Complete — each persona is a separate repo with its own state files. Zero contention by architecture. | Per-persona state dirs (`persona/{name}_workflow.json`) within shared repo. `session_state.json` remains shared. Contention possible during concurrent execution. | A |
| **Complexity / maintenance** | High — 5 repos + 1 orchestrator. 75+ shared files to sync. Kernel updates require propagation to all repos. `kernel-sync` command needed. | Low — 1 repo. Kernel updates apply instantly. No sync burden, no drift. Namespace prefixing keeps things organized. | **B** |
| **Scalability (adding personas)** | O(1) per persona but heavy — new repo, domain-setup, hook registration, kernel file copy. ~2 hours per persona. | O(1) per persona and lightweight — new command dir, skill dir, state file. ~10 minutes per persona. | **B** |
| **Autonomous operation** | Orchestrator dispatches to separate repos via `claude -p`. Context envelopes serialize/deserialize state. Cold start overhead (~30-60s) per dispatch. | Same repo, persona routed via state file. No envelope serialization. Warm context — same git history, same lessons. Spawned agents read same CLAUDE.md. | **B** |
| **Code reuse vs duplication** | Heavy duplication — shared skills (task-builder, execute-pipeline) must be copied or symlinked across repos. Symlinks break on Windows. Git submodules add complexity. | Zero duplication — shared skills are referenced directly. QA calls same task-builder as Developer. | **B** |
| **Hook enforcement** | Per-repo hooks, fully isolated. A broken QA hook only breaks QA. Clean blast radius. | Shared hooks with persona-aware branching. A broken hook affects all personas. Mitigated by per-persona hook files (Strategy 2). | A |
| **Inter-persona communication** | Envelope-based (lossy). Context must be serialized, passed, deserialized. Developer doesn't see QA's investigation context — only the outcome summary. | Direct — same repo, same file system. QA findings are in project files that Developer can read directly. Full context preserved in git log. | **B** |
| **Persona identity** | Clean — each repo has its own CLAUDE.md with distinct identity. Agent fully inhabits one persona. | Runtime identity via state file. Possible identity bleed. Mitigated by persona-specific protocol sections but less clean. | A |
| **Fault isolation** | Strong — broken persona doesn't affect others. Each harness is a blast radius boundary. | Weaker — shared hook/protocol errors cascade. Per-persona hook files (Strategy 2) mitigate but don't eliminate. | A |
| **Lessons/learning** | Independent — each persona learns from own failures. No cross-contamination but also no cross-pollination. | Hybrid — shared lessons for kernel rules, per-persona files for domain-specific. Cross-persona learning automatic for kernel issues. | **B** |
| **Operational overhead** | High — 6 repos, 6 git histories, 6 CI pipelines. Orchestrator is a non-trivial distributed system. | Low — 1 repo, 1 git history, 1 CI pipeline. No orchestrator needed. | **B** |
| **Existing pattern match** | Partial — job-application-spec already works this way (separate repo, own CLAUDE.md). But it's the only example. | Strong — sr_dev_workspace already has QA skills, PM skills, Developer skills in the same repo. Formalizes what exists. | **B** |

**Score: Approach A wins 3 dimensions, Approach B wins 9 dimensions.**

---

## Recommendation: Approach B (Unified Harness)

### Technical Justification

**1. The maintenance cost of Approach A is prohibitive.**

75+ shared kernel files across 5 repos creates a sync problem that grows with every kernel improvement. The kernel learns and evolves frequently (35 lessons recorded to date). Each lesson potentially changes hooks, protocol, or commands — and in Approach A, those changes must propagate to all persona repos. The `kernel-sync` command mitigates but doesn't solve: it adds operational burden and drift is guaranteed between sync runs.

**2. The existing workspace already IS Approach B.**

`sr_dev_workspace` already contains Developer skills (build-command, design-command), QA skills (prod-test, gap-check, eval, audit-workflow), PM skills (task-builder, backlog), and Marketing skills (website-cloner). These coexist in one repo under one protocol. Approach B formalizes this with namespace prefixes and persona routing — an incremental change. Approach A would require dismantling this and redistributing into 5+ repos — a disruptive restructuring.

**3. Inter-persona communication is a first-class requirement.**

The most common cross-persona flow is: Developer builds → QA tests → Developer fixes. In Approach A, this requires context envelopes (lossy serialization), cold starts, and the QA agent's investigation context is lost in translation. In Approach B, the QA agent writes findings to `projects/`, the Developer agent reads them directly — zero information loss.

**4. Windows symlink limitations make Approach A impractical.**

The current platform is Windows (MINGW64). Symlinks are unreliable. Shared skills (task-builder, execute-pipeline, run-task.sh) would need to be copied to each persona repo. Every kernel update requires copying to 5 repos. This is the exact sync burden that makes Approach A expensive.

**5. State isolation is solved without repo separation.**

The `agent-{id}-workflow.json` pattern already provides per-agent state isolation. Adding `persona/{name}_workflow.json` extends this to per-persona isolation within the same repo. The state contention lesson (2026-06-14) is addressed by the existing per-agent pattern, not by repo separation.

**6. Approach A's advantages are mitigatable in Approach B.**

- **Fault isolation** → Per-persona hook files (Strategy 2) contain blast radius
- **Persona identity** → Persona-specific protocol sections + `Active persona: X` at dispatch
- **State isolation** → Per-persona state dirs + existing agent-{id} pattern

Approach B's disadvantages (growing command surface, protocol complexity) are manageable with the indexed protocol pattern already in use.

---

## Implementation Roadmap

### Phase 1: Persona Infrastructure (Foundation)

Build the routing and state infrastructure that enables persona switching.

| Step | Action | Files |
|------|--------|-------|
| 1.1 | Create persona state directory | `.claude/state/persona/` |
| 1.2 | Create persona-active state file | `.claude/state/persona-active.json` |
| 1.3 | Add persona routing to gate enforcer | `.claude/hooks/sr_dev-gate-enforcer.py` — add `route_persona()` function that reads command prefix and sets active persona |
| 1.4 | Add persona sections to protocol | `.claude/protocols/sr_dev-protocol.md` — add `## Persona References` with per-persona skill/command tables |
| 1.5 | Update anchor to read persona lessons | `.claude/commands/kernel/anchor.md` — add step: "Read persona/{active}_lessons.md if exists" |
| 1.6 | Update learn to route lessons | `.claude/commands/kernel/learn.md` — add routing: kernel-level → shared, persona-specific → `persona/{active}_lessons.md` |

**Prerequisite:** None. This is pure infrastructure.
**Blocker:** None.

### Phase 2: QA Persona (First Persona Build)

QA is ~60% complete (most skills exist). Build the remaining orchestration.

| Step | Action | Files |
|------|--------|-------|
| 2.1 | Create QA command directory | `.claude/commands/qa/` |
| 2.2 | Build `/qa/run` command | `.claude/commands/qa/run.md` — sequences: prod-test → gap-check → eval → report |
| 2.3 | Build `/qa/report` command | `.claude/commands/qa/report.md` — aggregates test results, coverage, audit findings |
| 2.4 | Create QA state file | `.claude/state/persona/qa_workflow.json` |
| 2.5 | Create QA lessons file | `.claude/state/persona/qa_lessons.md` |
| 2.6 | Rename QA skills with prefix | `qa-prod-test/`, `qa-gap-check/`, `qa-eval/`, `qa-audit-workflow/` (or keep current names and register in persona section) |

**Prerequisite:** Phase 1 complete.
**Blocker:** None.

### Phase 3: PM Persona

PM is ~30% complete. Build prioritization and roadmap capabilities.

| Step | Action | Files |
|------|--------|-------|
| 3.1 | Create PM command directory | `.claude/commands/pm/` |
| 3.2 | Build `/pm/prioritize` command | `.claude/commands/pm/prioritize.md` — reads backlog, applies priority algorithm, outputs ranked list |
| 3.3 | Build `/pm/roadmap` command | `.claude/commands/pm/roadmap.md` — generates roadmap from backlog + completed work |
| 3.4 | Build `/pm/status-report` command | `.claude/commands/pm/status-report.md` — reads all persona metrics, compiles weekly status |
| 3.5 | Create PM state + lessons files | `.claude/state/persona/pm_workflow.json`, `pm_lessons.md` |

**Prerequisite:** Phase 1 complete.
**Blocker:** Velocity management research (backlog 181) informs prioritization algorithm.

### Phase 4: Sales Persona

Sales is ~20% complete. Extend job-apply with pipeline management.

| Step | Action | Files |
|------|--------|-------|
| 4.1 | Create Sales command directory | `.claude/commands/sales/` |
| 4.2 | Build `/sales/apply` command | `.claude/commands/sales/apply.md` — wraps existing job-apply from job-application-spec |
| 4.3 | Build `/sales/pipeline` command | `.claude/commands/sales/pipeline.md` — CRM-like tracking of applications, stages, follow-ups |
| 4.4 | Build `/sales/follow-up` command | `.claude/commands/sales/follow-up.md` — scan pipeline for overdue follow-ups, generate outreach |
| 4.5 | Create Sales state + lessons files | `.claude/state/persona/sales_workflow.json`, `sales_lessons.md` |

**Prerequisite:** Phase 1 complete.
**Blocker:** job-application-spec repo integration (how does /sales/apply delegate to the external repo?).

### Phase 5: Marketing Persona

Marketing is ~10% complete. Build content and deployment pipeline.

| Step | Action | Files |
|------|--------|-------|
| 5.1 | Create Marketing command directory | `.claude/commands/mktg/` |
| 5.2 | Build `/mktg/publish` command | `.claude/commands/mktg/publish.md` — content review + site deployment |
| 5.3 | Build `/mktg/content` command | `.claude/commands/mktg/content.md` — generate blog posts, case studies, technical articles |
| 5.4 | Create Marketing state + lessons files | `.claude/state/persona/mktg_workflow.json`, `mktg_lessons.md` |

**Prerequisite:** Phase 1 complete.
**Blocker:** isagawa.co site deployment pipeline (backlogs 135-140).

### Phase 6: Nightly Orchestration

Once personas are operational, add scheduled autonomous operation.

| Step | Action | Files |
|------|--------|-------|
| 6.1 | Create schedules config | `.claude/state/schedules.json` — persona + command + cron trigger |
| 6.2 | Build orchestrator script | `run-nightly.sh` — reads schedules, spawns persona agents sequentially |
| 6.3 | Build aggregate report command | `.claude/commands/kernel/nightly-report.md` — reads all persona metrics, compiles report |

**Prerequisite:** Phases 2-5 (at least QA + PM).
**Blocker:** None.

---

## Architecture Diagram — Recommended Approach

```
┌──────────────────────────────────────────────────────────────────────┐
│                      sr_dev_workspace (Unified Harness)              │
│                                                                      │
│  ┌────────────────────────────────────────────────────────────────┐  │
│  │                    SHARED KERNEL LAYER                         │  │
│  │                                                                │  │
│  │  CLAUDE.md                    .claude/protocols/sr_dev-protocol│  │
│  │  run-task.sh                  .claude/hooks/*-gate-enforcer.py │  │
│  │  .claude/commands/kernel/*    .claude/lessons/lessons.md       │  │
│  │  .claude/state/session_state  .claude/skills/task-builder/     │  │
│  │  .claude/skills/execute-pipeline/  spawn-subagent/ cycling/   │  │
│  └──────────────────────────┬─────────────────────────────────────┘  │
│                              │                                        │
│                    ┌─────────▼──────────┐                            │
│                    │   PERSONA ROUTER    │                            │
│                    │                     │                            │
│                    │ Command prefix →    │                            │
│                    │ active persona      │                            │
│                    │                     │                            │
│                    │ persona-active.json │                            │
│                    └─────────┬──────────┘                            │
│                              │                                        │
│       ┌──────────┬───────────┼──────────┬──────────┐                 │
│       ▼          ▼           ▼          ▼          ▼                 │
│  ┌─────────┐ ┌────────┐ ┌────────┐ ┌────────┐ ┌────────┐           │
│  │   DEV   │ │   QA   │ │   PM   │ │ SALES  │ │  MKTG  │           │
│  ├─────────┤ ├────────┤ ├────────┤ ├────────┤ ├────────┤           │
│  │cmd/dev/ │ │cmd/qa/ │ │cmd/pm/ │ │cmd/    │ │cmd/    │           │
│  │skills/  │ │skills/ │ │skills/ │ │sales/  │ │mktg/   │           │
│  │build-   │ │qa-prod-│ │pm-vel- │ │sales-  │ │mktg-   │           │
│  │command/ │ │test/   │ │ocity/  │ │pipe/   │ │content/│           │
│  │design-  │ │qa-gap/ │ │pm-dep/ │ │sales-  │ │mktg-   │           │
│  │command/ │ │qa-eval/│ │pm-road/│ │interv/ │ │seo/    │           │
│  └────┬────┘ └───┬────┘ └───┬────┘ └───┬────┘ └───┬────┘           │
│       │          │          │          │          │                   │
│  ┌────▼──────────▼──────────▼──────────▼──────────▼────┐            │
│  │              .claude/state/persona/                   │            │
│  │                                                       │            │
│  │  dev_workflow.json   qa_workflow.json   pm_workflow   │            │
│  │  dev_lessons.md      qa_lessons.md      pm_lessons    │            │
│  │  sales_workflow.json  mktg_workflow.json              │            │
│  │  sales_lessons.md     mktg_lessons.md                 │            │
│  └───────────────────────────────────────────────────────┘            │
└──────────────────────────────────────────────────────────────────────┘
```

### Persona Dispatch Flow (Autonomous)

```
Nightly / Manual Trigger
  │
  ├─ Read schedules.json
  │
  ├─ For each persona trigger:
  │   │
  │   ├─ Set persona-active.json → { "active": "qa" }
  │   │
  │   ├─ env -u CLAUDECODE claude -p \
  │   │     --cwd sr_dev_workspace/ \
  │   │     "Active persona: qa. Run /qa/run"
  │   │
  │   ├─ Agent reads CLAUDE.md (shared kernel)
  │   ├─ Agent runs /kernel/session-start
  │   ├─ Agent runs /kernel/anchor (reads qa lessons + shared lessons)
  │   ├─ Agent runs /qa/run (persona-specific command)
  │   ├─ Agent writes persona/qa_workflow.json + qa_metrics.json
  │   ├─ Agent runs /kernel/complete
  │   │
  │   └─ Next persona...
  │
  ├─ Read all persona/*_metrics.json
  ├─ Compile nightly report
  │
  ▼
DONE
```

---

## State Schemas

### persona-active.json

```json
{
  "active": "qa",
  "timestamp": "2026-07-07T05:00:00Z",
  "set_by": "command_prefix",
  "previous": "dev"
}
```

### persona/{name}_workflow.json

```json
{
  "persona": "qa",
  "completed_tasks": [],
  "skipped_tasks": [],
  "cycling": false,
  "cycling_complete": false,
  "current_task": null,
  "attempts_on_current": 0,
  "last_run": null,
  "metrics": {
    "tests_run": 0,
    "tests_passed": 0,
    "tests_failed": 0,
    "coverage": null
  }
}
```

### schedules.json

```json
{
  "nightly": [
    { "persona": "qa", "command": "/qa/run", "trigger": "cron:0 2 * * *" },
    { "persona": "pm", "command": "/pm/status-report", "trigger": "cron:0 8 * * 1" }
  ],
  "on_demand": [
    { "persona": "dev", "command": "/kernel/audit-workflow", "trigger": "manual" }
  ]
}
```

---

## Key Commands (Recommended Approach)

| Command | Persona | Purpose |
|---------|---------|---------|
| `/kernel/session-start` | All | Session lifecycle (shared) |
| `/kernel/anchor` | All | Protocol refresh (shared, reads persona lessons) |
| `/kernel/complete` | All | Completion gate (shared) |
| `/kernel/learn` | All | Record lesson (routes to shared or persona file) |
| `/dev/build` | Developer | Build a feature from spec |
| `/dev/design` | Developer | Design architecture for a requirement |
| `/qa/run` | QA | Full QA pass (prod-test + gap-check + eval) |
| `/qa/report` | QA | Aggregate QA results |
| `/pm/prioritize` | PM | Rank backlog by priority algorithm |
| `/pm/roadmap` | PM | Generate roadmap from backlog |
| `/pm/status-report` | PM | Weekly status across all personas |
| `/sales/apply` | Sales | Job application (wraps job-apply) |
| `/sales/pipeline` | Sales | Application pipeline tracking |
| `/mktg/publish` | Marketing | Content review + site deployment |
| `/mktg/content` | Marketing | Generate content (blog, case study) |

---

## Migration Path from Current State

The transition from current workspace to Approach B is incremental — no big-bang restructuring:

1. **Current state → Phase 1:** Add persona routing infrastructure. Zero disruption to existing workflow. All current commands continue to work. The persona router defaults to `dev` if no persona prefix is detected.

2. **Phase 1 → Phase 2:** QA skills already exist. Adding `/qa/run` orchestrator and persona state files. Existing skills (prod-test, gap-check, eval) continue to work as-is. The only change is they can now be invoked under a QA persona context.

3. **job-application-spec repo:** Remains a separate repo for now. `/sales/apply` delegates to it via `claude -p --cwd job-application-spec/`. This is the one case where cross-repo dispatch is needed — and it's a single, well-defined integration point rather than the 5-repo mesh of Approach A.

4. **No breaking changes:** Every existing command, skill, and hook continues to work throughout the migration. Persona infrastructure is additive.
