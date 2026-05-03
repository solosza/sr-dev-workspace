# 002 — Add Healthcare Fraud Patterns to fraud_patterns.json

## Type
BUILD

## Action
Add 3 new patterns to `D:\my_ai_projects\fraud-detection-app\src\patterns\fraud_patterns.json` for healthcare fraud.

## Patterns to Add

**PATTERN-026: Hospice Fraud at Scale**
- Signal: 100% fraud rate across entire state hospice program
- Source: Dr. Oz / California 450 hospices, $750M/year stolen
- check_logic: "hospice_provider stopped_billing after payment_suspension AND never_requested reinstatement AND billing_volume > $500K/year"
- data_sources: ["CMS hospice claims", "OIG exclusions", "State licensing boards"]
- sector: "healthcare"
- severity: HIGH

**PATTERN-027: Dark Web Identity Hospice Billing**
- Signal: Out-of-state identities purchased for fraudulent billing
- Source: CA AG — 5 arrested, $267M hospice fraud, dark web identity purchases
- check_logic: "patient_identity state_of_residence != provider_state AND patient_SSN appears_in multiple_provider_claims across states AND patient has no_verifiable_address in provider_state"
- data_sources: ["CMS claims cross-state", "SSA death master file", "State licensing boards"]
- sector: "healthcare"
- severity: HIGH

**PATTERN-028: Healthcare Facility License Stacking**
- Signal: 100+ medical licenses at single address, facility not ADA compliant
- Source: CA assemblywoman investigation — luxury cars, rooftop lounge, no handicap access
- check_logic: "address has license_count > 50 AND facility lacks ADA_compliance_records AND facility has no_handicap_parking OR no_ramp_access"
- data_sources: ["State medical license databases", "ADA compliance records", "Google Maps/Street View"]
- sector: "healthcare"
- severity: HIGH

## Target File
`D:\my_ai_projects\fraud-detection-app\src\patterns\fraud_patterns.json`

## Acceptance
- [ ] 3 new patterns added (PATTERN-026, 027, 028)
- [ ] Each has all required fields
- [ ] JSON remains valid

## Dependencies
None
