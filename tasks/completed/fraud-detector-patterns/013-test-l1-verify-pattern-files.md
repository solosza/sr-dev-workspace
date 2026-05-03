# 013 — L1 Structural Verification: Pattern Files Exist

## Type
TEST

## Action
Verify all new pattern definitions, check functions, and fixtures exist and have the expected content.

## Checks

```bash
# PATTERN-023 through PATTERN-034 exist in fraud_patterns.json
cd "D:/my_ai_projects/fraud-detection-app"
for i in $(seq 23 34); do
  pattern_id=$(printf "PATTERN-%03d" $i)
  grep -q "$pattern_id" src/patterns/fraud_patterns.json || echo "MISSING: $pattern_id"
done

# Check functions exist in pattern_checks_ext.py
for i in $(seq 23 34); do
  func_name=$(printf "check_pattern_%03d" $i)
  grep -q "def $func_name" src/patterns/pattern_checks_ext.py || echo "MISSING FUNC: $func_name"
done

# Fixture files exist
for f in ngo_grant_fixtures.json healthcare_fraud_fixtures.json government_finance_fixtures.json political_corruption_fixtures.json; do
  test -f "tests/fixtures/$f" || echo "MISSING FIXTURE: $f"
done
```

## Pass Criteria
- All 12 pattern IDs present in fraud_patterns.json
- All 12 check functions present in pattern_checks_ext.py
- All 4 fixture files exist

## Dependencies
001-012
