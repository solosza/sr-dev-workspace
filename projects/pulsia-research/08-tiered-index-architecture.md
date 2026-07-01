# Tiered Index Architecture — Pulsia Design Pattern Analysis

## Overview

The tiered-index-architecture is the knowledge organization primitive of the Isagawa kernel. It provides a 3-layer system — Organization, Pre-Generation Checkpoints, and Contracts & Dual Gates — that controls how AI agents find, read, and verify information. This document synthesizes the canonical pattern (documented in the `tiered-index-architecture` design specification) into the context of Pulsia's autonomous AI platform, showing how the pattern addresses the knowledge scaling challenges inherent in a multi-tenant system serving 2,000+ companies.

The pattern's significance for Pulsia is operational: it solves the information retrieval problem that emerges when autonomous agents must navigate tenant-specific state, cross-tenant shared lessons, and domain-specific operational knowledge at scale. Without tiered indexing, Pulsia's CEO orchestrator — described in `04-architectural-blueprint.md` — cannot reliably assess tenant state because the state files become too large and too numerous for the agent to process within a single context window.

---

## The Three Layers

### Layer 1: Tiered Index (Organization)

Every file is either an **index** (points to other files) or a **payload** (contains content). Never both. Files exceeding 200 lines split into an index pointing to sub-payloads. The structure is recursive — sub-payloads that exceed 200 lines split again.

The canonical folder structure follows a consistent pattern regardless of domain:

```
[topic-name]/
├── index.md              ← INDEX (entry point, points to references)
└── references/
    ├── payload-a.md      ← PAYLOAD (focused content, under 200 lines)
    ├── payload-b.md      ← PAYLOAD
    └── payload-c.md      ← PAYLOAD
```

**Why it exists:** AI agents skim or skip large files. A 500-line protocol file causes the agent to miss critical sections and drift. Small indexed files force the agent to load exactly the context it needs — nothing more, nothing less.

**Pulsia mapping — tenant state as index/payload:** In Pulsia's multi-tenant architecture, each tenant's state lives under `state/{tenant_id}/`. At 2,000+ tenants, the CEO orchestrator's `assess-state` step (from `04-architectural-blueprint.md`) cannot read every tenant's full state in one pass. The tiered index pattern structures tenant state as:

```
state/
├── tenant-registry.json            ← INDEX (list of tenant_ids, status, last_cycle)
└── {tenant_id}/
    ├── state-index.json            ← INDEX (points to domain-specific state files)
    ├── revenue/
    │   ├── metrics.json            ← PAYLOAD (current revenue data)
    │   └── history.json            ← PAYLOAD (30-day trend)
    ├── engineering/
    │   ├── backlog.json            ← PAYLOAD (pending features/bugs)
    │   └── deployments.json        ← PAYLOAD (recent deploys)
    ├── marketing/
    │   ├── campaigns.json          ← PAYLOAD (active campaigns)
    │   └── performance.json        ← PAYLOAD (campaign metrics)
    └── ads/
        ├── accounts.json           ← PAYLOAD (Meta ad accounts)
        └── spend.json              ← PAYLOAD (budget tracking)
```

The tenant registry is the top-level index. Each tenant's `state-index.json` is a second-level index pointing to domain-specific payloads. The CEO orchestrator reads the registry first, then the tenant's state index, then only the domain payloads relevant to the current assessment. This directed navigation prevents the context window from filling with irrelevant data.

### Layer 2: Pre-Generation Checkpoints (Directed Reading)

Each step in a workflow declares exactly which files the agent must read before writing anything. This is not a suggestion — it's a reading list that prevents the agent from generating output from memory instead of from current data.

The checkpoint format:

```markdown
### Step N: [Step Name]

**Pre-generation checkpoint:**
- Read canonical reference: `references/step-N/[example-file]`
- Read contract: `contracts/step-N-[artifact]-contract.json`
- Read [input from prior step]
```

**Why it exists:** Layer 1 organizes files into small payloads, but organization alone doesn't tell the agent *which* files to read for a given task. Without checkpoints, the agent either reads everything (wasting context), guesses (picks wrong files), or reads from memory (hallucinates details).

**Pulsia mapping — CEO assess-state as checkpoint pattern:** The CEO orchestrator's `assess-state` step from `04-architectural-blueprint.md` is architecturally a pre-generation checkpoint. Before the CEO can select an action, it must read:

