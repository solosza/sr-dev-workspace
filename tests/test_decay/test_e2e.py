"""End-to-end test for tiered memory decay lifecycle."""

import sys
from pathlib import Path
from datetime import datetime, timedelta

sys.path.insert(0, str(Path(__file__).resolve().parent.parent.parent))

from lessons.tiers import MemoryTier
from lessons.decay import DecayEngine
from lessons.promotion import run_promotion_check
from lessons.archival import archive_cold, get_archived, restore_from_archive


def test_full_lifecycle(tmp_path):
    registry = tmp_path / "tiered.json"
    archive = tmp_path / "archive.json"
    engine = DecayEngine(registry_path=registry)
    now = datetime.now()

    recent = engine.add_lesson("recent_key", "Recent issue")
    recent.last_triggered = now.isoformat()

    old = engine.add_lesson("old_key", "Old issue")
    old.last_triggered = (now - timedelta(days=45)).isoformat()
    old.trigger_count = 1

    ancient = engine.add_lesson("ancient_key", "Ancient issue")
    ancient.last_triggered = (now - timedelta(days=200)).isoformat()
    ancient.trigger_count = 1
    ancient.tier = MemoryTier.COLD
    ancient.demoted_at = (now - timedelta(days=100)).isoformat()
    engine._save()

    result = engine.run_decay_cycle(now=now)
    assert result["total_lessons"] == 3
    assert engine.get_lesson("recent_key").tier == MemoryTier.HOT
    assert engine.get_lesson("old_key").tier == MemoryTier.COLD

    promotions = run_promotion_check(engine, {"old_key": 5})
    assert len(promotions) == 1
    assert engine.get_lesson("old_key").tier == MemoryTier.WARM

    archived = archive_cold(engine, cold_threshold_days=90, archive_path=archive, now=now)
    assert len(archived) == 1
    assert archived[0]["pattern_key"] == "ancient_key"
    assert engine.get_lesson("ancient_key") is None

    archive_list = get_archived(archive_path=archive)
    assert len(archive_list) == 1

    restored = restore_from_archive("ancient_key", engine, archive_path=archive)
    assert restored is True
    assert engine.get_lesson("ancient_key") is not None
    assert engine.get_lesson("ancient_key").tier == MemoryTier.WARM
    assert len(get_archived(archive_path=archive)) == 0


def test_decay_and_promotion_interaction(tmp_path):
    registry = tmp_path / "tiered.json"
    engine = DecayEngine(registry_path=registry)
    now = datetime.now()

    lesson = engine.add_lesson("test_key", "Test issue")
    lesson.last_triggered = (now - timedelta(days=20)).isoformat()
    lesson.trigger_count = 1
    engine._save()

    engine.run_decay_cycle(now=now)
    assert engine.get_lesson("test_key").tier == MemoryTier.WARM

    promotions = run_promotion_check(engine, {"test_key": 5})
    assert len(promotions) == 1
    assert engine.get_lesson("test_key").tier == MemoryTier.HOT
