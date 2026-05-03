# 007 — Write Check Functions for Government Finance Patterns (029-031)

## Type
BUILD

## Action
Add 3 check functions to `D:\my_ai_projects\fraud-detection-app\src\patterns\pattern_checks_ext.py` for patterns PATTERN-029, PATTERN-030, and PATTERN-031.

## Functions to Write

**`check_pattern_029(data)`** — Homeless Services Embezzlement
- Check: grant recipient principal owns luxury property
- Check: property value > 2x annual salary
- Check: luxury vehicle registrations exist
- Check: overseas property filings exist
- Match if confidence >= 70

**`check_pattern_030(data)`** — Ghost Business Grant Fraud
- Check: grant recipient has no physical address on file
- Check: statutory address requirement not met
- Check: grant amount > $10,000
- Match if confidence >= 60

**`check_pattern_031(data)`** — In-Home Caregiver Circular Corruption
- Check: program funds flow to providers
- Check: providers pay union dues
- Check: union makes political contributions to officials who control program funding
- Match if confidence >= 70

## Target File
`D:\my_ai_projects\fraud-detection-app\src\patterns\pattern_checks_ext.py`

## Acceptance
- [ ] 3 functions added (check_pattern_029, check_pattern_030, check_pattern_031)
- [ ] Each returns PatternMatch with correct pattern_id
- [ ] File still imports without errors

## Dependencies
003
