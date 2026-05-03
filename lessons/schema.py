"""Lesson schema with pattern-key fingerprinting.

Provides a structured LessonRecord dataclass and deterministic fingerprint
generation for identifying recurring issues.
"""

import hashlib
import re
from dataclasses import dataclass, field
from datetime import datetime
from typing import List, Optional


@dataclass
class LessonRecord:
    """Structured lesson entry with recurrence tracking fields.

    Attributes:
        issue: What happened (the symptom/failure).
        root_cause: Why it happened (the underlying reason).
        fix: How it was resolved.
        pattern_key: Deterministic fingerprint of issue + root_cause.
        recurrence_count: Number of times this pattern has been seen.
        first_seen: ISO timestamp of first occurrence.
        last_seen: ISO timestamp of most recent occurrence.
        tags: Categorization tags for the lesson.
    """

    issue: str
    root_cause: str
    fix: str
    pattern_key: str = ""
    recurrence_count: int = 1
    first_seen: str = field(default_factory=lambda: datetime.now().isoformat())
    last_seen: str = field(default_factory=lambda: datetime.now().isoformat())
    tags: List[str] = field(default_factory=list)

    def __post_init__(self):
        """Auto-generate pattern_key if not provided."""
        if not self.pattern_key:
            self.pattern_key = generate_fingerprint(self.issue, self.root_cause)

    def to_dict(self) -> dict:
        """Serialize to dictionary."""
        return {
            "issue": self.issue,
            "root_cause": self.root_cause,
            "fix": self.fix,
            "pattern_key": self.pattern_key,
            "recurrence_count": self.recurrence_count,
            "first_seen": self.first_seen,
            "last_seen": self.last_seen,
            "tags": self.tags,
        }

    @classmethod
    def from_dict(cls, data: dict) -> "LessonRecord":
        """Deserialize from dictionary."""
        return cls(
            issue=data["issue"],
            root_cause=data["root_cause"],
            fix=data["fix"],
            pattern_key=data.get("pattern_key", ""),
            recurrence_count=data.get("recurrence_count", 1),
            first_seen=data.get("first_seen", datetime.now().isoformat()),
            last_seen=data.get("last_seen", datetime.now().isoformat()),
            tags=data.get("tags", []),
        )


def _normalize(text: str) -> str:
    """Normalize text for fingerprinting.

    Strips leading/trailing whitespace, collapses internal whitespace,
    and lowercases the text.
    """
    text = text.strip().lower()
    text = re.sub(r"\s+", " ", text)
    return text


def generate_fingerprint(issue: str, root_cause: str) -> str:
    """Generate a deterministic fingerprint from issue + root_cause.

    The fingerprint normalizes whitespace and case before hashing,
    so minor formatting differences don't create separate entries.

    Args:
        issue: The issue description.
        root_cause: The root cause description.

    Returns:
        A hex digest string (SHA-256, first 16 chars) serving as the pattern key.
    """
    normalized = f"{_normalize(issue)}|{_normalize(root_cause)}"
    return hashlib.sha256(normalized.encode("utf-8")).hexdigest()[:16]
