"""Tests for lessons.decay — DecayEngine."""

import sys
from pathlib import Path
from datetime import datetime, timedelta

sys.path.insert(0, str(Path(__file__).resolve().parent.parent.parent))

from lessons.tiers import MemoryTier
from lessons.decay import DecayEngine


def test_decay_cycle_demotes_stale(tmp_path):
    registry = tmp_path / "tiered.json"
    engine = DecayEngine(registry_path=registry)
    lesson = engine.add_lesson("abc123", "Old issue")
    lesson.last_triggered = (datetime.now() - timedelta(days=45)).isoformat()
    lesson.tier = MemoryTier.HOT
    lesson.trigger_count = 1
    engine._save()
    now = datetime.now()
    result = engine.run_decay_cycle(now=now)
    assert result["demotions"] >= 1
    assert engine.get_lesson("abc123").tier == MemoryTier.COLD


def test_get_lessons_by_tier(tmp_path):
    registry = tmp_path / "tiered.json"
    engine = DecayEngine(registry_path=registry)
    l1 = engine.add_lesson("hot1", "Hot issue")
    l1.tier = MemoryTier.HOT
    l2 = engine.add_lesson("warm1", "Warm issue")
    l2.tier = MemoryTier.WARM
    l3 = engine.add_lesson("cold1", "Cold issue")
    l3.tier = MemoryTier.COLD
    engine._save()
    hot = engine.get_lessons_by_tier(MemoryTier.HOT)
    assert len(hot) == 1
    assert hot[0].pattern_key == "hot1"
    cold = engine.get_lessons_by_tier(MemoryTier.COLD)
    assert len(cold) == 1


def test_update_trigger_resets_timer(tmp_path):
    registry = tmp_path / "tiered.json"
    engine = DecayEngine(registry_path=registry)
    engine.add_lesson("abc123", "Test")
    engine.update_trigger("abc123")
    updated = engine.get_lesson("abc123")
    assert updated.trigger_count == 2


def test_persistence(tmp_path):
    registry = tmp_path / "tiered.json"
    engine1 = DecayEngine(registry_path=registry)
    engine1.add_lesson("abc123", "Test issue")
    engine2 = DecayEngine(registry_path=registry)
    assert engine2.get_lesson("abc123") is not None
    assert engine2.get_lesson("abc123").issue_summary == "Test issue"


def test_empty_registry(tmp_path):
    registry = tmp_path / "tiered.json"
    engine = DecayEngine(registry_path=registry)
    result = engine.run_decay_cycle()
    assert result["total_lessons"] == 0
    assert result["demotions"] == 0