1. **Tenant state index** — `state/{tenant_id}/state-index.json` (which domains have updated data)
2. **Revenue metrics** — `state/{tenant_id}/revenue/metrics.json` (current business health)
3. **Pending bugs** — `state/{tenant_id}/engineering/backlog.json` (critical issues)
4. **Active campaigns** — `state/{tenant_id}/marketing/performance.json` (marketing ROI)
5. **Ad spend** — `state/{tenant_id}/ads/spend.json` (budget status)
6. **Shared lessons** — `shared-lessons/index.json` → relevant lesson payloads (cross-tenant insights)
7. **Historical decisions** — `state/{tenant_id}/decisions/history.json` (what worked before)

This reading list is the CEO's checkpoint. If the CEO skips reading revenue metrics, its action selection will be uninformed. If it reads from memory instead of from the current file, it will act on stale data. The checkpoint makes the reading explicit and auditable — you can verify that the CEO read the right files by checking the reading log.

Each primitive loop has its own checkpoint. The ad management loop's `analyze-performance` step must read Meta API metrics, budget allocation, and shared ads lessons before optimizing targeting. The marketing loop's `generate-content` step must read brand context, historical campaign performance, and shared marketing lessons before creating content. Every step declares its reading list; every reading list references specific payloads organized by Layer 1.

### Layer 3: Contracts & Dual Gates (Enforcement)

Contracts define what "correct" looks like. Two validation gates — soft (agent-driven) and hard (hook-driven) — both read the same contract JSON to validate every artifact.

**Soft gate:** The agent validates its own output against the contract's `soft_validation_rules` before writing. Catches semantic errors — content that has the right format but wrong substance.

**Hard gate:** A hook intercepts the write operation and applies `mechanical_validations` (regex, file checks, counts). Catches structural errors — missing headers, wrong patterns, format violations.

**Why it exists:** Layers 1 and 2 organize files and direct reading, but without enforcement the agent can skip the reading list and generate from memory. Contracts make validation declarative (JSON-driven, not hardcoded). Gates make validation mandatory (writes blocked until validation passes).

**Pulsia mapping — gate contracts from the blueprint:** The `04-architectural-blueprint.md` already specifies gate contracts at every loop boundary. The tiered-index-architecture pattern shows that these gates are instances of a deeper pattern:

| Blueprint Gate | Layer 3 Type | Validation |
|---------------|-------------|------------|
| CEO `cost-limit` | Hard gate | `total_cost_this_cycle <= budget_remaining` — mechanical, deterministic |
| CEO `tenant-isolation` | Hard gate | Path validation: all state I/O scoped to `state/{tenant_id}/` |
| Deploy `no-deploy-without-tests` | Hard gate | `tests_passed: true` in test report — structural check |
| Feature `iteration-limit` | Hard gate | `iteration_count <= max_iterations` — counter check |
| Marketing `compliance-required` | Hard gate | `compliance_passed: true` — blocks publication without compliance |
| CEO `select-action` decision tree | Soft gate | Agent applies strategic reasoning to priority scores — content quality |
| Feature `validate-output` | Soft gate | Agent checks generated code against acceptance criteria — semantic |
| Ad `optimize-targeting` | Soft gate | Agent evaluates ROAS and applies shared lessons — judgment call |

The dual gate model maps directly to Pulsia's safety architecture. Hard gates enforce non-negotiable constraints (budget limits, tenant isolation, test requirements) that no agent reasoning can override. Soft gates enforce quality standards (strategic correctness, code quality, targeting effectiveness) through agent judgment informed by shared lessons and historical data.

---

## Multi-Tenant State and Tiered Indexing at Scale

### The 200-Line Threshold at 2,000+ Tenants

The 200-line threshold rule has specific implications for Pulsia's scale. A single tenant's state is manageable — perhaps 50 lines of metrics, 30 lines of backlog, 20 lines of campaign data. But the system-wide views that the CEO orchestrator and the shared lessons aggregation require become unmanageable without tiered indexing:

**Tenant registry problem:** A flat list of 2,000 tenants with their status, last cycle timestamp, and summary metrics is 4,000+ lines. The tiered index solution: split the registry into regional or industry indices, each under 200 lines. The top-level registry becomes an index pointing to regional/industry payloads.

**Shared lessons problem:** At 10,000 companies generating 5 lessons per week, the lessons corpus reaches 50,000+ entries within a year. A flat `shared-lessons.json` is useless — the agent cannot load or search it within a context window. The tiered index solution:

