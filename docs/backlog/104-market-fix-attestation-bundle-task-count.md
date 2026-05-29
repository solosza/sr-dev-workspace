# Fix Attestation Bundle Task Count Accuracy

## Status
Open

## Priority
Medium — correctness issue; "0 tasks" in old bundles may be cosmetic (null→0 fallback) rather than genuine data, which means the portfolio feed is showing wrong numbers and the attestation record is not trustworthy for those entries

## Summary
Old May 27 attestation bundles displayed `null` for task count in the portfolio feed. Pipeline 099 fixed the renderer to show "0 tasks" instead of null. But "0" may be a cosmetic fallback — if `task_count` was never written into the bundle at attestation time and the renderer is just defaulting `null → 0`, the data bug is still present under a nicer label. This backlog item confirms the root cause and fixes it at the source (the bundle writer), not the renderer.

## The Specific Concern
From conversation context:
> "If those May 27 runs genuinely had zero tasks, '0' is correct and the fix was a proper null-to-integer handling. But if they actually did work and the count just never got written to the bundle, then '0' is the same data bug wearing a nicer label."

The tell: inspect one May 27 attestation bundle JSON. If `task_count` is missing or null in the bundle itself (not just in the renderer's interpretation), the writer never emitted it. That means any run attested before the fix has an unverifiable task count — and retroactive "0" display is misleading.

## Requirements
- Read one May 27 attestation bundle from `.claude/state/attestations/` — confirm whether `task_count` field exists and what its value is
- If `task_count` is missing/null in the bundle: trace the write path in `lib/attestation/attest.py` to find where it should be written
- Fix the bundle writer to emit the real task count at attestation time (not derived later)
- Determine if backfilling old bundles is feasible (may require re-attestation or a migration script)
- Verify that new bundles (May 29+) have correct `task_count` written

## References
- Attestation bundles: `.claude/state/attestations/`
- Bundle writer: `lib/attestation/attest.py`
- Feed renderer: `isagawa-co.github.io/generate-feed.py`
- Related pipeline: backlog 099 (fix portfolio feed null tasks) — `docs/backlog/done/099-market-fix-portfolio-feed-null-tasks.md`

## Task Builder Input
- **Deliverable:** `lib/attestation/attest.py` emits correct `task_count` at write time; old bundles diagnosed and either backfilled or flagged in feed
- **Location:** `workspace`
- **Scope:** BUILD
- **Constraints:** Must not retroactively alter signed Rekor entries; backfill is local bundle only (re-sign if needed); May 27 bundles are the specific test cases
