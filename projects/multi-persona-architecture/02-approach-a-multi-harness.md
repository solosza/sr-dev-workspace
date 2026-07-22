# Approach A: Multi-Harness Architecture

**Task:** 002-research-approach-a-multi-harness
**Date:** 2026-07-07

---

## Architecture Diagram

```
                    ┌─────────────────────────────┐
                    │     ORCHESTRATOR HARNESS     │
                    │   .claude/orchestrator/      │
                    │                             │
                    │  ┌─────────────────────┐    │
                    │  │ Dispatch Engine      │    │
                    │  │ - Backlog scanner    │    │
                    │  │ - Priority algorithm │    │
                    │  │ - Persona selector   │    │
                    │  │ - Context builder    │    │
                    │  └─────────┬───────────┘    │
                    │            │                 │
                    └────────────┼─────────────────┘
                                 │
              ┌──────────────────┼──────────────────┐
              │                  │                   │
    ┌─────────▼──────┐ ┌────────▼───────┐ ┌────────▼───────┐
    │  DEVELOPER      │ │  QA            │ │  SALES         │
    │  HARNESS        │ │  HARNESS       │ │  HARNESS       │
    │  (repo: kernel) │ │  (repo: qa)    │ │  (repo: sales) │
    │                 │ │                │ │                │
    │ protocol.md     │ │ protocol.md    │ │ protocol.md    │
    │ commands/       │ │ commands/      │ │ commands/      │
    │ skills/         │ │ skills/        │ │ skills/        │
    │ hooks/          │ │ hooks/         │ │ hooks/         │
    │ state/          │ │ state/         │ │ state/         │
    │ lessons/        │ │ lessons/       │ │ lessons/       │
    └────────────────┘ └────────────────┘ └────────────────┘
              │                  │                   │
    ┌─────────▼──────┐ ┌────────▼───────┐ ┌────────▼───────┐
    │  PM             │ │  MARKETING     │ │  (future)      │
    │  HARNESS        │ │  HARNESS       │ │  HARNESS       │
    │  (repo: pm)     │ │  (repo: mktg)  │ │  (repo: ??)    │
    │                 │ │                │ │                │
    │ protocol.md     │ │ protocol.md    │ │ protocol.md    │
    │ commands/       │ │ commands/      │ │ commands/      │
    │ skills/         │ │ skills/        │ │ skills/        │
    │ hooks/          │ │ hooks/         │ │ hooks/         │
    │ state/          │ │ state/         │ │ state/         │
    │ lessons/        │ │ lessons/       │ │ lessons/       │
    └────────────────┘ └────────────────┘ └────────────────┘
```

Each persona is a **separate repo** with its own full `.claude/` harness (protocol, commands, skills, hooks, state, lessons). The orchestrator harness sits above them and dispatches work.

---

## What Each Persona Harness Contains

Every harness repo follows the same directory structure:

```
persona-repo/
├── .claude/
│   ├── protocols/
│   │   └── {persona}-protocol.md       # Persona-specific protocol
│   ├── commands/
│   │   └── kernel/                     # Standard kernel commands (inherited)
│   │   └── {persona}/                  # Persona-specific commands
│   ├── skills/
│   │   └── {persona-skill-1}/         # Persona-specific skills
│   │   └── {persona-skill-2}/
│   ├── hooks/
│   │   └── universal-gate-enforcer.py  # Shared (copied from kernel)
│   │   └── {persona}-gate-enforcer.py  # Persona-specific enforcement
│   ├── state/
│   │   └── session_state.json
│   │   └── {persona}_workflow.json
│   └── lessons/
│       └── lessons.md                  # Persona-specific lessons
├── CLAUDE.md                           # Persona identity + loop definition
└── run-task.sh                         # Standard task runner
```

### Per-Persona Contents

| Persona | Commands | Skills | Hooks |
|---------|----------|--------|-------|
| **Developer** | session-start, anchor, complete, learn, fix, backlog, execute-pipeline | domain-setup, task-builder, autonomous-cycling, build-command, design-command, spawn-subagent, spawn-agent-swarm | universal-gate, sr_dev-gate, actions-log, test-failure |
| **QA** | qa-run, qa-schedule, qa-report | prod-test, gap-check, review-queue, eval, audit-workflow, human-check, reference-scanner | universal-gate, qa-gate, coverage-enforcer |
| **PM** | prioritize, roadmap, status-report | task-builder (shared), velocity-tracker, dependency-graph, milestone-planner | universal-gate, pm-gate, deadline-enforcer |
| **Sales** | job-apply, outreach, follow-up | pipeline-tracker, interview-prep, proposal-gen, crm-sync | universal-gate, sales-gate, response-tracker |
| **Marketing** | publish, campaign, analytics | website-cloner, content-gen, seo-optimizer, social-scheduler | universal-gate, mktg-gate, brand-enforcer |

