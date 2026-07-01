"""Metric Mapping: DeepEval metrics for kernel command evaluation.

Maps DeepEval's metric library to kernel command evaluation needs.
Kernel commands are Agent pipelines — they use tools, follow protocols,
produce artifacts. This module selects appropriate metrics and generates
GEval criteria from contract JSONs.
"""

import json
from pathlib import Path


# Threshold constants
THRESHOLD_MINIMUM_VIABLE = 0.5
THRESHOLD_ACCEPTABLE = 0.7
THRESHOLD_PRODUCTION_READY = 0.85
THRESHOLD_TARGET = 0.95

# Pipeline type to auto-selected metrics
PIPELINE_METRICS = {
    "agent": ["ToolCorrectness", "TaskCompletion"],
    "rag": ["Faithfulness", "AnswerRelevancy", "ContextualRelevancy"],
    "chatbot": ["AnswerRelevancy", "Hallucination"],
}


def select_metrics(pipeline_type):
    """Return auto-selected metrics for a given pipeline type.

    Args:
        pipeline_type: One of "agent", "rag", "chatbot".

    Returns:
        List of metric name strings.
    """
    return list(PIPELINE_METRICS.get(pipeline_type.lower(), []))


def generate_geval_criteria(contract):
    """Generate GEval criteria from a contract's soft_validation_rules.

    Each rule becomes a GEval criterion with name, criteria text,
    evaluation_params, and threshold.

    Args:
        contract: Parsed contract dict (or path to contract JSON).

    Returns:
        List of GEval criterion dicts.
    """
    if isinstance(contract, (str, Path)):
        with open(contract, "r", encoding="utf-8") as f:
            contract = json.load(f)

    rules = contract.get("soft_validation_rules", [])
    default_threshold = contract.get("confidence_threshold", THRESHOLD_ACCEPTABLE)
    criteria = []

    for rule in rules:
        criterion = {
            "name": f"{rule.get('rule_id', 'UNKNOWN')} Compliance",
            "criteria": (
                f"Evaluate whether the agent satisfied rule {rule.get('rule_id', '?')}: "
                f"{rule.get('description', rule.get('check', 'No description'))}. "
                f"The agent should have verified: {rule.get('check', 'N/A')}."
            ),
            "evaluation_params": ["input", "actual_output", "expected_output"],
            "threshold": rule.get("threshold", default_threshold),
        }
        criteria.append(criterion)

    return criteria


def generate_geval_from_success_criteria(contract):
    """Generate GEval criteria from a contract's success_criteria.

    Used for TaskCompletion scoring — each success criterion becomes
    a GEval evaluation point.

    Args:
        contract: Parsed contract dict (or path to contract JSON).

    Returns:
        List of GEval criterion dicts.
    """
    if isinstance(contract, (str, Path)):
        with open(contract, "r", encoding="utf-8") as f:
            contract = json.load(f)

    success_criteria = contract.get("success_criteria", [])
    criteria = []

    for i, sc in enumerate(success_criteria):
        text = sc if isinstance(sc, str) else sc.get("description", str(sc))
        criterion = {
            "name": f"SC-{i + 1} TaskCompletion",
            "criteria": (
                f"Evaluate whether the agent completed this success criterion: {text}"
            ),
            "evaluation_params": ["input", "actual_output", "expected_output"],
            "threshold": THRESHOLD_ACCEPTABLE,
        }
        criteria.append(criterion)

    return criteria


def get_optional_metrics(contract):
    """Return additional metrics based on contract signals.

    Inspects the contract for signals that indicate optional metrics:
    - Faithfulness: if soft_validation_rules reference context/documents
    - Hallucination: if steps read from xlsx/DB sources

    Args:
        contract: Parsed contract dict (or path to contract JSON).

    Returns:
        List of dicts with "metric" name and "reason" for inclusion.
    """
    if isinstance(contract, (str, Path)):
        with open(contract, "r", encoding="utf-8") as f:
            contract = json.load(f)

    optional = []
    rules = contract.get("soft_validation_rules", [])
    steps = contract.get("steps", [])

    # Check for context references in rules -> Faithfulness
    context_keywords = ["document", "reference", "canonical", "lookup", "table", "registry"]
    for rule in rules:
        check_text = rule.get("check", "").lower() + rule.get("description", "").lower()
        if any(kw in check_text for kw in context_keywords):
            optional.append({
                "metric": "Faithfulness",
                "reason": f"Rule {rule.get('rule_id', '?')} references context: {rule.get('check', '')}",
            })
            break

    # Check for data source reads -> Hallucination
    data_keywords = ["xlsx", "spreadsheet", "database", "db", "read", "cell", "column", "row"]
    all_step_text = " ".join(
        json.dumps(s).lower() if isinstance(s, dict) else str(s).lower()
        for s in steps
    )
    rule_text = " ".join(
        (rule.get("check", "") + rule.get("description", "")).lower()
        for rule in rules
    )
    combined_text = all_step_text + " " + rule_text

    if any(kw in combined_text for kw in data_keywords):
        optional.append({
            "metric": "Hallucination",
            "reason": "Contract involves reading from data sources — output must match source",
        })

    # Check for user-facing output -> AnswerRelevancy
    output_keywords = ["display", "output", "show", "present", "report", "user-facing"]
    if any(kw in combined_text for kw in output_keywords):
        optional.append({
            "metric": "AnswerRelevancy",
            "reason": "Contract produces user-facing output that must be relevant",
        })

    return optional
