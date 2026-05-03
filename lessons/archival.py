"""Archival module for cold lessons.

Moves lessons that have been COLD for an extended period to an archive file,
keeping the active lesson set manageable. Supports restoration.
"""

import json
from datetime import datetime
from pathlib import Path
from typing import List, Optional

from lessons.tiers import MemoryTier, TieredLesson
from lessons.decay import DecayEngine


# Default archive file path
DEFAULT_ARCHIVE_PATH = Path(".claude/state/archived_lessons.json")


def _load_archive(archive_path: Path) -> List[dict]:
    """Load archived lessons from disk."""
    if archive_path.exists():
        try:
            return json.loads(archive_path.read_text())
        except (json.JSONDecodeError, IOError):
            return []
    return []


def _save_archive(archive_path: Path, lessons: List[dict]):
    """Save archived lessons to disk."""
    archive_path.parent.mkdir(parents=True, exist_ok=True)
    archive_path.write_text(json.dumps(lessons, indent=2))


def archive_cold(
    engine: DecayEngine,
    cold_threshold_days: int = 90,
    archive_path: Optional[Path] = None,
    now: Optional[datetime] = None,
) -> List[dict]:
    """Move lessons that have been COLD for > threshold days to archive.

    Args:
        engine: The DecayEngine instance.
        cold_threshold_days: Days in COLD tier before archiving. Default 90.
        archive_path: Path to archive file. Default `.claude/state/archived_lessons.json`.
        now: Current time (for testing). Defaults to datetime.now().

    Returns:
        List of archived lesson dicts.
    """
    if archive_path is None:
        archive_path = DEFAULT_ARCHIVE_PATH
    if now is None:
        now = datetime.now()

    cold_lessons = engine.get_lessons_by_tier(MemoryTier.COLD)
    archived = []

    for lesson in cold_lessons:
        # Check how long it's been cold
        if lesson.demoted_at:
            demoted_dt = datetime.fromisoformat(lesson.demoted_at)
        else:
            demoted_dt = datetime.fromisoformat(lesson.last_triggered)
        days_cold = (now - demoted_dt).days

        if days_cold >= cold_threshold_days:
            lesson_data = lesson.to_dict()
            lesson_data["archived_at"] = now.isoformat()
            archived.append(lesson_data)
            engine.remove_lesson(lesson.pattern_key)

    if archived:
        existing = _load_archive(archive_path)
        existing.extend(archived)
        _save_archive(archive_path, existing)

    return archived


def get_archived(archive_path: Optional[Path] = None) -> List[dict]:
    """Return all archived lessons.

    Args:
        archive_path: Path to archive file.

    Returns:
        List of archived lesson dicts.
    """
    if archive_path is None:
        archive_path = DEFAULT_ARCHIVE_PATH
    return _load_archive(archive_path)


def restore_from_archive(
    pattern_key: str,
    engine: DecayEngine,
    archive_path: Optional[Path] = None,
) -> bool:
    """Restore an archived lesson back to the active registry as WARM.

    Args:
        pattern_key: The lesson fingerprint to restore.
        engine: The DecayEngine to restore into.
        archive_path: Path to archive file.

    Returns:
        True if restored, False if not found in archive.
    """
    if archive_path is None:
        archive_path = DEFAULT_ARCHIVE_PATH

    archive = _load_archive(archive_path)
    found = None
    remaining = []

    for entry in archive:
        if entry["pattern_key"] == pattern_key:
            found = entry
        else:
            remaining.append(entry)

    if found is None:
        return False

    # Restore to active registry as WARM
    lesson = engine.add_lesson(pattern_key, found.get("issue_summary", ""))
    lesson.tier = MemoryTier.WARM
    lesson.promoted_at = datetime.now().isoformat()
    engine._save()

    # Update archive
    _save_archive(archive_path, remaining)
    return True
