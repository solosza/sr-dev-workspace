# Spec-Led Growth (SLG)
**The Isagawa Business Model**

---

## The Core Thesis

The kernel is the platform. The spec is the product. Every new domain is just a new spec.

Most software companies build products, then find distribution. Isagawa builds a spec factory, then sells the output. The factory runs autonomously. Distribution is the only human constraint.

---

## The Stack

```
Kernel (constant)
  └── Domain Spec (variable)
          └── Governed AI Agent (output)
```

The kernel never changes. The spec encodes domain knowledge. Drop a new spec in, domain-setup runs, a governed agent exists for that domain. One command. No config. No DevOps.

**Install experience:** download repo → type domain-setup → running.

---

## The Factory

### How Specs Get Built

A meta-spec defines the objective and business context. A cycling agent reads it, identifies the next vertical, sources public domain knowledge, authors the spec, tests it, and the learn loop hardens it. No human in the loop after the meta-spec is written.

```
Meta-spec → Scoring agent → Priority queue →
Autonomous build cycle → Spec library → Distribution
```

The scoring agent derives its own criteria from business context — revenue potential, buyer accessibility, pain intensity, documentation availability. No human decides what to build next. The system does.

**Key insight:** The agent doesn't need a human domain expert to validate. It sources authoritative public documentation, builds the spec, then tests the spec against that same documentation. The learn loop catches failures. The spec self-improves.

### Production Speed

The Docker image testing spec proved the model. The cognitive architecture can produce and validate a domain spec autonomously. Speed of production is not the constraint. Distribution is.

**Strategic implication:** Build wide on autopilot. Sell narrow with focus. The factory stacks inventory while the sales motion stays concentrated on proven verticals.

---

## The Business Model

### Three Revenue Tiers

**Tier 1 — Passive (Gumroad)**
- Developer / vibe coder specs: $50
- SMB domain specs: $500–2K
- Payment via Gumroad → auto-provisions private repo access → buyer installs kernel + spec
- Zero human touchpoints after purchase

**Tier 2 — Services (LinkedIn / Trojan Horse)**
- Domain setup engagements: $15–50K
- Custom enterprise specs: $50K+
- Trojan Horse demo: build live on prospect's actual environment during the sales call
- LinkedIn Sales Navigator: Series A/B, 11–50 headcount, CTO/VP Eng, AI coding tool keywords

**Tier 3 — Community (SDD Ecosystem)**
- Teach Spec-Driven Development methodology + kernel at 50+ specs
- Community builds specs, extends the library, markets organically
- Kernel stays open source (MIT) — adoption engine
- Specs remain proprietary IP — monetization engine

### Unit Economics

- No compute costs — buyers run their own LLM infrastructure
- Isagawa licenses the governance layer only
- Cost per spec produced: near zero (autonomous build cycle)
- Margin on Tier 1: platform margin
- Margin on Tier 2: high (services + IP leverage)
- Stickiness: learn loop accumulates domain-specific lessons — switching costs compound over time

---

## The Distribution Strategy

**Channel 1: LinkedIn (Active, Now)**
- Target: CTO / VP Eng at Series A/B companies, 11–50 employees
- Signal keywords: Claude Code, Cursor, AI agents, LLM
- Message: lead with agent drift pain, not product pitch
- Conversion: Trojan Horse demo → services engagement

**Channel 2: Gumroad (Passive, Scales with Spec Library)**
- Organic discovery via GitHub stars, content, community
- Self-serve purchase → instant access → one-command install
- No sales motion required

**Channel 3: Open Source Community (Compounding, Post-50 Specs)**
- Publish kernel (MIT license) → GitHub adoption
- Teach SDD methodology → developers build their own specs
- Community extends the spec library → Isagawa stays ahead
- Developer adoption at companies → enterprise upsell path

### The Flywheel

```
LinkedIn closes services deals
  → Services engagements harden specs
      → Specs go to Gumroad
          → Gumroad drives community awareness
              → Community builds more specs
                  → Larger library → more LinkedIn proof points
```

---

## The Competitive Position

### Why Focus Wins

Anthropic vs OpenAI proved the model: OpenAI chased every vertical and consumer surface simultaneously — 42x more users, only 2.5x more revenue. Anthropic focused on enterprise and coders — 8x better revenue per user, on track to break even while OpenAI burns $9B/year.

The Isagawa read: The factory can build specs for every vertical. That's not permission to sell every vertical simultaneously. Sales capacity is one person. Focus the sales motion on verticals with proven pain, reachable buyers, and existing proof points. Let the factory run in the background.

**Current anchor verticals:** QA/testing (validated, live client), image/infrastructure testing (active client extension).

### The Moat

Not the kernel code — replicable. Not any single spec — learnable.

The moat is:

1. **Accumulated domain specs** — each one encodes judgment the cycling agent validated through real execution
2. **The learn loop corpus** — lessons accumulated across sessions that compound quality over time
3. **First-mover on SDD methodology** — teach it before anyone else names it
4. **Community network effects** — at scale, the spec library grows faster than any single team can replicate

---

## The Model Name: Spec-Led Growth

PLG (Product-Led Growth) uses the product as the primary distribution mechanism. **SLG (Spec-Led Growth)** uses the spec as the product, the installer, and the distribution mechanism simultaneously.

The spec is downloaded. The spec installs the governance layer. The spec encodes the domain knowledge. The spec improves through the learn loop. The spec is what gets shared in the community.

**One artifact does everything.**

---

## Current Status

| Layer | Status |
|---|---|
| Kernel | Shipped (MIT, open source) |
| Domain Setup | Implemented |
| Learn Loop | Implemented |
| Autonomous Build Cycle | Validated |
| QA Domain Spec | Validated, live client |
| Image Testing Spec | In progress, client interest confirmed |
| Meta-spec / Priority Factory | Designed, build queued |
| Gumroad Distribution | Designed, pending spec library |
| SDD Community | Planned, post-50 specs |

---

*Isagawa — Agent-Managed Operations — Designed by Alain Ignacio*
