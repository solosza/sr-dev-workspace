# Write Fraud Patterns JSON

## Type
BUILD

## Description
Create the fraud pattern library — all 22 validated patterns from the backlog as a structured JSON file.

## Requirements
Create `D:\my_ai_projects\fraud-detection-app\src\patterns\fraud_patterns.json` as a JSON array. Each pattern object must have:
- `id`: "PATTERN-NNN" (1-22)
- `name`: short descriptive name
- `description`: what the pattern detects
- `source_case`: which real-world case validated this pattern
- `severity`: "HIGH" | "MEDIUM" | "LOW"
- `data_sources`: list of APIs/databases needed to check this pattern
- `check_logic`: description of what to look for (e.g., "formation_date within 12 months of first award AND no prior 990 filings")
- `sector`: which sector this applies to (or "all")

Include all 22 patterns from the backlog:
- Patterns 1-9: Feeding Our Future / Minnesota
- Patterns 10-13: California homeless shelter fraud
- Patterns 14-17: Salt Lake City theater land deal
- Patterns 18-22: NoKings political nonprofit fraud

Read `D:\my_ai_projects\project_test_repos\sr_dev_workspace\docs\backlog\025-domain-build-government-spending-tracker.md` for the full pattern definitions.

## Acceptance Criteria
- [ ] `test -f D:/my_ai_projects/fraud-detection-app/src/patterns/fraud_patterns.json`
- [ ] `python -c "import json; d=json.load(open('D:/my_ai_projects/fraud-detection-app/src/patterns/fraud_patterns.json')); assert len(d) == 22"`
- [ ] `python -c "import json; d=json.load(open('D:/my_ai_projects/fraud-detection-app/src/patterns/fraud_patterns.json')); assert all('id' in p and 'name' in p and 'check_logic' in p for p in d)"`
