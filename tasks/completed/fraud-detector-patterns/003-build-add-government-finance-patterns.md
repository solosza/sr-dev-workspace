# 003 — Add Government Finance Fraud Patterns to fraud_patterns.json

## Type
BUILD

## Action
Add 3 new patterns to `D:\my_ai_projects\fraud-detection-app\src\patterns\fraud_patterns.json` for government finance fraud.

## Patterns to Add

**PATTERN-029: Homeless Services Embezzlement**
- Signal: Homelessness program funds diverted to personal assets (luxury property, vehicles, overseas accounts)
- Source: LA Housing / $23M mansion scheme, US Attorney confirmed 12+ similar active investigations in CA
- check_logic: "grant_recipient_principal owns luxury_property AND property_value > 2x annual_salary AND vehicle_registrations include luxury_brands AND overseas_property_filings exist"
- data_sources: ["HUD grants", "LAHSA disbursements", "County property records", "Vehicle registrations", "Foreign property filings"]
- sector: "government housing"
- severity: HIGH

**PATTERN-030: Ghost Business Grant Fraud**
- Signal: $6B+ in grants to businesses with no filed physical address
- Source: White House Fraud Task Force / 400 businesses flagged
- check_logic: "grant_recipient has no_physical_address_on_file AND statutory_address_requirement is not_met AND grant_amount > $10000"
- data_sources: ["SAM.gov registrations", "SBA grant records", "State business registries", "USPS address validation"]
- sector: "government grants"
- severity: HIGH

**PATTERN-031: In-Home Caregiver Circular Corruption**
- Signal: Government program funds flow to providers, providers pay union dues, unions donate back to politicians who fund the program
- Source: Newsom / $30B in-home caregiver program, high fraud rates in provider enrollment
- check_logic: "program_appropriation flows_to provider_payments AND provider pays union_dues AND union makes political_contributions to officials_who_control program_funding"
- data_sources: ["State program disbursements", "Union financial disclosures", "FEC/state campaign finance records", "Provider enrollment audits"]
- sector: "government healthcare"
- severity: HIGH

## Target File
`D:\my_ai_projects\fraud-detection-app\src\patterns\fraud_patterns.json`

## Acceptance
- [ ] 3 new patterns added (PATTERN-029, 030, 031)
- [ ] Each has all required fields (id, name, description, source_case, severity, data_sources, check_logic, sector)
- [ ] JSON remains valid after edit

## Dependencies
None
