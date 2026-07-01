# Step 01 — Parse Input

## Purpose
Accept the target text for AI-tell detection. Supports file path or inline text.

## Input
One of:
- **File path** — absolute path to a `.md`, `.txt`, or any text file
- **Inline text** — raw text passed directly in the command invocation

## Output
- `target_text` — the full text content to scan
- `source` — either the file path or `"inline"`

## Procedure

1. Check if the argument is a valid file path (exists on disk).
2. If file: read the file contents into `target_text`, set `source` to the file path.
3. If not a file: treat the entire argument as inline text, set `source` to `"inline"`.
4. If no argument provided: error with usage message.
5. Pass `target_text` and `source` to Step 02.
