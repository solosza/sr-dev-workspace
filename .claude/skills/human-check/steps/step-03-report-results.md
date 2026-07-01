# Step 03 — Report Results

## Purpose
Format detection findings into a readable report and set the exit status.

## Input
- `findings` — list of AI tell findings from Step 02
- `source` — file path or `"inline"`
- `total_findings` — count

## Output
- Formatted report to stdout
- Exit code: 0 if clean, 1 if findings exist

## Procedure

1. If `total_findings == 0`:
   - Output: `CLEAN: No AI tells detected in <source>`
   - Exit 0.

2. If findings exist, format report:
   ```
   FINDINGS: <total_findings> AI tells detected in <source>

   | Line | Category | Text | Suggestion |
   |------|----------|------|------------|
   | N    | category | text | suggestion |
   ...

   Summary by category:
   - em_dash: N
   - hedge_word: N
   ...
   ```

3. Group findings by category for the summary section.

4. Exit 1 (findings present = gate failure).
