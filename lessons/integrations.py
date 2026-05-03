"""Integration points for cross-feature communication.

Connects recurrence detection with tiered decay and skill extraction.
Both integrations are active.
"""

from lessons.decay import DecayEngine
from lessons.maturity import evaluate_maturity


# Readiness flags
INTEGRATION_READY = {
    "tiered_decay": True,
    "skill_extraction": True,
}


def notify_tiered_decay(pattern_key: str, recurrence_count: int) -> None:
    """Notify the tiered decay system about a lesson's recurrence.

    Updates the lesson's trigger timestamp in the decay engine,
    which may affect its tier assignment on the next decay cycle.

    Args:
        pattern_key: The fingerprint of the lesson.
        recurrence_count: Current recurrence count.
    """
    engine = DecayEngine()
    existing = engine.get_lesson(pattern_key)
    if existing:
        engine.update_trigger(pattern_key)
    else:
        engine.add_lesson(pattern_key, issue_summary=f"Auto-added from recurrence (count={recurrence_count})")


def notify_skill_extraction(
    pattern_key: str, recurrence_count: int, issue: str, fix: str
) -> dict:
    """Evaluate whether a recurring lesson is mature enough for skill extraction.

    When a lesson recurs, this function checks maturity and returns
    the assessment. The caller (learn command) uses this to decide
    whether to trigger draft generation.

    Args:
        pattern_key: The fingerprint of the lesson.
        recurrence_count: Current recurrence count.
        issue: The issue description.
        fix: The fix description.

    Returns:
        Maturity assessment dict with is_mature, score, recommendation.
    """
    assessment = evaluate_maturity(recurrence_count)
    return assessment
