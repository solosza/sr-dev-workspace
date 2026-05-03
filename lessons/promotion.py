"""Promotion rules for tiered memory system.

Lessons that recur frequently should be promoted to higher tiers.
Promotion is the opposite of decay — it rewards lessons that prove relevant.
"""

from typing import Dict, List, Optional

from lessons.tiers import MemoryTier, HOT_TRIGGER_COUNT
from lessons.decay import DecayEngine


# Minimum recurrence count to trigger promotion consideration
PROMOTION_THRESHOLD = 3


def evaluate_promotion(
    pattern_key: str,
    recurrence_count: int,
    current_tier: MemoryTier,
) -> MemoryTier:
    """Evaluate whether a lesson should be promoted based on recurrence.

    Rules:
    - 3+ recurrences promotes COLD -> WARM
    - 3+ recurrences promotes WARM -> HOT
    - Already HOT stays HOT
    - Below threshold: no change

    Args:
        pattern_key: The lesson fingerprint.
        recurrence_count: Total recurrence count.
        current_tier: Current tier assignment.

    Returns:
        The new tier (may be same if no promotion).
    """
    if recurrence_count < PROMOTION_THRESHOLD:
        return current_tier

    if current_tier == MemoryTier.COLD:
        return MemoryTier.WARM
    elif current_tier == MemoryTier.WARM:
        return MemoryTier.HOT
    else:
        return MemoryTier.HOT  # Already HOT


def run_promotion_check(
    engine: DecayEngine,
    recurrence_data: Dict[str, int],
) -> List[dict]:
    """Check all lessons for promotion eligibility.

    Args:
        engine: The DecayEngine instance.
        recurrence_data: Dict mapping pattern_key -> recurrence count.

    Returns:
        List of promotion records: { pattern_key, old_tier, new_tier, reason }.
    """
    promotions = []

    for pattern_key, count in recurrence_data.items():
        lesson = engine.get_lesson(pattern_key)
        if lesson is None:
            continue

        new_tier = evaluate_promotion(pattern_key, count, lesson.tier)
        if new_tier != lesson.tier:
            old_tier = lesson.tier
            lesson.tier = new_tier
            from datetime import datetime
            lesson.promoted_at = datetime.now().isoformat()
            promotions.append({
                "pattern_key": pattern_key,
                "old_tier": old_tier.value,
                "new_tier": new_tier.value,
                "reason": f"Recurrence count {count} >= threshold {PROMOTION_THRESHOLD}",
            })

    # Save changes
    if promotions:
        engine._save()

    return promotions
