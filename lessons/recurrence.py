"""Recurrence tracker — maintains a registry of lesson fingerprints and counts.

Persists to a JSON file so recurrence data survives across sessions.
"""

import json
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Optional

from lessons.schema import LessonRecord


class RecurrenceTracker:
    """Tracks lesson recurrence via pattern-key fingerprints.

    The registry maps pattern_key -> { count, first_seen, last_seen, issue_summary }.
    It persists to a JSON file at the given path.

    Args:
        registry_path: Path to the JSON registry file.
            Defaults to `.claude/state/recurrence_registry.json`.
    """

    def __init__(self, registry_path: Optional[Path] = None):
        if registry_path is None:
            registry_path = Path(".claude/state/recurrence_registry.json")
        self.registry_path = Path(registry_path)
        self._registry: Dict[str, dict] = {}
        self._load()

    def _load(self):
        """Load registry from disk."""
        if self.registry_path.exists():
            try:
                self._registry = json.loads(self.registry_path.read_text())
            except (json.JSONDecodeError, IOError):
                self._registry = {}
        else:
            self._registry = {}

    def _save(self):
        """Persist registry to disk."""
        self.registry_path.parent.mkdir(parents=True, exist_ok=True)
        self.registry_path.write_text(json.dumps(self._registry, indent=2))

    def record(self, lesson: LessonRecord) -> int:
        """Register a lesson occurrence. Increments recurrence_count if pattern_key exists.

        Args:
            lesson: The lesson record to track.

        Returns:
            The new recurrence_count for this pattern.
        """
        now = datetime.now().isoformat()
        key = lesson.pattern_key

        if key in self._registry:
            self._registry[key]["count"] += 1
            self._registry[key]["last_seen"] = now
        else:
            self._registry[key] = {
                "count": 1,
                "first_seen": now,
                "last_seen": now,
                "issue_summary": lesson.issue,
            }

        self._save()
        return self._registry[key]["count"]

    def get_count(self, pattern_key: str) -> int:
        """Get current recurrence count for a pattern key.

        Args:
            pattern_key: The fingerprint to look up.

        Returns:
            The recurrence count, or 0 if not found.
        """
        entry = self._registry.get(pattern_key)
        if entry is None:
            return 0
        return entry["count"]

    def get_all(self) -> Dict[str, dict]:
        """Return the full registry.

        Returns:
            Dictionary mapping pattern_key to entry data.
        """
        return dict(self._registry)

    def get_recurring(self, min_count: int = 3) -> List[dict]:
        """Return lessons with recurrence count at or above the threshold.

        Args:
            min_count: Minimum recurrence count to include. Default 3.

        Returns:
            List of registry entries (with pattern_key added) above threshold.
        """
        results = []
        for key, entry in self._registry.items():
            if entry["count"] >= min_count:
                result = dict(entry)
                result["pattern_key"] = key
                results.append(result)
        return results
