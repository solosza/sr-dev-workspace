# 014 — L2 Functional Verification: Import and Parse

## Type
TEST

## Action
Verify all files are syntactically valid and importable.

## Checks

```bash
cd "D:/my_ai_projects/fraud-detection-app"

# fraud_patterns.json is valid JSON
python -c "import json; data=json.load(open('src/patterns/fraud_patterns.json')); print(f'Loaded {len(data[\"patterns\"])} patterns')"

# pattern_checks_ext.py imports without errors
python -c "from src.patterns.pattern_checks_ext import *; print('Import OK')"

# All fixture files are valid JSON
for f in tests/fixtures/ngo_grant_fixtures.json tests/fixtures/healthcare_fraud_fixtures.json tests/fixtures/government_finance_fixtures.json tests/fixtures/political_corruption_fixtures.json; do
  python -c "import json; json.load(open('$f')); print('Valid: $f')"
done
```

## Pass Criteria
- fraud_patterns.json parses as valid JSON with 34 patterns
- pattern_checks_ext.py imports without errors
- All 4 fixture files parse as valid JSON

## Dependencies
001-012
