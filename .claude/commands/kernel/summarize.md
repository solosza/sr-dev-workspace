# /kernel/summarize

Summarize completed agent output with requirement diffing and decision flags.

## Usage

```
/kernel/summarize 188           — summarize backlog 188's output
/kernel/summarize projects/ssh-*  — summarize a project folder
/kernel/summarize               — summarize all unreviewed completions
```

## Skill Reference

→ `.claude/skills/summarize/SKILL.md`

## Instructions

1. Read the skill SKILL.md: `.claude/skills/summarize/SKILL.md`
2. Follow the workflow steps 1-6 sequentially:
   - Step 1: Resolve target (parse input, find source files)
   - Step 2: Gather sources (read backlog, tasks, deliverables, agent state)
   - Step 3: Diff requirements (check each requirement against deliverables)
   - Step 4: Classify findings (decisions vs informational vs problems)
   - Step 5: Format summary (assemble dynamic report)
   - Step 6: Write + report (persist to review-status.json and/or display)
3. Read each step file before executing that step
4. Dynamic sizing: show ALL findings and files. No artificial compression.
5. If called by `/kernel/complete`: write summary to review-status.json entry

## Integration

- **`/kernel/complete`** calls this after one-shot agent completion (integrated mode)
- **`/kernel/review-queue`** shows stored summaries when presenting review cards
- **Standalone** when user invokes directly
