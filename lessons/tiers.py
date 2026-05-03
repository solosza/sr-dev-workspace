"""Memory tier definitions and assignment logic.

Provides HOT/WARM/COLD tier classification for lessons based on
recency of last trigger and trigger frequency.
"""

from dataclasses import dataclass, field
from datetime import datetime
from enum import Enum
from typing import Optional


# Tier thresholds (in days)
HOT_THRESHOLD_DAYS = 7
WARM_THRESHOLD_DAYS = 30

# Promotion threshold: triggers in the hot window that auto-promote
HOT_TRIGGER_COUNT = 3


class MemoryTier(Enum):
    """Memory tier for a lesson."""
    HOT = "hot"
    WARM = "warm"
    COLD = "cold"


@dataclass
class TieredLesson:
    """A lesson with tier tracking metadata.

    Attributes:
        pattern_key: Fingerprint identifying the lesson pattern.
        tier: Current memory tier.
        last_triggered: ISO timestamp of last trigger.
        trigger_count: Number of times triggered in the hot window.
        promoted_at: ISO timestamp of last promotion, or None.
        demoted_at: ISO timestamp of last demotion, or None.
        issue_summary: Brief description of the issue.
    """
    pattern_key: str
    tier: MemoryTier = MemoryTier.WARM
    last_triggered: str = field(default_factory=lambda: datetime.now().isoformat())
    trigger_count: int = 1
    promoted_at: Optional[str] = None
    demoted_at: Optional[str] = None
    issue_summary: str = ""

    def to_dict(self) -> dict:
        """Serialize to dictionary."""
        return {
            "pattern_key": self.pattern_key,
            "tier": self.tier.value,
            "last_triggered": self.last_triggered,
            "trigger_count": self.trigger_count,
            "promoted_at": self.promoted_at,
            "demoted_at": self.demoted_at,
            "issue_summary": self.issue_summary,
        }

    @classmethod
    def from_dict(cls, data: dict) -> "TieredLesson":
        """Deserialize from dictionary."""
        return cls(
            pattern_key=data["pattern_key"],
            tier=MemoryTier(data.get("tier", "warm")),
            last_triggered=data.get("last_triggered", datetime.now().isoformat()),
            trigger_count=data.get("trigger_count", 1),
            promoted_at=data.get("promoted_at"),
            demoted_at=data.get("demoted_at"),
            issue_summary=data.get("issue_summary", ""),
        )


def assign_tier(last_triggered_days: int, trigger_count: int = 1) -> MemoryTier:
    """Assign a memory tier based on recency and activity.

    Rules:
    - Triggered in last 7 days OR 3+ triggers in the hot window -> HOT
    - 8-30 days since last trigger -> WARM
    - >30 days since last trigger -> COLD

    Args:
        last_triggered_days: Days since the lesson was last triggered.
        trigger_count: Number of triggers in the recent window.

    Returns:
        The appropriate MemoryTier.
    """
    # High frequency always promotes to HOT
    if trigger_count >= HOT_TRIGGER_COUNT:
        return MemoryTier.HOT

    # Recency-based assignment
    if last_triggered_days <= HOT_THRESHOLD_DAYS:
        return MemoryTier.HOT
    elif last_triggered_days <= WARM_THRESHOLD_DAYS:
        return MemoryTier.WARM
    else:
        return MemoryTier.COLD
