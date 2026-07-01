"""Iteration Tracking: Score progression across DeepEval L3 passes.

Tracks DeepEval scores across iteration passes so progression is visible.
Each pass through the backlog -> task-builder -> cycle -> prod-test loop
produces scores. Tracking enables: "Pass 1: 0.62 -> Pass 3: 0.91" reporting.
"""

import json
from dataclasses import dataclass, field, asdict
from pathlib import Path
from typing import Optional


PRODUCTION_READY_THRESHOLD = 0.85
REGRESSION_THRESHOLD = 0.1


@dataclass
class ScoreRecord:
    pass_number: int
    timestamp: str
    command: str
    contract_id: str
    metrics: dict
    overall_pass: bool
    failing_metrics: list = field(default_factory=list)
    gaps_identified: list = field(default_factory=list)


def record_pass(score_history_path, score_record):
    """Append a score record to score-history.json.

    Creates the file and parent directories if they don't exist.
    Updates the progression dict and production_ready status.

    Args:
        score_history_path: Path to score-history.json.
        score_record: ScoreRecord instance.
    """
    path = Path(score_history_path)
    path.parent.mkdir(parents=True, exist_ok=True)

    if path.exists():
        with open(path, "r", encoding="utf-8") as f:
            history = json.load(f)
    else:
        history = {
            "command": score_record.command,
            "passes": [],
            "progression": {},
            "production_ready": False,
            "production_ready_at_pass": None,
        }

    pass_entry = {
        "pass_number": score_record.pass_number,
        "timestamp": score_record.timestamp,
        "scores": score_record.metrics,
        "overall_pass": score_record.overall_pass,
        "failing_metrics": score_record.failing_metrics,
        "gaps_identified": score_record.gaps_identified,
    }
    history["passes"].append(pass_entry)

    # Update progression arrays
    for metric_name, metric_data in score_record.metrics.items():
        score = metric_data["score"] if isinstance(metric_data, dict) else metric_data
        if metric_name not in history["progression"]:
            history["progression"][metric_name] = []
        history["progression"][metric_name].append(score)

    # Update production_ready
    all_pass = all(
        (m["score"] if isinstance(m, dict) else m) >= PRODUCTION_READY_THRESHOLD
        for m in score_record.metrics.values()
    )
    if all_pass and not history["production_ready"]:
        history["production_ready"] = True
        history["production_ready_at_pass"] = score_record.pass_number

    with open(path, "w", encoding="utf-8") as f:
        json.dump(history, f, indent=2)


def detect_regression(score_history_path):
    """Compare latest pass to previous, flag regressions.

    A regression is:
    - Score drops > 0.1 from previous pass
    - A previously-passing metric fails
    - Overall pass reverts to fail

    Args:
        score_history_path: Path to score-history.json.

    Returns:
        List of regression dicts, each with metric, previous, current, delta.
        Empty list if no regressions or fewer than 2 passes.
    """
    path = Path(score_history_path)
    if not path.exists():
        return []

    with open(path, "r", encoding="utf-8") as f:
        history = json.load(f)

    passes = history.get("passes", [])
    if len(passes) < 2:
        return []

    prev_pass = passes[-2]
    curr_pass = passes[-1]
    prev_scores = prev_pass.get("scores", {})
    curr_scores = curr_pass.get("scores", {})

    regressions = []

    for metric_name, curr_data in curr_scores.items():
        if metric_name not in prev_scores:
            continue

        curr_score = curr_data["score"] if isinstance(curr_data, dict) else curr_data
        prev_data = prev_scores[metric_name]
        prev_score = prev_data["score"] if isinstance(prev_data, dict) else prev_data

        delta = curr_score - prev_score

        # Score drop > threshold
        if delta < -REGRESSION_THRESHOLD:
            regressions.append({
                "metric": metric_name,
                "previous": prev_score,
                "current": curr_score,
                "delta": round(delta, 4),
                "reason": "score_drop",
            })
            continue

        # Previously passing, now failing
        prev_passed = prev_data.get("pass", True) if isinstance(prev_data, dict) else True
        curr_passed = curr_data.get("pass", True) if isinstance(curr_data, dict) else True
        if prev_passed and not curr_passed:
            regressions.append({
                "metric": metric_name,
                "previous": prev_score,
                "current": curr_score,
                "delta": round(delta, 4),
                "reason": "pass_to_fail",
            })

    # Overall pass revert
    if prev_pass.get("overall_pass") and not curr_pass.get("overall_pass"):
        regressions.append({
            "metric": "_overall",
            "previous": "PASS",
            "current": "FAIL",
            "delta": None,
            "reason": "overall_revert",
        })

    return regressions


def generate_progression_report(score_history_path):
    """Produce a formatted progression table across all passes.

    Args:
        score_history_path: Path to score-history.json.

    Returns:
        Formatted string with the progression table, or empty string
        if no history exists.
    """
    path = Path(score_history_path)
    if not path.exists():
        return ""

    with open(path, "r", encoding="utf-8") as f:
        history = json.load(f)

    passes = history.get("passes", [])
    progression = history.get("progression", {})
    command = history.get("command", "unknown")

    if not passes:
        return ""

    latest_pass = passes[-1]
    pass_count = len(passes)

    lines = []
    lines.append(f"DEEPEVAL L3 SCORES — {command} (Pass {pass_count})")
    lines.append("")

    # Header
    header = f"  {'Metric':<22}"
    for i in range(1, pass_count + 1):
        header += f"Pass {i:<4}  "
    header += "Status"
    lines.append(header)

    # Rows
    latest_scores = latest_pass.get("scores", {})
    for metric_name, scores in progression.items():
        row = f"  {metric_name:<22}"
        for score in scores:
            row += f"{score:<10.2f}"
        # Determine pass/fail from latest
        metric_data = latest_scores.get(metric_name, {})
        if isinstance(metric_data, dict):
            passed = metric_data.get("pass", metric_data.get("score", 0) >= PRODUCTION_READY_THRESHOLD)
        else:
            passed = metric_data >= PRODUCTION_READY_THRESHOLD
        status = "PASS" if passed else "FAIL"
        row += status
        lines.append(row)

    lines.append("")
    overall = "PASS" if latest_pass.get("overall_pass") else "FAIL"
    lines.append(f"  Overall: {overall}")

    if history.get("production_ready"):
        lines.append(f"  Production ready at pass {history['production_ready_at_pass']}.")

    return "\n".join(lines)


def is_production_ready(score_history_path):
    """Check if all metrics meet the production_ready threshold (0.85).

    Args:
        score_history_path: Path to score-history.json.

    Returns:
        True if the latest pass has all metrics >= 0.85, False otherwise.
    """
    path = Path(score_history_path)
    if not path.exists():
        return False

    with open(path, "r", encoding="utf-8") as f:
        history = json.load(f)

    return history.get("production_ready", False)
