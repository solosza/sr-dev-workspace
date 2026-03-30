# Government Spending & Grant Fraud Detection Platform

## Status
Open

## Priority
High — validated by active federal crackdown (Treasury/DOJ Minnesota fraud cases); direct revenue opportunity for Isagawa

## Summary
Build a fraud detection platform that tracks federal grant disbursements, cross-references nonprofit/NGO filings, and flags anomalies indicating potential misuse of funds. The app ingests public data (USASpending.gov, IRS 990 filings, SAM.gov registrations, Treasury disbursements, FinCEN alerts) and surfaces red flags: newly created organizations receiving large payouts, missing IRS registrations, lack of federal disclosures, disproportionate funding relative to financial history, and suspicious international money flows.

This is not theoretical. Treasury Secretary Bessent called Minnesota "ground zero for the most egregious welfare scam in our nation's history" — $300M+ stolen through Feeding Our Future alone, 98 defendants charged, funds potentially diverted to al-Shabab. The tools Treasury used to crack this (Geographic Targeting Orders, FinCEN alerts, money services business audits) are exactly what this platform would automate and democratize.

## Market Opportunity
- **Government agencies** — Treasury, DOJ, HHS, state AGs need automated fraud detection. Current process is manual and reactive (caught after billions stolen).
- **Compliance firms** — AML/KYC firms need grant fraud data to cross-reference with their transaction monitoring.
- **Investigative journalism** — ProPublica, local newsrooms investigating government spending.
- **Nonprofits themselves** — legitimate orgs want to prove they're clean.
- **Congressional oversight** — committees need tools to audit program spending.

## Validated Fraud Patterns (from Minnesota cases)
- **Feeding Our Future:** Nonprofit created to receive COVID school meal funding. $300M stolen. 98 defendants, 64 convicted. Funds sent to Somalia via money services businesses.
- **Pattern 1:** Org created shortly before receiving massive government payout (no prior history)
- **Pattern 2:** Org not registered in IRS database but receiving federal funds
- **Pattern 3:** Total prior revenue disproportionate to grant amount (received $2B, prior revenue was $100)
- **Pattern 4:** Funds routed through money services businesses to high-risk countries
- **Pattern 5:** Missing or late federal disclosure filings
- **Pattern 6:** Multiple orgs at same address receiving separate grants
- **Pattern 7:** Rapid spend-down of funds with no program deliverables

## Requirements
- Ingest federal grant data from USASpending.gov API
- Cross-reference recipient orgs against IRS 990 database (ProPublica Nonprofit Explorer API or IRS BMF extract)
- Cross-reference against SAM.gov entity registrations
- Ingest FinCEN alerts and Geographic Targeting Orders (public notices)
- Flag anomalies with configurable thresholds:
  - Org created within N months of receiving grant
  - Org not found in IRS database
  - Org total prior revenue disproportionate to grant amount
  - Missing or late federal disclosure filings
  - No public 990 on record
  - Multiple entities at same registered address
  - Rapid international wire transfers post-award
- Dashboard showing flagged disbursements with drill-down to source data
- Filter by spending category (nutrition, healthcare, housing, climate, defense), agency, date range, recipient state
- Risk scoring model per entity (composite of all red flags)
- Export flagged items as report (PDF/CSV)
- Alert system for new grants matching fraud patterns
- All data sourced from public records

## Data Sources
- **USASpending.gov** — federal award and subaward data (REST API)
- **IRS 990** — nonprofit tax filings (ProPublica API or IRS bulk download)
- **SAM.gov** — entity registration and exclusion data (API)
- **Treasury** — disbursement records, Geographic Targeting Orders
- **FinCEN** — alerts, suspicious activity report aggregates
- **GuideStar/Candid** — nonprofit profiles (may require API key)
- **OFAC SDN List** — sanctioned entities cross-reference

## References
- Treasury press release: https://home.treasury.gov/news/press-releases/sb0354
- Treasury action on Somali fraud: https://home.treasury.gov/news/press-releases/sb0358
- AML Intelligence coverage: https://www.amlintelligence.com/2026/01/breaking-us-treasury-launches-minnesota-fraud-crackdown-audits-3000-gto-and-fincen-alert/
- USASpending.gov API: https://api.usaspending.gov/
- ProPublica Nonprofit Explorer API
- SAM.gov Entity Management API
- Context: climate fund spending concerns ($375B IRA disbursements), Minnesota Feeding Our Future ($300M fraud), Bessent crackdown

## Task Builder Input
- **Deliverable:** Fraud detection platform with data ingestion pipeline, anomaly detection engine, risk scoring model, dashboard UI, and alert system
- **Scope:** BUILD
- **Constraints:** Public data APIs only. Python backend (FastAPI), PostgreSQL for entity cross-referencing. Start as CLI tool that generates risk reports, then add dashboard. Could integrate with existing compliance specs (AML/KYC, SOC) for cross-referencing. Revenue model: SaaS subscription for government agencies and compliance firms.
