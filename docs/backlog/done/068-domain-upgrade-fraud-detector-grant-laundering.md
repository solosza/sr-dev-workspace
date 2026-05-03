# Upgrade Fraud Detector — Grant-to-Union Political Donation Laundering

## Status
Open

## Priority
High — $30B+ in taxpayer disbursements flowing through a documented cycle; pattern is replicable across states and program types

## Summary
Add the grant-to-union-to-politician donation laundering pattern to the fraud detection app. The pattern: government gives $30B in taxpayer money to in-home caregivers → caregivers pay $150M/year to unions → unions donate back to the politicians who authorized the spending. This is a documented cycle in California's in-home care program but the pattern (taxpayer funds → service providers → union dues → PAC donations → same politicians) is a general detection template that applies across states and program types.

## Requirements

### New Fraud Pattern: Grant-to-Union Political Donation Cycle

#### Pattern Definition
- **Signal:** Taxpayer-funded program where service providers are required or incentivized to join a union, and that union's PAC donations flow back to the politicians who control the program's budget
- **Red flags:**
  - Program budget exceeds $1B AND mandatory/quasi-mandatory union membership for recipients
  - Union PAC is top-5 donor to politicians who vote on program funding
  - Program has documented fraud rates (e.g., phantom caregivers, deceased clients)
  - Union lobbies for program expansion while fraud audits show waste
- **Detection method:**
  1. Identify large government programs with unionized service providers
  2. Cross-reference union PAC filings (FEC) with campaign finance records of politicians on appropriations/budget committees
  3. Flag circular flows: politician votes for program → program pays providers → providers pay union → union donates to politician
  4. Overlay with program fraud audit findings (OIG, GAO, state auditors)

#### Data Sources
- **FEC filings:** Union PAC contributions to federal candidates
- **State campaign finance:** Secretary of State databases for state-level donations
- **Program spending:** USAspending.gov for federal programs, state controller data for state programs
- **Union financials:** DOL LM-2 annual reports (union income, dues, political spending)
- **Fraud audits:** GAO, HHS-OIG, state auditor reports on program waste/fraud
- **Lobbying disclosures:** Senate/House lobbying databases, state lobbying registries

#### California In-Home Care Case Study (Reference Implementation)
- **Program:** In-Home Supportive Services (IHSS), ~$30B budget
- **Union:** SEIU (represents IHSS workers)
- **Flow:** State funds → 500,000+ caregivers → ~$150M/year in union dues → SEIU PAC → California Democratic candidates
- **Known fraud:** Phantom caregivers, deceased clients, provider-client collusion
- **Detection query:** Match IHSS provider payments (state controller) → SEIU LM-2 income → SEIU PAC FEC filings → campaign recipients who sit on Health & Human Services committees

#### Generalization
- Template should work for any program type: healthcare, education, public safety, infrastructure
- Key variables: program name, budget, union name, PAC name, target politicians, committee assignments
- Network graph: program → providers → union → PAC → politicians → program (cycle detection)

### Integration
- Add to existing pattern library in the fraud detection app
- Include the California IHSS case as the reference implementation
- Generalize into a reusable detection template
- Follow format from backlog 039

## References
- Source: @WallStreetApes X post (2026-04-28) — Newsom caregiver/union money laundering scheme
- Fraud detection app: `D:\my_ai_projects\fraud-detection-app`
- Pattern library: backlog [039](done/039-domain-upgrade-fraud-detector-pattern-library.md) (done)
- Government fraud detection: backlog [025](done/025-domain-build-government-spending-tracker.md) (done)

## Task Builder Input
- **Deliverable:** Grant-to-union political donation cycle detection pattern added to fraud detection app, with California IHSS reference implementation, generalized template, network graph detection logic, and integration tests
- **Location:** `new-repo:D:\my_ai_projects\fraud-detection-app`
- **Scope:** BUILD
- **Constraints:** Must follow existing pattern library format. The cycle detection requires linking 4 separate data sources (program spending, union financials, PAC filings, campaign finance). The California IHSS case is the reference implementation but the template must generalize to any state/program. FEC data is public; state data availability varies.
