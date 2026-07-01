# Reddit Pain Analyzer Harness — Specification Build

## Status
Open

## Priority
High — Proof of concept for agent-driven harness architecture

## Summary

Build the **Reddit Pain Analyzer as a harness specification** (agent-driven orchestration). No code. Pure specification: commands (markdown), skills (markdown + steps), references (guidelines), gate contracts (JSON schemas), and state files (JSON).

Agent reads the specification and orchestrates autonomously. User provides subreddit URL → agent executes workflow (fetch posts → LLM analysis → export results) → returns JSON + Markdown deliverables.

**Reference:** https://redditpainanalyzer.com/?ref=aiagentslive.com (functionality cloned via agent orchestration)

## Design Documents

| Document | Purpose |
|----------|---------|
| [[127-saas-build-reddit-pain-analyzer/README]] | Overview of harness specification |
| [[127-saas-build-reddit-pain-analyzer/product-spec]] | What the harness accomplishes (inputs, outputs) |
| [[127-saas-build-reddit-pain-analyzer/harness-architecture]] | Outer loop, inner loops, agent execution flow |
| [[127-saas-build-reddit-pain-analyzer/reddit-data-pipeline]] | Skill specification: fetch Reddit posts (3 steps) |
| [[127-saas-build-reddit-pain-analyzer/ai-analysis-engine]] | Skill specification: LLM analysis (3 steps) |
| [[127-saas-build-reddit-pain-analyzer/results-processor]] | Skill specification: validation & export (3 steps) |
| [[127-saas-build-reddit-pain-analyzer/gate-contracts]] | Data contracts (JSON schemas) between phases |
| [[127-saas-build-reddit-pain-analyzer/commands-design]] | Command specifications (/analyze, /status, /export) |
| [[127-saas-build-reddit-pain-analyzer/references-design]] | Soft constraints (protocol, philosophy, guidelines) |
| [[127-saas-build-reddit-pain-analyzer/deliverables-design]] | Output specifications (JSON + Markdown format) |

## Harness Structure

```
reddit-pain-analyzer-harness/
├── .claude/
│   ├── protocols/
│   │   └── reddit-pain-analyzer-protocol.md    (INDEX of all specs)
│   │
│   ├── commands/reddit-pain/
│   │   ├── analyze.md                          (main entry point)
│   │   ├── status.md                           (check progress)
│   │   └── export.md                           (download results)
│   │
│   ├── skills/
│   │   ├── reddit-data-pipeline/
│   │   │   ├── SKILL.md                        (skill identity + step table)
│   │   │   └── references/
│   │   │       ├── step-01-validate.md         (validate subreddit)
│   │   │       ├── step-02-fetch.md            (fetch posts via Playwright)
│   │   │       ├── step-03-extract.md          (extract & clean text)
│   │   │       └── gate-contracts.json
│   │   │
│   │   ├── ai-analysis-engine/
│   │   │   ├── SKILL.md
│   │   │   └── references/
│   │   │       ├── step-01-pain-points.md      (LLM identify pain points)
│   │   │       ├── step-02-ideas.md            (LLM generate ideas)
│   │   │       ├── step-03-scores.md           (LLM score potential)
│   │   │       └── gate-contracts.json
│   │   │
│   │   └── results-processor/
│   │       ├── SKILL.md
│   │       └── references/
│   │           ├── step-01-validate.md         (validate results)
│   │           ├── step-02-store.md            (store in state)
│   │           ├── step-03-export.md           (export JSON + MD)
│   │           └── gate-contracts.json
│   │
│   ├── references/
│   │   ├── autonomy-contract.md                (no pauses, agent-driven)
│   │   ├── cost-optimization.md                (budget guidelines)
│   │   ├── data-schema-patterns.md             (state file structure)
│   │   └── deliverables-format.md              (JSON + MD output)
│   │
│   ├── lessons/
│   │   └── lessons.md                          (learned patterns)
│   │
│   ├── hooks/
│   │   ├── universal-gate-enforcer.py          (validate gate contracts)
│   │   └── cost-limiter.py                     (block if cost > €0.50)
│   │
│   └── state/
│       └── reddit-pain-analyzer_workflow.json  (runtime state)
│
└── docs/
    └── (harness specification documentation)
```

**Total:** All markdown + JSON. ZERO code in harness itself.

---

## Harness Specification

### Entry Point: /reddit-pain/analyze [url]

**Specification:** `.claude/commands/reddit-pain/analyze.md`

What the agent must do:
1. Parse subreddit URL
2. Validate format
3. Initialize state
4. Call inner loop A: reddit-data-pipeline skill
5. Call inner loop B: ai-analysis-engine skill
6. Call inner loop C: results-processor skill
7. Return results.json + results.md

### Inner Loop A: reddit-data-pipeline

**Specification:** `.claude/skills/reddit-data-pipeline/SKILL.md` + step files

