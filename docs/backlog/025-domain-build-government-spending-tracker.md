# AI-Powered Government Fraud Detection — Whistleblower Revenue Play

## Status
Open

## Priority
High — validated by active federal crackdown; direct revenue via qui tam whistleblower rewards (15-30% of recovered funds)

## Summary
Build an internal Isagawa tool that uses AI agents to autonomously scan public government spending data, detect fraud patterns, and generate evidence packages for qui tam (whistleblower) filings under the False Claims Act. Isagawa finds the fraud, files the claim, collects the reward.

This is not a SaaS product for others. This is Isagawa's own fraud-hunting operation — the agent does the detective work, we file the claims through a qui tam attorney, and collect 15-30% of recovered funds.

## Revenue Model — Qui Tam Whistleblower Rewards

Under the False Claims Act (31 U.S.C. 3730):
- **15-25%** of recovered funds if the government intervenes and prosecutes
- **25-30%** if the government declines and we pursue independently
- Damages are **trebled** (3x the fraud amount) — reward is percentage of the trebled amount
- FY2024 was a record year: 979 qui tam suits filed, $2.4B+ in settlements/judgments

**Example math on Minnesota-scale fraud:**
- Feeding Our Future: $300M stolen
- Trebled damages: $900M
- Whistleblower share (15-25%): $135M - $225M
- Even a small case finding $10M in fraud → $4.5M - $7.5M reward

## How the Agent Works

The agent autonomously:
1. **Scans** USASpending.gov for new federal awards daily
2. **Cross-references** each recipient against IRS 990 filings, SAM.gov registration, state incorporation records
3. **Flags** entities matching fraud patterns (see below)
4. **Deep-dives** flagged entities — searches news, court records, social media, corporate filings for corroborating evidence
5. **Scores** each finding on a risk model (composite of all red flags)
6. **Generates** evidence package with sourced citations for attorney review
7. **Alerts** Isagawa team when high-confidence findings surface

The agent runs continuously. New grants are published daily. The agent watches.

## Validated Fraud Patterns (from Minnesota cases)
- **Feeding Our Future:** Nonprofit created to receive COVID school meal funding. $300M stolen. 98 defendants, 64 convicted. Funds sent to Somalia via money services businesses.
- **Pattern 1:** Org created shortly before receiving massive government payout (no prior history)
- **Pattern 2:** Org not registered in IRS database but receiving federal funds
- **Pattern 3:** Total prior revenue disproportionate to grant amount
- **Pattern 4:** Funds routed through money services businesses to high-risk countries
- **Pattern 5:** Missing or late federal disclosure filings
- **Pattern 6:** Multiple orgs at same address receiving separate grants
- **Pattern 7:** Rapid spend-down of funds with no program deliverables
- **Pattern 8:** Officers/directors with prior fraud convictions or sanctions
- **Pattern 9:** Org claims serving population that doesn't match geography or scale

## What Needs Research
- Exact qui tam filing process — do we need a law firm partner or can we file directly?
- Whether AI-discovered fraud qualifies as "original source" under the FCA (key legal question)
- Which federal programs have the highest fraud rates (target those first)
- Whether state False Claims Acts offer additional reward channels (many states have their own)
- SEC whistleblower program (10-30% for securities fraud) — separate channel
- IRS whistleblower program (15-30% for tax fraud over $2M) — separate channel
- How to structure Isagawa's legal entity for qui tam filings
- Attorney partnership model — qui tam attorneys typically work on contingency

## Data Sources
- **USASpending.gov** — federal award and subaward data (REST API, updated daily)
- **IRS 990** — nonprofit tax filings (ProPublica API or IRS bulk download)
- **SAM.gov** — entity registration and exclusion data (API)
- **Treasury** — disbursement records, Geographic Targeting Orders
- **FinCEN** — alerts, suspicious activity report aggregates
- **OFAC SDN List** — sanctioned entities cross-reference
- **GuideStar/Candid** — nonprofit profiles
- **State incorporation records** — Secretary of State databases
- **PACER** — federal court records for prior fraud cases
- **OpenCorporates** — corporate officer cross-referencing

## References
- Treasury press release: https://home.treasury.gov/news/press-releases/sb0354
- Treasury action on Somali fraud: https://home.treasury.gov/news/press-releases/sb0358
- AML Intelligence: https://www.amlintelligence.com/2026/01/breaking-us-treasury-launches-minnesota-fraud-crackdown-audits-3000-gto-and-fincen-alert/
- False Claims Act qui tam rewards: https://www.schneiderwallace.com/practice-areas/whistleblower-claims/false-claims-act-qui-tam-whistleblower/false-claims-act-qui-tam-whistleblower-rewards/
- FCA overview: https://constantinecannon.com/practice/whistleblower/whistleblower-types/whistleblower-reward-laws/fca/
- USASpending.gov API: https://api.usaspending.gov/
- Context: $375B IRA/climate disbursements, Minnesota Feeding Our Future ($300M), Bessent crackdown

## Task Builder Input
- **Deliverable:** Phase 1: Research report on qui tam legal viability + attorney partner identification. Phase 2: Agent pipeline scanning USASpending.gov with fraud pattern matching. Phase 3: Evidence package generator for attorney review.
- **Scope:** RESEARCH (Phase 1), then BUILD (Phases 2-3)
- **Constraints:** Phase 1 is critical — must confirm AI-discovered fraud qualifies as "original source" before building. Need qui tam attorney consultation. All data public records only. Agent runs in sr-dev-workspace or dedicated fraud-detection repo.
