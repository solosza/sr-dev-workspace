# Upgrade Fraud Detector — Real-World Pattern Library from Public Investigations

## Status
Open

## Priority
High — validated fraud patterns with public evidence, directly feeds the app's pattern matching engine

## Summary
Integrate real-world fraud patterns and investigative findings into the fraud detection app's pattern library. These come from public congressional testimony, investigative journalism (Nick Shirley, Chris Rufo, O'Keefe Media Group), DOJ/ICE press releases, and White House fraud task force disclosures. Each pattern should be codified as a detection rule with source attribution.

## Fraud Patterns to Codify

### 1. NGO Grant Dependency Shell (Interior Dept / Burgum disclosure)
- **Signal:** NGO where 80-100% of revenue is a single federal grant
- **Red flags:** CEO comp >$500K, multiple lobbyists on payroll at >$300K each, no diversified revenue
- **Detection:** Cross-reference SAM.gov grants with nonprofit 990 filings — flag orgs where federal grants exceed 80% of total revenue AND executive comp exceeds median by 3x+

### 2. NGO Political Activism Laundering (CHIRLA / Stop Nick Shirley Act)
- **Signal:** Taxpayer-funded NGO using funds for political protest activity, then sponsoring legislation to block oversight
- **Red flags:** Grant recipient org appears as bill sponsor/lobbyist, same org linked to protest event funding
- **Detection:** Match grant recipient EINs against lobbying disclosures and bill sponsor registries

### 3. Homeless Services Embezzlement (LA Housing / $23M mansion scheme)
- **Signal:** Homelessness program funds diverted to personal assets
- **Red flags:** Luxury property purchases by org principals, vehicles registered to org at luxury price points, overseas property acquisitions
- **Detection:** Cross-reference HUD/LAHSA grant recipients with property records, vehicle registrations, and foreign property filings
- **Note:** US Attorney's office confirmed 12+ similar active investigations in California alone

### 4. Hospice Fraud at Scale (Dr. Oz / California 450 hospices)
- **Signal:** 100% fraud rate in entire state hospice program — $750M/year stolen
- **Red flags:** Hospice billing with no patient verification, out-of-state identity purchases (dark web), facilities not ADA compliant, luxury vehicles at facility
- **Detection:** Flag hospices that stop billing after payment suspension AND never request reinstatement. Cross-reference patient identities across state lines. Physical compliance checks (no handicap access = not a real medical facility)
- **Related arrest:** 5 arrested for $267M hospice fraud using out-of-state dark web identities

### 5. Ghost Business Grant Fraud (White House Task Force / 400 businesses)
- **Signal:** $6B+ in grants to businesses with no filed physical address
- **Red flags:** Missing statutory address requirement, no verifiable business location
- **Detection:** Validate all grant recipients against address filing requirement. Flag any recipient with no physical address on file — statutory violation

### 6. In-Home Caregiver Circular Corruption (Newsom / $30B program)
- **Signal:** Government program funds flow to providers, providers pay union dues, unions donate back to politicians
- **Red flags:** High fraud rates in provider enrollment, union political contributions correlating with program funding increases
- **Detection:** Map the money circle: program appropriation -> provider payments -> union dues -> political contributions. Flag programs where the feedback loop exists

### 7. Gift Card Skimming to Foreign Military (ICE / Chinese CCP scheme)
- **Signal:** Retail gift card barcode theft with funds routed to foreign military units
- **Red flags:** Barcode tampering at retail locations, immediate fund transfers to overseas accounts upon card activation
- **Detection:** Flag patterns of gift card fraud reports clustered by geography, trace fund destinations

### 8. Municipal Pension Book-Cooking (Sacramento / $2B discrepancy)
- **Signal:** Double-counting pension payments to inflate budget shortfall
- **Red flags:** CalPERS payment duplication ($1.6B), future rate miscalculation ($450M), delayed correction
- **Detection:** Reconcile pension payment records against actual disbursements. Flag discrepancies >1% of total

### 9. Healthcare Facility License Stacking (CA assemblywoman investigation)
- **Signal:** 100+ medical licenses in a single building that isn't ADA compliant
- **Red flags:** Rooftop lounge in medical plaza, luxury vehicles in parking lot, no handicap parking/ramps
- **Detection:** Flag addresses with abnormally high license density. Cross-reference with ADA compliance records

### 10. Developer-Government Loan Collusion (Utah Lake scheme)
- **Signal:** Private developer seeks $1B federal loan, local mayor secretly pledges $5M public funds without council vote
- **Red flags:** Secret support letters from officials, no public vote on fund commitment, developer bankruptcy after project blocked
- **Detection:** FOIA EPA loan applications, cross-reference with municipal council minutes — flag commitments made without recorded votes

### 11. State Employee Whistleblower Retaliation Pattern (Minnesota / Walz admin)
- **Signal:** Employees who report fraud internally get smeared as racist/incompetent
- **Red flags:** HR complaints filed against fraud reporters, "racism" accusations following fraud reports
- **Detection:** Not a financial pattern — but a metadata pattern. Track whistleblower complaint timelines against retaliation actions

### 12. Soros-Backed NGO Prosecutorial Direction (DOJ / FACE Act)
- **Signal:** External NGOs directing federal prosecutors on who to target
- **Red flags:** NGO communications to DOJ naming specific prosecution targets, targets broke no laws
- **Detection:** FOIA DOJ communications, match NGO donor lists against prosecution target selection

## Target Repo
`D:\my_ai_projects\fraud-detection-app`

## Requirements
- Each pattern becomes a detection rule in `src/patterns/`
- Include source attribution (who disclosed, when, where)
- Include detection method (what data sources to cross-reference)
- Include estimated dollar magnitude where known
- Update existing pattern library — don't replace, extend
- Add test fixtures with mock data for each new pattern
- Total estimated fraud exposed in these patterns: $40B+ annually

## References
- Existing pattern library: `D:\my_ai_projects\fraud-detection-app\src\patterns\`
- API clients: `D:\my_ai_projects\fraud-detection-app\src\apis\`
- Sources: Congressional testimony, Nick Shirley investigations, Chris Rufo reporting, O'Keefe Media Group hidden camera, ICE press releases, White House fraud task force disclosures, CA AG press releases

## Task Builder Input
- **Deliverable:** 12 new detection patterns in the fraud app's pattern library with test fixtures
- **Scope:** BUILD
- **Constraints:** Must integrate with existing pattern architecture. Each pattern needs source attribution. Test fixtures must use realistic mock data, not real PII.
