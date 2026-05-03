# Upgrade Fraud Detector — Federal Benefits Fraud Patterns

## Status
Open

## Priority
High — new federal legislation specifically targets these fraud types; detection patterns can be codified now while enforcement is ramping up

## Summary
Add federal benefits fraud detection patterns to the existing fraud detection app. The US House passed legislation targeting fraud involving SNAP, Social Security, conspiracy to defraud, and identity fraud. These are specific, well-defined fraud categories with public data sources that can be programmatically scanned. Each pattern should be codified as a detection rule in the pattern library, following the same format as backlog 039's pattern additions.

## Requirements

### New Fraud Patterns to Codify

#### 1. SNAP Benefits Fraud
- **Signal:** SNAP/EBT benefits claimed by ineligible recipients or trafficked for cash
- **Red flags:** Benefits claimed at addresses with no residents, benefits redeemed at stores known for trafficking, duplicate SSNs across multiple state SNAP programs
- **Detection:** Cross-reference USDA SNAP retailer data with FNS fraud reports, match EBT transaction patterns against known trafficking indicators
- **Data sources:** USDA FNS retailer database, state SNAP enrollment data (FOIA), OIG audit reports

#### 2. Social Security Fraud
- **Signal:** Benefits claimed by deceased persons, identity theft for SSI/SSDI claims, representative payee abuse
- **Red flags:** Benefits continuing after death date in SSDI, multiple claims from same address, representative payees with unusually large caseloads
- **Detection:** Cross-reference SSA death master file with active benefit rolls, flag addresses with 5+ SSI/SSDI recipients
- **Data sources:** SSA death master file (public), OIG semiannual reports, SSDI/SSI statistical data

#### 3. Identity Fraud (Federal Benefits Context)
- **Signal:** Stolen or synthetic identities used to claim federal benefits
- **Red flags:** SSNs issued to minors used for adult benefit claims, addresses flagged in identity fraud databases, benefits claimed across multiple states simultaneously
- **Detection:** Cross-reference benefit enrollment records across states using SSN/name/DOB matching, flag synthetic identity indicators (SSNs with no credit history but active federal benefits)
- **Data sources:** SAM.gov exclusion list, FinCEN suspicious activity reports (aggregated), FTC identity theft reports

#### 4. Conspiracy to Defraud (Organized Schemes)
- **Signal:** Coordinated multi-person schemes to defraud federal programs
- **Red flags:** Multiple applicants from same address/phone, applicants sharing same representatives/attorneys, sudden spikes in applications from specific geographic areas
- **Detection:** Network analysis of shared attributes (address, phone, representative, bank account) across benefit applications, clustering analysis for coordinated submission patterns
- **Data sources:** DOJ press releases (convicted schemes as training data), OIG investigation summaries

### Integration
- Add to existing pattern library in the fraud detection app
- Follow the format established by backlog 039 (pattern name, signal, red flags, detection method, data sources)
- Each pattern should be implementable as a detection rule
- Include source attribution (legislation reference, enforcement context)

## References
- Source: @DRPOOLQ17 X post (2026-04-28) — US House passes fraud deportation legislation targeting SNAP, Social Security, ID fraud
- Fraud detection app: `D:\my_ai_projects\fraud-detection-app` (built via backlog 025)
- Pattern library upgrade: backlog [039](done/039-domain-upgrade-fraud-detector-pattern-library.md) (done — established the pattern format)
- Government fraud detection: backlog [025](done/025-domain-build-government-spending-tracker.md) (done — the base app)

## Task Builder Input
- **Deliverable:** 4 new fraud detection patterns added to the fraud detection app's pattern library, with detection rules, data source references, and integration tests
- **Location:** `new-repo:D:\my_ai_projects\fraud-detection-app`
- **Scope:** BUILD
- **Constraints:** Must follow existing pattern library format from backlog 039. Each pattern needs detection logic that can actually query public data sources. The legislation provides the legal framework — our detection patterns should map to the specific fraud categories named in the bill.
