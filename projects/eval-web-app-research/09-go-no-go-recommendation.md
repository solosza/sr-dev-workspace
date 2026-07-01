# Go/No-Go Recommendation: Multi-Vertical AI Testing Platform

## Decision: GO (Conditional)

We recommend proceeding with MVP development, subject to the conditions outlined below. The market opportunity is real, the technical architecture is feasible, and the differentiation is defensible. However, the recommendation is conditional on starting with a single vertical and validating the component flywheel before expanding.

## Feasibility Summary

**Technical feasibility: HIGH.** The core infrastructure exists. The Isagawa Kernel provides the execution engine, the platform specs (deepeval, ssh, selenium) provide the vertical intelligence, and the `_reference/` architecture enables dynamic component creation. The Claude Agent SDK supports containerized deployment with tool use, subagents, and persistent sessions. Container orchestration (Cloud Run) is mature and cost-effective for ephemeral workloads. No fundamental technical blockers were identified.

**Market demand: HIGH.** LLM evaluation is the fastest-growing segment — 57% of organizations have agents in production, with quality as the #1 deployment barrier. The compliance testing market is valued at $787M (2025) growing to $1.3B by 2034. The QA automation market is growing 18% annually with 80% planned enterprise adoption by 2027. BYOK is now an expected enterprise capability, not a differentiator.

**Competitive positioning: STRONG in LLM Eval, MODERATE in other verticals.** No competitor offers harness-specific testing with a self-extending component library. The dynamic component creation mechanism and kernel governance layer are genuine differentiators. In compliance and QA verticals, incumbents are better-funded but lack the AI-driven, multi-vertical architecture.

## Risk Assessment

### Risk 1: Component Curation Bottleneck (HIGH)
The flywheel depends on curated components reaching the shared library. At scale (1,000+ submissions/month), human review becomes a 25+ hour/month burden. If curation falls behind, the flywheel stalls and the moat never forms.
**Mitigation:** Strict automated quality gates (targeting 70% auto-resolution). AI-assisted review with confidence scoring. Tiered review: auto-approve >95% confidence, human review 70-95%, auto-reject <70%. Control growth by limiting free tier runs until automation matures.

### Risk 2: Cold Start Problem (HIGH)
The component library starts empty. Early users get less value because fewer existing components means more "build from scratch" runs that are slower and more expensive. Users may not return if the first experience is slow.
**Mitigation:** Pre-seed the library with components generated from the existing platform spec test suites. Run internal evaluations to build an initial component base before public launch. Target 50-100 pre-built components per vertical before opening.

