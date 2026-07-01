# Loop Architecture — Pulsia Through the Lens of the Loop Primitive

## Overview

The Isagawa kernel is built on a single primitive: the **loop**. Every capability — from governance to verification to deployment — is a loop with inputs, phases, and outputs. Loops nest inside loops. Any loop can become an orchestrator by integrating other loops as inner steps. There is no other composition mechanism.

This document maps the kernel's loop architecture (documented in `loop-architecture/design.md`) to Pulsia's autonomous company operating system, showing how every component of the Pulsia blueprint is a direct instantiation of the loop primitive.

**Source:** Isagawa kernel loop architecture design doc (`loop-architecture/design.md`)
**Cross-reference:** Pulsia architectural blueprint (`04-architectural-blueprint.md`)

---

## The Loop Primitive

A loop is a unit of work with three properties:

1. **Inputs** — what it reads before executing
2. **Phases** — the steps it executes, each with its own verification
3. **Outputs** — what it produces when complete

Every loop can re-enter its own phases. A failed phase triggers a fix-and-retry cycle. A completed phase advances to the next. When all phases complete, the loop produces its output and exits.

In Pulsia's context, every business operation — coding a feature, running an ad campaign, sending a marketing email, escalating to a human — is a loop. The CEO orchestrator is a loop. Each specialized function it delegates to is a loop. The nightly cycle itself is a loop. There is nothing in Pulsia that is not a loop.

---

## The Full System View: Kernel Layers Mapped to Pulsia

The kernel defines five layers of nesting. Each layer runs inside the one above it. Here is how Pulsia's architecture maps to every layer:

```
┌─────────────────────────────────────────────────────────────────────────┐
│  KERNEL (outermost loop — governs everything)                          │
│  In Pulsia: the platform runtime itself — multi-tenant governance      │
│  session-start → anchor → WORK → complete                              │
│                                                                        │
│  ┌ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ┐   │
│    DOMAIN SETUP (one-shot compiler)                                    │
│  │ In Pulsia: tenant onboarding — each new company gets its domain │   │
│    compiled into the system                                            │
│  └ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ┘   │
│                           │                                            │
│                           ▼                                            │
│  ┌──────────────────────────────────────────────────────────────────┐  │
│  │  DOMAIN SPEC (knowledge + rules layer)                           │  │
│  │  In Pulsia: company_background, brand_context, compliance rules  │  │
│  │                                                                  │  │
│  │  ┌──────────────────────────────────────────────────────────┐   │  │
│  │  │  COMMANDS (task execution loops)                          │   │  │
│  │  │  In Pulsia: CEO orchestrator, feature-coding, marketing, │   │  │
│  │  │  ad-management, deployment, escalation                   │   │  │
│  │  │                                                          │   │  │
│  │  │  ┌──────────────────────────────────────────────────┐   │   │  │
│  │  │  │  STEPS / PHASES (innermost loops)                 │   │   │  │
│  │  │  │  In Pulsia: assess-state, select-action,          │   │   │  │
│  │  │  │  generate-content, run-tests, adjust-bidding      │   │   │  │
│  │  │  └──────────────────────────────────────────────────┘   │   │  │
│  │  └──────────────────────────────────────────────────────────┘   │  │
│  └──────────────────────────────────────────────────────────────────┘  │
│                                                                        │
│  SELF-EXTENSION: shared lessons feed back across tenants,              │
│  expanding system capability with every nightly cycle                  │
└─────────────────────────────────────────────────────────────────────────┘
```

### Layer-by-Layer Mapping

| Kernel Layer | Pulsia Equivalent | What It Provides |
|---|---|---|
| **Kernel** (outermost) | Platform runtime | Governance, anchor cycle, state persistence, tenant isolation |
| **Domain Setup** (compiler) | Tenant onboarding | Reads company background → produces protocol, hooks, commands, state scoped to `state/{tenant_id}/` |
| **Domain Spec** (knowledge) | Company configuration | Brand context, compliance rules, historical decisions, budget constraints |
| **Commands** (execution) | The six loops | CEO orchestrator, feature-coding, marketing-automation, ad-management, deployment, escalation |
| **Steps/Phases** (innermost) | Per-step verification | assess-state, select-action, generate-content, compliance-check, run-tests, adjust-bidding |

---

## The CEO Orchestrator as a Loop Composition Instance

The kernel's loop architecture states: "Any loop can become an orchestrator by integrating other loops as inner steps." The CEO orchestrator defined in the Pulsia architectural blueprint (`04-architectural-blueprint.md`) is the most direct instantiation of this principle.

The CEO loop does not execute business operations itself. It reads state, selects the highest-leverage action, and delegates to a specialized primitive loop. It is an orchestrator in exactly the way the kernel describes — it invokes inner loops at the right step and consumes their output:

```
CEO Orchestrator (ORCHESTRATOR LOOP)
  │
  ├─ Step 1: assess-state (read all tenant state)
  ├─ Step 2: select-action (strategic reasoning → pick loop)
  ├─ Step 3: delegate-execution
  │    │
  │    ├─ ══▶ feature-coding (INNER LOOP)
  │    │       reads: feature_spec, codebase_context
  │    │       produces: validated code changes
  │    │
  │    ├─ ══▶ marketing-automation (INNER LOOP)
  │    │       reads: brand_context, historical_performance
  │    │       produces: published content + analytics
  │    │
  │    ├─ ══▶ ad-management (INNER LOOP)
  │    │       reads: ad_accounts, performance_history
  │    │       produces: optimized bids + creative
  │    │
  │    ├─ ══▶ autonomous-deployment (INNER LOOP)
  │    │       reads: code_changes, test_suite
  │    │       produces: deployed application
  │    │
  │    └─ ══▶ human-escalation (INNER LOOP)
  │            reads: blocked context, urgency
  │            produces: pending decision record
  │
  ├─ Step 4: generate-report (compile morning email)
  └─ Step 5: update-shared-lessons (submit insights)
```

The CEO loop knows **when** to invoke each inner loop and **what inputs** to pass. It does not know **how** the inner loop operates. Feature-coding's three-iteration validation cycle, marketing-automation's compliance checks, ad-management's bidding algorithms — all invisible to the orchestrator. This is the loop composition contract: inputs in, outputs out, internals hidden.

---

## The Nightly CEO Cycle as a Kernel Loop Instance

The kernel loop follows a fixed pattern: `session-start → anchor → WORK → complete`. The Pulsia CEO's nightly cycle maps directly to each phase:

| Kernel Phase | CEO Nightly Cycle | What Happens |
|---|---|---|
| **session-start** | CEO wakes (cron trigger at 2 AM) | Read session state, check domain exists, resume from prior cycle |
| **anchor** | Reads all tenant state | Re-read protocol (company background, compliance rules), review prior cycle's results, check for pending escalations |
| **WORK** | Assess → Select → Delegate → Report | The strategic reasoning and delegation loop — the actual business operations |
| **complete** | Send morning report | Final gate — verify all outputs, compile results, update state for next cycle |

The anchor mechanism is especially important for Pulsia. Each nightly CEO cycle starts by re-reading the company's full state — revenue metrics, support tickets, deployment status, ad performance, pending decisions. This is not an optimization; it is the kernel's anchor pattern applied to business governance. Just as the kernel re-reads the protocol every N actions to prevent drift, the CEO re-reads business state every cycle to prevent strategic drift.

The failure path also maps directly:

```
Kernel:  violation → fix → learn → anchor
Pulsia:  failed deployment → rollback → lesson submitted → CEO re-assesses
```