```
shared-lessons/
├── index.json                     ← INDEX (topic categories, freshness scores)
├── engineering/
│   ├── index.json                 ← INDEX (subtopics: testing, deployment, security)
│   ├── testing-patterns.json      ← PAYLOAD (lessons about test strategies)
│   └── deployment-failures.json   ← PAYLOAD (lessons about deploy errors)
├── marketing/
│   ├── index.json                 ← INDEX (subtopics: email, social, content)
│   ├── email-optimization.json    ← PAYLOAD (email campaign lessons)
│   └── social-timing.json         ← PAYLOAD (social media posting lessons)
└── ads/
    ├── index.json                 ← INDEX (subtopics: targeting, creative, bidding)
    ├── targeting-strategies.json   ← PAYLOAD (audience targeting lessons)
    └── budget-allocation.json      ← PAYLOAD (spend optimization lessons)
```

The CEO orchestrator's checkpoint directs it to read the relevant lesson index first, then only the payloads matching the current tenant's domain needs. A tenant with critical engineering bugs gets engineering lessons loaded; a tenant with declining ad ROAS gets ads lessons loaded. The agent never reads the full 50,000-entry corpus — it reads the 50-entry payload that matches its current assessment.

### Tenant State Isolation as Index/Payload

The `04-architectural-blueprint.md` specifies that all state reads and writes are scoped to `state/{tenant_id}/`. This tenant isolation requirement maps directly to Layer 1's organization pattern:

- **The tenant registry is an index** — it lists all tenants and their metadata, points to each tenant's state directory. It does not contain state data.
- **Each tenant's state is a set of payloads** — scoped, focused, under 200 lines per file. The CEO orchestrator navigates index → tenant → domain → payload to read exactly the data it needs.
- **Cross-tenant operations use a separate index** — shared lessons, system metrics, and platform-wide configuration have their own index/payload trees that are never mixed with tenant state.

This separation ensures tenant isolation by design rather than by policy. The hard gate that enforces `state/{tenant_id}/` path scoping is Layer 3 enforcement of Layer 1 organization.

---

## Anti-Patterns Applied to Autonomous Platform Design

The tiered-index-architecture specification identifies six anti-patterns. Each has specific failure modes in Pulsia's multi-tenant context:

| Anti-Pattern | Kernel Failure | Pulsia Failure |
|-------------|---------------|----------------|
| File is both index AND payload | Grows unbounded, agent skims | Tenant state-index.json starts accumulating metrics inline → becomes 500 lines → CEO skims and misses critical bugs |
| Flat directory with 10+ files | Hard to scan | `state/{tenant_id}/` with 15 loose JSON files → CEO reads wrong file → acts on stale campaign data instead of current metrics |
| Duplicating content across files | Drift, contradictions | Shared lesson appears in both `engineering/testing-patterns.json` and `ads/budget-allocation.json` → diverges after updates → CEO gets contradictory advice |
| Payload over 200 lines | Agent loses context | Tenant's `backlog.json` grows to 400 lines after 6 months → CEO's assess-state step skims the middle → misses month-old P1 bug |
| Index without checkpoints | Agent browses randomly | CEO has well-organized tenant state but no reading list → reads revenue but skips engineering → deploys marketing while production is down |
| Checkpoints without contracts | No enforcement | CEO reads correct state but no validation → generates report with stale metrics → user receives inaccurate morning email |

The anti-pattern table demonstrates that tiered indexing is not optional polish for Pulsia — it is structural infrastructure that prevents cascading failures in autonomous decision-making. Each anti-pattern, left uncorrected, produces a failure that compounds over cycles: the CEO makes a bad decision → records a misleading lesson → distributes the bad lesson to other tenants → systemic error propagation.

---

## Connection to the Harness Design Pattern

The tiered-index-architecture is one of three core design patterns that define how the harness primitive operates internally. While the command-skill pattern (see `07-command-skill-pattern.md`) defines the 6-layer execution architecture and the loop architecture defines the execution lifecycle, the tiered-index-architecture defines how knowledge is organized, accessed, and validated at every layer.

In the harness model, the agent IS the runtime — it reads specifications and executes them. Tiered indexing ensures those specifications remain readable at scale. Without it, the harness pattern breaks at exactly the point Pulsia needs it most: when the number of tenants, lessons, and state files exceeds what an agent can hold in a single context window.

The three patterns are complementary:
- **Command-skill pattern** → *how each loop is built* (structure)
- **Tiered-index-architecture** → *how each loop finds and reads its knowledge* (navigation)
- **Loop architecture** → *how each loop executes and persists across sessions* (lifecycle)

---

## Sources

- Tiered Index Architecture design specification (`hmsa-healthcare-qa/.claude/docs/design/tiered-index-architecture/`)
- Architectural Blueprint (`projects/pulsia-research/04-architectural-blueprint.md`)
- Command/Skill Pattern analysis (`projects/pulsia-research/07-command-skill-pattern.md`)
- Pulsia architecture analysis (`projects/pulsia-research/02-architecture.md`)
