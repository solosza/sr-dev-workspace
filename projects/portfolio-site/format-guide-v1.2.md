# GitHub Portfolio Format Guide (v1.2 — Merged & Corrected)
### For an Agentic SDD / AI Developer Tooling Builder

**Goal:** present the builder clearly enough for a recruiter to understand in under one minute *and* an engineering hiring manager to validate the architecture in under ten — while protecting proprietary implementation details and never publishing an unverified claim.

**Changelog from v1.1 draft:**
- Removed LangChain/LlamaIndex/OpenTelemetry from the stack row — not part of the verified toolchain; Isagawa's differentiator is that it sits *beneath* agent frameworks, not on top of one.
- Removed all invented metrics (token caps, pass rates, workflow counts). Replaced with `[INSERT: verified metric]` placeholders — fill in only with numbers you can defend if asked.
- Rewrote the case-study trade-off box to drop absolute/guarantee language ("100%," "guaranteeing"), consistent with the original guide's own rule against absolute claims.
- Kept the structural additions that added real value: stack badges, DX teaser snippet, quantified evidence card format, trade-off callout, expanded decision matrix.

---

## 1. Portfolio Strategy

**Primary positioning:** Agent Systems Engineer / AI Developer Tooling Builder who designed and implemented an agentic spec-driven development framework with governed execution.

**Public description of Isagawa:** A proprietary agentic SDD environment for building and governing domain-specific software workflows.

**What the site must prove:**
- The builder personally designed and implemented a credible agent-systems platform.
- The work extends beyond prompt engineering into software architecture, runtime design, evaluation, and developer tooling.
- The platform has produced real systems and repeatable workflows across more than one domain.
- The builder understands limitations, trade-offs, and evidence — not just ambitious product language.

**What the site must not do:**
- Reveal proprietary state schemas, enforcement logic, command protocols, meta-factory internals, or domain-compilation methods.
- Read like a startup sales page, pricing page, or catalog of every experiment.
- Use absolute claims such as "unbypassable," "zero drift," "100%," or "guaranteed."
- Publish any metric you can't defend in a follow-up interview question.
- Force recruiters to infer who built the system or what role the applicant wants.

---

## 2. One-Page Navigation

| About | Isagawa | Evidence | Case Study | Selected Work | Resume | Contact |
|---|---|---|---|---|---|---|

Each item scrolls to a section on the same page.

---

## 3. Hero Section (updated: stack badge row added)

**Purpose:** Identify the builder, the role target, the central technical accomplishment, and pass a technical recruiter's toolchain scan — immediately.

**Include:**
- Full name and concise role identity.
- One-line value proposition.
- A direct statement that Isagawa was personally designed and built.
- **A stack badge row** — real, verified toolchain only.
- Buttons for Resume, GitHub, LinkedIn, and Email.
- A one-line hiring target.

**Avoid:**
- Opening with only the Isagawa logo or company identity.
- Long architecture explanations above the fold.
- "Founder" as the only role label if the goal is employment.
- Listing any tool not actually part of the build (do not add frameworks for keyword coverage).

> **Sample copy**
>
> YOUR NAME
>
> Agent Systems Engineer | AI Developer Tooling | Spec-Driven Development
>
> I built Isagawa, a proprietary agentic SDD environment used to structure, govern, and validate AI-assisted software workflows across multiple domains.
>
> `Python` `TypeScript` `Selenium` `Playwright` `Docker` `Paramiko` `pyodbc` `Claude Code`
>
> Seeking roles in agent infrastructure, AI developer tooling, evaluation systems, and applied AI engineering.

---

## 4. What I Built: Isagawa (updated: DX teaser added)

**Purpose:** Explain the system category and scope, and prove it's a real developer tool — without disclosing the proprietary recipe.

**Include:**
- A concise definition of Isagawa.
- High-level capabilities: specification, domain adaptation, governed execution, validation, review, workflow tracking.
- A small conceptual diagram: input → governed workflow → validated output.
- A clear statement of personal ownership.
- **A 6–8 line sanitized, illustrative input-spec snippet** — labeled explicitly as representative, not a literal excerpt of internal schema.

**Avoid:**
- Exact internal layer names, folder structures, protocols, hook order, or state fields.
- Detailed meta-factory process or domain-generation logic.
- Presenting the snippet as an actual internal file rather than an illustrative example.

> **Sample copy**
>
> Isagawa is an agentic spec-driven development environment. It turns high-level intent into structured development workflows, applies domain-aware controls during execution, and produces reviewable software artifacts with explicit validation evidence.
>
> I designed and implemented the system architecture, workflow runtime, evaluation mechanisms, and applied platforms.