What the agent must do:
- Step 1: Validate subreddit (read `step-01-validate.md`)
- Step 2: Fetch posts (read `step-02-fetch.md`)
- Step 3: Extract text (read `step-03-extract.md`)

Each step has markdown instructions describing the action in English.

### Inner Loop B: ai-analysis-engine

**Specification:** `.claude/skills/ai-analysis-engine/SKILL.md` + step files

What the agent must do:
- Step 1: LLM identify pain points (read `step-01-pain-points.md`)
- Step 2: LLM generate ideas (read `step-02-ideas.md`)
- Step 3: LLM score potential (read `step-03-scores.md`)

### Inner Loop C: results-processor

**Specification:** `.claude/skills/results-processor/SKILL.md` + step files

What the agent must do:
- Step 1: Validate results (read `step-01-validate.md`)
- Step 2: Store in state (read `step-02-store.md`)
- Step 3: Export JSON + MD (read `step-03-export.md`)

### Data Contracts

**Specification:** Gate contract JSON schemas at phase boundaries

Ensure correctness between loops:
- reddit-data-pipeline → ai-analysis-engine (text validated)
- ai-analysis-engine → results-processor (ideas validated)
- results-processor → user (deliverables validated)

Each gate contract defined in `gate-contracts.json` per skill.

### References (Soft Constraints)

**Specifications:** Markdown files describing patterns

Examples:
- `autonomy-contract.md` — No pauses during execution
- `cost-optimization.md` — Keep cost below €0.50/analysis
- `data-schema-patterns.md` — How to structure state files

Agent reads these and follows them.

### Protocol (Index)

**Specification:** `.claude/protocols/reddit-pain-analyzer-protocol.md`

Links to all other specifications:
- Commands
- Skills
- References
- Lessons
- Hooks

Agent reads protocol first, then follows wikilinks.

---

## Requirements

**Phase 1: MVP Harness Specification**

Write these specifications (markdown + JSON):
- ✓ Main protocol file (index)
- ✓ Command: /reddit-pain/analyze (main entry)
- ✓ Command: /reddit-pain/status
- ✓ Command: /reddit-pain/export
- ✓ Skill: reddit-data-pipeline (3 steps)
- ✓ Skill: ai-analysis-engine (3 steps)
- ✓ Skill: results-processor (3 steps)
- ✓ Gate contracts (JSON) for all phase boundaries
- ✓ References (markdown) for autonomy, cost, data schema
- ✓ Lessons (markdown) for learned patterns
- ✓ State file schema (JSON)

**Deliverables:** All markdown + JSON files. Ready for agent to read and execute.

---

## Constraints

- **Zero code:** No Python, no JavaScript, no compiled files
- **Pure specification:** Markdown (instructions) + JSON (schemas, state)
- **Agent-driven:** Agent reads specs and orchestrates autonomously
- **No dependencies:** No libraries, no external runtime needed
- **Portable:** All files versioned in git, shareable as specification
- **Deterministic:** Same input → consistent output (barring LLM variance)

---

## Success Criteria

| Criterion | Target |
|-----------|--------|
| All commands specified | 3 markdown files created |
| All skills specified | 3 skill folders with step files |
| All gate contracts defined | JSON schemas at boundaries |
| All references written | Autonomy, cost, data patterns documented |
| Agent executes without error | Specification is unambiguous |
| Results produced | results.json + results.md generated |
| Cost tracked | Actual cost vs. estimate in state |
| State managed | Workflow state updated at each step |

---

## References

- **Harness Design Pattern:** `docs/HARNESS-DESIGN-PATTERN.md` (meta-spec)
- **Kernel Framework:** `isagawa-kernel` repo (parent implementation)
- **Example Harness:** `job-application-spec` (protocol + skills reference)

---

## Task Builder Input

- **Deliverable:** Reddit Pain Analyzer Harness Specification (MVP complete)
- **Location:** `new-repo:D:\my_ai_projects\reddit-pain-analyzer-harness`
- **Scope:** SPECIFY (write markdown + JSON, no code)
- **Constraints:**
  - ZERO runtime code
  - Pure specification (markdown + JSON)
  - Agent-executable (unambiguous instructions)
  - All phase boundaries have gate contracts
  - Delivery includes: harness repo + design docs
  - Ready for agent to execute via `/reddit-pain/analyze`

---

## What Makes This Different

| Aspect | Traditional App | Harness |
|--------|-----------------|---------|
| **Code** | Python, JavaScript, SQL | None |
| **Runtime** | Server, database, API | Agent |
| **Execution** | Request-response | State-driven loops |
| **Specification** | Implicit in code | Explicit markdown |
| **Testing** | Unit tests, integration tests | Specification + agent trace |
| **Portability** | Docker, deployment tools | Git versioning (all text) |

**Harness = Specification-first, agent-driven, zero code.**

This proves the harness pattern works and validates that **agent + specification = application.**
