# HTML Em Dash Cleanup

## Type
BUILD

## Deliverable Root
D:\my_ai_projects\isagawa-portfolio-site

## File
index.html

## Acceptance Criteria
Replace all em dashes in copy with natural punctuation. Do NOT touch em dashes inside `<script>` tags (JS code).

| Location | Current | Replacement |
|----------|---------|-------------|
| title tag | `Isagawa — Conversational Agent Factory` | `Isagawa \| Conversational Agent Factory` |
| hero p | `artifacts — including new capabilities — under` | `artifacts (including new capabilities) under` |
| seed subtitle | `kernel — hooks, commands, and a protocol — that` | `kernel (hooks, commands, and a protocol) that` |
| seed narrative | `bypassed — not by the agent` | `bypassed. Not by the agent` |
| seed card (Anchor Token) | `re-centered — it cannot fake` | `re-centered. It cannot fake` |
| seed card (Learn Loop) | `impossible — not because the agent` | `impossible. Not because the agent` |
| growth subtitle | `operate — specs, a factory, workspaces` | `operate: specs, a factory, workspaces` |
| growth narrative | `Workspaces followed — complete development` | `Workspaces followed. Complete development` |
| growth card (Spec Factory) | `the kernel — the system built` | `the kernel. The system built` |
| self-ext subtitle | `conversation — capabilities that extend` | `conversation. Capabilities that extend` |
| self-ext narrative | `workflows — all produced by the system` | `workflows, all produced by the system` |
| self-ext card (Cloner) | `Playwright — colors, typography` | `Playwright: colors, typography` |
| this-page narrative | `conversational intent — including this one` | `conversational intent, including this one` |
| provenance subtitle | `attestation bundles — verify them yourself` | `attestation bundles. Verify them yourself` |
| JS fallback (line ~325) | `Verification unavailable — view on Rekor` | `Verification unavailable. View on Rekor` |

## Gates
HTML-01

## Reference
docs/backlog/053-market-refactor-portfolio-site-visual-layer/em-dash-cleanup.md
