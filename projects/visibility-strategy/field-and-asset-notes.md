# Field Context + Asset Inventory — Visibility Plan (282)

Task: 001-research-field-and-assets.md | Gate: VP-01

## 1. 2026 Field Context (re-verified live)

### Harness engineering — named the 2026 discipline
Martin Fowler and Birgitta Boeckeler (ThoughtWorks) published the definitional framework in **April 2026**: harness engineering is the discipline of designing the systems, constraints, and feedback loops around an AI agent that make it reliable in production — "everything in an AI agent except the model itself." Formula: **Agent = Model + Harness**. Faros AI's 2026 write-up frames it as the **third phase of AI-engineering maturity** (after prompt engineering, then context engineering) and names it the main focus of engineering investment in 2026. A production-grade harness has five layers: tool orchestration, verification loops, context/memory, guardrails, observability.
- Source: [Faros — Harness Engineering: Making AI Coding Agents Work in 2026](https://www.faros.ai/blog/harness-engineering) (2026)
- Source: [Cobus Greyling — The Rise of AI Harness Engineering](https://cobusgreyling.substack.com/p/the-rise-of-ai-harness-engineering) (2026)

**Relevance:** the Isagawa Kernel *is* a harness-engineering implementation (self-built protocol + mechanical hook enforcement + learn loop) — it predates the term's naming and matches the five-layer model point for point (tool orchestration = kernel commands/skills, verification loops = gate contracts, context/memory = session_state.json, guardrails = PreToolUse hooks, observability = actions.jsonl/anchor-logs).

### Spec Kit — the mainstream SDD standard, at scale
GitHub's Spec Kit (spec-driven development toolkit) has grown to **120.2k GitHub stars, global rank #79** as of **2026-07-14** (star-history.com), up from ~111k (2026-06-11) and ~117k (2026-07-03) — one of the fastest-growing dev tools of the year. Visual Studio Magazine covered its breakout adoption on **2026-05-12** framing it as "the antidote to piecemeal vibe coding."
- Source: [star-history.com/github/spec-kit](https://www.star-history.com/github/spec-kit/) (2026-07-14 snapshot)
- Source: [Visual Studio Magazine — GitHub Spec Kit Takes Off](https://visualstudiomagazine.com/articles/2026/05/12/github-spec-kit-takes-off-as-antidote-to-piecemeal-vibe-coding.aspx) (2026-05-12)

**Relevance:** Spec Kit validates spec-driven development as a mainstream category at massive scale, but it is a *specification* tool (turns intent into a spec/plan). It does not enforce mechanically at runtime and has no learn-from-failure loop — the kernel's differentiator (self-built + self-enforcing + self-improving) sits one layer deeper than Spec Kit's category.

### The arxiv frontier proposing what's already shipped
- **[arXiv 2606.04455 — "The Meta-Agent Challenge: Are Current Agents Capable of Autonomous Agent Development?"](https://arxiv.org/abs/2606.04455)** (published **2026-06-03**, Chinese Academy of Sciences + Ant Group). Proposes an evaluation framework (MAC) where a "meta-agent" is given a sandbox, an eval API, and time to autonomously *construct, refine, and optimize* an agent system across 5 domains — testing autonomous agent-*engineering* capability, not just task execution. **Finding: meta-agents rarely match human-engineered baselines**; the few that do are dominated by proprietary frontier models.
- **[arXiv 2605.25665 — "Meta-Engineering Harnesses for AI-Native Software Production: A Contract-Driven Adversarial Verification Architecture with Early Deployment Report"](https://arxiv.org/abs/2605.25665)** (published **2026-05-25**, Satadru Sengupta, Tamunokorite Briggs, Ivan Myshakivskyi — HireNimbus). Proposes a meta-engineering harness architecture: turns requirements into explicit contracts, routes work through role-specialized agents, performs independent + adversarial verification, and *improves itself* via structured failure classification and outer-loop calibration. Motivating application: "CTO-as-a-service" for small service firms (websites, booking, payments, backoffice automation, agent interfaces) as continuously-evolving infra, not one-off deliverables. Includes an **early deployment report** (i.e., this is a live-tested proposal, not pure theory).

**Response angle assessment:** 2605.25665 is the closer match — contract-driven, adversarial verification, self-improving via failure classification, deployed. The Isagawa Kernel + task-builder + gate-contract + audit-workflow + /kernel/learn stack **is an independently-built, running instance of the same architecture pattern** (contracts = gate-contract.md; role-specialized routing = task-builder's BUILD/TEST split + model router; adversarial verification = orchestrator re-validation lessons #37–#44; self-improvement = /kernel/learn + lessons.md). 2606.04455's finding (meta-agents rarely beat human baselines) is a useful foil: the kernel's approach is not "agent designs an agent from scratch" (MAC's framing) but "agent builds and mechanically enforces its OWN governance scaffold" — a narrower, more tractable slice that appears to already clear MAC's bar in this operator's own runs. This is exactly the "you're theorizing this, here's it running" wedge named in the backlog.

### Provenance / attestation trend
- **[Microsoft Agent Governance Toolkit](https://opensource.microsoft.com/blog/2026/04/02/introducing-the-agent-governance-toolkit-open-source-runtime-security-for-ai-agents/)** (open-sourced **2026-04-02**): a 7-package, multi-language (Python/TS/Rust/Go/.NET) runtime security system for AI agents — "Agent OS" is a stateless policy engine intercepting every agent action pre-execution; "Agent Mesh" gives cryptographic agent identity (DIDs + Ed25519) and an inter-agent trust protocol; build pipeline includes SLSA-compatible provenance, OpenSSF Scorecard, CodeQL.
- **[Red Hat Trusted Software Factory](https://developers.redhat.com/articles/2026/05/13/trusted-software-factory-building-trust-agentic-ai-era)** (**2026-05-13**): generates/consumes SBOMs, embeds provenance + signatures + attestation so every artifact is verifiable/tamper-resistant in the agentic-AI era.

**Relevance:** both are runtime-policy / supply-chain provenance (post-hoc verifiable artifacts). The kernel's attestation/intent chain is a different provenance layer — it hashes the *human's original words* at backlog-creation time and chains decisions forward, proving intent-to-execution fidelity rather than artifact-to-build fidelity. Complementary, not identical — worth naming precisely in any writeup to avoid overclaiming equivalence.

### HITL / reliability findings
No independent "port.io" HITL study was locatable via live search (the specific source cited in the backlog could not be re-verified — flagging rather than fabricating a citation). Substantiated instead by:
- **Stanford Digital Economy Lab, 2026**: agentic implementations show median productivity gains of **71%** vs 40% for non-agentic — but gains concentrate on tasks with *recoverable errors and clear success criteria* (i.e., where a harness/gate can catch and re-route failure).
- **EU AI Act Article 14**, enforceable **2026-08-02**: mandates human-oversight capability for high-risk AI systems — a regulatory tailwind for HITL-by-design architectures.
- Source: [OneReach — Human-in-the-Loop Agentic AI for High-Stakes Oversight 2026](https://onereach.ai/blog/human-in-the-loop-agentic-ai-systems/)

**Relevance:** directly supports the RT-automation venture's HITL-mandatory invariant and the kernel's "propose, human approves" pattern generally — this is now a regulatory + productivity argument, not just a safety preference.

### Enterprise adoption baseline
**[Anthropic — The 2026 State of AI Agents Report](https://resources.anthropic.com/hubfs/The%202026%20State%20of%20AI%20Agents%20Report.pdf)** (survey of 500+ technical leaders, late 2025): 57% of orgs use agents for multi-stage workflows, 80% report measurable ROI already, 90% use AI for coding, 46% cite integration-with-existing-systems as the top blocker. Focus is shifting from *building* agents to *operating them reliably* — the exact frame harness engineering and this operator's work sit inside.

---

## 2. Asset Inventory (IP-tagged)

| Asset | IP Tag | Notes |
|---|---|---|
| **Isagawa Kernel** (`isagawa-co/isagawa-kernel`) | **MIT — shareable** | Self-building/self-improving governance framework; the core differentiated IP that is safe and intended to be public. |
| **platform-selenium** (`isagawa-qa/platform-selenium`) | **Public reference implementation** | QA domain-pack reference; publicly visible per protocol but not the commercial product itself. |
| **Orderly** (clean-room demo app) | **Shareable** | Built specifically as a clean-room stand-in — no client vocabulary, safe for public demos/screen recordings. |
| **Domain-spec meta-factory** | **MIT/shareable (kernel-adjacent)** | The task-builder/gate-contract/audit-workflow pattern — same license posture as the kernel since it's kernel tooling, not a client build. |
| **Attestation / intent chain** | **MIT/shareable** | Kernel subsystem; safe to describe and demo. |
| **Portfolio site** (https://solosza.github.io/) | **Public (personal)** | Already live; existing distribution surface, currently under-leveraged per this backlog's premise. |
| **Both GitHub orgs** — isagawa-co (company/kernel) + isagawa-qa (QA platform org) | **Structure public, contents mixed** | Org existence and the MIT kernel repo are shareable; proprietary platform repos inside isagawa-qa are not. |
| **HMSA-adjacent QA platforms** (`hmsa-qa-platform`, `hmsa-healthcare-qa`, `healthcare-qa-spec-master` local dirs) | **CONFIDENTIAL — never exposed** | Client identity + healthcare vocabulary; clean-room boundary is absolute — Orderly exists precisely so these never need to surface publicly. |
| **isagawa-qa-zentyant / other proprietary platform dirs** | **PROPRIETARY** | Commercial QA platform internals — architecture, code, and client-specific detail all stay private. |
| **Internal strategy / GTM / backlog docs** (this workspace, `sr_dev_workspace`) | **CONFIDENTIAL** | Never shipped publicly per CLAUDE.md ("Internal docs, GTM plans, and strategy live here — never in public repos"). |
| **RT-automation venture materials** | **CONFIDENTIAL (cousin venture, pre-launch)** | Business-plan-stage; not a visibility asset until/unless the venture goes public. |

**Boundary rule (binding on the rest of this plan):** every recommended artifact in the visibility plan must state which row above it draws from, and confirm it draws only from MIT/shareable/public rows. Anything touching HMSA/healthcare/client identity or proprietary platform internals is categorically excluded from any public artifact.

---

## 3. Operator Context

Active job search in flight (pipeline 029, AI-infra-focused: OpenAI Agent Infrastructure, Google Agents Infrastructure, Cohere Applied AI Engineer among top matches — see workspace memory). This is the most time-sensitive of the three candidate goal branches (career / venture / recognition) named in the backlog, and should weight the channel ranking in task 002 accordingly — visibility artifacts that double as portfolio/interview evidence carry higher leverage right now than pure thought-leadership plays.
