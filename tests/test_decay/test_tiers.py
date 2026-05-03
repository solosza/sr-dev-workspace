"""Tests for lessons.tiers — MemoryTier, TieredLesson, and assign_tier."""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent.parent))

from lessons.tiers import MemoryTier, TieredLesson, assign_tier


def test_memory_tier_values():
    assert MemoryTier.HOT.value == "hot"
    assert MemoryTier.WARM.value == "warm"
    assert MemoryTier.COLD.value == "cold"


def test_assign_tier_recent():
    assert assign_tier(0) == MemoryTier.HOT
    assert assign_tier(3) == MemoryTier.HOT
    assert assign_tier(7) == MemoryTier.HOT


def test_assign_tier_warm():
    assert assign_tier(8) == MemoryTier.WARM
    assert assign_tier(15) == MemoryTier.WARM
    assert assign_tier(30) == MemoryTier.WARM


def test_assign_tier_cold():
    assert assign_tier(31) == MemoryTier.COLD
    assert assign_tier(60) == MemoryTier.COLD
    assert assign_tier(365) == MemoryTier.COLD


def test_assign_tier_high_frequency():
    assert assign_tier(50, trigger_count=3) == MemoryTier.HOT
    assert assign_tier(100, trigger_count=5) == MemoryTier.HOT


def test_tiered_lesson_creation():
    lesson = TieredLesson(pattern_key="abc123", tier=MemoryTier.HOT, issue_summary="Test issue")
    assert lesson.pattern_key == "abc123"
    assert lesson.tier == MemoryTier.HOT
    assert lesson.trigger_count == 1


def test_tiered_lesson_serialization():
    original = TieredLesson(pattern_key="abc123", tier=MemoryTier.WARM, issue_summary="Test")
    data = original.to_dict()
    restored = TieredLesson.from_dict(data)
    assert restored.pattern_key == original.pattern_key
    assert restored.tier == original.tier