When a primitive loop fails (tests don't pass, compliance check blocks, ad spend exceeds budget), the CEO loop doesn't retry blindly. The failure produces a lesson. The lesson feeds into shared knowledge. The next cycle's anchor reads the updated lessons. The system self-corrects through the same mechanism the kernel uses: fail → learn → re-read → adapt.

---

## Domain Setup as Tenant Onboarding

In the kernel, domain setup is a one-shot compiler that reads raw inputs (repository structure, domain spec) and produces runtime infrastructure (protocol, hooks, commands, state files). It runs once per domain. After that, evolution happens through the learn loop.

In Pulsia, tenant onboarding is the domain setup compiler. When a new company signs up:

1. **Reads inputs:** Company background, industry, tech stack, brand voice, budget constraints, compliance requirements
2. **Produces runtime:**
   - Protocol → company-specific rules (compliance gates, budget ceilings, escalation thresholds)
   - Hooks → mechanical enforcement (cost limits, tenant isolation, rate limiting)
   - Commands → the six loops configured for this tenant (CEO orchestrator schedule, ad platform connections, deployment targets)
   - State → tenant-scoped state directory (`state/{tenant_id}/`)
   - Lessons → empty initially, seeded from shared lessons of similar businesses

After onboarding, the company's configuration evolves through the learn loop — not by re-running onboarding. A lesson learned from a failed marketing campaign becomes a rule in the company's protocol. A discovered compliance requirement becomes a gate in the company's hooks. The system grows smarter for that specific tenant through the same mechanism the kernel uses: fix → learn → anchor reads updated rules.

---

## Self-Extension: The Hive Mind

The kernel's self-extension property is emergent: repeated kernel cycles produce new capabilities that expand what the system can do next. In Pulsia, this emergent property manifests as the **shared lessons system** — the hive mind.

Each company's loops produce lessons through operation:
- "Emoji subject lines increase email open rates by 23%" (marketing loop)
- "React component tests with shallow rendering fail on SSR — use integration tests" (feature-coding loop)
- "Meta ad audiences under 50K in tier-3 markets have CPA > $15 — not viable" (ad-management loop)

These lessons are anonymized and aggregated across tenants. When a new company onboards or an existing company enters a new market, the shared lessons provide domain knowledge that no single tenant could have generated alone. The CEO loop reads shared lessons during its anchor step and passes relevant ones to primitive loops via their input gates.

This is self-extension at a platform scale. Each tenant's nightly cycles contribute knowledge. That knowledge expands what every tenant can do in their next cycle. The system's surface area grows with every iteration — not because new code was written, but because new lessons were learned. This is exactly the kernel's self-extension pattern: `intent → execute → new capability → next intent benefits from it`.

---

## Three Properties Loops Solve

The kernel identifies three problems that loops solve and pipelines don't. Each maps directly to Pulsia's operational requirements:

### 1. Resume

A loop has state. Interrupt it anywhere, read the state, resume where you left off.

**Pulsia requirement:** The CEO cycle runs nightly. Each cycle must be independent — it cannot assume the prior cycle completed successfully. The cycle reads state files, not in-memory context. If a cycle crashes mid-execution, the next cycle reads the same state and picks up where things left off. Pending escalations persist in state files. Incomplete deployments leave rollback SHAs in state. The ad-management loop's bid adjustments survive across cycles because they're written to state, not held in memory.

### 2. Self-Correction

A loop can re-enter. Anchor re-reads the protocol. Learn updates the rules. Re-verify confirms fixes landed.

**Pulsia requirement:** Every primitive loop has retry logic and failure paths. Feature-coding retries code generation up to 3 times with validation feedback. Deployment rolls back on health check failure. Marketing revises content on compliance violations. Ad-management pauses underperforming campaigns. None of these are one-shot pipelines — they're loops that re-enter their own phases when something fails. The CEO loop itself self-corrects at the strategic level: a failed delegation in cycle N becomes a lesson that changes the priority scores in cycle N+1.

### 3. Composition

A loop is a black box with inputs and outputs. Nest it inside another loop. The outer loop doesn't care about the inner loop's internals.

**Pulsia requirement:** The hub-and-spoke architecture from the blueprint (`04-architectural-blueprint.md`) is loop composition. The CEO orchestrator calls five primitive loops. Feature-coding hands off to deployment. Any loop can call the escalation loop when a gate blocks. The composition contract is simple: pass structured inputs that satisfy the inner loop's input gate, receive structured outputs from the inner loop's output gate. No shared memory, no message buses, no event systems — just gate contracts between loops.

---

## Hub-and-Spoke: Build Standalone, Integrate Second

The kernel's composition rule is: "Build standalone first, integrate second." The Pulsia blueprint follows this exactly.

Each of the five primitive loops is self-contained:
- **Feature-coding** can run independently — give it a feature spec and a codebase, it produces validated code
- **Marketing-automation** can run independently — give it brand context and a campaign type, it produces published content
- **Ad-management** can run independently — give it ad accounts and performance history, it produces optimized bids
- **Autonomous-deployment** can run independently — give it code changes and a test suite, it deploys
- **Human-escalation** can run independently — give it a blocked context, it notifies and waits

The CEO orchestrator doesn't change any of these loops' internals. It integrates them by invoking them at the right step (delegate-execution) and consuming their outputs (execution_result, actions_taken, cost_incurred). The primitive loops don't know they're inside an orchestrator. They read inputs, produce outputs.

This is why Pulsia can scale: adding a new business capability (e.g., customer support automation, inventory management) means building a new standalone primitive loop, testing it independently, and then adding it as a new case in the CEO's `delegate-execution` step. The CEO's assessment step gains a new priority dimension. The new loop follows the same contract — input gate, phases, output gate. The composition is structural, not bespoke.

---

## Summary

| Kernel Concept | Pulsia Instantiation |
|---|---|
| Loop primitive | Every business operation is a loop |
| Outermost loop (kernel) | Platform runtime — multi-tenant governance |
| Domain setup (compiler) | Tenant onboarding — company → runtime |
| Domain spec (knowledge) | Company configuration — brand, rules, history |
| Commands (execution) | Six loops — CEO + five primitives |
| Steps (innermost) | Per-step verification within each loop |
| Orchestrator composition | CEO delegates to primitives via gate contracts |
| Build standalone, integrate second | Each primitive loop works independently |
| Self-extension | Shared lessons (hive mind) across tenants |
| Resume | State files survive across nightly cycles |
| Self-correction | Retry, rollback, re-assess at every level |
| Composition | Hub-and-spoke via input/output gate contracts |

The loop architecture is not a metaphor applied to Pulsia. It is the literal mechanism by which Pulsia operates. The CEO orchestrator calling feature-coding during its delegate-execution step is the same pattern as create-test-artifacts calling create-sit-xlsx during its Step 3a. The nightly cycle is a kernel session. The morning report is `/kernel/complete`. Tenant onboarding is domain setup. Shared lessons are self-extension. Every piece of Pulsia is a loop, nested inside other loops, governed by the outermost kernel loop.

---

## Sources

- Isagawa kernel loop architecture design doc (`loop-architecture/design.md`)
- Pulsia architectural blueprint (`04-architectural-blueprint.md`)
- Pulsia company overview (`01-company-overview.md`)
- Pulsia architecture analysis (`02-architecture.md`)
