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

## Legal Viability — "Original Source" Question: RESOLVED

The 2010 ACA amendment changed the FCA's "original source" requirement. You **no longer need direct and independent knowledge** of the fraud. You need to **"materially add"** to publicly disclosed information (31 U.S.C. 3730(e)(4)).

**This means:** Taking public data (USASpending + IRS 990s + SAM.gov) and connecting dots nobody else connected = materially adding. The fraud patterns may exist in public records, but assembling them into a cross-referenced evidence package that expands scope, adds timeframe, or establishes defendant knowledge IS the material addition.

AI-discovered fraud from public data qualifies as long as the analysis goes beyond what's already publicly known as a fraud allegation. We're not forwarding news articles — we're building evidence packages from 8+ databases that no human assembled.

## Investigation Loop — "Follow the Money" in Practice

The agent runs a 6-layer investigation loop per entity, all from public data:

**Layer 1: Who Got Paid?** (USASpending.gov API — free, daily updates)
- Every federal award is public: recipient, amount, program, date
- Scan for awards to entities matching fraud patterns

**Layer 2: Are They Real?** (IRS 990 + SAM.gov + Secretary of State)
- IRS 990: 3M+ filings searchable on ProPublica. Revenue vs. award size mismatch = red flag
- SAM.gov: registration date, exclusion/debarment status
- State incorporation: formation date, address, officer names

**Layer 3: Where Did It Go?** (990 expense analysis + county records)
- 990 expense categories: if $10M nutrition award but $0 food costs = flag
- Officer compensation vs. program spending ratio
- County assessor records: did officers buy property after large awards?

**Layer 4: Who Are These People?** (OSINT)
- PACER: prior fraud convictions ($0.10/page)
- OFAC SDN: sanctioned individuals
- OpenCorporates: officers running multiple grant-receiving entities
- Public profiles: does org's claimed capacity match its staff?

**Layer 5: Connect the Network** (cross-entity analysis)
- Same address across multiple recipients
- Same officers across multiple entities
- Related-party transactions visible in 990 disclosures
- Geographic clustering of awards to entities with no local presence

**Layer 6: Build the Case** (evidence package for attorney)
- Timeline: entity creation → award → spending anomalies
- Every claim sourced to a public record with URL
- Estimated fraud amount calculated
- Mapped to specific FCA violation elements

## Execution Architecture — run-task.sh Based

The fraud detection loop runs as a scheduled agent pipeline via `run-task.sh`:

```
Daily cron → run-task.sh fraud-scan-repo →
  Task 1: Ingest new USASpending awards (API pull)
  Task 2: Cross-reference against IRS 990 database
  Task 3: Cross-reference against SAM.gov
  Task 4: Apply fraud pattern scoring
  Task 5: Deep-dive flagged entities (PACER, state records, OSINT)
  Task 6: Generate evidence packages for high-score findings
  Task 7: Alert Isagawa team of new findings
```

Each task is a spawned `claude -p` agent operating under kernel enforcement. The pipeline runs daily, scanning every new federal award. Zero marginal cost per investigation.

## Public Data Access — All Free or Low Cost

| Data | Source | Cost |
|------|--------|------|
| Federal awards | USASpending.gov API | Free |
| Nonprofit 990 filings | ProPublica Nonprofit Explorer | Free |
| Entity registration | SAM.gov API | Free |
| State incorporation | Secretary of State websites | Free |
| Federal court records | PACER | $0.10/page |
| Sanctioned entities | OFAC SDN List | Free |
| Corporate officers | OpenCorporates | Free tier |
| Real estate records | County assessor websites | Free |
| FinCEN alerts | FinCEN.gov | Free |

## What Still Needs Research
- Which federal programs have the highest fraud rates (target those first)
- State False Claims Acts — additional reward channels (many states have their own)
- SEC whistleblower program (10-30% for securities fraud) — separate channel
- IRS whistleblower program (15-30% for tax fraud over $2M) — separate channel
- How to structure Isagawa's legal entity for qui tam filings
- Attorney partnership model — qui tam attorneys typically work on contingency
- Optimal cron schedule and API rate limits for daily scanning

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
- **Deliverable:** Phase 1: Attorney partner identification + engagement letter. Phase 2: Fraud-scan repo with run-task.sh pipeline (daily USASpending ingest → cross-reference → score → evidence package). Phase 3: First batch of findings submitted through attorney.
- **Scope:** BUILD
- **Constraints:** Legal viability confirmed (materially adds standard). Need qui tam attorney on contingency. All data public records only. Pipeline runs via run-task.sh + cron in dedicated fraud-scan repo. Kernel enforces investigation quality gates.
