# AI-Powered Government Fraud Detection — Whistleblower Revenue Play

## Status
Open

## Priority
High — validated by active federal crackdown; direct revenue via qui tam whistleblower rewards (15-30% of recovered funds)

## Design Documents

| Document | Purpose |
|----------|---------|
| [[025-domain-build-government-spending-tracker/reporting-channels]] | 3 filing tracks: qui tam, FinCEN whistleblower, Treasury OIG/GAO |
| [[025-domain-build-government-spending-tracker/gaps-analysis]] | 8 identified gaps with severity ratings + phase mapping |

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

The agent runs a 7-layer investigation loop, all from public data:

**Layer 0: Discover New Fraud Patterns** (web scanning — runs before entity investigation)
- Scan investigative journalism sources daily: James O'Keefe, Fox News Digital, Project Veritas, local investigative reporters, ProPublica investigations, state auditor reports
- Monitor PACER for newly filed qui tam cases and DOJ fraud press releases
- Monitor state AG press releases for fraud indictments (CA, NY, TX, FL, IL — highest spend states)
- Scan Reddit (r/fraud, r/government, r/nonprofit), X/Twitter for trending fraud exposés
- Scan GAO reports and Inspector General reports for flagged programs/entities
- **Extract patterns:** For each discovered case, decompose into: entity type, fraud mechanism, dollar amount, data sources that could have caught it, red flags visible in public records
- **Add to pattern library:** New patterns get a Pattern ID (Pattern-NNN), added to the detection criteria automatically
- **Retroactive scan:** After adding new patterns, re-score all previously ingested entities against the new pattern — fraud that was invisible under old patterns becomes visible
- **Track sources:** Maintain a source watchlist with RSS/API endpoints for each source, last-checked timestamp, and hit rate (how often each source yields actionable patterns)

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
  Task 0: Pattern discovery — scan journalism, PACER, AG press releases, IG reports for new fraud cases
  Task 0a: Extract new patterns from discovered cases, add to pattern library
  Task 0b: Retroactive re-score of existing entities against new patterns
  Task 1: Ingest new USASpending awards (API pull)
  Task 2: Cross-reference against IRS 990 database
  Task 3: Cross-reference against SAM.gov
  Task 4: Apply fraud pattern scoring (all patterns including newly discovered)
  Task 5: Deep-dive flagged entities (PACER, state records, OSINT)
  Task 6: Generate evidence packages for high-score findings
  Task 7: Alert Isagawa team of new findings + new patterns discovered
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
| DOJ fraud press releases | justice.gov/fraud | Free |
| State AG press releases | State AG websites (CA, NY, TX, FL, IL) | Free |
| GAO reports | gao.gov | Free |
| Inspector General reports | oversight.gov (IG report aggregator) | Free |
| Investigative journalism | RSS/web scraping (O'Keefe, Fox Digital, ProPublica, local news) | Free |
| Qui tam case filings | PACER new case alerts | $0.10/page |
| Social media fraud tips | X/Twitter, Reddit (r/fraud, r/government) | Free |

## Real-World Fraud Cases — Pattern Library

These are documented cases that validate the fraud patterns above and expand the detection criteria.

### California Homeless Shelter Fraud (2026)
**Source:** CA Controller's Office admission (hidden camera), James O'Keefe investigation

- **CA Controller's Office admits audits "are not getting done"** due to staffing cuts — Acting Deputy Controller Bismarck Obando (Press Secretary for Controller Malia Cohen) confirmed on hidden camera
- **No statewide plan on homelessness** despite counties/cities requesting $1B/year
- **Abundant Blessings Inc.** — homeless shelter claiming to end homelessness via short/long-term housing. Received **$23M** in public funds. Executive director Alexander Soofer arrested for fraudulently obtaining the $23M. On-ground investigation found **zero homeless people** at the shelter.
- **Urban Alchemy** — claims to provide hygiene services and "safe sleep villages." Received **$60M+** in government contracts, including **$12M+ through LAHSA** since 2021. Homeless individuals reported shelters are always out of basic items (blankets, socks, toothpaste).
- **New patterns:**
  - **Pattern 10:** Nonprofit receives millions but physical location shows no evidence of services being delivered (empty shelters, no clients present)
  - **Pattern 11:** State/local auditing bodies admit they cannot conduct audits — creates cover for fraud at scale
  - **Pattern 12:** Homeless services nonprofits — high-fraud sector due to difficulty verifying beneficiary counts and service delivery
  - **Pattern 13:** LAHSA (LA Homeless Services Authority) as a conduit — track all LAHSA subgrantees for cross-referencing

### Salt Lake City Theater Land Deal (2026)
**Source:** Public records investigation

- City purchased historical theater for **millions of dollars**
- Theater sat empty for years, removed from tax rolls
- Building demolished and **sold to developer for $0**
- County simultaneously passed **property tax hike** on residents
- Developer was making **campaign donations** to politicians involved
- **New patterns:**
  - **Pattern 14:** Government purchases asset at high price → holds/demolishes → transfers to private developer at zero or below-market value
  - **Pattern 15:** Campaign donation correlation — track developer donations to officials who approved favorable deals
  - **Pattern 16:** Asset removed from tax rolls while publicly owned, then tax increases passed to cover the gap
  - **Pattern 17:** Government real estate transactions where purchase price >> sale price with no public benefit explanation

### #NoKings Protest Funding — Political Nonprofit Fraud (2026)
**Source:** Fox News Digital investigation, on-ground vendor identification

- "Flagship" #NoKings protest in St. Paul, MN was a **$250K professionally engineered production** presented as grassroots/spontaneous
- **9 identified paid vendors:** Slamhammer Sound ($100K), Fire Up Video ($20K), Algorithm AV ($25K), Common World Productions ($10K), Warning Lites of MN ($15K), E5 Energy ($15K), Ultimate Events ($30K), On Site Companies ($25K), Fast Kat Connects ($10K)
- Funded by **Indivisible** (Democratic nonprofit) — refused to respond to comment requests
- Senior advisor: **Roger Fisk** (former Obama/Biden political strategist)
- Protest partners included **pro-communist groups funded by Neville Roy Singham** (tech tycoon living in Shanghai)
- Parroted Chinese government propaganda (demonizing America as "fascist")
- **New patterns:**
  - **Pattern 18:** 501(c)(3/4) nonprofits funding political events disguised as grassroots protests — tax-exempt dollars used for political activity
  - **Pattern 19:** Professional event production costs ($250K+) for events media reports as "spontaneous" — track vendor payments through nonprofit disclosures
  - **Pattern 20:** Foreign influence laundering — track nonprofits with funding ties to foreign nationals/entities (Singham → Shanghai) funneling into domestic political activity
  - **Pattern 21:** Political operatives (Fisk) running "nonprofit" events — cross-reference nonprofit board/advisor lists against political campaign staff registrations
  - **Pattern 22:** Vendor payment analysis — large nonprofits paying event production vendors at rates consistent with political campaigns, not charitable work

### Cross-Cutting Detection Criteria

| Criteria | What to scan | Source |
|----------|-------------|--------|
| **Entity type: Nonprofit** | 501(c)(3), 501(c)(4) | IRS 990, state charity registrations |
| **Sector: Homeless services** | NTEE codes L (Housing), P (Human Services) | ProPublica Nonprofit Explorer |
| **Sector: Political nonprofits** | 501(c)(4) "social welfare" orgs, 527 political orgs | IRS 990, FEC, state campaign finance |
| **Government real estate deals** | Municipal property transfers below market value | County recorder, assessor records |
| **Campaign finance correlation** | Developer/vendor donations to approving officials | FEC, state campaign finance databases |
| **Foreign funding ties** | Grants/donations from foreign-connected entities | FARA registrations, IRS 990 Schedule B |
| **Audit gap exploitation** | Entities in jurisdictions where auditing is admitted to be deficient | State auditor reports, news coverage |

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
- **Location:** `new-repo:D:\my_ai_projects\fraud-detection-app`
- **Scope:** BUILD
- **Constraints:** Legal viability confirmed (materially adds standard). Need qui tam attorney on contingency. All data public records only. Pipeline runs via run-task.sh + cron in dedicated fraud-scan repo. Kernel enforces investigation quality gates.
