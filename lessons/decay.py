"""Decay engine — processes lessons and re-evaluates tier assignments.

Handles automatic demotion of lessons that haven't been triggered recently
and provides tier-based filtering.
"""

import json
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Optional

from lessons.tiers import MemoryTier, TieredLesson, assign_tier


class DecayEngine:
    """Manages tiered lesson lifecycle: decay, promotion, and querying.

    Args:
        registry_path: Path to the tiered lessons JSON file.
            Defaults to `.claude/state/tiered_lessons.json`.
    """

    def __init__(self, registry_path: Optional[Path] = None):
        if registry_path is None:
            registry_path = Path(".claude/state/tiered_lessons.json")
        self.registry_path = Path(registry_path)
        self._lessons: Dict[str, TieredLesson] = {}
        self._load()

    def _load(self):
        """Load tiered lessons from disk."""
        if self.registry_path.exists():
            try:
                data = json.loads(self.registry_path.read_text())
                self._lessons = {
                    k: TieredLesson.from_dict(v) for k, v in data.items()
                }
            except (json.JSONDecodeError, IOError):
                self._lessons = {}
        else:
            self._lessons = {}

    def _save(self):
        """Persist tiered lessons to disk."""
        self.registry_path.parent.mkdir(parents=True, exist_ok=True)
        data = {k: v.to_dict() for k, v in self._lessons.items()}
        self.registry_path.write_text(json.dumps(data, indent=2))

    def add_lesson(self, pattern_key: str, issue_summary: str = "") -> TieredLesson:
        """Add a new lesson or update existing one.

        Args:
            pattern_key: The lesson fingerprint.
            issue_summary: Brief description.

        Returns:
            The TieredLesson instance.
        """
        if pattern_key in self._lessons:
            lesson = self._lessons[pattern_key]
            lesson.trigger_count += 1
            lesson.last_triggered = datetime.now().isoformat()
        else:
            lesson = TieredLesson(
                pattern_key=pattern_key,
                issue_summary=issue_summary,
            )
            self._lessons[pattern_key] = lesson
        self._save()
        return lesson

    def run_decay_cycle(self, now: Optional[datetime] = None) -> dict:
        """Re-evaluate all lessons and demote stale ones.

        Args:
            now: Current time (for testing). Defaults to datetime.now().

        Returns:
            Summary dict with counts of demotions/promotions.
        """
        if now is None:
            now = datetime.now()

        demotions = 0
        promotions = 0

        for key, lesson in self._lessons.items():
            last_dt = datetime.fromisoformat(lesson.last_triggered)
            days_since = (now - last_dt).days
            new_tier = assign_tier(days_since, lesson.trigger_count)

            if new_tier != lesson.tier:
                old_tier = lesson.tier
                lesson.tier = new_tier
                now_iso = now.isoformat()
                # Determine if demotion or promotion
                tier_order = {MemoryTier.HOT: 0, MemoryTier.WARM: 1, MemoryTier.COLD: 2}
                if tier_order[new_tier] > tier_order[old_tier]:
                    lesson.demoted_at = now_iso
                    demotions += 1
                else:
                    lesson.promoted_at = now_iso
                    promotions += 1

        self._save()
        return {
            "total_lessons": len(self._lessons),
            "demotions": demotions,
            "promotions": promotions,
        }

    def get_lessons_by_tier(self, tier: MemoryTier) -> List[TieredLesson]:
        """Get all lessons in a specific tier.

        Args:
            tier: The tier to filter by.

        Returns:
            List of TieredLesson instances in that tier.
        """
        return [l for l in self._lessons.values() if l.tier == tier]

    def update_trigger(self, pattern_key: str) -> Optional[TieredLesson]:
        """Mark a lesson as recently triggered.

        Resets the last_triggered timestamp and increments trigger count.

        Args:
            pattern_key: The lesson fingerprint.

        Returns:
            The updated TieredLesson, or None if not found.
        """
        lesson = self._lessons.get(pattern_key)
        if lesson is None:
            return None
        lesson.last_triggered = datetime.now().isoformat()
        lesson.trigger_count += 1
        self._save()
        return lesson

    def get_lesson(self, pattern_key: str) -> Optional[TieredLesson]:
        """Get a specific lesson by pattern key."""
        return self._lessons.get(pattern_key)

    def remove_lesson(self, pattern_key: str) -> Optional[TieredLesson]:
        """Remove a lesson from the active registry.

        Args:
            pattern_key: The lesson to remove.

        Returns:
            The removed lesson, or None if not found.
        """
        lesson = self._lessons.pop(pattern_key, None)
        if lesson is not None:
            self._save()
        return lesson
