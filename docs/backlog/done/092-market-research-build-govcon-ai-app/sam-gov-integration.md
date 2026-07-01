# SAM.gov Integration — Opportunity Pipeline

## Status
NEW — built during Phase 2

## Location
`D:\my_ai_projects\govcon-ai\lib\sam_client.py`

## Purpose
Automated opportunity discovery from SAM.gov. Scan, filter, rank, and surface actionable contract opportunities.

## SAM.gov API
- **Opportunities API:** `api.sam.gov/opportunities/v2/search`
- **Entity API:** `api.sam.gov/entity-information/v3/entities`
- **API Key:** Free, requires registration at beta.sam.gov
- **Rate Limits:** Vary by endpoint, typically 10 req/sec

## Pipeline

```
SAM.gov API -> Filter (NAICS, $, set-aside) -> Rank (margin potential, complexity) -> Surface
```

### Filter Criteria
- NAICS codes (user-configured)
- Dollar range (default: $10K - $250K for entry)
- Set-aside type (total small business, 8(a), etc.)
- Location (state/region)
- Response deadline (>= 7 days out)
- Contract type (fixed-price preferred for spread model)

### Ranking Signals
- **Margin potential:** Higher dollar value + common service type = more sub options = better margins
- **Competition level:** Fewer bidders = higher win probability
- **Complexity:** Lower complexity = easier to sub out
- **Past performance:** Not required (below SAT) scores higher for new entrants

## Data Contract
Each opportunity normalized to:
```json
{
  "solicitation_number": "string",
  "title": "string",
  "agency": "string",
  "naics_code": "string",
  "set_aside_type": "string",
  "estimated_value_usd": "number",
  "response_deadline": "ISO8601",
  "place_of_performance": "string",
  "contract_type": "string",
  "past_performance_required": "boolean",
  "solicitation_url": "string",
  "rank_score": "number",
  "risk_flags": ["string"]
}
```

## Dependencies
- SAM.gov API key (free registration)
- Phase 1 research (determines which NAICS codes and set-aside types to target)
