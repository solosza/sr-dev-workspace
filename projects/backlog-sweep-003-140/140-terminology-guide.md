# Terminology Guide — Backlog 140

## Purpose

Audit of every technical term used across isagawa.co (homepage + kernel page), the Kernel README, and related documentation. For each term: current usage patterns, definition, accessibility-first alternative, and content strategy guidance on where precision is essential vs. where simplification improves reach.

---

## Master Glossary

### 1. Domain Spec

**Definition:** A folder of markdown files that encode patterns, conventions, and quality gates for a specific industry or workflow. Dropped into `.claude/skills/` and merged with the kernel's discovered patterns during setup.

**Current usage:**
- Homepage: "the domain-spec factory builds vertical packs" (hero), "Domain Spec + Repo Context" (architecture diagram)
- Kernel page: "Optional domain specs layer industry-specific knowledge" (domain setup section), "domain-aware governance" (throughout)
- README: "A domain spec is a folder of markdown files that encode patterns, conventions, and quality gates for a specific domain" (clearest definition in any surface)

**Accessibility issue:** "Spec" is well-understood in engineering circles but "domain spec" is Isagawa-specific jargon. Readers outside the framework have no prior association. "Domain-spec factory" compounds the problem by stacking two abstractions.

**Alternative language:**
- Marketing/homepage: "workflow pack" or "skill pack" or simply "spec" with a one-line gloss
- Technical docs: "domain spec" is appropriate when defined on first use
- README: Current usage is good — defines the term clearly on first mention

**Content strategy:**
| Surface | Recommendation |
|---------|---------------|
| Homepage hero | Replace "domain-spec factory" with a phrase that communicates the outcome, not the mechanism. E.g., "A spec compiler builds governed agents for any vertical." |
| Homepage architecture diagram | Keep "Domain Spec" but add a parenthetical: "Domain Spec (workflow knowledge for a vertical)" |
| Kernel page | Keep as-is. The kernel page is for technical readers who expect precision. |
| README | Keep as-is. Already well-defined. |

---

### 2. Harness

**Definition:** A governed agent execution environment — the combination of kernel enforcement, domain-specific protocol, commands, hooks, and state that together make an agent capable of autonomous work in a specific domain.

**Current usage:**
- Homepage: "governed agent harnesses" (hero), "Specification-driven agent harnesses that learn from failures" (architecture), "Harnesses, agents, and domain specs compiled from specifications" (Section 02)
- Kernel page: "Produced Harnesses" (section header), "agent harness" in card descriptions
- README: "self-improving harness for AI coding agents" (original tagline, now "self-improving framework"), referenced throughout

**Accessibility issue:** "Harness" has a specific meaning in test engineering (test harness = the scaffolding around test execution) but Isagawa extends it to mean a full governed agent environment. Readers from QA will partially understand it; everyone else will not. "Agent harness factory" stacks three abstractions.

**Alternative language:**
- Marketing/homepage: "governed agent" or "governed workspace" or "agent environment"
- When paired with "factory": replace the full phrase. "Spec compiler" or "agent builder" communicates the same idea without requiring prior knowledge of "harness"
- Technical docs / README: "harness" is appropriate. The test-engineering audience understands the metaphor.

**Content strategy:**
| Surface | Recommendation |
|---------|---------------|
| Homepage hero | Avoid "harness" in the first sentence a visitor reads. Use "governed agent" or "governed workspace" instead. Introduce "harness" later when explaining the architecture. |
| Homepage Section 02 | Keep "harnesses" — by this point the reader has context from Sections 01. |
| Kernel page | Keep. The audience is technical. |
| README | Keep. Already clear in context. |

---

### 3. Enforcement Loop

**Definition:** The recurring cycle (session-start, anchor, work, complete) that governs every agent session. Hooks fire at each step; protocol is re-read periodically; failures trigger mandatory learning. The loop is the core runtime that prevents drift.

**Current usage:**
- Homepage: "The loop is the core runtime architecture" (Section 04 closing)
- Kernel page: "the enforcement loop applies regardless of what the skill does" (specialized skills), diagram in "The Loop" section
- README: "The Enforcement Loop" (section header), full diagram, table explaining each step

**Accessibility issue:** Low. "Enforcement loop" is descriptive enough that a non-technical reader can grasp the concept — something that enforces, and it repeats. The term works across audiences.

**Alternative language:**
- Marketing: "governance cycle" or "enforcement cycle" if "loop" feels too technical
- Generally: no change needed. This is one of the most self-explanatory terms in the system.

