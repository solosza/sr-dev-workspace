"""Tests for lessons.promotion — promotion rules."""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent.parent))

from lessons.tiers import MemoryTier
from lessons.decay import DecayEngine
from lessons.promotion import evaluate_promotion, run_promotion_check


def test_promote_cold_to_warm():
    result = evaluate_promotion("abc", 5, MemoryTier.COLD)
    assert result == MemoryTier.WARM


def test_promote_warm_to_hot():
    result = evaluate_promotion("abc", 5, MemoryTier.WARM)
    assert result == MemoryTier.HOT


def test_no_promotion_low_count():
    result = evaluate_promotion("abc", 1, MemoryTier.COLD)
    assert result == MemoryTier.COLD


def test_hot_stays_hot():
    result = evaluate_promotion("abc", 10, MemoryTier.HOT)
    assert result == MemoryTier.HOT


def test_run_promotion_check(tmp_path):
    registry = tmp_path / "tiered.json"
    engine = DecayEngine(registry_path=registry)
    lesson = engine.add_lesson("abc123", "Recurring issue")
    lesson.tier = MemoryTier.COLD
    engine._save()
    recurrence_data = {"abc123": 5}
    promotions = run_promotion_check(engine, recurrence_data)
    assert len(promotions) == 1
    assert promotions[0]["old_tier"] == "cold"
    assert promotions[0]["new_tier"] == "warm"
    assert engine.get_lesson("abc123").tier == MemoryTier.WARM
