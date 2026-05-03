"""Maturity evaluator for lessons.

Determines whether a lesson has been applied enough times with enough
consistency to graduate into a reusable skill or command.
"""

from collections import Counter
from typing import List


# Default threshold: how many recurrences before considering extraction
MATURITY_THRESHOLD = 5

# Minimum fix consistency to extract (0.0 to 1.0)
MIN_FIX_CONSISTENCY = 0.7


def calculate_fix_consistency(fixes: List[str]) -> float:
    """Calculate how consistent the fix pattern is across occurrences.

    Returns the ratio of the most common fix to total fixes.
    A ratio of 1.0 means every occurrence used the same fix.

    Args:
        fixes: List of fix description strings.

    Returns:
        Consistency ratio between 0.0 and 1.0.
    """
    if not fixes:
        return 0.0

    # Normalize fixes for comparison
    normalized = [f.strip().lower() for f in fixes]
    counts = Counter(normalized)
    most_common_count = counts.most_common(1)[0][1]
    return most_common_count / len(normalized)


def evaluate_maturity(
    recurrence_count: int,
    fix_consistency: float = 1.0,
    threshold: int = MATURITY_THRESHOLD,
) -> dict:
    """Evaluate whether a lesson is mature enough to extract into a skill.

    Args:
        recurrence_count: Number of times the lesson has been triggered.
        fix_consistency: How consistent the fix pattern is (0.0 to 1.0).
        threshold: Minimum recurrence count for maturity.

    Returns:
        Dict with:
        - is_mature: bool
        - score: float (0.0 to 1.0)
        - recommendation: "extract", "monitor", or "too_early"
    """
    # Calculate maturity score
    count_score = min(recurrence_count / threshold, 1.0)
    score = count_score * fix_consistency

    if recurrence_count < threshold:
        return {
            "is_mature": False,
            "score": score,
            "recommendation": "too_early",
        }

    if fix_consistency < MIN_FIX_CONSISTENCY:
        return {
            "is_mature": False,
            "score": score,
            "recommendation": "monitor",
        }

    return {
        "is_mature": True,
        "score": score,
        "recommendation": "extract",
    }
