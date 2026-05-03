"""End-to-end test for the recurrence detection flow."""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent.parent))

from lessons.schema import LessonRecord, generate_fingerprint
from lessons.recurrence import RecurrenceTracker
from lessons.alerts import check_threshold, escalate, get_escalation_report
from lessons.integrations import (
    notify_tiered_decay,
    notify_skill_extraction,
    INTEGRATION_READY,
)


def test_full_recurrence_flow(tmp_path):
    """Full pipeline: create lesson, fingerprint, track 4x, verify alert."""
    registry = tmp_path / "registry.json"

    lesson = LessonRecord(
        issue="Hook bypass via direct state file edit",
        root_cause="Agent edited session_state.json directly",
        fix="Added PROTECTED_PATHS check",
        tags=["hook", "enforcement"],
    )
    assert lesson.pattern_key != ""
    assert lesson.pattern_key == generate_fingerprint(lesson.issue, lesson.root_cause)

    tracker = RecurrenceTracker(registry_path=registry)
    for i in range(4):
        count = tracker.record(lesson)
        assert count == i + 1

    assert tracker.get_count(lesson.pattern_key) == 4
    assert check_threshold(tracker, lesson.pattern_key) is True

    report = get_escalation_report(tracker)
    assert len(report) == 1
    assert report[0]["count"] == 4

    msg = report[0]["escalation_message"]
    assert lesson.pattern_key in msg
    assert "ESCALATION" in msg

    # Integration calls should not crash
    notify_tiered_decay(lesson.pattern_key, 4)
    result = notify_skill_extraction(lesson.pattern_key, 4, lesson.issue, lesson.fix)
    assert "is_mature" in result

    # Both integrations are active in the merged workspace
    assert INTEGRATION_READY["tiered_decay"] is True
    assert INTEGRATION_READY["skill_extraction"] is True


def test_multiple_patterns_tracking(tmp_path):
    registry = tmp_path / "registry.json"
    tracker = RecurrenceTracker(registry_path=registry)

    lesson_a = LessonRecord(issue="Hook bypass", root_cause="Direct state edit", fix="Added check")
    lesson_b = LessonRecord(issue="Test failure missed", root_cause="Missing pattern", fix="Added pattern")

    for _ in range(3):
        tracker.record(lesson_a)
    tracker.record(lesson_b)

    assert check_threshold(tracker, lesson_a.pattern_key) is True
    assert check_threshold(tracker, lesson_b.pattern_key) is False

    report = get_escalation_report(tracker)
    assert len(report) == 1
    assert report[0]["pattern_key"] == lesson_a.pattern_key