---

## Orchestrator Design

### How the Orchestrator Knows What the Company Needs

The orchestrator reads from three sources:

1. **Backlog queue** — `docs/backlog/*.md` files, each tagged with a persona prefix (`kernel-`, `qa-`, `domain-`, etc.). Existing convention already does this.
2. **Metrics/signals** — Each persona harness writes a `state/metrics.json` after each run with outcomes (tests passed, applications submitted, content published). The orchestrator reads these.
3. **Schedule** — A `schedules.json` config defines recurring operations:
   ```json
   {
     "nightly": [
       { "persona": "qa", "command": "qa-run", "trigger": "cron:0 2 * * *" },
       { "persona": "pm", "command": "status-report", "trigger": "cron:0 8 * * 1" }
     ],
     "on_commit": [
       { "persona": "qa", "command": "qa-run", "trigger": "git:post-commit" }
     ]
   }
   ```

### Dispatch Logic

```
ORCHESTRATOR DISPATCH:

1. Read backlog queue (sorted by priority)
2. For each backlog item:
   a. Parse persona tag from backlog prefix
   b. Map persona → harness repo path
   c. Build context envelope (see State Schema below)
   d. Spawn agent:
      env -u CLAUDECODE claude -p \
        --cwd {harness_repo_path} \
        "Read CLAUDE.md, execute task: {task_description}" \
        < context_envelope.json
   e. Wait for completion (poll state/workflow.json)
   f. Read results from state/metrics.json
   g. Update orchestrator state with outcome
3. If scheduled trigger fires:
   a. Identify persona + command from schedules.json
   b. Same dispatch as above
4. Report aggregate results
```

### Persona Selection Algorithm

```python
def select_persona(backlog_item):
    # Explicit tag takes priority
    if backlog_item.prefix in PERSONA_MAP:
        return PERSONA_MAP[backlog_item.prefix]

    # Keyword matching fallback
    keywords = {
        "developer": ["build", "refactor", "fix", "kernel"],
        "qa": ["test", "audit", "verify", "compliance"],
        "pm": ["plan", "roadmap", "prioritize", "milestone"],
        "sales": ["apply", "outreach", "pitch", "proposal"],
        "marketing": ["content", "publish", "seo", "campaign"]
    }
    return best_keyword_match(backlog_item.title, keywords)
```

---

## State Schema for Inter-Harness Communication

### Context Envelope (Orchestrator → Persona)

Passed at dispatch time. The persona harness reads this to understand its assignment.

```json
{
  "envelope_version": "1.0",
  "dispatch_id": "uuid-v4",
  "timestamp": "ISO-8601",
  "source": "orchestrator",
  "target_persona": "qa",
  "task": {
    "backlog_id": 175,
    "title": "QA audit SSH platform 5-layer compliance",
    "type": "RESEARCH",
    "description": "...",
    "acceptance_criteria": ["..."]
  },
  "context": {
    "prior_results": [
      {
        "dispatch_id": "prev-uuid",
        "persona": "developer",
        "outcome": "complete",
        "deliverables": ["path/to/file.md"],
        "notes": "Built SSH platform, needs QA pass"
      }
    ],
    "shared_state": {
      "active_repos": ["isagawa-kernel", "isagawa-qa-platform"],
      "current_sprint": "2026-W27",
      "blockers": []
    }
  }
}
```

### Result Envelope (Persona → Orchestrator)

Written by the persona harness after completion. The orchestrator reads this.

```json
{
  "envelope_version": "1.0",
  "dispatch_id": "uuid-v4",
  "timestamp": "ISO-8601",
  "persona": "qa",
  "outcome": "complete | failed | blocked",
  "deliverables": ["projects/ssh-5-layer-audit/report.md"],
  "metrics": {
    "tests_run": 24,
    "tests_passed": 22,
    "tests_failed": 2,
    "coverage": 0.92
  },
  "lessons_added": 1,
  "follow_up": {
    "persona": "developer",
    "task": "Fix 2 failing SSH compliance tests",
    "priority": "high"
  }
}
```

### Shared State Directory

```
orchestrator-repo/
├── state/
│   ├── dispatch-log.jsonl          # Append-only log of all dispatches
│   ├── persona-registry.json       # Maps persona → repo path
│   ├── schedules.json              # Recurring triggers
│   └── envelopes/
│       ├── {dispatch-id}-request.json
│       └── {dispatch-id}-result.json
```

---

## Autonomous Nightly Operation Flow

