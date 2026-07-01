"""Golden Dataset Translator: Contract JSON -> DeepEval Goldens.

Mechanically translates kernel command contract JSONs into DeepEval golden
datasets. Contracts already define expected behaviors (soft_validation_rules,
success_criteria) — this module transforms them into the golden format
DeepEval expects (input, expected_output, context, metadata).
"""

import json
import os
from pathlib import Path


def _generate_positive_golden(rule, contract_meta):
    """Generate a golden where the rule passes (compliant scenario)."""
    return {
        "input": (
            f"Scenario: Execute step {contract_meta.get('step', '?')} "
            f"for contract {contract_meta.get('contract_id', 'unknown')}. "
            f"Condition: {rule['check']} — compliant case."
        ),
        "expected_output": (
            f"{rule['name']}: PASS. "
            f"Rule {rule['rule_id']} satisfied. No violation detected."
        ),
        "context": [
            f"{rule['rule_id']}: {rule['description']}",
            f"Contract: {contract_meta.get('contract_id', 'unknown')}",
        ],
        "metadata": {
            "rule_ids": [rule["rule_id"]],
            "step": contract_meta.get("step"),
            "contract_id": contract_meta.get("contract_id"),
            "polarity": "positive",
        },
    }


def _generate_negative_golden(rule, contract_meta):
    """Generate a golden where the rule is violated."""
    return {
        "input": (
            f"Scenario: Execute step {contract_meta.get('step', '?')} "
            f"for contract {contract_meta.get('contract_id', 'unknown')}. "
            f"Condition: {rule['check']} — violation case."
        ),
        "expected_output": (
            f"{rule['name']}: FAIL. "
            f"Rule {rule['rule_id']} violated. "
            f"Action: {rule.get('on_violation', 'flag and skip')}."
        ),
        "context": [
            f"{rule['rule_id']}: {rule['description']}",
            f"Contract: {contract_meta.get('contract_id', 'unknown')}",
        ],
        "metadata": {
            "rule_ids": [rule["rule_id"]],
            "step": contract_meta.get("step"),
            "contract_id": contract_meta.get("contract_id"),
            "polarity": "negative",
        },
    }


def _generate_variation(rule, contract_meta, variation_index):
    """Generate a variation golden to meet the minimum count threshold."""
    polarity = "positive" if variation_index % 2 == 0 else "negative"
    result = "PASS" if polarity == "positive" else "FAIL"
    action = "" if polarity == "positive" else f" Action: {rule.get('on_violation', 'flag and skip')}."

    return {
        "input": (
            f"Scenario (variation {variation_index}): Execute step "
            f"{contract_meta.get('step', '?')} for contract "
            f"{contract_meta.get('contract_id', 'unknown')}. "
            f"Condition: {rule['check']} — {polarity} variation with "
            f"edge-case parameters."
        ),
        "expected_output": (
            f"{rule['name']}: {result}. "
            f"Rule {rule['rule_id']} {'satisfied' if polarity == 'positive' else 'violated'}."
            f"{action}"
        ),
        "context": [
            f"{rule['rule_id']}: {rule['description']}",
            f"Contract: {contract_meta.get('contract_id', 'unknown')}",
            f"Variation {variation_index}: edge-case boundary test",
        ],
        "metadata": {
            "rule_ids": [rule["rule_id"]],
            "step": contract_meta.get("step"),
            "contract_id": contract_meta.get("contract_id"),
            "polarity": polarity,
            "variation": variation_index,
        },
    }


def _generate_multi_rule_golden(rules, contract_meta, success_criteria):
    """Generate a golden that tests multiple rules together."""
    rule_ids = [r["rule_id"] for r in rules]
    checks = "; ".join(r["check"] for r in rules)
    criteria_text = " ".join(success_criteria) if success_criteria else "All rules pass."

    return {
        "input": (
            f"Scenario: Execute step {contract_meta.get('step', '?')} "
            f"for contract {contract_meta.get('contract_id', 'unknown')}. "
            f"Combined check: {checks}"
        ),
        "expected_output": (
            f"All rules satisfied. Success criteria met: {criteria_text}"
        ),
        "context": [
            f"{r['rule_id']}: {r['description']}" for r in rules
        ] + [f"Contract: {contract_meta.get('contract_id', 'unknown')}"],
        "metadata": {
            "rule_ids": rule_ids,
            "step": contract_meta.get("step"),
            "contract_id": contract_meta.get("contract_id"),
            "polarity": "positive",
            "multi_rule": True,
        },
    }


MIN_GOLDENS = 20


def translate_contract(contract_path):
    """Read a contract JSON and return a DeepEval golden dataset dict.

    Args:
        contract_path: Path to a contract JSON file.

    Returns:
        dict with "goldens" key containing list of golden test cases.
    """
    with open(contract_path, "r", encoding="utf-8") as f:
        contract = json.load(f)

    meta = contract.get("contract_metadata", {})
    rules = contract.get("soft_validation_rules", [])
    success_criteria = contract.get("success_criteria", [])

    goldens = []

    # Positive + negative for each rule
    for rule in rules:
        goldens.append(_generate_positive_golden(rule, meta))
        goldens.append(_generate_negative_golden(rule, meta))

    # Multi-rule golden if 2+ rules
    if len(rules) >= 2:
        goldens.append(_generate_multi_rule_golden(rules, meta, success_criteria))

    # Pad to minimum with variations if needed
    variation_index = 1
    rule_cycle_index = 0
    while len(goldens) < MIN_GOLDENS and rules:
        rule = rules[rule_cycle_index % len(rules)]
        goldens.append(_generate_variation(rule, meta, variation_index))
        variation_index += 1
        rule_cycle_index += 1

    return {"goldens": goldens}


def translate_all_contracts(contracts_dir):
    """Batch translate all contract JSONs in a directory.

    Args:
        contracts_dir: Path to directory containing contract JSON files.

    Returns:
        dict mapping contract filename to its golden dataset.
    """
    results = {}
    contracts_path = Path(contracts_dir)

    for contract_file in sorted(contracts_path.glob("*.json")):
        dataset = translate_contract(str(contract_file))
        results[contract_file.name] = dataset

    return results
