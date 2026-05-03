"""Bookmark state tracking — tracks processed post IDs to enable idempotent runs."""

import json
from datetime import datetime
from pathlib import Path
from typing import Optional


DEFAULT_STATE_PATH = Path(".claude/state/x_bookmarks_processed.json")


class BookmarkState:
    """Tracks which bookmarks have been processed.

    Args:
        state_path: Path to the state JSON file.
    """

    def __init__(self, state_path: Optional[Path] = None):
        if state_path is None:
            state_path = DEFAULT_STATE_PATH
        self.state_path = Path(state_path)
        self._data = self._load()

    def _load(self) -> dict:
        if self.state_path.exists():
            try:
                return json.loads(self.state_path.read_text())
            except (json.JSONDecodeError, IOError):
                pass
        return {"processed": {}, "last_scan": None}

    def _save(self):
        self.state_path.parent.mkdir(parents=True, exist_ok=True)
        self.state_path.write_text(json.dumps(self._data, indent=2))

    def is_processed(self, post_id: str) -> bool:
        """Check if a post has already been processed."""
        return post_id in self._data["processed"]

    def mark_processed(self, post_id: str, summary: str = "") -> None:
        """Mark a post as processed."""
        self._data["processed"][post_id] = {
            "summary": summary,
            "processed_at": datetime.now().isoformat(),
        }
        self._save()

    def get_last_scan_date(self) -> Optional[str]:
        """Get the date of the last scan."""
        return self._data.get("last_scan")

    def set_last_scan_date(self, date: Optional[str] = None) -> None:
        """Set the last scan date."""
        if date is None:
            date = datetime.now().isoformat()
        self._data["last_scan"] = date
        self._save()

    def get_processed_count(self) -> int:
        """Get count of processed posts."""
        return len(self._data["processed"])