**Content strategy:**
| Surface | Recommendation |
|---------|---------------|
| All surfaces | Keep "enforcement loop." It communicates clearly. On first use in marketing copy, consider a brief gloss: "the enforcement loop — a recurring cycle that re-checks the agent's work and blocks non-compliance." |

---

### 4. Gate Contract

**Definition:** A specification attached to each task that defines preconditions (what must be true before the task runs) and success criteria (what must be true after). BUILD gates verify construction; TEST gates verify integration. Failed gates block task completion.

**Current usage:**
- Homepage: "Contracts + Gates + Lessons" (execution pipeline diagram), "Each step enforces contracts, validates gates" (pipeline caption)
- Kernel page: "gate contract that defines preconditions and success criteria" (task execution section), "Gate Contract" (flow card header)
- README: "quality gate" and "gate" used interchangeably, no explicit "gate contract" definition

**Accessibility issue:** Moderate. "Gate" alone is widely understood (a checkpoint that must pass). "Contract" alone is understood (an agreement about expectations). "Gate contract" as a compound is Isagawa-specific but intuitive. The issue is when it appears alongside other compound terms ("domain spec," "anchor token," "learn loop") — the density becomes impenetrable.

**Alternative language:**
- Marketing: "quality gate" or "validation checkpoint"
- First mention on any page: "gate contract — preconditions and success criteria that must pass before the task completes"
- Technical docs: "gate contract" is correct and should stay

**Content strategy:**
| Surface | Recommendation |
|---------|---------------|
| Homepage | Use "quality gates" in the hero/architecture overview. Reserve "gate contract" for deeper sections. |
| Kernel page | Keep "gate contract" — the audience expects precision. |
| README | Already uses "quality gate" in accessible spots and "gate" in technical spots. Good pattern. |

---

### 5. Governance Loop / Governance

**Definition:** The overall system of enforcement that prevents agent drift. Encompasses hooks (mechanical tier), protocol re-reads (behavioral tier), and the learn cycle (improvement tier). "Governance" is the umbrella; the "enforcement loop" is the specific mechanism.

**Current usage:**
- Homepage: "governance baked in" (removed in latest version), "Governed Agent Execution" (architecture diagram), "kernel governance" (Section 02)
- Kernel page: "Governed agent runtime" (page title/hero), "Governance During Cycling," "governance enforcement continues throughout cycling"
- README: "Governance that agents can't bypass" (positioning report recommendation), "governed agent" (throughout)

**Accessibility issue:** Low. "Governance" is a widely understood concept. In the AI agent context, it maps directly to the question "how do you make sure the agent does what it's supposed to?" This is one of the strongest terms in the system.

**Alternative language:**
- No change needed. "Governance" is both precise and accessible.
- When explaining to non-technical audiences: "rules the agent physically can't break"

**Content strategy:**
| Surface | Recommendation |
|---------|---------------|
| All surfaces | Lead with "governance" in marketing. It is the bridge term — understood by engineers, compliance teams, and founders alike. |

---

### 6. Hook

**Definition:** A Python script that fires at the tool-call boundary (before or after the agent uses a tool). Hooks read state, check preconditions, and block the agent's action if requirements are not met. They are the mechanical tier of enforcement.

**Current usage:**
- Homepage: "Hooks. Commands. Protocol." (Section 01 subtitle), card tag "HOOK / RUNTIME / WRITE-GATE"
- Kernel page: "hook-enforced execution" (hero, meta description), "Hooks fire at the tool-call boundary" (SDD architecture), "hook-blocked write" (design decision)
- README: "enforcement hooks" and "hooks" throughout, "Enforcement operates at the tool-call level"

**Accessibility issue:** Moderate. Software engineers understand "hook" (a callback at a lifecycle point). Non-engineers do not. On the homepage, "hook" appears without definition. On the kernel page, it is explained well ("Fire at the tool-call boundary. Block writes when state preconditions fail.").

**Alternative language:**
- Marketing: "enforcement checkpoint" or "automated check"
- First mention: "hooks — automated checks that fire every time the agent tries to act"
- Technical docs: "hook" is the correct term

**Content strategy:**
| Surface | Recommendation |
|---------|---------------|
| Homepage | On first use, gloss it: "Hooks (automated enforcement at every action)." After that, "hooks" alone is fine. |
| Kernel page | Keep as-is. Well-explained in context. |
| README | Keep as-is. Audience understands. |

---

### 7. Anchor / Anchor Token

