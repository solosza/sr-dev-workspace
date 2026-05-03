# 006 — Write Check Functions for Healthcare Fraud Patterns (026-028)

## Type
BUILD

## Action
Add 3 check functions to `D:\my_ai_projects\fraud-detection-app\src\patterns\pattern_checks_ext.py` for patterns PATTERN-026, PATTERN-027, and PATTERN-028.

## Functions to Write

**`check_pattern_026(data)`** — Hospice Fraud at Scale
- Check: `hospice_provider` stopped billing after `payment_suspension`
- Check: never requested reinstatement
- Check: `billing_volume > 500000`
- Match if confidence >= 60

**`check_pattern_027(data)`** — Dark Web Identity Hospice Billing
- Check: `patient_state_of_residence != provider_state`
- Check: `patient_SSN` appears in multiple provider claims across states
- Check: patient has no verifiable address in provider state
- Match if confidence >= 70

**`check_pattern_028(data)`** — Healthcare Facility License Stacking
- Check: address has `license_count > 50`
- Check: facility lacks `ADA_compliance_records`
- Check: no handicap parking or ramp access
- Match if confidence >= 60

## Target File
`D:\my_ai_projects\fraud-detection-app\src\patterns\pattern_checks_ext.py`

## Acceptance
- [ ] 3 functions added (check_pattern_026, check_pattern_027, check_pattern_028)
- [ ] Each returns PatternMatch with correct pattern_id
- [ ] File still imports without errors

## Dependencies
002
