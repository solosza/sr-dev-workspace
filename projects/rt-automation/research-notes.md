# Research Notes: ROI / Pricing / Competitive Comparables

**Task:** 001 (274 RT Compliance Business Plan) | **Reuses:** `compliance-research/go-no-go.md`, `compliance-research/market-and-switching.md` cited figures — not re-derived here.
**Scope:** New comparables beyond what 269 already cites, for the business plan's ROI/Pricing/GTM sections (tasks 002-004).

---

## 1. SNF/Therapy Claim Denial & Clawback Cost Context (beyond 269)

269 already established the system-wide baseline (35-56% MA SNF denial rates, 79.1% of 2023 improper payments from documentation failures, $6.8B FY2025 FCA recoveries, $5.9B SNF improper-payment scale — `market-and-switching.md` §2.1-2.2). This pass searched specifically for a closer SNF-RT/therapy FCA comparable than the non-SNF $852,378 respiratory-therapy settlement 269 already flagged.

- **Symphony Healthcare Facilities — $300,000 settlement (May 2026):** three affiliated Illinois SNFs resolved False Claims Act allegations for submitting claims for **medically unnecessary rehabilitation services** (DOJ press release + matching HHS-OIG enforcement page, both accessed 2026-07-22). This is a **closer comparable than the 269 figure** — same facility type (SNF) and same failure mode category (medical-necessity/therapy-utilization overbilling) — but "rehabilitation services" in DOJ releases typically spans PT/OT/SLP and is not confirmed to include RT/respiratory-specific billing. **Flag: closer but still not RT-specific — do not present as an RT settlement without that caveat.**
- **St. Margaret's Center — $1.3M settlement (Feb 2026):** grossly-substandard-care allegations that explicitly named failure to provide **respiratory and tracheostomy care** among the deficiencies (DOJ, Northern District of NY, accessed 2026-07-22). This is a quality-of-care/CMP case, not a billing/coding FCA case — **not usable as a clawback/billing-cost comparable**, but worth citing in the business plan's risk section as evidence that respiratory-specific care deficiencies are an active enforcement target at SNFs.
- **No SNF-RT-specific billing/coding FCA settlement was found in this pass either.** Combined with 269's own search, this gap now reflects two independent research passes. **Recommendation for task 004: state the gap explicitly rather than search a third time** — the honest framing is "no SNF-RT-specific clawback settlement is publicly documented; the closest comparables are a non-SNF RT settlement ($852,378, unlicensed personnel) and an SNF rehab-therapy settlement of unconfirmed RT-scope ($300,000, Symphony, 2026)."
- **Per-claim labor-correction cost:** still not found (269 already searched; this pass did not re-search, per the task's instruction not to re-derive 269's own gap-finding). **This unverified number remains OWNER/EXPERT-TO-CONFIRM — do not fabricate a figure for the business plan.**

---

## 2. Pricing Models — SNF Compliance / Billing-Integrity / RCM Tools

Three pricing structures recur across the market, each with a source-quality caveat:

### 2.1 Per-facility / per-bed SaaS subscription
- SNF compliance/EHR platforms (PointClickCare-class) typically price **$150-$300 per bed/month** depending on modules and facility size (aggregator estimate — WifiTalents/ITQlick-class sites, accessed 2026-07-22; **self-reported/estimated by review-aggregator sites, not sourced from a vendor rate card — treat as directional, not quoted**).
- PointClickCare's own general pricing is quote-based; third-party aggregators cite a **$300/user/month** starting point and **$500-$1,000/month for a small clinic** (ITQlick/FindEMR, accessed 2026-07-22 — **same caveat: aggregator-estimated, not PCC-published**).
- **Recommendation for a single-facility pilot:** a flat per-facility monthly SaaS fee is the cleanest fit for the cousin's segment (owner-operator, fast decision, no CFO-gated procurement per `market-and-switching.md` §3) — avoids the metering/trust friction of a percentage-of-collections or per-claim model with a first pilot customer.

