# Assay — Idea → Capturable-Revenue Engine (Design)

**Status:** BUILT 2026-07-30 — grew from a single idea-engine into a **9-command venture-loop family** (see "The venture-loop system" below). This doc = the system spec (commands + dependencies) + the original assay-engine design kept for lineage.
**Emerged:** 2026-07-30, from manually vetting hustle reels (surplus recovery, YouTube nursery-rhymes, AI real-estate video). That manual vetting WAS the prototype.

## Goal
From any idea (mine, or pulled from anywhere on the internet), surface the revenue streams **I can actually capture** — ranked by **speed-to-first-dollar and defensibility**, favoring ones that **reuse/compound with what I already own** — and get **sharper every pass**.

## Metaphor
Raw idea = ore. Assay = test for real value + extractability. Output = the **lode** (capturable, buildable revenue) or a **fast kill**.

## Core principle
**Diverge wide, converge hard.** Generation is generous (weird welcome); gates are adversarial, **kill-by-default**. Separate the two modes or it becomes a rationalization machine. Same shape as the kernel's fan-out -> adversarially-verify -> rank.

---

## The venture-loop system (built 2026-07-30)

Assay is the origin; the system is a **family of governed loops** that carry a business from idea -> money. Each loop is a command + a lean single-file skill, **standalone + modular** (callable alone or as a sub-step by another loop).

### Commands (9)

| Command | Loop | One-liner | Kind |
|---------|------|-----------|------|
| `/source` | Source/Scan | surface + dedup + rank ideas -> feeds assay | queue |
| `/assay` | Idea-worth | diverge + kill-by-default -> capturable shortlist | kill |
| `/competition` | Arena | rivals + gaps + winning angle | kill |
| `/deep-dive` | Validate | evidence -> go/no-go + first-90-days plan (calls `/competition`) | kill |
| `/offer` | Offer/Pricing | package + price to capture, honestly | kill |
| `/gtm` | Go-to-Market | channel + funnel to get customers | kill |
| `/launch` | Build/Launch | ship the smallest sellable thing (reuse-first) | kill |
| `/operate` | Operate | run it, propose -> human approves | govern |
| `/sharpen` | Learn/Meta | outcomes -> propose engine upgrades | meta |

### Chain
`/source -> /assay -> /competition -> /deep-dive -> [GO] -> /offer -> /gtm -> /launch -> /operate`; `/sharpen` reads all.

