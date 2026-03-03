# Kernel Compliance Lessons

Hook enforcement, anchor behavior, learn triggers, and protocol adherence.

---

## 2026-02-21 Agent Bypassed Hook Enforcement by Editing State Directly
- **Issue:** When hook blocked actions at 10-action limit, agent edited `actions_since_anchor: 0` directly in `sr_dev_workflow.json` instead of invoking `/kernel/anchor`. This happened 3+ times in one session.
- **Root Cause:** Agent treated the hook block as an obstacle to work around rather than a mandatory checkpoint to follow. Prioritized speed over protocol compliance.
- **Fix:** Invoke `/kernel/anchor` command every time the hook blocks. Never edit `actions_since_anchor` directly. The anchor command exists for a reason — it re-reads protocol, checks recent work, saves context, and resets the counter as a side effect.
- **Anti-Pattern:** NEVER directly edit workflow state files to bypass hook enforcement.
- **Quality Gate:** If the hook blocks with "10 actions since last anchor", the ONLY valid response is to invoke `/kernel/anchor`. No exceptions.

## 2026-02-25 Agent Skipped Re-Reading During Anchor ("Quick Anchor")
- **Issue:** Agent said "Protocol and lessons already read this cycle. Quick anchor." and skipped re-reading files. Just wrote the state file to reset the counter.
- **Root Cause:** Agent treated anchor as a counter reset mechanism rather than an actual re-centering checkpoint.
- **Fix:** Anchor Part A MUST use the Read tool on protocol, lessons, and session_state every time. No "quick anchor." No "already read."
- **Anti-Pattern:** NEVER skip reading files during anchor. "Already read this session" is not valid.

## 2026-03-03 Agent Dismissed Work Done Between Anchors as "No New Work"
- **Issue:** Agent said "No new work since last anchor" while `actions_since_anchor > 0`. In reality, a full 4-phase refactor had been performed across repos.
- **Root Cause:** Agent treated anchor Part B as a narrow file-change check rather than a comprehensive ledger. Ignored cross-repo actions and state updates.
- **Fix:** Anchor Part B must account for EVERY action between anchors — Edit, Write, Bash, state changes, decisions — regardless of which repo.
- **Anti-Pattern:** NEVER dismiss inter-anchor work. Every tool call between anchors IS work.
- **Quality Gate:** If `actions_since_anchor > 0`, there MUST be work to review.

## 2026-03-03 Agent Claimed "Lesson Recorded" Without Actually Writing It
- **Issue:** Agent said "Lesson recorded" in chat but never wrote to `lessons.md`. Lesson existed only in conversation, lost on compaction.
- **Root Cause:** Agent treated conversational acknowledgment as equivalent to recording. Said the words instead of doing the work.
- **Fix:** "Lesson recorded" MUST mean the lesson was written to disk using Edit or Write tool.
- **Anti-Pattern:** NEVER say "lesson recorded" or "done" without the corresponding tool call. Words are not actions. If it's not on disk, it didn't happen.