### 2.2 Per-claim pricing
- Some RCM vendors charge **$5-$25 per claim processed** (PUREDI/Practolytics-class RCM pricing surveys, accessed 2026-07-22 — **industry-survey aggregation, not a single named vendor's published rate**).
- Fit assessment: per-claim pricing scales naturally with facility census/billing volume, but is a harder pitch for a compliance *gate* tool (which runs on every claim regardless of outcome) than for a recovery tool (which only runs on claims with identified issues) — worth naming as an option but not the lead recommendation.

### 2.3 Percentage-of-collections / rev-share
- Comprehensive RCM services commonly price at **3-7% of monthly collections** (CareCloud-class vendors) or more broadly **4-8% of monthly collections** (Denial Journal/getmonetizely-class sourcing, accessed 2026-07-22 — **industry-survey aggregation, not this system's own vendor comparable**).
- Enterprise SaaS RCM subscriptions for hospital-scale systems run **$10,000-$75,000+/month**, with hybrid models (flat per-clinician base + a smaller collections percentage) also common (same sourcing, accessed 2026-07-22).
- Fit assessment: rev-share models fit "revenue recovery" tools (e.g., Revecore's ReClaim, below) better than a **pre-submission validate-and-flag gate** — a rev-share fee on a system that prevents bad claims (rather than recovering already-denied ones) is harder to attribute and measure, and risks the exact FCA "cause" exposure `go-no-go.md` flags (a rubric with a financial incentive to find claims billable). **Recommendation: avoid rev-share/percentage-of-collections for this system's pricing — it works against the liability-first, never-auto-bill positioning task 002/004 require.**

### 2.4 Recommended pricing for the single-facility pilot
Flat per-facility monthly SaaS fee, priced below the low end of the $150-300/bed/month EHR-platform range (this is an add-on compliance gate, not a full EHR) — a specific dollar figure should be set by the business plan (task 003) using facility bed-count once known, not asserted here as a researched market rate.

---

## 3. PointClickCare Advisor Suite — Positioning & Pricing Signals

Confirms and extends `market-and-switching.md` §4.2 (same launch, additional pricing/positioning detail):

- **Billing Advisor** is described in PCC's own press release (PR Newswire + pointclickcare.com, both accessed 2026-07-22) as scanning clinical documentation to identify **missed charges** and billing-code mapping, producing ancillary batches for review — PCC's own language leans toward **revenue capture** (finding billable services that would otherwise be missed), not explicitly toward **denial/compliance prevention** (catching claims that shouldn't be billed). This is a positioning nuance beyond what 269 captured: **Billing Advisor's stated job is revenue-forward, this system's stated job is compliance/liability-forward — genuinely different framing even though both touch "before claims submission."** Worth naming explicitly in the business plan's competitive-differentiation section, not just "PCC does something similar."
- Availability: PCC states Billing Advisor is **already available today to all skilled nursing providers using the PointClickCare EHR** (same press release) — i.e., zero-incremental-cost distribution to the entire existing PCC install base, a distribution advantage this system cannot match.
- No Billing-Advisor-specific price was found (PCC's pricing pages are quote-based, consistent with 269's finding of a $65/month FHIR API tier as the only published PCC price point). **This remains an open item — do not assert a Billing Advisor price in the business plan; state it is bundled/included for PCC EHR customers per the press release, not separately priced.**

---

## 4. Source-Quality Summary (self-reported vs independent)

| Claim | Source type | Independent? |
|---|---|---|
| Symphony $300K SNF rehab-therapy settlement | DOJ + HHS-OIG press releases | Independent (government primary source) |
| St. Margaret's $1.3M respiratory-care CMP case | DOJ press release | Independent (government primary source) |
| $150-300/bed/month SNF software pricing | Review-aggregator sites (WifiTalents, ITQlick) | Self-reported/estimated — not vendor-published |
| PCC $300/user/month, $500-1000/mo small clinic | Aggregator sites (ITQlick, FindEMR) | Self-reported/estimated — not PCC-published |
| $5-25/claim RCM pricing | Industry pricing-survey blogs | Aggregated industry survey, not a single named vendor quote |
| 3-8% of collections RCM pricing | Industry pricing-survey blogs (CareCloud cited) | Aggregated industry survey; CareCloud figure attributed but not independently verified against CareCloud's own rate card |
| PCC Billing Advisor "missed charges" framing + free-to-existing-customers | PCC's own press release | Vendor-published (self-reported by PCC, but a primary vendor statement, not a third party's estimate) |

## 5. Open Items / To-Confirm (do NOT fabricate resolution in the business plan)

1. **SNF-RT-specific clawback/FCA settlement dollar figure** — not found across two independent research passes (269 + this pass). State as an open item.
2. **Per-claim labor-correction cost for RT billing specifically** — not found (269's original gap, not re-searched here per task scope). Owner/expert-to-confirm.
3. **Exact pilot pricing figure** — a specific dollar amount depends on the cousin's target facility's bed count, not yet known; task 003 should recommend a *model* (flat per-facility SaaS, per §2.4) and leave the number as a pilot-negotiation variable, not a researched market rate.
