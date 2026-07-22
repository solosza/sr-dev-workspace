# RT Compliance Business Plan — Pre-Submission Validation Gate (for Facility Owners)

## Status
Open

## Priority
High — administrators are actively asking for a plan they can push to facility owners; the 269 research verdict is GO (conditional), which unblocks this Phase-2 deliverable.

## Summary
Produce the business plan facility OWNERS can act on, for the RT Medicare Part B **compliance/validation product** — scoped deliberately to the pre-submission validation gate, **not** full-workflow automation. The product reads the RT's existing PCC charting + the CPT codes about to be billed, runs the eligibility rules + three checks (deterministic hard-gates + model-assisted-with-human-review), and flags/blocks unsupported claims before submission with a queryable audit trail. It does **not** chart for the RT and does **not** push billing. Grounded in the 269 research (GO verdict, GTM, liability analysis).

## Scope Boundary (LOAD-BEARING — carry through the whole plan)
- **In scope:** a validate-and-flag compliance gate over charting/billing outputs; deterministic checks (Part A/B status, order presence, refusal flag, manual-review code list); model-assisted judgment (medical necessity, skilled-vs-custodial, charting-supports-CPT) with **mandatory human review**; full audit ledger of every decision + rationale.
- **Explicitly OUT of scope:** automating patient filtering, automating charting, and executing/submitting billing. The product **never auto-charts and never auto-bills** — this is the liability firewall, not a feature limitation.
- **Why:** 269's single highest-severity, least-mitigated risk is vendor-side False Claims Act "cause" exposure. A validate-and-flag product that never auto-bills stays on the safe side of that line; scoping in billing execution takes on that exposure directly.

## Requirements
- **Problem** (for owners): manual, ungated compliance → frequent human error (ranked error modes from `domain-and-compliance.md` §5, led by Part A/B miscoding and refused-treatment-billed), denial/clawback exposure, and audit indefensibility (no queryable "why CPT X for Pt Y on date Z"). Anchor value to catching errors **before** submission — NOT to billing-labor savings.
- **Solution:** the pre-submission validation gate as scoped above; deterministic-vs-judgment split as the accuracy/defensibility argument; human-in-the-loop as a guarantee, not a caveat.
- **Proof/accuracy argument:** deterministic hard-gates catch the bright-line errors (#1 Part A/B, #2 refusal) with certainty; model-assisted+human-review addresses the judgment errors (#3 necessity, #4 wrong CPT) without converting a human error into a systematic auto-billed one.
- **ROI (for owners):** denied-claim + clawback avoidance, audit-defensibility, compliance-risk reduction — modeled against the incumbent manual cost. Use 269's cited system-level figures (documentation drove 79.1% of 2023 CMS improper payments; MA SNF denial 35-56%; FCA recoveries $6.8B FY2025) and clearly mark the two SNF-RT-specific numbers still unverified as pitch-deck gaps, not fabricated.
- **Pricing / business model:** evaluate per-facility SaaS, per-chart/per-claim-validated, and revenue-share-on-clean-claims — recommend one for the single-facility independent-SNF pilot.
- **Go-to-market:** administrators as champions → owner approval; pilot-first at the cousin's single-facility independent SNF (fast-decision segment where admin≈owner); on-the-ground RT validators as proof. Position on **liability/audit-defensibility**, not automation speed (per `market-and-switching.md` §3 and the PCC Advisor Suite competitive reality).
- **Risk & compliance posture:** HIPAA/BAA, the never-auto-bill billing-liability boundary, human-review guarantee, and the four gating preconditions from `go-no-go.md` (BAA in writing, PCC API access, judgment-accuracy baseline, audit-ledger export validated vs a real CMS audit) stated honestly as open items.

## References
- `projects/therapy-compliance-automation/go-no-go.md` (GO verdict, preconditions, de-risking actions, narrowed differentiation)
- `projects/therapy-compliance-automation/domain-and-compliance.md` (rules, error modes, workflow stages, the missing gate §4.5)
- `projects/therapy-compliance-automation/market-and-switching.md` (buyer, incumbent, PCC Advisor Suite, FCA/kill risks)
- `projects/therapy-compliance-automation/isagawa-feasibility.md` (3-layer + judgment-layer + audit-ledger fit)
- `docs/backlog/done/269-domain-research-therapy-compliance-automation/business-plan.md` (original stub structure this fulfils)
- `projects/rt-automation/01-design-baseline.md` (venture context, comp discussed)

## Task Builder Input
- **Deliverable:** `projects/therapy-compliance-automation/business-plan.md` — an owner-facing business plan for the compliance/validation-gate product (problem, solution, proof, ROI, pricing, GTM, risk posture), scoped strictly to validate-and-flag (never auto-chart, never auto-bill).
- **Location:** subproject:therapy-compliance-automation
- **Scope:** RESEARCH
- **Constraints:** Web research only to firm up ROI/pricing comparables (cite source + date; flag self-reported vs independent; do NOT fabricate the two unverified SNF-RT numbers — mark them as owner/expert-to-confirm). No code, no harness build (that is a separate future BUILD backlog gated on the preconditions). Runs in PARALLEL with the 270-273 kernel-fix pipeline — different files (projects/ vs runner/lib), no collision. Carry the never-auto-bill boundary and liability-first framing throughout.
