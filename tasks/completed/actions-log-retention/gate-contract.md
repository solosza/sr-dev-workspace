# Gate Contract — Actions-Log Retention

## L1: Structural Gates

| ID | Check | Method |
|----|-------|--------|
| STRUCT-01 | actions-log-appender.py references actions.jsonl | grep |
| STRUCT-02 | actions-log-appender.py appends JSON lines to file | grep |
| STRUCT-03 | anchor.md references actions.jsonl for review | grep |
| STRUCT-04 | anchor.md includes retention/truncation instruction | grep |

## L2: Functional Gates

| ID | Check | Method |
|----|-------|--------|
| FUNC-01 | actions-log-appender.py runs without syntax errors | python -c "import" |
| FUNC-02 | Hook processes valid stdin JSON without crashing | echo JSON \| python hook |

## L3: Integration Gates

| ID | Check | Method |
|----|-------|--------|
| INTEG-01 | After a Bash action, actions.jsonl contains a new line | trigger + read file |
| INTEG-02 | Each line in actions.jsonl is valid JSON | python json.loads per line |
| INTEG-03 | actions.jsonl does not exceed 200 lines after rotation | wc -l |
