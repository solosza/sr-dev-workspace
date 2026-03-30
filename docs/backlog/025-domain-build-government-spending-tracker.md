# Government Spending & Grant Accountability Tracker

## Status
Open

## Priority
Medium — novel domain with real market demand; no active client deadline but aligns with accountability/transparency tooling interest

## Summary
Build an application that tracks federal grant disbursements, cross-references nonprofit/NGO filings, and flags anomalies indicating potential misuse of funds. The app ingests public data (USASpending.gov, IRS 990 filings, SAM.gov registrations, Treasury disbursements) and surfaces red flags: newly created organizations receiving large payouts, missing IRS registrations, lack of federal disclosures, and disproportionate funding relative to an organization's financial history.

Inspired by concerns around climate fund spending — billions routed to organizations with no filing history, created shortly before receiving payouts, or with no prior fundraising track record. The tool is framework-agnostic and applies to any federal spending category, not just climate.

## Requirements
- Ingest federal grant data from USASpending.gov API
- Cross-reference recipient orgs against IRS 990 database (ProPublica Nonprofit Explorer API or IRS BMF extract)
- Cross-reference against SAM.gov entity registrations
- Flag anomalies:
  - Org created within N months of receiving grant (configurable threshold)
  - Org not found in IRS database
  - Org total prior revenue disproportionate to grant amount (e.g., received $2B but prior revenue was $100)
  - Missing or late federal disclosure filings
  - No public 990 on record
- Dashboard showing flagged disbursements with drill-down to source data
- Filter by spending category (climate, defense, health, etc.), agency, date range, recipient state
- Export flagged items as report (PDF/CSV)
- All data sourced from public records — no proprietary data required

## Data Sources
- **USASpending.gov** — federal award and subaward data (REST API available)
- **IRS 990** — nonprofit tax filings (ProPublica API or IRS bulk download)
- **SAM.gov** — entity registration and exclusion data (API available)
- **Treasury** — disbursement records
- **GuideStar/Candid** — nonprofit profiles (may require API key)

## References
- USASpending.gov API: https://api.usaspending.gov/
- ProPublica Nonprofit Explorer API
- SAM.gov Entity Management API
- Context: climate fund spending concerns ($375B IRA disbursements, allegations of funds routed to newly created or unregistered NGOs)

## Task Builder Input
- **Deliverable:** Web application with data ingestion pipeline, anomaly detection engine, and dashboard UI
- **Scope:** BUILD
- **Constraints:** Public data APIs only (no proprietary access needed). Tech stack TBD — likely Python backend (FastAPI), PostgreSQL for entity cross-referencing, React or simple dashboard frontend. Could start as CLI tool that generates reports, then add UI. No active client deadline — build when capacity allows.