**Definition:** A periodic forced stop (every N actions) where the agent must re-read its protocol, audit its recent work, and produce a UUID token proving it actually re-centered. The anchor reverses protocol drift on a schedule.

**Current usage:**
- Homepage: "Anchor Token" (evidence card header), "Every N actions (configurable), the system forces a full protocol re-read. A UUID token proves the agent actually re-centered." (card body)
- Kernel page: "Anchors fire every N actions" (multiple sections), "anchor command forces the agent to re-read the protocol" (design decision)
- README: "Periodic Re-Anchoring" (capabilities), "Anchor — Re-reads protocol, audits recent work" (enforcement loop table)

**Accessibility issue:** High on first encounter, low once explained. "Anchor" as a metaphor (something that holds you in place) is good. "Anchor token" is more opaque — why does re-reading need a token? The homepage card explains it well, but the term appears in the Section 01 subtitle without explanation: "Hooks. Commands. Protocol."

**Alternative language:**
- Marketing: "periodic re-check" or "protocol checkpoint"
- When the UUID token is relevant: "anchor token — cryptographic proof the agent actually stopped and re-read its rules"
- Technical docs: "anchor" is the correct term

**Content strategy:**
| Surface | Recommendation |
|---------|---------------|
| Homepage | The evidence card explanation is excellent. No change needed there. In the Section 01 subtitle, consider expanding: "Hooks. Commands. Anchors. Protocol." — since "anchor" appears as a card header, having it in the subtitle provides a bridge. |
| Kernel page | Keep. Well-explained. |
| README | Keep. The enforcement loop table defines it clearly. |

---

### 8. Cycling / Autonomous Cycling

**Definition:** The agent executing a queue of tasks sequentially, maintaining governance enforcement throughout, with state persistence across sessions. Failed tasks are retried, then skipped with audit trails.

**Current usage:**
- Homepage: Not explicitly used (the concept appears in Section 03 as "90+ completed pipelines" but "cycling" as a term does not appear)
- Kernel page: "Autonomous Cycling" (section header), "autonomous-cycle command," "cycling" (throughout the section)
- README: "Autonomous Cycling" (capabilities section), "task cycling"

**Accessibility issue:** Low. "Cycling through tasks" is natural English. "Autonomous cycling" adds the automation dimension clearly.

**Alternative language:**
- Generally no change needed
- For non-technical audiences: "automated task queue execution"

**Content strategy:**
| Surface | Recommendation |
|---------|---------------|
| All surfaces | Keep "autonomous cycling." Self-explanatory. |

---

### 9. Spec-Driven Development (SDD)

**Definition:** The architectural pattern where specifications (not prompts, not configuration) drive agent behavior. The kernel compiles specs into protocols, and the agent builds to spec rather than interpreting instructions ad hoc.

**Current usage:**
- Homepage: "Spec-Driven Agent Framework" (page title, meta tags), "Spec-driven loop engineering for AI agents" (hero h2), "specification-driven agent harnesses" (architecture caption), "SDD architecture" (Section 02 subtitle)
- Kernel page: "SDD Architecture" (section header)
- README: Not explicitly named "SDD" but the concept is described: "Specification-driven agent harnesses"

**Accessibility issue:** High. "Spec-driven development" is an Isagawa-coined term. No prior art in the broader industry. A reader encountering "SDD" for the first time has no reference point. "Spec-driven" alone is more intuitive than the acronym.

**Alternative language:**
- Marketing: Avoid the acronym "SDD" entirely on public-facing surfaces. Use the full phrase "spec-driven" and let the concept speak.
- If a label is needed: "specification-first development" or "spec-first architecture" (parallels "test-driven," "behavior-driven" which are known patterns)
- Technical docs: "SDD" is fine after first defining it

**Content strategy:**
| Surface | Recommendation |
|---------|---------------|
| Homepage | Drop the "SDD" acronym. Use "spec-driven" as a descriptor, not a branded methodology name. The hero subtitle "Spec-driven loop engineering for AI agents" works because "spec-driven" reads naturally. The Section 02 subtitle "SDD architecture" does not — replace with "Spec-driven architecture." |
| Kernel page | Replace "SDD Architecture" section header with "Spec-Driven Architecture" or "Architecture." The acronym adds nothing for readers who have not already bought in. |
| README | Currently does not use the acronym. Keep it that way. |

---

### 10. Learn Loop / Learn Cycle

