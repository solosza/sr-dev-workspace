# Compliance Rules Engine

## Status
NEW — built during Phase 2

## Location
`D:\my_ai_projects\govcon-ai\references\`

## Purpose
All FAR/SBA rules encoded as visible, auditable JSON. Same pattern as SSH compliance validators and RT automation — rules are data, not code. Updateable without touching application logic.

## Core Rules to Encode

### FAR 52.219-14 — Limitations on Subcontracting
```json
{
  "rule_id": "FAR-52.219-14",
  "name": "Limitations on Subcontracting",
  "applies_to": ["small_business_set_aside", "8a", "hubzone", "wosb", "sdvosb"],
  "thresholds": {
    "services": { "prime_min_pct": 50, "basis": "cost_of_personnel" },
    "supplies": { "prime_min_pct": 50, "basis": "cost_of_manufacturing_or_supply" },
    "construction": { "prime_min_pct": 15, "basis": "cost_with_own_employees" }
  },
  "similarly_situated_exception": true,
  "penalty": "contract_termination_and_debarment"
}
```

### Simplified Acquisition Threshold
```json
{
  "rule_id": "FAR-13",
  "threshold_usd": 250000,
  "effects": {
    "below": ["simplified_procedures", "reduced_past_performance_requirements", "fewer_proposal_sections"],
    "above": ["full_source_selection", "past_performance_evaluation", "formal_proposal_required"]
  }
}
```

### Micro-Purchase Threshold
```json
{
  "rule_id": "FAR-13.2",
  "threshold_usd": 10000,
  "effects": {
    "below": ["no_competition_required", "purchase_card_eligible"],
    "above": ["competition_required"]
  }
}
```

## Validation Pattern
Same as SSH compliance: `check_rule(bid, rule) -> pass/fail/warn` with structured output. Hook enforcement prevents submission when rules fail.

## Dependencies
- Phase 1 research (verifies actual thresholds and applicability)
