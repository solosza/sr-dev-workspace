# Step 5: Route

## Purpose
Convert annotations into real state changes — through kernel commands only.
Reply-channel schema: → [[../../docs/design/render/references/annotation-contract.md]] § Reply Channel.

## Pre-generation Checkpoint
- Read: `annotations.json` (the wake payload)
- Read: the template's `template.md` action map BEFORE any routing

## Procedure

### 1. Validate
Validate every entry against the annotation schema `{target, action, raw_words, at}`. Unknown action for this template → report + skip that entry. Never guess.

### 2. Dry-run filter
Entries with `test: true` → append target to `dry_run_ack` in `<session_dir>/session-reply.json`, never route. Continue to next entry.

### 3. Destructive confirm (via reply channel)
Collect template-flagged destructive actions. For each:
1. Write a `confirms[]` entry to `<session_dir>/session-reply.json` with `status: "processing"`.
2. Re-arm the watcher (Step 4 re-entry) — session returns control and waits for the confirm/cancel annotation.
3. On `action: "confirm"` arriving for the target → route the ORIGINAL action (proceed to step 4).
4. On `action: "cancel"` arriving for the target → log declined, do NOT route.

### 4. Route
Route each non-dry-run, confirmed entry per the action map. review-board v1: accept → review-queue accept transition · iterate → `/kernel/backlog` with raw_words VERBATIM, parent-linked · reject → review-queue reject with raw_words reason · skip → nothing · defer → review-queue defer.

### 5. Record results
After each entry routes (or declines), append to `results[]` in `<session_dir>/session-reply.json`:
```json
{ "target": "197", "outcome": "accepted" }
```
The page polls this file — results appear as cards update.

### 6. Failure handling
On a routing failure: STOP, report routed vs pending — annotations.json is the recovery source.

### 7. Log
Write the routing log (`target → command → result`) to the session dir; bump `routed_count`.

## Acceptance Criteria
- [ ] RND-05 satisfied (contracts/step-05-contract.json): all entries validated, raw_words untouched, destructive confirmed via reply channel, dry-run entries never routed, results written, log written
