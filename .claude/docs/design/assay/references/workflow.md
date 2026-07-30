# Assay Workflow — Step Specs (v1: Loops 1-3 + Decide)

## Step 1 — Opportunity
**Purpose:** From one idea, produce a ranked set of capturable revenue wedges.
**Pre-generation checkpoint:** read [[lenses]] (the 6 divergence lenses), [[gates]] (the adversarial gate battery), [[io-contracts]] (Idea, Wedge). Contract: `contracts/step-01-contract.json`.
**Procedure:**
1. Normalize: strip the idea to `{ value, who_pays, mechanism }`.
2. Legitimacy: real business vs funnel; who actually earns (the doer vs the seller-of-the-how-to).
3. Abstract up: literal -> pattern -> underlying capability/market; keep each rung as a candidate root.
4. DIVERGE: apply the 6 lenses ([[lenses]]) to each rung -> candidate wedges. Generous, no killing yet.
5. GATE: run every candidate through the adversarial battery ([[gates]]), kill-by-default.
6. Find the opening: for survivors, name the un-easy part the crowd skips (distribution / integration / service / compliance).
7. Rank survivors by gate scores; emit `Wedge[]` ([[io-contracts]]).
**Output:** `Wedge[]` (may be empty = "no opening found").

## Step 2 — Buildability
**Purpose:** Decide, per surviving wedge, whether the operator can build + automate + govern it with an edge.
**Pre-generation checkpoint:** read [[io-contracts]] (Wedge in, BuildVerdict out); input = Step 1's `Wedge[]`. Contract: `contracts/step-02-contract.json`.
**Procedure:**
1. For each `Wedge`, score: buildable (reuse stack vs new), automatable_pct + HITL line, moat_applies (does governance/audit make our version defensible), compounds (stacks on existing builds), build_cost, strategic_dividend.
2. If "can't build the literal wedge, but could build the layer/tool for it" -> emit a picks-and-shovels variant that RE-ENTERS Step 1's diverge (bounded: 1 hop).
3. Decide build / pass per wedge.
**Output:** `BuildVerdict[]` ([[io-contracts]]).

## Step 3 — Validate
**Purpose:** Cheapest real-world signal before recommending commit.
**Pre-generation checkpoint:** read [[io-contracts]] (ValidationResult); input = build-viable wedges from Step 2. Contract: `contracts/step-03-contract.json`.
**Procedure:**
1. For each build-viable wedge, pick the single cheapest test that would CHANGE the decision (landing page + ad spend / N cold outreaches / one concierge delivery).
2. Define the pass threshold up front (X signups / Y replies / 1 paying pilot); time- + cost-box it.
3. v1: propose the test + threshold; the operator may run it. Record `signal` + `pass`.
**Output:** `ValidationResult[]` ([[io-contracts]]).

## Step 4 — Decide
**Purpose:** Intersect the three verdicts and hand back a ranked shortlist for the human commit.
**Pre-generation checkpoint:** read [[io-contracts]] (Decision), [[state-schema]] (ledger). Contract: `contracts/step-04-contract.json`.
**Procedure:**
1. Green light = market (survived Step 1) x build (Step 2 = build) x demand (Step 3 = pass).
2. Rank green-lit wedges by (speed-to-first-dollar x defensibility x reuse-with-existing-builds).
3. Append the full run (idea, all verdicts, decision) to the ledger ([[state-schema]]).
4. Present the ranked shortlist + each wedge's single precondition-to-clear-first.
**HITL:** the human picks which wedge (if any) to actually pursue — the only real-world commit. Any ambiguous gate from Steps 1-3 surfaces here for a human call.
**Output:** `Decision` (ranked shortlist + preconditions).
