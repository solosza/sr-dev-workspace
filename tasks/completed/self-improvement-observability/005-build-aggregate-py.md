# Create aggregate.py metrics aggregator

## Context
The core metrics aggregation tool that reads metrics.jsonl and produces trend reports. CLI interface for querying kernel performance over time.

## Type
BUILD

## Execution
inline

## Dependencies
- 002 (metrics schema exists)

## Phase Gate
- [ ] `D:/my_ai_projects/kernel-observatory/schemas/metrics.jsonl.schema.json` exists

## Requirements
- Create `D:/my_ai_projects/kernel-observatory/lib/aggregate.py`
- CLI interface:
  - `python aggregate.py --file <path>` — read from specific metrics.jsonl
  - `python aggregate.py --last 30d` — filter to last 30 days
  - `python aggregate.py --pipeline <id>` — filter to specific pipeline
  - `python aggregate.py --trend violations` — show violation trend
  - `python aggregate.py --help` — show usage
- Output: JSON or markdown table with computed averages, rates, trends
- Compute: total events, events by type, average actions per anchor, violation rate, pipeline pass rate
- Python 3.10+ only, no external dependencies (stdlib only: json, argparse, datetime, statistics)
- Handle empty or missing file gracefully (exit 0 with empty report)

## Acceptance Criteria
- [ ] `D:/my_ai_projects/kernel-observatory/lib/aggregate.py` exists
- [ ] `python D:/my_ai_projects/kernel-observatory/lib/aggregate.py --help` exits 0
- [ ] Script handles empty input without error

## Gates Satisfied
- BUILD-05, FUNC-01

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