**Definition:** The mandatory process after any failure: diagnose the root cause, fix the issue, record what was learned. The lesson becomes permanent — encoded in the protocol so the same failure cannot recur. The learn cycle is enforced by hooks (the agent cannot write until `/kernel/learn` is invoked).

**Current usage:**
- Homepage: "Learn Loop" (evidence card header), "Every failure records a lesson. The protocol updates mechanically." (card body)
- Kernel page: "Learn cycles trigger on test failures" (autonomous cycling section), "mandatory learn step" (the loop section)
- README: "Mandatory Learn Loop" (capabilities), "Every failure triggers a mandatory learn cycle"

**Accessibility issue:** Low. "Learn from failure" is universally understood. "Learn loop" communicates that it repeats. "Mandatory" communicates that it is not optional. This is strong, accessible language.

**Alternative language:**
- No change needed. This is one of the best-named concepts in the system.

**Content strategy:**
| Surface | Recommendation |
|---------|---------------|
| All surfaces | Keep "learn loop" or "learn cycle." Universally clear. |

---

### 11. Protocol

**Definition:** The agent-generated ruleset that governs behavior in a specific repository. Built during domain setup from repo structure + optional domain spec. Re-read at every anchor. Updated after every learn cycle.

**Current usage:**
- Homepage: "Protocol + Commands + Gates + Lessons" (architecture diagram), "Hooks. Commands. Protocol." (Section 01 subtitle)
- Kernel page: "protocol re-reads," "re-read the protocol," "protocol drift" (throughout)
- README: "Builds own protocol," "protocol from what it finds" (throughout)

**Accessibility issue:** Low-to-moderate. "Protocol" is understood broadly as "a set of rules." In this context it is a specific file the agent generates. The gap is: most readers think "protocol" means a fixed standard (like a network protocol), not a living, self-updating document. The README handles this well by saying "the agent builds its own protocol."

**Alternative language:**
- Marketing: "ruleset" or "playbook" for initial explanation, then use "protocol" once the self-building aspect is clear
- Technical docs: "protocol" is correct

**Content strategy:**
| Surface | Recommendation |
|---------|---------------|
| Homepage | On first mention, gloss: "protocol — a self-built ruleset the agent updates after every failure." |
| Kernel page | Keep as-is. Context makes it clear. |
| README | Keep as-is. Well-defined. |

---

### 12. Pipeline / Execute Pipeline

**Definition:** The command (`/kernel/execute-pipeline`) that takes a backlog item, decomposes it into tasks via the task builder, and executes them sequentially with full governance. A complete backlog-to-delivery workflow.

**Current usage:**
- Homepage: "Execution Pipeline" (architecture subsection), "/kernel/execute-pipeline" (Section 03 card), "90+ completed pipelines"
- Kernel page: "execute-pipeline command" (task execution section)
- README: "execute-pipeline" (roadmap, capabilities)

**Accessibility issue:** Low. "Pipeline" is widely understood in software engineering as a sequence of automated steps. "/kernel/execute-pipeline" is a command, so the slash-prefix format is expected.

**Alternative language:**
- No change needed for engineering audiences
- For non-technical audiences: "automated build pipeline" or "task execution workflow"

**Content strategy:**
| Surface | Recommendation |
|---------|---------------|
| All surfaces | Keep. Well-understood term. |

---

### 13. Backlog

**Definition:** A numbered specification item that captures intent. Created via `/kernel/backlog`, hash-signed with an intent chain. The starting point for any pipeline execution.

**Current usage:**
- Homepage: "Backlog" (execution pipeline diagram), "/kernel/backlog" (Section 03 card)
- Kernel page: "backlog item" (task execution section)
- README: "backlogs processed" (proof points)

**Accessibility issue:** None. "Backlog" is universal in software development.

**Alternative language:** None needed.

**Content strategy:** Keep everywhere.

---

### 14. Intent Chain

**Definition:** An append-only, hash-signed log of every revision to a backlog item. Records the SHA-256 of the user's raw input and the resulting specification file. Provides cryptographic proof of what was requested and what was produced.

**Current usage:**
- Homepage: Embedded in attestation bundles (JSON) but not explained in copy
- Kernel page: "Intent Chains" (cross-session persistence card), "hash of raw user input and resulting specification file"
- README: Not mentioned

**Accessibility issue:** Moderate. "Intent chain" is Isagawa-specific. The concept (a tamper-proof log of what was requested) is valuable but the name does not communicate it.

