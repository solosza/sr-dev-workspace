# 001 — Add NGO Grant Fraud Patterns to fraud_patterns.json

## Type
BUILD

## Action
Add 3 new patterns to `D:\my_ai_projects\fraud-detection-app\src\patterns\fraud_patterns.json` for NGO grant fraud.

## Patterns to Add

**PATTERN-023: NGO Grant Dependency Shell**
- Signal: NGO where 80-100% of revenue is a single federal grant
- Source: Interior Dept / Doug Burgum disclosure
- Red flags: CEO comp >$500K, multiple lobbyists >$300K, no diversified revenue
- check_logic: "federal_grant_revenue / total_revenue > 0.80 AND executive_comp > 500000 AND lobbyist_count >= 2 AND lobbyist_comp > 300000"
- sector: "nonprofits"
- severity: HIGH

**PATTERN-024: NGO Political Activism Laundering**
- Signal: Taxpayer-funded NGO using funds for political protest then sponsoring anti-oversight legislation
- Source: CHIRLA / Stop Nick Shirley Act (AB 2624)
- check_logic: "grant_recipient_EIN matches lobbying_disclosure_registrant AND grant_recipient linked to protest_event_funding AND grant_recipient sponsors_or_supports legislation blocking oversight"
- sector: "political nonprofits"
- severity: HIGH

**PATTERN-025: Soros-Backed NGO Prosecutorial Direction**
- Signal: External NGOs directing federal prosecutors on who to target
- Source: DOJ internal emails / FACE Act / Todd Blanche discovery
- check_logic: "NGO donor_list includes major_political_donors AND NGO sent communications to DOJ naming prosecution_targets AND targets had no prior_criminal_record for alleged offense"
- sector: "political nonprofits"
- severity: HIGH

## Target File
`D:\my_ai_projects\fraud-detection-app\src\patterns\fraud_patterns.json`

## Acceptance
- [ ] 3 new patterns added (PATTERN-023, 024, 025)
- [ ] Each has all required fields (id, name, description, source_case, severity, data_sources, check_logic, sector)
- [ ] JSON remains valid after edit

## Dependencies
None
