# Review Board Template

Parent: [[../../SKILL.md]]. Spec sheet for review-board page generation.

## Data Source

Unreviewed backlog items, discovered by diffing completed backlogs against review state:

1. Glob `docs/backlog/done/*.md` → extract NNN from filenames
2. Read `.claude/state/review-status.json` → extract `reviewed` keys
3. Diff: completed numbers minus reviewed numbers = unreviewed set

→ [[../../../review-queue/steps/step-01-discover.md]]

### Per-Item Fields

For each unreviewed backlog file, extract:

| Field | Source |
|-------|--------|
| `number` | NNN prefix from filename |
| `title` | First `#` heading |
| `scope` | `## Summary` or `## Task Builder Input` section |
| `priority` | `## Priority` section (default: normal) |
| `summary` | First paragraph after title |

→ [[../../../review-queue/steps/step-02-present.md]]

## Action Map

Copied from the annotation contract — the canonical source of truth.

| action | destructive | type | routes to |
|--------|------------|------|-----------|
| accept | no | standard | review-queue accept transition |
| iterate | no | standard | `/kernel/backlog` (raw_words verbatim, parent-linked) |
| reject | yes | standard | review-queue reject with raw_words reason |
| skip | no | standard | no state change |
| defer | no | standard | review-queue defer marker |
| confirm | no | meta | commits the original held action from the matching confirms[] entry |
| cancel | no | meta | logs the action as declined; original held action discarded |

**Meta-actions** (`confirm` / `cancel`) are not routed directly to review-queue. They resolve a pending confirms[] entry for the given target: `confirm` commits the originally held action (e.g., the reject that triggered the confirmation), `cancel` discards it. Both carry the same annotation schema — `{ "target": "<N>", "action": "confirm|cancel" }`.

### Test Flag

Annotations carry an optional `test` field (boolean, default `false`). When `test: true`, the session acknowledges via the reply file's `dry_run_ack` array and **NEVER routes** the annotation — no state change, no kernel command, no side effect. Solves the test-noise-into-intent-chain problem.

**Schema change is ADDITIVE — v1 annotations (without `test` or meta-actions) remain valid and route identically to before.**

→ [[../../../docs/design/render/references/annotation-contract.md]] (law)

## Page Requirements

1. **Self-contained** — zero external hosts; all CSS/JS inline in the generated HTML
2. **Frozen schema POST** — each action button POSTs `{ "target": "<number>", "action": "<action>", "raw_words": <text-input-value|null>, "at": "<ISO timestamp>" }`
3. **Send-to-session affordance** — form submits to the render server's `/annotate` endpoint
4. **Session-dir banner** — page header displays the session directory path
5. **Per-card layout** — each unreviewed item rendered as a card with: number, title, scope, priority, summary, action buttons, and a text input for raw_words (used by iterate and reject)
6. **Destructive confirmation** — reject button visually distinct (red/warning) to signal destructive action

## Reply Channel (v2)

The page polls the session for status and renders feedback inline:

1. **Status polling** — `GET /status` every ~2s; response is `session-reply.json` or `{"status":"idle"}`
2. **Status strip** — displays current status (idle / processing / closed) with timestamp
3. **Confirm bars** — when `confirms[]` contains an entry for a card's target, render inline Confirm / Cancel buttons on that card; buttons POST ordinary annotations (`action: "confirm"` or `"cancel"`)
4. **Results rendering** — when `results[]` contains an outcome for a target, flip the card to show the outcome with status icons
5. **Dry-run toggle** — page-level switch; when ON, all queued annotations carry `"test": true`

→ [[../../../docs/design/render/references/annotation-contract.md#reply-channel-v2--the-full-circle]] (design payload)

## Annotation Schema

```json
{ "target": "231", "action": "iterate", "raw_words": "go deeper on kernel compat", "at": "2026-07-15T09:00:00Z" }
```
→ [[../../../docs/design/render/references/annotation-contract.md]] (full schema + laws)
