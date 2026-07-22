# Review Queue — Priority Ordering

## Sort Order

Items are presented in this priority (highest first):

1. **Iteration follow-ups** — backlogs that are follow-ups from a previous iterate action (have `parent_backlog` field). These are re-reviews of previously flagged work.
2. **Recent completions** — backlogs completed in the last 7 days, newest first.
3. **High-priority backlogs** — backlogs with `Priority: High` or `Priority: Critical` in their content.
4. **Older completions** — everything else, newest first.

## Detection

- **Follow-up detection:** Check if backlog content contains `parent_backlog` or `Parent:` field.
- **Completion date:** Use file modification time of the file in `docs/backlog/done/`.
- **Priority detection:** Parse `## Priority` section from backlog content.

## Tie-breaking

Within the same priority tier, sort by backlog number descending (newest first).
