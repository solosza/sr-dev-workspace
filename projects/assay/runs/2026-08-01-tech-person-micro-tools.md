# Assay — "The tech person for people who don't have one" (done-for-you micro-tools)

**Date:** 2026-08-01 · **Idea source:** operator (mine) · full input at `projects/tech-person-business/idea.md`
**Verdict: PARK -> GO-IF one paid customer.** The build capability is proven and the referral channel is genuinely strong (it solves the reachability killer that sank the two adjacent SMB-services ideas in the ledger). But every data point so far is one unpaid favor for a friend. Demand at a real price is untested, so nothing green-lights yet. Two of three (market + build) pass; demand is the open gate.

## Prior-art note
Two adjacent runs exist (2026-07-30): "build-first local website agency" and "AI-automation agency (Katou)." Neither is a meaning-match. They differ on mechanism (cold-build-first websites / n8n workflows vs. generic bespoke tools) and on distribution (cold outreach / vertical channel vs. REFERRAL). Their shared lesson (reachability is the recurring killer for SMB services) is inherited here, and the referral model is the direct answer to it.

## Normalized idea
- **value:** my specific manual problem becomes a working tool, done for me, without touching anything technical
- **who_pays:** non-technical individuals and small teams (proof: a home-care nurse's team)
- **mechanism:** AI-accelerated bespoke micro-tool + full-stack delivery (accounts, DB, hosting, deploy, test), distributed by referral inside a niche
- **legitimacy:** real business, operator is the doer (not selling a how-to). Note: the surrounding "AI agency" space is guru-hyped; that down-weights copycats, not this doer.

## Abstraction ladder
1. Literal: build custom micro-tools for non-technical people, referral-driven
2. Pattern: the outsourced technical co-founder / IT department for those who can't or won't hire one
3. Capability: AI collapses software delivery cost below the old floor, so the long tail of tiny bespoke needs becomes individually serviceable
4. Market: the "too small for a dev shop" long tail of manual micro-processes

## Wedges (survivors ranked, then killed, nothing discarded)

### SURVIVORS
1. **Payer-swap to the org (highest ceiling).** `lens: payer-swap · rung 2`
   Sell one templated tool to the entity that has MANY identical small-team processes and a budget: a home-care agency, franchise HQ, staffing agency, or professional association, deployed across all its locations or members.
   **Opening:** the multi-location / multi-member org whose tiny recurring processes are beneath any vendor's attention but painful at scale. Flips the model from one-tool-per-person (your bottleneck) to one-build-many-seats. Ladders up from an individual referral (nurse -> her agency's ops manager). fit: **conditional**.
2. **Nail ONE referral-clustered niche + templatize.** `lens: adjacent + zoom · rung 0-1`
   Start where you have proof: small home-care / visiting-nurse teams (shared schedules, visit sign-ups, shift swaps). Reuse the tool as a near-configurable template for the next team.
   **Opening:** enterprise scheduling tools (When I Work, Connecteam) are too heavy and pricey for tiny teams; referral trust + a purpose-fit template beats them. This is the escape from the bespoke-services trap. fit: **high**.
3. **Package as "your on-call tech person" (recurring wrapper).** `lens: constraint-break · rung 1`
   Flat monthly for the segment that wants an ongoing person, not a project: small tools + tweaks + hosting under one subscription.
   **Opening:** converts one-shot builds into recurring revenue and smooths the solo-capacity problem. This is the monetization wrapper for #2, not a separate business. fit: **high**.
4. **Done-for-you automations / integrations, governed-niche + fixed-package only.** `lens: transpose · rung 2`
   Same "I handle the plumbing" mechanism, different artifact: glue their existing tools (booking -> calendar -> SMS) instead of a bespoke app.
   **Opening (constrained by prior art):** only survives via a warm/vertical channel + fixed packages + a governance edge; heavier to deliver and maintain. Run only after #2 proves out. fit: **conditional**.