### Dependencies
- `/source` **feeds** `/assay` (hands it ranked candidates).
- `/deep-dive` **calls** `/competition` (reuses the arena read; doesn't repeat it).
- `/sharpen` **reads** every loop's ledger + the venture records (to propose upgrades).
- **Every loop writes** the venture record `projects/assay/ventures/<slug>.md` — the cross-loop journey (Stage · Verdict · Next-action + a Journey table). Dashboard: `ventures/INDEX.md`.
- **All loops standalone + modular:** a missing upstream input is gathered/asked, never required.

### Two phases
- **Pre-GO** (`/source`->`/assay`->`/competition`->`/deep-dive`): light, adversarial, **kill-fast** — burn ideas, not money.
- **GO line** = `/deep-dive` go/no-go.
- **Post-GO** (`/offer`->`/gtm`->`/launch`->`/operate`): real spend, **heavier HITL** (propose -> approve) — the kernel's governance.

### Shared conventions (every loop)
- **Prior-art check** at start (dedup vs its ledger, match on meaning).
- **Kill-by-default** (pre-GO + offer/gtm/launch) or **govern-by-default** (`/operate`).
- **One HITL commit** — the loops never act; the human decides.
- **Lean output** — quickest view, never long docs.
- **Persist 3-layer:** readable report (`projects/assay/<loop>/runs/`) + ledger (`.claude/skills/<loop>/state/ledger.jsonl`) + index; plus the venture record.

### Where it lives
- Commands: `.claude/commands/kernel/<name>.md` · Skills: `.claude/skills/<name>/SKILL.md` (lean single-file; deeper per-loop design/contracts can come later) · Output + state: `projects/assay/` · One-screen map: `projects/assay/roadmap.md`.
- **Future:** lift the whole system into its own kernel-governed spec repo when it grows (frees this workspace).

*The "Architecture — 5 loops, 2 tiers" below is the ORIGINAL assay-engine design — now realized as `/assay`'s internal steps (Opportunity/Buildability/Validate) plus the extracted `/source` and `/sharpen`. Kept for lineage.*

---

## Architecture — 5 loops, 2 tiers

### Tier 1 — TRIGGERED (fire on an idea)

**Loop 1 — Opportunity** (is there a real, capturable, defensible revenue stream?)
- capture -> normalize: value / who pays / mechanism
- legitimacy: real business vs funnel; who *actually* earns (doer vs seller-of-the-how-to)
- abstract up: literal idea -> pattern -> underlying capability/market (evaluate each rung)
- **DIVERGE (6 lenses):** adjacent (same capability, new market) · transpose (mechanism -> far domain) · recombine (+ an asset I already own) · invert / picks-and-shovels (sell *to* the crowd, be the layer) · constraint-break (target who won't DIY; drop the assumed limit) · zoom (category tool <-> hyper-niche)
- **GATES (adversarial, kill-by-default):** legal/reg · unit economics · saturation · timing/"why now" · moat · fit-to-me · speed + cost-to-first-dollar · recurring vs one-shot
- find the opening: the un-easy part the tutorial crowd skips (distribution, integration, service, compliance)
- **output:** ranked surviving wedges (highest rung with a real opening, or "none")

**Loop 2 — Buildability / Isagawa-fit** (can/should WE build it, with an edge?)
- buildable: reuse the stack (ALA scrapers/data, kernel, agents, check-5-layer-style gates) vs new
- automatable: how much + where's the HITL line (90%-manual = not our leverage)
- governance-moat applies?: does audit/compliance/HITL make *our* version defensible, or does governance add nothing
- compounds: stacks on what we're already building
- build economics: speed to a shippable MVP from existing parts
- operable: runs as a low-babysit governed pipeline
- strategic dividend: does building it also strengthen Isagawa (new reusable capability / dogfood)
- **output:** build / pass + the build-path

**Loop 3 — Validate** (cheapest real test before committing)
- pick the single cheapest signal that would CHANGE the decision: landing page + small ad spend (demand) · N cold outreaches (B2B interest) · one manual concierge delivery (will they actually pay)
- pass = a pre-set threshold (e.g., X signups / Y replies / 1 paying pilot); below -> kill. Time- and cost-boxed.
- **output:** ValidationResult (signal + pass/kill)

**GREEN LIGHT = intersection:** viable market × we-can-build-with-edge × validated demand.

### Tier 2 — AMBIENT (run continuously / background = self-improvement)

**Loop 4 — Source/Scan** — hunt ideas + catalysts from the internet.
- sources: trend feeds, competitor moves, new-tool launches, reg/platform shifts, my own inbox of reels/links
- filter before feeding Loop 1: does it map to a capability we have or a market we understand, AND is there a "why now" catalyst? dedupe against the ledger (don't re-run seen ideas)
- also writes freshness into the world-model (saturation / tools / reg snapshots)

**Loop 5 — Learn/Meta** — sharpens all loops:
- outcome calibration: log verdict (kill/park/go) vs later ground-truth (go -> revenue? kill -> someone else won?) -> tune which gates over/under-fire
- kill-pattern library (anti-library): structured death-reasons -> faster kills; "everyone dies on X" -> X *is* the opportunity
- internet refresh: re-scan saturation / tools / reg -> verdicts don't go stale
- lesson ingestion: kernel lessons + external post-mortems -> new gates/lenses
- versioned gates + lenses: missed opening -> add a lens; flopped go -> tighten a gate

---

## Coupling (a cycle, not silos)
- Loop 2 "can't build the literal thing, but could build the governance/automation layer for it" -> re-enters **Loop 1's DIVERGE** (picks-and-shovels).
- Loop 3 outcomes -> Loop 5.
- Loop 5 -> updates the gates/lenses used by Loops 1 + 2.
- Loop 4 -> keeps Loop 1/2 gates' world-model fresh.

## State & Persistence (the substrate)
Self-improvement + audit need durable stores (kernel-style append-only files, git-friendly to start):
- **ledger** — every run: idea, per-loop verdicts, final decision, timestamp (the audit trail)
- **outcomes** — ground-truth attached to past verdicts later (go -> revenue? kill -> won elsewhere?) for calibration
- **anti-library** — structured kill-patterns: reason -> count -> "everyone dies on X" flag
- **world-model** — saturation / tools / reg snapshots per domain, with freshness timestamps (Loop 4 refreshes)
- **registry** — versioned gates + the 6 lenses (Loop 5 evolves them)

## I/O Contracts (loops are pure functions: in -> out)
- **Idea** (in): {source, raw, normalized:{value, who_pays, mechanism}}
- **Wedge** (Loop 1 out): {abstraction_rung, lens_origin, description, opening, gate_scores, rank}
- **BuildVerdict** (Loop 2 out): {wedge, buildable, automatable_pct, hitl_line, moat_applies, compounds, build_cost, strategic_dividend, decision}
- **ValidationResult** (Loop 3 out): {wedge, test, signal, pass}
- **Decision** (green light): {wedge, market x build x demand, next_action, precondition}
Defined contracts = task-builder can decompose + test each loop independently.

## Orchestration & HITL
- **Triggered pipeline:** Idea -> Loop 1 -> (per surviving wedge) Loop 2 -> (per build-viable) Loop 3 -> Decision. Sequential, autonomous.
- **Re-entry:** Loop 2's picks-and-shovels variant auto-re-enters Loop 1's DIVERGE, bounded to 1 hop (no infinite loops).
- **Ambient:** Loops 4 + 5 run on a schedule / on-demand, independent of triggered runs.
- **HITL is minimal — Assay is a RESEARCH engine, it does NOT act.** The loops run autonomously; a human enters only at (1) the **terminal commit** — which validated wedge to actually pursue/build (the real-world spend decision) — and (2) **ambiguity escalation** — a gate that can't confidently kill-or-keep flags for a human instead of forcing it. No per-step approval. The kernel's mandatory-HITL applies DOWNSTREAM, when a chosen wedge is actually built/operated — outside Assay.

## Portfolio (cross-idea compounding)
Verdicts accumulate in the ledger; a portfolio view ranks ACROSS ideas by (speed-to-$ x defensibility x reuse-with-existing-builds) and clusters ideas that stack on the same reusable capability — delivering the goal's "compounding" (a prioritized queue, not isolated verdicts).

## Build notes
- Kernel-governed loops: deterministic gates + judgment layer + a decision + an audit trail.
- Triggered by feeding an idea; Tier-2 loops run ambiently.
- NO CODE yet — this doc is the input for `/design` + the build pipeline.
