# Command/Skill Pattern — Pulsia Design Pattern Analysis

## Overview

The command-skill pattern is the foundational architectural primitive of the Isagawa kernel. Every autonomous operation — from a single developer command to a multi-tenant CEO orchestrator — follows a 6-layer architecture that separates concerns between user entry, orchestration, execution, knowledge, validation, and enforcement. This document synthesizes the canonical pattern (documented in the `command-skill-pattern` design specification) into the context of Pulsia's autonomous AI platform, showing how the pattern maps to the hub-and-spoke loop composition defined in `04-architectural-blueprint.md`.

The pattern's significance for Pulsia is structural: it provides the missing implementation architecture for how each loop in the blueprint actually executes. The blueprint defines *what* the loops do and *how they communicate*; the command-skill pattern defines *how each loop is built internally*.

---

## The 6-Layer Architecture

The command-skill pattern organizes every autonomous operation into six layers, each with a single responsibility:

### Layer 1: Command

The user-facing entry point. A command defines the invocation signature, parses input, routes to its skill, and reports results. In Pulsia's architecture, each loop's command serves as the API contract between the CEO orchestrator and its primitive loops.

**Pulsia mapping:** The CEO orchestrator invokes `/company/{tenant_id}/ceo-cycle` as its command. Each primitive loop has its own command — `/company/{tenant_id}/deploy`, `/company/{tenant_id}/code-feature`, `/company/{tenant_id}/marketing`, `/company/{tenant_id}/ads`, `/company/{tenant_id}/escalate`. The `delegate-execution` step in the CEO loop calls these commands, passing tenant-scoped inputs that satisfy each primitive loop's input gate.

### Layer 2: Skill

The orchestrator layer. A skill defines the workflow (steps 1 through N), enforces phase gates between steps, manages state persistence, and calls step procedures in sequence. The skill contains the agent's identity, philosophy, vocabulary, and critical rules — everything the agent needs to behave correctly within this operation.

**Pulsia mapping:** The CEO orchestrator's skill orchestrates five steps: assess-state, select-action, delegate-execution, generate-report, and update-shared-lessons. Each primitive loop has its own skill — the feature-coding skill orchestrates analyze-codebase → generate-code → validate-output → handoff-to-deployment. The skill layer is where Pulsia's strategic reasoning lives: the CEO skill's select-action step contains the decision tree (priority scores, cost constraints, historical outcomes) that determines which primitive loop to invoke.

### Layer 3: Steps

Individual workflow procedures with defined inputs, outputs, and acceptance criteria. Each step reads its references, executes its procedure, and produces an artifact that satisfies its output gate. Steps are the atomic units of execution — they can fail independently, retry, and recover without affecting other steps.

**Pulsia mapping:** The blueprint's step definitions (assess-state, select-action, etc.) map directly to Layer 3. Each step has an `output_gate` that defines the schema its output must satisfy before the next step can proceed. For example, the deploy step's `input_gate` requires `tests_passed: true` from the run-tests step — this is a cross-step gate contract enforced at the step layer.

### Layer 4: References

Canonical examples, patterns, and templates that guide step execution. References are organized using tiered indexing: an INDEX.md points to per-step reference directories, each containing canonical examples with frontmatter (artifact_type, related_step, purpose, source, canonical_hash).

**Pulsia mapping:** In a multi-tenant system, references serve a dual purpose. Tenant-specific references capture historical performance data, brand context, and codebase patterns. Cross-tenant references capture shared lessons — the generalizable insights that Pulsia's hive-mind system distributes. The shared lessons aggregation described in `04-architectural-blueprint.md` is architecturally a cross-tenant reference layer that the CEO loop reads during its assess-state step and passes to primitive loops via their input gates.

### Layer 5: Contracts

JSON specifications that define valid artifact structure and validation rules. Each step's output has a contract with two types of validations: soft validations (content quality, checked by the agent) and mechanical validations (structural compliance, checked deterministically by hooks). One contract per step artifact. Both the agent (soft gate) and the hook (hard gate) read the same contract — single source of truth.

**Pulsia mapping:** The blueprint's `input_gate` and `output_gate` schemas are contracts. The CEO loop's cost-limit gate (`total_cost_this_cycle <= budget_remaining`) is a mechanical validation. The tenant-isolation gate (`all state reads/writes scoped to state/{tenant_id}/`) is a hard gate that blocks cross-tenant access. The ad management loop's budget-ceiling, monthly-budget, and minimum-roas gates are all mechanical validations that map to Layer 5 contracts with `severity: BLOCK`.

