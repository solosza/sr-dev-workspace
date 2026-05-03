"""Tests for lessons.schema — LessonRecord and fingerprint generation."""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent.parent))

from lessons.schema import LessonRecord, generate_fingerprint


def test_lesson_record_creation():
    record = LessonRecord(
        issue="Hook bypass",
        root_cause="Direct state edit",
        fix="Added protected paths check",
        tags=["hook", "enforcement"],
    )
    assert record.issue == "Hook bypass"
    assert record.root_cause == "Direct state edit"
    assert record.fix == "Added protected paths check"
    assert record.tags == ["hook", "enforcement"]
    assert record.recurrence_count == 1
    assert record.pattern_key != ""


def test_fingerprint_deterministic():
    fp1 = generate_fingerprint("Hook bypass", "Direct state edit")
    fp2 = generate_fingerprint("Hook bypass", "Direct state edit")
    assert fp1 == fp2


def test_fingerprint_normalization():
    fp1 = generate_fingerprint("Hook Bypass", "Direct State Edit")
    fp2 = generate_fingerprint("hook bypass", "direct state edit")
    fp3 = generate_fingerprint("  hook   bypass  ", "  direct   state   edit  ")
    assert fp1 == fp2
    assert fp2 == fp3


def test_fingerprint_different_inputs():
    fp1 = generate_fingerprint("Hook bypass", "Direct state edit")
    fp2 = generate_fingerprint("Test failure", "Missing pattern")
    assert fp1 != fp2


def test_lesson_record_defaults():
    record = LessonRecord(issue="Test issue", root_cause="Test cause", fix="Test fix")
    assert record.recurrence_count == 1
    assert record.tags == []
    assert record.first_seen != ""
    assert record.last_seen != ""
    assert record.pattern_key != ""


def test_lesson_record_serialization():
    original = LessonRecord(
        issue="Hook bypass", root_cause="Direct state edit",
        fix="Added check", tags=["hook"],
    )
    data = original.to_dict()
    restored = LessonRecord.from_dict(data)
    assert restored.issue == original.issue
    assert restored.root_cause == original.root_cause
    assert restored.pattern_key == original.pattern_key
    assert restored.tags == original.tags
