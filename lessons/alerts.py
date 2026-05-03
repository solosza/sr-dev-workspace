"""Alert and escalation module for recurring lessons.

When a lesson recurs above a threshold, the current fix is insufficient.
This module provides threshold checking, escalation message generation,
and reporting for recurring patterns.
"""

from typing import List

from lessons.recurrence import RecurrenceTracker


def check_threshold(
    tracker: RecurrenceTracker, pattern_key: str, threshold: int = 3
) -> bool:
    """Check if a pattern's recurrence count meets or exceeds the threshold.

    Args:
        tracker: The recurrence tracker instance.
        pattern_key: The fingerprint to check.
        threshold: Minimum count to trigger escalation. Default 3.

    Returns:
        True if count >= threshold.
    """
    return tracker.get_count(pattern_key) >= threshold


def escalate(pattern_key: str, count: int, issue_summary: str) -> str:
    """Generate a formatted escalation message.

    Args:
        pattern_key: The fingerprint of the recurring lesson.
        count: Current recurrence count.
        issue_summary: Brief description of the issue.

    Returns:
        Formatted escalation message string.
    """
    return (
        f"ESCALATION: Recurring issue detected\n"
        f"\n"
        f"  Pattern Key:  {pattern_key}\n"
        f"  Recurrences:  {count}\n"
        f"  Issue:        {issue_summary}\n"
        f"\n"
        f"  Recommendation: The current lesson/hook is not preventing this issue.\n"
        f"  Investigate the root cause at a deeper level. Consider:\n"
        f"  - Adding a PreToolUse hook to block the problematic action\n"
        f"  - Updating the protocol with a stronger constraint\n"
        f"  - Creating a dedicated command to handle this pattern\n"
    )


def get_escalation_report(
    tracker: RecurrenceTracker, threshold: int = 3
) -> List[dict]:
    """Get all lessons above the threshold with escalation details.

    Args:
        tracker: The recurrence tracker instance.
        threshold: Minimum count to include. Default 3.

    Returns:
        List of dicts with pattern_key, count, issue_summary,
        and escalation_message for each recurring issue.
    """
    recurring = tracker.get_recurring(min_count=threshold)
    report = []
    for entry in recurring:
        report.append(
            {
                "pattern_key": entry["pattern_key"],
                "count": entry["count"],
                "issue_summary": entry["issue_summary"],
                "first_seen": entry["first_seen"],
                "last_seen": entry["last_seen"],
                "escalation_message": escalate(
                    entry["pattern_key"], entry["count"], entry["issue_summary"]
                ),
            }
        )
    return report