5. **Replicate the niche-template playbook into a second vertical (trades).** `lens: adjacent · rung 0`
   Once #2 works, repeat in plumbers/electricians/landscapers (job booking, quote forms, follow-up trackers). Validates that the compounding thesis is not nurse-specific. fit: **high**. (Second move, not first.)

### KILLED (preserved as content + revisitable)
- **Builder-kit for other AI-agency solopreneurs.** `payer-swap` · KILL: sells to hype-driven aspirants, guru-saturated (course-sellers), low realizability. Cousin of the ledger's "wrap assay in a UI for <$10" kill.
- **Done-for-you data cleanup / spreadsheet-to-system.** `transpose` · KILL (soft): every job unique, resists templating, pure services with no compounding.
- **Vertical-SaaS last-mile customization partner.** `payer-swap` · KILL: needs enterprise BD and long sales cycles a solo referral operator cannot run. Wrong channel. Revisit later.
- **Broad catalog of 10 templated micro-tools.** `zoom-out` · KILL (soft): premature horizontal; spreading across tool types fights the niche-clustering advantage. Nail one niche first.
- **Teach the model / agency-in-a-box.** `invert` · KILL: classic sell-the-blueprint; abandons the real business and manufactures your own competitors.

**Quotas:** transpose met (automations, data). payer-swap met (org, platform). Not a divergence-failure.
**Bias-check:** survivors lean on the proof point, but the #1 by merit (payer-swap to org) is a genuine distance move ranked above the easiest/highest-fit wedge, so no bias-failure flag. Fit shown as a tag only, never ranked.

## Buildability (Step 2)
All five survivors are BUILD (the operator shipped the proof in an afternoon; the plumbing is now a reusable template; free hosting tiers keep build_cost near zero). **compounds = YES** is the whole thesis: each niche build becomes a template. #1 (org) needs a light multi-tenant seat model. #4 (automations) is heavier and carries more maintenance/liability, so BUILD-CONDITIONAL. hitl_line: requirements-gathering + client acceptance stay human.

## Validation (Step 3) — cheapest decision-changing test, threshold pre-set
- **#2 (niche template):** ask the nurse for 3 intros to other small care teams. **PASS = >=1 team pays** (one-time or monthly) for the same tool within 30 days. Proves willingness-to-pay AND that referral converts. This is THE test; run it first.
- **#1 (org payer-swap):** ladder one referral up to an agency ops manager, pitch one tool deployed agency-wide. **PASS = >=1 org agrees to a paid pilot** (a setup fee or >= $500/mo an individual would never pay) within 30 days.
- **#3 (recurring wrapper):** offer 3 warm contacts a flat monthly "on-call tech person." **PASS = >=1 subscribes.**
- **#4 (automations):** one governed-niche automation as a fixed package for a warm referral. **PASS = paid.** Run only if #2 passes.

## Decision (Step 4) — market x build x demand
- market: PASS (real long-tail pain, AI why-now, referral reachability)
- build: PASS (proven, compounding templates)
- demand: **UNVALIDATED** (one unpaid friend). Green light requires all three, so: **no green light yet -> PARK, convert to GO on the paid-customer test.**

**Recommended first move:** wedge #2 (one referral-clustered niche + templatize) as the beachhead, priced via #3 (recurring), with #1 (org payer-swap) as the ceiling to ladder into once 2-3 teams pay. Speed-to-first-dollar is days, defensibility comes from the template library + referral graph, reuse is the core compounding loop.

**Riskiest assumption:** non-technical referral customers will pay real money (not just accept free favors), and enough per build to beat your hourly rate. Everything rides on this and it is completely untested.

**Kill-conditions:** no one pays within 30 days of a direct ask; or every job stays bespoke with no template reuse (then it is freelancing, not a business); or referrals never extend past the first friend.

**HITL:** commit `#2` (run the paid-customer test) · park · kill-all.
