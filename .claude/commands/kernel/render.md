# /kernel/render

Render any agent artifact as an interactive local page with a closed annotation return path — your clicks and words come back and get routed through kernel commands.

## Usage

```
/kernel/render [template] [artifact]
/kernel/render review-board
/kernel/render --close
```

| Argument | Purpose | Example |
|----------|---------|---------|
| `template` | Registered template name | `review-board` |
| `artifact` | Optional artifact ref (defaults per template) | a report path |
| `--close` | Tear down the active render session | |

## What It Does

Generates a self-contained HTML page from a registered template, serves it on localhost with a POST endpoint, opens your browser, and arms a background watcher. You annotate in the page at your own pace (click actions, type notes); on submit, the session wakes and routes every annotation through the proper kernel command — accept → review transition, iterate notes → `/kernel/backlog` with your words verbatim. The UI never touches state; the intent chain stays intact.

## Examples

```
# Visual review of the unreviewed backlog queue
/kernel/render review-board

# End the session (keeps annotations + routing log as audit trail)
/kernel/render --close
```

## Critical Behavior

- Localhost only; one active session at a time; server + watcher torn down by recorded PID.
- Destructive actions (e.g., reject) queue in the page and re-confirm in chat before routing.
- Runtime status: `lib/render_server.py` + `templates/review-board/` are PENDING BUILD via the loop — the command is not operational until that pipeline merges.

## Design Reference

> `.claude/docs/design/render/index.md`

## Skill Reference

> `.claude/skills/render/`
