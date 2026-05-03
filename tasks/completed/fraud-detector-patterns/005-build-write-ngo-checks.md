# 005 — Write Check Functions for NGO Grant Fraud Patterns (023-025)

## Type
BUILD

## Action
Add 3 check functions to `D:\my_ai_projects\fraud-detection-app\src\patterns\pattern_checks_ext.py` for patterns PATTERN-023, PATTERN-024, and PATTERN-025.

## Functions to Write

Follow the existing pattern in `pattern_checks.py` and `pattern_checks_ext.py`:
- Each function takes `data: dict`, returns `PatternMatch`
- Build confidence score from multiple indicators (0-100)
- Match threshold at 60-70
- Collect evidence strings

**`check_pattern_023(data)`** — NGO Grant Dependency Shell
- Check: `federal_grant_revenue / total_revenue > 0.80`
- Check: `executive_comp > 500000`
- Check: `lobbyist_count >= 2 AND lobbyist_comp > 300000`
- Match if confidence >= 70

**`check_pattern_024(data)`** — NGO Political Activism Laundering
- Check: `grant_recipient_EIN` matches `lobbying_disclosure_registrant`
- Check: `grant_recipient` linked to `protest_event_funding`
- Check: `grant_recipient` supports legislation blocking oversight
- Match if confidence >= 70

**`check_pattern_025(data)`** — Soros-Backed NGO Prosecutorial Direction
- Check: NGO donor list includes major political donors
- Check: NGO sent communications to DOJ naming prosecution targets
- Check: Targets had no prior criminal record for alleged offense
- Match if confidence >= 70

## Target File
`D:\my_ai_projects\fraud-detection-app\src\patterns\pattern_checks_ext.py`

## Acceptance
- [ ] 3 functions added (check_pattern_023, check_pattern_024, check_pattern_025)
- [ ] Each returns PatternMatch with correct pattern_id
- [ ] File still imports without errors

## Dependencies
001
