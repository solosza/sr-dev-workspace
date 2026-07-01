# Golden Dataset Translator: Contract JSON → DeepEval Goldens

## Status
NEW

## Purpose

Mechanically translate kernel command contract JSONs into DeepEval golden datasets. This eliminates manual fixture creation — contracts already define expected behaviors, they just need schema transformation.

## Input: Contract JSON (existing)

```json
{
  "contract_metadata": { "contract_id": "check-data-step-03", "step": 3 },
  "soft_validation_rules": [
    {
      "rule_id": "SV-301",
      "name": "Date pair unique per history claim",
      "description": "No two TCs sharing the same history claim may have identical (admit, discharge) pairs",
      "check": "For this history_claim_id, no existing entry in date_registry has same (admit, discharge)",
      "on_violation": "log error, flag TC as blocked, skip"
    },
    {
      "rule_id": "SV-305",
      "name": "Clean break per member (no overlap, no touching)",
      "description": "All DOS ranges for the same member must have at least 1 day gap.",
      "check": "For this member_id, no existing range overlaps or is adjacent to proposed range.",
      "on_violation": "log error, pick next available date pair with clean break."
    }
  ],
  "success_criteria": [
    "Date pair is unique in registry for this history claim",
    "Clean break from all other date ranges for this member (min 1 day gap)"
  ]
}
```

## Output: DeepEval Golden (generated)

```json
{
  "goldens": [
    {
      "input": "TC-002: Assign dates for readmission. History claim 25329E0025027 (member R00002417147200). History enddate 10/29/2025. Existing dates for this member: [(11/01-11/03, TC-001)].",
      "expected_output": "Date pair unique: YES. Clean break from 11/01-11/03: YES (gap >= 1 day). Admit >= history enddate 10/29: YES.",
      "context": ["SV-301: Date pair unique per history claim", "SV-305: Clean break per member", "Contract: check-data-step-03"],
      "metadata": {
        "rule_ids": ["SV-301", "SV-305"],
        "step": 3,
        "contract_id": "check-data-step-03"
      }
    },
    {
      "input": "TC-009: Assign dates for readmission. History claim 26156E0000198 (member R00002900510500). History enddate 10/29/2025. Existing dates for this member: [(11/01-11/03, TC-001), (10/29-10/30, TC-007), ...].",
      "expected_output": "Date pair 11/10-11/11: unique YES. Clean break: YES (nearest neighbor 11/08-11/09 TC-005E, gap = 1 day).",
      "context": ["SV-301", "SV-305", "Heavy member with 20+ existing ranges"],
      "metadata": {
        "rule_ids": ["SV-301", "SV-305"],
        "step": 3,
        "contract_id": "check-data-step-03",
        "difficulty": "high"
      }
    }
  ]
}
```

## Translation Algorithm

1. **Read contract JSON.** Extract `soft_validation_rules` and `success_criteria`.
2. **Generate positive goldens.** For each rule, create a test case where the rule passes. The `input` describes the scenario, `expected_output` describes what compliance looks like.
3. **Generate negative goldens.** For each rule, create a test case where the rule is violated. The `expected_output` describes the expected violation detection.
4. **Add context.** Each golden's `context` includes the rule descriptions (for faithfulness evaluation).
5. **Scale from real data.** If an xlsx or state file is available, generate goldens from actual TC data (realistic inputs).

## Minimum Golden Count

DeepEval requires minimum 20 goldens for statistically reliable scores. Per contract:
- N rules × 2 (positive + negative) × M scenarios = goldens
- If under 20, generate variations (different member counts, edge dates, boundary conditions)

## Dependencies

- Contract JSONs must follow the existing schema (soft_validation_rules, success_criteria)
- Real TC data (xlsx) improves golden quality but isn't required (synthetic fallback)