**Alternative language:**
- Marketing: "audit trail" or "request log" for initial framing
- When precision matters: "intent chain — a cryptographic record of every request and its resulting output"
- Technical docs: "intent chain" is fine

**Content strategy:**
| Surface | Recommendation |
|---------|---------------|
| Homepage | Already embedded implicitly in attestation. No change needed. |
| Kernel page | Keep — well-explained in the persistence section. |
| README | If added, define on first use. |

---

### 15. Attestation / Sigstore / Rekor

**Definition:** Cryptographic signing of pipeline outputs using Sigstore, logged to the Rekor transparency log. Provides third-party-verifiable proof that a specific pipeline run produced specific artifacts.

**Current usage:**
- Homepage: Full attestation section with verification badges and Rekor links
- Kernel page: "Full attestation chain at /attestation.html"
- README: "Sigstore attestation with Rekor transparency log" (proof points)

**Accessibility issue:** Low for the concept (signing work for proof), high for the specific tools (Sigstore, Rekor). Most readers will not know what Sigstore or Rekor are.

**Alternative language:**
- Marketing: "cryptographic proof" or "verifiable provenance"
- When the tools matter: "signed with Sigstore and logged to Rekor — open-source tools for software supply chain verification"

**Content strategy:**
| Surface | Recommendation |
|---------|---------------|
| Homepage | The attestation section works well — it shows real bundles and links to Rekor. Add a one-sentence explanation of what Sigstore/Rekor are for readers unfamiliar with them. |
| Kernel page | Keep reference. |
| README | Keep. Brief enough. |

---

### 16. Smart Gates

**Definition:** The enforcement pattern where blocked actions include a diagnostic message telling the agent exactly what is wrong and how to fix it. Not just "blocked" but "blocked because X, run Y to proceed."

**Current usage:**
- README: "Smart Gates" (capabilities section)
- Homepage: Not used
- Kernel page: Not used explicitly, though the concept appears in the hooks description

**Accessibility issue:** Low. "Smart gates" is intuitive — gates that are intelligent about what went wrong.

**Alternative language:** None needed.

**Content strategy:** Consider promoting this term to the homepage. It communicates a user-facing benefit (the system helps itself recover) in accessible language.

---

### 17. Two-Tier Enforcement / Mechanical vs. Behavioral

**Definition:** The design decision to split governance into two tiers: Tier 1 (mechanical) uses hooks that physically block the agent; Tier 2 (behavioral) uses periodic protocol re-reads that correct drift through re-centering. Neither tier alone is sufficient.

**Current usage:**
- Kernel page: "Two-tier governance. Mechanical and behavioral." (design decision section), full explanation of why both are necessary
- README: "Advisory vs enforceable" framing (implicit)
- Homepage: Not explicitly named, though the mechanism cards in Section 01 describe both tiers

**Accessibility issue:** Low. "Mechanical" and "behavioral" are common English words. The two-tier framing is clear.

**Alternative language:**
- Marketing: "hard enforcement + soft enforcement" or "rules that block + rules that guide"

**Content strategy:**
| Surface | Recommendation |
|---------|---------------|
| Homepage | Consider adding a brief mention. The kernel page's "Two-tier governance" section is one of the strongest pieces of copy in the entire site — a simplified version would strengthen the homepage. |
| Kernel page | Keep. Excellent as-is. |

---

## Terminology Density Analysis

### Homepage — Term Density Per Section

| Section | Isagawa-Specific Terms | Verdict |
|---------|----------------------|---------|
| Hero | "spec-driven," "governed agent harnesses," "domain-spec factory," "vertical packs," "backlog pipeline" | **Too dense.** Five novel terms in three sentences. A first-time visitor processes none of them. |
| Architecture ("Why This Isn't Prompt Engineering") | "Backlog," "Execute Pipeline," "Task Builder," "Kernel-Governed Agent," "Contracts + Gates + Lessons," "Domain Spec," "Protocol," "Commands" | **Acceptable.** These are labels in a diagram — visual context helps. |
| Section 01 (The Seed) | "Anchor Token," "Gate Enforcer," "Learn Loop," "Session Protocol" | **Good.** Each term is a card header with an explanation beneath it. |
| Section 02 (Growth) | "Harnesses," "agents," "domain specs," "Agent Harness Factory" | **Moderate.** "Agent Harness Factory Steps" is the densest phrase. |
| Section 03 (Self-Extension) | "/kernel/backlog," "/kernel/execute-pipeline," "Produced Harnesses," "Produced Skills" | **Good.** Command-style terms are self-documenting. |
| Section 04 (This Page) | "Kernel," "Agent Harness Factory," "Agent Harnesses," "Workspaces," "Rekor" | **Good.** Chain list format provides progressive context. |

