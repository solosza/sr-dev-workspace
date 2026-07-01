# Step 02 — Run Detection

## Purpose
Invoke the detection engine against the parsed text and collect all findings.

## Input
- `target_text` — text content from Step 01
- `source` — file path or `"inline"`

## Output
- `findings` — list of detected AI tells with line numbers, categories, and suggestions
- `total_findings` — count of all findings

## Procedure

1. If `source` is a file path, invoke detect.py via Bash:
   ```
   python .claude/skills/human-check/detect.py <file-path>
   ```
   Parse the JSON output.

2. If `source` is `"inline"`, write the text to a temporary file, invoke detect.py against it, then delete the temp file.

3. Collect the JSON report: `file`, `total_findings`, `findings[]`.

4. Each finding contains:
   - `line_number` — where the tell appears
   - `text` — the matched text or context
   - `category` — detection category (em_dash, hedge_word, etc.)
   - `suggestion` — how to fix it

5. Pass findings to Step 03.
