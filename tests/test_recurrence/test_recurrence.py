"""Tests for lessons.recurrence — RecurrenceTracker."""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent.parent))

from lessons.schema import LessonRecord
from lessons.recurrence import RecurrenceTracker


def test_record_new_lesson(tmp_path):
    registry = tmp_path / "registry.json"
    tracker = RecurrenceTracker(registry_path=registry)
    lesson = LessonRecord(issue="Hook bypass", root_cause="Direct state edit", fix="Added check")
    count = tracker.record(lesson)
    assert count == 1


def test_record_recurring_lesson(tmp_path):
    registry = tmp_path / "registry.json"
    tracker = RecurrenceTracker(registry_path=registry)
    lesson = LessonRecord(issue="Hook bypass", root_cause="Direct state edit", fix="Added check")
    tracker.record(lesson)
    tracker.record(lesson)
    count = tracker.record(lesson)
    assert count == 3


def test_get_count_unknown(tmp_path):
    registry = tmp_path / "registry.json"
    tracker = RecurrenceTracker(registry_path=registry)
    assert tracker.get_count("nonexistent_key") == 0


def test_get_recurring_above_threshold(tmp_path):
    registry = tmp_path / "registry.json"
    tracker = RecurrenceTracker(registry_path=registry)
    lesson_a = LessonRecord(issue="Hook bypass", root_cause="Direct state edit", fix="Check A")
    for _ in range(4):
        tracker.record(lesson_a)
    lesson_b = LessonRecord(issue="Test failure", root_cause="Missing pattern", fix="Check B")
    tracker.record(lesson_b)
    recurring = tracker.get_recurring(min_count=3)
    assert len(recurring) == 1
    assert recurring[0]["count"] == 4
    assert recurring[0]["pattern_key"] == lesson_a.pattern_key


def test_persistence(tmp_path):
    registry = tmp_path / "registry.json"
    tracker1 = RecurrenceTracker(registry_path=registry)
    lesson = LessonRecord(issue="Hook bypass", root_cause="Direct state edit", fix="Added check")
    tracker1.record(lesson)
    tracker1.record(lesson)
    tracker2 = RecurrenceTracker(registry_path=registry)
    assert tracker2.get_count(lesson.pattern_key) == 2


def test_get_all(tmp_path):
    registry = tmp_path / "registry.json"
    tracker = RecurrenceTracker(registry_path=registry)
    lesson_a = LessonRecord(issue="Issue A", root_cause="Cause A", fix="Fix A")
    lesson_b = LessonRecord(issue="Issue B", root_cause="Cause B", fix="Fix B")
    tracker.record(lesson_a)
    tracker.record(lesson_b)
    all_entries = tracker.get_all()
    assert len(all_entries) == 2