### Kernel Page — Term Density

Generally well-managed. Each section introduces its terms and defines them in context. The "SDD Architecture" acronym is the only term that appears without prior definition.

### README — Term Density

Best of the three surfaces. Terms are introduced with definitions, comparisons, or examples. The FAQ section explicitly addresses common confusion points.

---

## Content Strategy Summary

### Terms That Should Stay Precise Everywhere

These terms are clear, well-defined, and do not benefit from simplification:

- **Governance** — universally understood, maps to the core value prop
- **Enforcement loop** — descriptive, self-explanatory
- **Learn loop / learn cycle** — intuitive, strong metaphor
- **Backlog** — standard software term
- **Pipeline** — standard software term
- **Autonomous cycling** — self-explanatory compound
- **Protocol** — widely understood (with a one-line gloss on marketing surfaces)

### Terms That Need Context on First Use (Marketing Surfaces)

These terms are precise but require a brief explanation when used on the homepage or in introductory materials:

- **Hook** — gloss as "automated check at every action"
- **Anchor / anchor token** — gloss as "periodic forced re-check of rules"
- **Gate contract** — use "quality gate" in marketing, "gate contract" in technical docs
- **Intent chain** — use "audit trail" in marketing, "intent chain" in technical docs
- **Two-tier enforcement** — use "rules that block + rules that guide" in marketing
- **Smart gates** — promote to homepage; it is accessible and communicates a benefit

### Terms That Should Be Simplified on Marketing Surfaces

These terms create barriers for first-time visitors and should be replaced or restructured on the homepage:

- **Domain spec** — replace with "workflow spec" or "skill pack" on first mention; define if the full term is used
- **Harness** — replace with "governed agent" or "governed workspace" in the hero; introduce "harness" in deeper sections
- **SDD / Spec-driven development** — drop the acronym entirely on public surfaces; use "spec-driven" as a natural descriptor
- **Domain-spec factory** — replace entirely. "Spec compiler" or "agent builder" communicates the same idea without stacking abstractions
- **Vertical packs** — replace with "industry-specific specs" or "domain packs"

### Where to Add Explanatory Callouts

1. **Homepage hero** — The single biggest accessibility improvement is reducing term density in the first three sentences. Replace compound jargon with outcome language, then introduce terms in the architecture section below.

2. **Homepage Section 01 evidence cards** — Already have good explanatory text. No change needed.

3. **Kernel page hero subtitle** — Currently packs "domain setup," "task execution," "verification gates," and "tool-call boundary" into one paragraph. Each is explained later, but the hero should preview in plain language first.

4. **README "What You Get" section** — Add a parenthetical gloss for "domain spec" on first mention: "a domain spec (a folder of markdown files encoding industry patterns)."

---

## Cross-Reference with Related Backlogs

| Backlog | Relationship | Coordination Notes |
|---------|-------------|-------------------|
| 135 (Homepage messaging) | Direct dependency — terminology choices drive copy | Homepage hero rewrite should use simplified terms from this guide |
| 137 (README tone refactor) | Completed — README already uses accessible language | No further action needed; README is the gold standard for term introduction |
| 138 (Audience messaging) | Terminology mapping per audience segment | Segment 1 (AI infra) gets full technical terms; Segment 2 (compliance) gets governance/audit language; Segment 3 (founders) gets simplified alternatives |
| 139 (Ownership positioning) | Terminology affects credibility framing | "Spec-driven" as a descriptor (not a branded methodology) supports the ownership narrative without creating gatekeeping language |

---

## Implementation Priority

1. **High impact, low effort:** Remove "SDD" acronym from homepage and kernel page headers. Replace with "Spec-Driven" or drop the label entirely.

2. **High impact, medium effort:** Rewrite homepage hero to reduce term density from 5 novel terms to 2 or fewer. Lead with the problem and outcome, introduce terminology in the architecture section.

3. **Medium impact, low effort:** Add one-line glosses to "hook," "anchor," and "protocol" on first use in homepage copy.

4. **Medium impact, medium effort:** Replace "domain-spec factory" and "vertical packs" with accessible alternatives throughout the homepage.

5. **Low impact (already good):** Kernel page and README terminology usage. Both surfaces handle term introduction well. Minor improvements only (remove "SDD" acronym, add Sigstore/Rekor explanation on homepage attestation section).
