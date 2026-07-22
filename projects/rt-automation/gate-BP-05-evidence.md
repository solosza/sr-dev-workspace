# Gate BP-05 Evidence — Scope-Boundary Gate

**Task:** 005-test-scope-boundary-gate.md | **Target:** `business-plan.md` | **Method:** grep + read

## Checks

**1. Boundary explicitly stated (never-auto-bill AND never-auto-chart AND never-automate-filtering)**
- `business-plan.md:12` — "**It never auto-charts. It never auto-bills. It never automates patient filtering.**" (SCOPE BOUNDARY section, load-bearing, stated first)
- Restated in Solution: `business-plan.md:42` — "Nothing about 'automating billing' or 'automating charting' is in scope, now or as a stated future phase"
- Restated in Risk & Compliance Posture: `business-plan.md:107` — "The never-auto-bill / never-auto-chart boundary is the liability firewall, restated here because this is where it matters most."
- Restated in Proof/Accuracy: `business-plan.md:61` — "This split is also why the product can never auto-bill"
- Restated in Pricing (rev-share rejection): `business-plan.md:85` — "conflicts with the liability-first, never-auto-bill positioning"
- **Result: PASS** — boundary present in Scope Boundary, Solution, Proof, Pricing, and Risk sections (5 of 9 section headers), not stated once and forgotten.

**2. Zero prohibited claims (automate billing submission, perform charting, auto-filter patients)**
- Grep pattern `auto-bill|auto-chart|auto-filter|automat` (case-insensitive) against `business-plan.md`: 8 matches (lines 12, 42, 49, 61, 85, 99, 107, 109, 116).
- Every match is a **negation or scope restriction** ("never auto-bills," "does not, and structurally cannot, automate," "not in scope," "browser automation against live PHI-bearing sessions" — itself a rejected fallback, line 116) — none assert the product performs auto-billing, auto-charting, or auto-filtering as a feature.
- **Result: PASS** — zero affirmative auto-workflow claims found.

**3. Positioning is liability/audit-defensibility, not automation speed**
- `business-plan.md:99` — "**Positioning — liability/audit-defensibility, not automation speed.**" Explicit GTM differentiation against PCC's Billing Advisor (revenue-forward, not compliance-forward).
- ROI section (lines 65-73) is framed entirely as avoided cost (denial avoidance, clawback/FCA avoidance, audit-defensibility), not generated revenue or speed.
- **Result: PASS**

**4. All five required section groups present**
| Group | Section(s) | Line |
|---|---|---|
| Problem | Problem | 16 |
| Solution | Solution | 33 |
| Proof | Proof / Accuracy Model | 53 |
| ROI/Pricing/GTM | ROI (65), Pricing (77), Go-to-Market (91) | 65-99 |
| Risk/Preconditions | Risk & Compliance Posture (103), Preconditions (111) | 103-120 |
- **Result: PASS** — all 5 groups present (9 section headers total including the Scope Boundary preamble).

**5. Unverified numbers flagged, not fabricated**
- `business-plan.md:70` — "No SNF-RT-specific billing/coding FCA settlement is publicly documented — this gap has now been checked across two independent research passes... and should be stated to the owner as an honest open item, not papered over with an extrapolated figure."
- `business-plan.md:73` — per-claim labor-correction cost explicitly marked "owner/expert-to-confirm... Fabricating that number to complete an ROI formula would violate the gate contract's 'never fabricate' rule."
- `business-plan.md:87` — pilot price point explicitly deferred to cousin negotiation, not asserted as researched market rate.
- **Result: PASS**

## Verdict

**GATE BP-05: PASS.** Scope boundary present (never-auto-bill / never-auto-chart / never-automate-filtering) in 5 of 9 sections, zero prohibited auto-workflow claims, positioning confirmed liability/audit-defensibility, all 5 required section groups present, unverified numbers flagged not fabricated.