```
CRON (2:00 AM)
  │
  ▼
ORCHESTRATOR boots
  │
  ├─ Read schedules.json → find nightly triggers
  │
  ├─ QA: spawn agent → qa-harness-repo
  │   └─ Run qa-run → prod-test all repos → gap-check → report
  │   └─ Write result envelope
  │
  ├─ PM: spawn agent → pm-harness-repo
  │   └─ Run status-report → read all persona metrics → compile
  │   └─ Write result envelope
  │
  ├─ Developer: spawn agent → kernel-repo
  │   └─ Run audit-workflow → check kernel integrity
  │   └─ Write result envelope
  │
  ├─ Read all result envelopes
  ├─ If follow_up items exist → queue as new backlog
  ├─ Write aggregate nightly report
  │
  ▼
DONE (results in orchestrator/reports/nightly/YYYY-MM-DD.md)
```

---

## Pros and Cons

### Pros

| # | Pro | Technical Rationale |
|---|-----|-------------------|
| 1 | **Complete state isolation** | Each persona has its own `session_state.json`, `workflow.json`, and `lessons.md`. Zero contention — the state contention bug (lesson 2026-06-14) is architecturally impossible. No shared mutable state between personas. |
| 2 | **Independent evolution** | QA persona can add hooks, skills, and protocol rules without affecting Developer. Each persona evolves at its own pace. Version control is per-repo — no merge conflicts between persona changes. |
| 3 | **Clean persona identity** | Each repo has its own `CLAUDE.md` with a distinct identity ("You are a QA engineer", "You are a sales agent"). The agent fully inhabits one persona at a time. No identity confusion or protocol bleeding. |
| 4 | **Scalable** | Adding a new persona = creating a new repo with the standard harness structure + registering it in `persona-registry.json`. No changes to existing harnesses. O(1) addition cost. |
| 5 | **Independent lessons** | QA failures go to QA lessons. Sales failures go to Sales lessons. No cross-contamination. Each persona learns from its own mistakes without polluting others' lesson files. |
| 6 | **Fault isolation** | If the Sales harness breaks, QA and Developer continue unaffected. A broken hook in one persona doesn't block others. Each harness is a blast radius boundary. |
| 7 | **Existing pattern match** | The job-application-spec repo already works this way — separate repo, own CLAUDE.md, own commands, own domain-setup. This approach formalizes what already exists. |

### Cons

| # | Con | Technical Rationale |
|---|-----|-------------------|
| 1 | **Kernel duplication** | Every persona repo needs a copy of kernel commands (session-start, anchor, complete, learn, fix) and hooks (universal-gate-enforcer.py). 5 personas × ~15 shared files = 75 files to keep in sync. Kernel updates require propagation to all repos. |
| 2 | **Sync burden** | When kernel learns a new lesson or adds a new hook, all persona repos must be updated. No automatic propagation — requires a "kernel-sync" command or manual copy. Drift between personas is guaranteed over time. |
| 3 | **Orchestrator complexity** | The orchestrator must manage dispatch, context passing, result collection, failure handling, retries, and scheduling across 5+ repos. This is a non-trivial distributed system. Error handling (persona hangs, partial completion, cross-persona dependencies) adds significant complexity. |
| 4 | **Cross-persona context loss** | When QA finds a bug, the context must be serialized into an envelope, passed to Developer, and deserialized. The Developer persona doesn't have QA's lessons, history, or investigation context. Envelopes are lossy — they capture outcomes, not the reasoning that produced them. |
| 5 | **Repo proliferation** | 5 personas = 5 repos + 1 orchestrator = 6 repos minimum. Each needs its own domain-setup run, its own git history, its own CI. Operational overhead scales linearly with persona count. |
| 6 | **Cold start per dispatch** | Each dispatch spawns a fresh `claude -p` session in the persona repo. The agent must read CLAUDE.md, run session-start, anchor, internalize protocol — before doing any work. This adds ~30-60 seconds of overhead per dispatch. For small tasks, overhead > work. |
| 7 | **Shared skill duplication** | task-builder is used by both Developer and PM. prod-test is used by both Developer and QA. In multi-harness, these skills must be duplicated or symlinked. Symlinks break on Windows (current platform). Git submodules add complexity. |
| 8 | **Testing complexity** | Testing the orchestrator requires all persona repos to be set up and functional. Integration tests must span 6 repos. Mocking is possible but doesn't test the real dispatch path. |

---

## Risk Assessment

| Risk | Severity | Mitigation |
|------|----------|------------|
| Kernel drift between personas | HIGH | Build a `kernel-sync` command that checksums and propagates kernel files. Run weekly. |
| Orchestrator becomes bottleneck | MEDIUM | Keep orchestrator stateless (reads config, dispatches, reads results). No complex state machine. |
| Envelope format becomes insufficient | LOW | Start with v1.0 schema, add fields as needed. Backward-compatible by design (additive only). |
| Persona repos fall out of date | MEDIUM | Nightly QA audit includes "kernel version check" — each persona reports its kernel hash. |
| Windows symlink limitations | HIGH | Use file copies, not symlinks. Accept the duplication cost. |