> **Illustrative input spec (representative example, not an internal file)**
> ```yaml
> # representative-workflow.sdd.yaml
> domain: qa-automation
> spec:
>   goal: "Validate REST and database state consistency across a checkout flow"
>   governance:
>     require_verification_gate: true
>   invariants:
>     - check: "order_status matches api_response_status"
>       type: deterministic
> ```
> *Shows how developer intent is externalized into a declarative spec before entering the governed execution runtime.*

---

## 5. The Problem and Design Thesis

**Include:**
- Three concise problems: advisory prompts, fragile conversational state, self-reported completion.
- One sentence on the systems approach.
- Why specifications alone weren't enough.

**Avoid:** claims the system solves all agent reliability problems; academic language without a concrete engineering problem.

> **Sample copy**
>
> The problem: coding agents can lose procedural context, reinterpret instructions, and report completion without independent evidence.
>
> My approach: treat reliability as a software runtime and verification problem — not only a prompting problem.

---

## 6. High-Level Architecture

**Include:**
- Four public concepts: structured intent, domain-aware workflow, governed execution, independent validation/review.
- A conceptual flow diagram, not an implementation diagram.
- Short engineering principles: externalized state, bounded work, tool-aware controls, explicit gates.

**Avoid:** raw state diagrams; exact enforcement paths or bypass mitigations; internal command names, hook event names, private data formats, or orchestration sequences.

> **Sample copy**
>
> Intent → Structured specification → Domain-aware execution → Validation evidence → Reviewable artifact
>
> Key principle: the model does not serve as the only source of state or the only judge of completion.

---

## 7. Evidence Section (updated: quantified format + visual trace)

**Purpose:** Prove the system runs and produces inspectable outcomes, with numbers you can defend, without publishing internals.

**Include:** 3–4 sanitized evidence cards, each with a factual result and why it matters. One card should include a short (10–15s) sanitized CLI/terminal trace GIF or screenshot. Every metric must be one you can source and explain if asked in an interview.

| Evidence Card | Sanitized Outcome | Visual / Proof Type |
|---|---|---|
| Governed workflow | `[INSERT: e.g. bounded work units per run, verified count]` | Sanitized completion summary or CLI trace |
| Independent validation | `[INSERT: verified gate pass/fail behavior — describe the mechanism, not a claimed %]` | Gate summary or test result screenshot |
| Controlled delivery | Generated changes isolated to feature branches pending review | Sanitized branch/commit/PR summary |
| Evaluation routing | Evaluation routing changes based on workload type; invalid inputs are rejected | Sanitized router log excerpt |

**Avoid:** raw state files, full contracts, sensitive logs/credentials/paths/internal identifiers, and any metric without a clear, defensible definition and date.

---

## 8. Flagship Case Study (updated: trade-off box, de-absolutized)

**Purpose:** Prove the framework supports a substantial real-world platform.

**Include:** the multi-interface QA platform as the flagship example — problem, personal role, solution scope, result, Browser/REST/SQL Server/SOAP coverage, unified architectural governance at a high level, technologies, and one concrete trade-off the design had to navigate.

**Avoid:** publishing the complete five-layer contract, fixture wiring or constructor rules, a full method-by-method spec, or absolute/guarantee language.

> **Sample copy**
>
> Case study: Multi-Interface QA Platform
>
> Problem: enterprise workflows required coordinated browser, API, database, and SOAP validation without duplicating architecture across tools.
>
> My role: designed the framework architecture, cross-interface contracts, dependency model, test-data strategy, and AI-assisted development workflow.
>
> Result: one coherent platform model across four interfaces, built and validated through Isagawa.

> **Architectural trade-off**
>
> Challenge: keeping asynchronous browser steps and synchronous database assertions from drifting out of sync during a single test run.
>
> Decision: state is checkpointed outside the model's context window rather than held in conversation — the model acts as an execution worker, not the source of truth for state. This trades some runtime flexibility for reproducibility across interfaces.

---

## 9. Selected Work

Two or three additional applications only: an AI evaluation workflow, a compliance/attestation workflow, one developer-tooling or domain platform example. For each: problem, personal contribution, result, technologies.

**Avoid:** a card for every prototype; pricing or sales copy; leading with anything not central to the agent-infrastructure narrative.

---

## 10. Engineering Decisions and Trade-offs (updated: expanded)

