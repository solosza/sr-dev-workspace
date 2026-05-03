# 015 — L3 Integration Verification: Run Fixtures Against Patterns

## Type
TEST

## Action
Run each fixture through its corresponding check function and verify match/no-match results.

## Test Script

```python
import json
import sys
sys.path.insert(0, "D:/my_ai_projects/fraud-detection-app")
from src.patterns import pattern_checks_ext as checks

fixture_files = [
    "tests/fixtures/ngo_grant_fixtures.json",
    "tests/fixtures/healthcare_fraud_fixtures.json",
    "tests/fixtures/government_finance_fixtures.json",
    "tests/fixtures/political_corruption_fixtures.json",
]

total = 0
passed = 0
failed = 0

for fixture_path in fixture_files:
    with open(f"D:/my_ai_projects/fraud-detection-app/{fixture_path}") as f:
        fixtures = json.load(f)

    for fixture in fixtures:
        pattern_num = int(fixture["pattern_id"].split("-")[1])
        check_fn = getattr(checks, f"check_pattern_{pattern_num:03d}")
        result = check_fn(fixture["input"])
        total += 1

        if result.matched == fixture["expected_match"]:
            passed += 1
            print(f"  PASS: {fixture['description']}")
        else:
            failed += 1
            print(f"  FAIL: {fixture['description']} — expected {fixture['expected_match']}, got {result.matched} (confidence={result.confidence})")

print(f"\nResults: {passed}/{total} passed, {failed} failed")
match_rate = passed / total * 100 if total > 0 else 0
print(f"Match rate: {match_rate:.0f}%")

if match_rate < 80:
    print("FAIL: Match rate below 80% threshold")
    sys.exit(1)
else:
    print("PASS: Match rate meets 80% threshold")
```

## Pass Criteria
- All fixtures load and run without crashes
- At least 80% of fixtures produce expected match/no-match result
- Pattern scanner can load all 34 patterns total

## Dependencies
009-012
