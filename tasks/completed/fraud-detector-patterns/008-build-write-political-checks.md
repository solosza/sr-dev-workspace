# 008 — Write Check Functions for Political Corruption Patterns (032-034)

## Type
BUILD

## Action
Add 3 check functions to `D:\my_ai_projects\fraud-detection-app\src\patterns\pattern_checks_ext.py` for patterns PATTERN-032, PATTERN-033, and PATTERN-034.

## Functions to Write

**`check_pattern_032(data)`** — Gift Card Skimming to Foreign Military
- Check: gift card fraud reports clustered by geography
- Check: fund transfers to overseas accounts within 24h of activation
- Check: destination country is adversary nation
- Match if confidence >= 70

**`check_pattern_033(data)`** — Municipal Pension Book-Cooking
- Check: pension payment records have duplicate entries
- Check: discrepancy amount > 1% of total pension fund
- Check: correction delayed > 12 months
- Match if confidence >= 70

**`check_pattern_034(data)`** — Developer-Government Loan Collusion
- Check: federal loan application contains support letter from local official
- Check: municipal council minutes have no recorded vote for fund commitment
- Check: developer has bankruptcy filing within 24 months
- Match if confidence >= 70

## Target File
`D:\my_ai_projects\fraud-detection-app\src\patterns\pattern_checks_ext.py`

## Acceptance
- [ ] 3 functions added (check_pattern_032, check_pattern_033, check_pattern_034)
- [ ] Each returns PatternMatch with correct pattern_id
- [ ] File still imports without errors

## Dependencies
004
