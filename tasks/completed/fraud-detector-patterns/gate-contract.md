# Gate Contract — Fraud Detector Patterns

## L1: Structural Gates

| ID | Check | Method |
|----|-------|--------|
| STRUCT-01 | fraud_patterns.json contains PATTERN-023 through PATTERN-034 | grep |
| STRUCT-02 | Each new pattern has id, name, description, source_case, severity, data_sources, check_logic, sector | python parse |
| STRUCT-03 | pattern_checks_ext.py contains check functions for new patterns | grep |
| STRUCT-04 | Test fixtures exist for each pattern group | file_exists |

## L2: Functional Gates

| ID | Check | Method |
|----|-------|--------|
| FUNC-01 | fraud_patterns.json is valid JSON | python json.load |
| FUNC-02 | pattern_checks_ext.py imports without errors | python -c "import" |
| FUNC-03 | All test fixtures are valid JSON | python json.load per fixture |

## L3: Integration Gates

| ID | Check | Method |
|----|-------|--------|
| INTEG-01 | pattern_scanner can load all 34 patterns | python import + count |
| INTEG-02 | Each new check function runs against its fixture without crashing | python run checks |
| INTEG-03 | At least 80% of fixture inputs trigger their expected pattern match | python assert match rate |