### Layer 6: Hooks

Hard gate enforcement implemented as Python scripts that intercept file writes and tool invocations. Hooks load contracts and run mechanical_validations deterministically — they block (severity=BLOCK) or warn (severity=WARN) based on the contract rules. Hooks are the enforcement mechanism that makes contracts non-negotiable.

**Pulsia mapping:** The blueprint's `hard_gates` section on each loop maps directly to hooks. The `no-deploy-without-tests` gate on the deployment loop is a hook that intercepts the deploy step and blocks execution unless the test report's `tests_passed` field is true. The `no-auto-resolve-critical` gate on the human escalation loop is a hook that maintains a block on critical decisions regardless of deadline expiration. In a multi-tenant deployment, hooks enforce tenant isolation by validating that every state file path contains the correct `{tenant_id}` prefix.

---

## CEO Orchestrator as Command-Skill Pattern

The CEO orchestrator loop from `04-architectural-blueprint.md` is the clearest demonstration of how the command-skill pattern scales from single-user developer tooling to autonomous business operations.

| Layer | Kernel Example | Pulsia CEO Equivalent |
|-------|---------------|----------------------|
| Command | `/kernel/anchor` | `/company/{tenant_id}/ceo-cycle` |
| Skill | `anchor.md` orchestrates read-protocol, review-work, save-state | CEO skill orchestrates assess-state, select-action, delegate-execution, generate-report, update-shared-lessons |
| Steps | Part A (refresh), Part B (review), Part C (save) | 5 steps with output gates and decision points |
| References | Protocol file, lessons file | Company background, historical decisions, shared lessons |
| Contracts | Anchor ceremony requirements (token, hash) | Input gate schema (tenant_id, metrics, budget), output gate schema (report, lesson) |
| Hooks | Universal gate enforcer, domain gate enforcer | Cost-limit hook, tenant-isolation hook |

The structural parallel is exact. The CEO loop's `select-action` step contains decision points — conditional routing to different primitive loops based on business state. This is the same mechanism as the kernel's session-start command routing to anchor vs. domain-setup based on whether a domain exists. The pattern is: read state → apply decision logic → route to appropriate sub-operation.

---

## Primitive Loops Follow the Pattern

Each of Pulsia's five primitive loops (feature-coding, marketing-automation, ad-management, autonomous-deployment, human-escalation) is itself a command-skill pattern instance:

**Feature Coding:** Command receives feature spec and codebase context → Skill orchestrates analyze → generate → validate → handoff → Contracts enforce iteration limits and cost budgets → Hooks block deployment of unvalidated code.

**Marketing Automation:** Command receives campaign type and brand context → Skill orchestrates generate → compliance-check → publish → analytics → Contracts enforce compliance rules and rate limits → Hooks block publication of non-compliant content.

**Ad Management:** Command receives ad accounts and budget → Skill orchestrates analyze → optimize → creative → bidding → Contracts enforce budget ceilings and ROAS minimums → Hooks block overspend and unprofitable expansion.

**Autonomous Deployment:** Command receives code changes and test suite → Skill orchestrates commit → test → deploy → verify → Contracts enforce the testing-before-deployment gate → Hooks block deployment without passing tests and trigger rollback on health check failure.

**Human Escalation:** Command receives blocked context and urgency → Skill orchestrates compile → notify → write-pending → check-response → Contracts enforce that critical escalations cannot auto-resolve → Hooks maintain the block until human response is received.

The pattern's value is consistency: every loop has the same internal structure regardless of what domain it operates in. A developer who understands the feature-coding loop's architecture immediately understands the ad-management loop's architecture. This consistency reduces cognitive overhead and makes the system auditable — you can inspect any loop by reading its 6 layers in order.

---

## Gate Contracts and Dual Validation in Pulsia

The command-skill pattern's dual validation model — soft gates (agent-driven content quality checks) and hard gates (hook-driven mechanical enforcement) — maps directly to Pulsia's gate architecture described in `04-architectural-blueprint.md`.

### Soft Gates in Pulsia

The CEO loop's `select-action` step applies strategic reasoning: evaluate priority scores, consider cost budget, reference historical outcomes, and apply shared lessons. This is a soft gate — the agent reads the validation rules (decision points) and the references (historical decisions, shared lessons) and makes a judgment call. If the judgment is wrong (e.g., investing in ads when engineering has critical bugs), the error is caught by the next cycle's assessment, and a lesson is recorded.

### Hard Gates in Pulsia