### Risk 3: API Cost Unpredictability (MEDIUM)
The eval agent's Claude API usage per run varies based on artifact complexity. Complex artifacts may trigger expensive multi-step evaluations. Users with BYOK absorb their own costs, but the platform's orchestration overhead (agent running on platform's Anthropic key for non-BYOK operations) is harder to predict.
**Mitigation:** All LLM costs via BYOK — platform never subsidizes API calls. Hard timeout at 10 minutes caps maximum per-run cost. Pre-baked container images skip domain-setup compilation (reducing agent token usage by ~30%). Monitor average tokens/run and adjust pricing tiers if unit economics shift.

## Recommended First Vertical

**LLM Eval (platform-deepeval).**

This recommendation is based on convergent evidence across all research sections:

1. **Idea Validation (01):** Highest demand signals — 57% of orgs have agents in production, quality is the #1 barrier. Existing platform spec (`platform-deepeval`) means least new infrastructure required.
2. **Competitive Landscape (02):** No competitor offers harness-specific evaluation with dynamic component creation. The gap is clear and defensible.
3. **Tech Stack (03):** Claude Agent SDK is designed for exactly this use case — containerized agent execution with tool use. The eval vertical aligns naturally with the SDK's capabilities.
4. **BYOK Model (04):** Simplest BYOK for LLM Eval — users bring one Anthropic key. Compliance vertical might not need user keys at all (potential future freemium hook).
5. **Business Model (07):** LLM Eval pricing ($49/mo Pro) is positioned below competitors (DeepEval $19.99/user = more expensive for teams of 3+, LangSmith $39/user = expensive at scale).

## Estimated MVP Effort

### Team
- **1 full-stack engineer** (backend API + container pipeline + frontend)
- **1 platform/kernel engineer** (container image builds, component review workflow, Agent SDK integration)
- **Part-time designer** (submission UI + results dashboard)

### Timeline
| Phase | Duration | Deliverables |
|-------|----------|-------------|
| **Phase 1: Foundation** | 4-6 weeks | Container pipeline (submit → queue → run → results), Claude Agent SDK integration, pre-baked eval container image |
| **Phase 2: Web UI** | 3-4 weeks | Submission form, results dashboard, user accounts, API key management |
| **Phase 3: Component Flywheel** | 3-4 weeks | Automated quality gates, review queue, component library versioning |
| **Phase 4: Beta** | 2-3 weeks | Pre-seed component library, invite beta users, iterate on UX |
| **Total MVP** | **12-17 weeks** | Single-vertical (LLM Eval) platform with BYOK, component flywheel, and basic dashboard |

### Infrastructure Cost (Monthly, Post-Launch)
| Component | Estimated Cost |
|-----------|---------------|
| Cloud Run (compute) | $50-200 (scales with usage) |
| PostgreSQL (Cloud SQL) | $30-50 |
| Cloud Storage | $5-10 |
| Domain + CDN | $20 |
| Claude API (platform operations, not user BYOK) | $50-100 |
| **Total** | **$155-380/month** |

At this cost level, 4 Pro subscribers ($196/mo) covers infrastructure. Break-even at ~10 Pro users.

## Multi-Vertical Expansion Path

```
Month 0-4:   LLM Eval MVP (Phase 1-4 above)
Month 4-6:   LLM Eval beta, iterate, grow component library
Month 6-9:   Compliance Testing vertical (platform-ssh integration)
Month 9-12:  QA Generation vertical (platform-selenium integration)
Month 12+:   Code Review vertical (new platform spec required)
```

Each new vertical requires:
1. Pre-bake container image with existing platform spec (~1 week)
2. Pre-seed component library from existing test suites (~1 week)
3. Vertical-specific submission UI fields (~1 week)
4. Quality gates tuned for the vertical's component patterns (~1 week)

**Estimated effort per new vertical: 3-4 weeks** (after MVP infrastructure is built).

## Key Dependencies

1. **Backlog 157 (/kernel/eval command):** Must be designed and validated — provides the eval loop that runs inside the container. Currently designed, build in progress.
2. **Claude Agent SDK containerization:** Requires a working containerized Agent SDK setup. Reference implementation exists (github.com/receipting/claude-agent-sdk-container).
3. **Component review workflow:** Must be operational before public launch to prevent unreviewed components from entering the library.
4. **Pre-seeded component library:** At least 50 components must exist before beta users arrive to demonstrate flywheel value.

## 159 Prerequisite Gate Checklist

All 9 items from backlog 159's prerequisite gate are covered:

| # | Gate Item | Covered In | Status |
|---|-----------|-----------|--------|
| 1 | Idea validation (demand, target user, first vertical) | 01-idea-validation.md | Complete |
| 2 | Competitive landscape (per-vertical, differentiation) | 02-competitive-landscape.md | Complete |
| 3 | Tech stack recommendation (container, API, frontend/backend) | 03-tech-stack.md | Complete |
| 4 | BYOK model (key management, provider support) | 04-byok-model.md | Complete |
| 5 | Component flywheel + curation (automated gates, human review, cost) | 05-component-flywheel-curation.md | Complete |
| 6 | Security & isolation (sandboxing, abuse prevention, data retention) | 06-security-isolation.md | Complete |
| 7 | Business model (pricing, comparable benchmarks) | 07-business-model.md | Complete |
| 8 | Legal/IP (component ownership, user submission boundaries) | 08-legal-ip.md | Complete |
| 9 | Go/no-go recommendation | This document | Complete |

## MVP Scope: What's In and What's Deferred

### In (MVP)
- Single vertical: LLM Eval
- BYOK (Anthropic key required, optional OpenAI/Google for LLM-as-judge)
- Pre-baked container images on Cloud Run (gVisor sandbox)
- Submission UI + results dashboard (Next.js)
- Job queue + results storage (FastAPI + PostgreSQL)
- Automated component quality gates (pattern conformance, tests, dedup)
- Human review queue (internal team)
- Free + Pro tiers

### Deferred (Post-MVP)
- Compliance and QA verticals
- Enterprise tier (dedicated infrastructure, SLA, SSO)
- GCP Secret Manager for key management (upgrade from session-scoped)
- Firecracker microVM isolation (upgrade from gVisor)
- Community reviewer program
- AI-assisted component review
- Component library licensing/access as separate product
- On-demand domain-setup for custom platform specs

## Sources

All research sections referenced:
- [01-idea-validation.md](./01-idea-validation.md) — Demand signals, target users, first vertical recommendation
- [02-competitive-landscape.md](./02-competitive-landscape.md) — Per-vertical competitors, differentiation analysis
- [03-tech-stack.md](./03-tech-stack.md) — Container orchestration, agent execution, pipeline architecture
- [04-byok-model.md](./04-byok-model.md) — Key management, provider support, leakage prevention
- [05-component-flywheel-curation.md](./05-component-flywheel-curation.md) — Growth mechanism, quality gates, curation cost
- [06-security-isolation.md](./06-security-isolation.md) — Sandboxing, abuse prevention, data retention
- [07-business-model.md](./07-business-model.md) — Pricing benchmarks, unit economics, pricing recommendation
- [08-legal-ip.md](./08-legal-ip.md) — Component ownership, ToS, open source licensing
