"""Tests for lessons.alerts — threshold checking and escalation."""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent.parent))

from lessons.schema import LessonRecord
from lessons.recurrence import RecurrenceTracker
from lessons.alerts import check_threshold, escalate, get_escalation_report


def test_check_threshold_below(tmp_path):
    registry = tmp_path / "registry.json"
    tracker = RecurrenceTracker(registry_path=registry)
    lesson = LessonRecord(issue="Hook bypass", root_cause="Direct state edit", fix="Check")
    tracker.record(lesson)
    assert check_threshold(tracker, lesson.pattern_key, threshold=3) is False


def test_check_threshold_at(tmp_path):
    registry = tmp_path / "registry.json"
    tracker = RecurrenceTracker(registry_path=registry)
    lesson = LessonRecord(issue="Hook bypass", root_cause="Direct state edit", fix="Check")
    for _ in range(3):
        tracker.record(lesson)
    assert check_threshold(tracker, lesson.pattern_key, threshold=3) is True


def test_check_threshold_above(tmp_path):
    registry = tmp_path / "registry.json"
    tracker = RecurrenceTracker(registry_path=registry)
    lesson = LessonRecord(issue="Hook bypass", root_cause="Direct state edit", fix="Check")
    for _ in range(5):
        tracker.record(lesson)
    assert check_threshold(tracker, lesson.pattern_key, threshold=3) is True


def test_escalate_message_format():
    msg = escalate("abc123", 5, "Hook bypass via state edit")
    assert "abc123" in msg
    assert "5" in msg
    assert "Hook bypass via state edit" in msg
    assert "ESCALATION" in msg


def test_escalation_report_empty(tmp_path):
    registry = tmp_path / "registry.json"
    tracker = RecurrenceTracker(registry_path=registry)
    lesson = LessonRecord(issue="Hook bypass", root_cause="Direct state edit", fix="Check")
    tracker.record(lesson)
    report = get_escalation_report(tracker, threshold=3)
    assert report == []


def test_escalation_report_with_recurring(tmp_path):
    registry = tmp_path / "registry.json"
    tracker = RecurrenceTracker(registry_path=registry)
    lesson = LessonRecord(issue="Hook bypass", root_cause="Direct state edit", fix="Check")
    for _ in range(4):
        tracker.record(lesson)
    report = get_escalation_report(tracker, threshold=3)
    assert len(report) == 1
    assert report[0]["count"] == 4
    assert "ESCALATION" in report[0]["escalation_message"]
