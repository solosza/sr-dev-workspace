# Write Layer 0 — Pattern Discovery

## Type
BUILD

## Description
Layer 0: Autonomous pattern discovery — scan journalism, PACER, AG press releases, IG reports for new fraud cases. Extract patterns. Add to library.

## Requirements
Create `D:\my_ai_projects\fraud-detection-app\src\pipeline\layer0_pattern_discovery.py` with class `PatternDiscovery`:
- `__init__(self, source_watchlist_path)` — load source watchlist
- `scan_sources(self) -> list[DiscoveredCase]` — scan all sources for new fraud cases
- `extract_patterns(self, case: DiscoveredCase) -> list[NewPattern]` — decompose case into patterns
- `add_to_library(self, patterns: list[NewPattern])` — append to fraud_patterns.json
- `retroactive_scan(self, new_patterns, existing_entities)` — re-score entities against new patterns
- Source watchlist: JSON file with RSS/API endpoints, last-checked timestamp, hit rate
- Sources: DOJ press releases (justice.gov/fraud), state AG press releases, GAO reports, IG reports (oversight.gov), PACER new filings
- `DiscoveredCase` model: source_url, title, entities_involved, fraud_mechanism, dollar_amount, date_discovered
- `NewPattern` model: name, description, check_logic, severity, source_case, sector

## Acceptance Criteria
- [ ] `test -f D:/my_ai_projects/fraud-detection-app/src/pipeline/layer0_pattern_discovery.py`
- [ ] `grep -q "class PatternDiscovery" D:/my_ai_projects/fraud-detection-app/src/pipeline/layer0_pattern_discovery.py`
- [ ] `grep -q "retroactive_scan" D:/my_ai_projects/fraud-detection-app/src/pipeline/layer0_pattern_discovery.py`