| Decision | Reason | Operational Trade-off / Invariant |
|---|---|---|
| Persist workflow state outside chat | Supports inspection, recovery, continuity | Adds a persistence layer to maintain; state must survive session boundaries |
| Bound work into explicit units | Reduces ambiguity, improves validation | Requires upfront task decomposition before execution |
| Separate mechanical and semantic checks | Different invariants need different verification methods | Semantic checks remain model-assisted and probabilistic; mechanical checks are deterministic |
| Use controlled integration | Keeps generated changes reviewable before merge | Adds a review step; trades some autonomy for auditability |
| Adapt by domain | Reusable runtime without hardcoding one vertical | Domain specs must be authored per vertical; runtime stays constant |

**Avoid:** internal enforcement implementation; claims that every decision is universally optimal.

---

## 11. Current Limitations

**Include:** only limitations you're comfortable making public — executor dependence, incomplete external benchmarking, model-assisted semantic review, ongoing concurrency hardening are reasonable categories. A short "current work" list.

**Avoid:** publishing security-sensitive weaknesses; sounding apologetic; calling planned features completed.

> **Sample copy**
>
> Current scope: early-stage proprietary implementation exercised extensively by its builder. External reproduction, broader executor support, and comparative benchmarking are active validation areas.

---

## 12. About and Hiring Intent

**Include:** 2–4 sentences about the builder, core technical strengths, exact role families targeted, location/work authorization if helpful, resume/LinkedIn/GitHub/email.

> **Sample copy**
>
> I am a systems-oriented builder focused on agent infrastructure, AI developer tooling, spec-driven development, evaluation, and quality platforms. I built Isagawa and its applied systems end to end.
>
> I am seeking roles involving agent runtimes, AI infrastructure, developer tooling, evaluation systems, and applied AI architecture.

---

## 13. IP-Safe Disclosure Checklist

Before publishing any section, apply this rule: **show that you can build the system — do not teach the reader how to reproduce or bypass it.**

| Safe to publish | Keep private or heavily abstracted |
|---|---|
| System category and purpose | Meta-factory process |
| High-level capabilities | Internal state schemas |
| Sanitized outcomes and defensible metrics | Hook logic, hook event names, and order |
| Verified technology list (no aspirational additions) | Gate rules and bypass mitigations |
| Conceptual diagrams | Command protocols |
| Personal contribution | Full domain contracts |
| Public limitations | Private data paths and logs |
| Screenshots of non-sensitive outputs | Proprietary generation and adaptation methods |

---

## 14. GitHub Pages Implementation Notes

- One static page, semantic HTML sections, anchor links.
- JavaScript optional; page fully readable without it.
- Neutral light or dark theme, one accent color, generous spacing.
- Body width ~760–980px.
- Responsive two-column layout only for evidence cards and decision tables.
- Resume as PDF, linked from hero and final CTA.
- Basic Open Graph metadata, clear browser title.
- Privacy-conscious analytics only, or none.
- Test on mobile, desktop, and print-to-PDF before sending applications.

**Suggested browser title:** YOUR NAME — Agent Systems Engineer and SDD Framework Builder

**Suggested headline:** I build governed infrastructure for AI-assisted software development.

**Suggested subheadline:** Creator of Isagawa, a proprietary agentic spec-driven development environment used to structure, govern, and validate domain-specific software workflows.

---

## 15. Final Review Checklist (v1.2)

- [ ] Builder's name and desired role appear before the Isagawa brand explanation
- [ ] First screen understandable in under ten seconds
- [ ] Stack badge row lists only verified, actually-used tools
- [ ] Page explains Isagawa as an agentic SDD environment without exposing internal architecture
- [ ] Every metric has a clear, defensible definition and date — no placeholder numbers shipped unfilled
- [ ] DX teaser snippet is labeled illustrative, not presented as a literal internal file
- [ ] Every showcased project states the builder's personal contribution
- [ ] No absolute or universal reliability claims anywhere on the page ("100%," "guaranteed," "unbypassable," "zero drift")
- [ ] Evidence is sanitized and intentionally public
- [ ] Page includes one flagship case study and no more than three secondary projects
- [ ] Limitations are honest but don't expose exploitable detail
- [ ] Page clearly asks for interviews in relevant role families
- [ ] Resume, GitHub, LinkedIn, and email links are easy to find
- [ ] Complete page can be skimmed in one minute, explored in under ten
- [ ] Timing check: if this is going live before a second client deployment closes, confirm the "produced real systems across more than one domain" language still holds up to scrutiny
