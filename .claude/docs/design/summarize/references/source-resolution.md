# Source Resolution — /summarize

## How to Find Input Files for a Target

### Backlog Number Input (e.g., `188`)

| Source | Primary Path | Fallback Path |
|--------|-------------|---------------|
| Backlog file | `docs/backlog/done/NNN-*.md` | `docs/backlog/NNN-*.md` |
| Task folder | `tasks/completed/[slug]/` | `tasks/[slug]/` |
| Deliverable | `projects/[slug]/` | Path from backlog Location field |
| Agent state | `.claude/state/agent-[slug]-*.json` | Glob for agent ID match |

**Slug derivation:** Extract from backlog filename. `188-kernel-research-llm-market-shift-analysis.md` → slug is `llm-market-shift-research` (strip prefix type words like `kernel-research-`, `domain-build-`, `qa-fix-`).

### Project Path Input (e.g., `projects/ssh-*`)

| Source | Resolution |
|--------|-----------|
| Deliverable | Glob-expand the input path |
| Backlog file | Search `docs/backlog/done/` for backlogs referencing the project folder |
| Task folder | Search `tasks/completed/` for matching slug |
| Agent state | Search `.claude/state/` for matching agent ID |

### Empty Input (summarize unreviewed)

1. Read `review-status.json`
2. Scan `docs/backlog/done/` for all completed backlogs
3. Find backlogs NOT in `review-status.json.reviewed` or with `status: "unreviewed"`
4. Pick the highest-priority unreviewed item (same priority as review-queue)
5. Resolve sources using the backlog number path

### Build Deliverables (`.claude/skills/`, `.claude/commands/`)

For BUILD scope backlogs, deliverables are typically in:
- `.claude/skills/[name]/` — skill package
- `.claude/commands/kernel/[name].md` — command entry point
- `.claude/docs/design/[name]/` — design doc

Check the backlog's Location field for the exact paths.

### Research Deliverables (`projects/`)

For RESEARCH scope backlogs, deliverables are typically in:
- `projects/[name]/` — research report and supporting files
- Sometimes `projects/[name]-research/` with `-research` suffix