The deployment loop's `no-deploy-without-tests` gate is a hard gate — it mechanically checks that `tests_passed: true` exists in the test report. No agent reasoning involved; the check is deterministic. Similarly, the ad management loop's `budget-ceiling` gate mechanically verifies that `total_daily_budget <= budget_allocation.daily_max`. These are non-negotiable constraints that the agent cannot override.

### Why Both Gates Matter

| Gate Type | Catches | Pulsia Example |
|-----------|---------|---------------|
| Soft | Content is wrong but formatted correctly | CEO selects marketing when engineering has critical bugs — decision is valid format but wrong strategy |
| Hard | Format is wrong regardless of content | Deployment triggered without test report — structural violation regardless of code quality |

Neither gate alone provides sufficient safety for an autonomous business system. Soft gates catch strategic errors through agent reasoning and lesson accumulation. Hard gates catch structural violations through mechanical enforcement. Together they implement the defense-in-depth model that Pulsia's multi-tenant architecture requires.

---

## Inner/Outer Loop Design and Hub-and-Spoke Composition

The command-skill pattern supports two invocation modes that map directly to Pulsia's hub-and-spoke architecture:

**Outer loop (standalone):** A user invokes `/company/{tenant_id}/marketing` directly. The marketing skill runs all steps and returns results to the user.

**Inner loop (called by orchestrator):** The CEO orchestrator's `delegate-execution` step invokes the marketing loop as a sub-operation. The marketing skill runs the same steps but returns results to the CEO loop rather than to a user.

Same skill code works in both contexts — only the invocation path differs. This is the composability that makes Pulsia's architecture practical: you can test any primitive loop in isolation (outer loop mode) and then compose it into the CEO orchestrator (inner loop mode) without modification.

The hub-and-spoke composition from `04-architectural-blueprint.md` is the inner loop pattern applied at scale: the CEO orchestrator is the outer loop, and each primitive loop runs as an inner loop when delegated to. The feature-coding loop can itself invoke the deployment loop as an inner loop (code changes → deploy), creating a chain of inner loop calls that the CEO orchestrator initiated.

---

## The 8 Design Decisions Applied to Multi-Tenant Autonomous Systems

The command-skill pattern codifies 8 baseline design decisions. Each has specific implications for Pulsia's multi-tenant architecture:

| # | Decision | Multi-Tenant Implication |
|---|----------|------------------------|
| 1 | **Contract Chaining** — downstream declares requires (dbt pattern) | Primitive loops declare dependency on CEO loop's output gate. Deployment declares dependency on feature-coding's code changes. Chain is tenant-scoped. |
| 2 | **One Artifact Per Step** — each step produces one primary artifact | CEO's assess-state produces one assessment object. Marketing's generate-content produces one content object. Prevents conflation of concerns within steps. |
| 3 | **Canonical Reference Versioning** — hash-based tracking | Shared lessons use hash-based versioning. When a cross-tenant lesson is updated, all tenants receive the new version on their next CEO cycle. Stale references detected via hash mismatch. |
| 4 | **Dual Validation** — soft (agent) + hard (hook) on same contract | CEO applies strategic reasoning (soft) while hooks enforce cost limits and tenant isolation (hard). Same contract, two enforcement mechanisms. |
| 5 | **Contract Metadata** — dependencies + staleness + validation timestamps | Enables Pulsia to detect stale campaign data (marketing analytics older than 48h), expired decision packages (escalations past deadline), and outdated shared lessons. |
| 6 | **Learning Integration** — record lessons via /kernel/learn on violations | Pulsia's shared lessons aggregation is this decision at scale. Each loop records lessons locally; the CEO loop's update-shared-lessons step anonymizes and distributes generalizable insights across tenants. |
| 7 | **Override Handling** — project-scoped exceptions with expiry + audit trail | Tenant-scoped overrides allow individual companies to customize gate thresholds (e.g., higher ad budget ceiling, different ROAS minimum). Overrides expire and leave audit trails for compliance. |
| 8 | **Soft/Hard Gate Integration** — unified workflow, single source of truth | Every loop reads the same contract for both agent reasoning and hook enforcement. No divergence between what the agent thinks is valid and what the system enforces. |

---

## Sources

- Command/Skill Pattern design specification (`hmsa-healthcare-qa/.claude/docs/design/command-skill-pattern/`)
- Architectural Blueprint (`projects/pulsia-research/04-architectural-blueprint.md`)
- Pulsia architecture analysis (`projects/pulsia-research/02-architecture.md`)
- Harness applicability assessment (`projects/pulsia-research/03-harness-applicability.md`)
