# 001 — Build the loop-to-leaderboard adapter module

Type: BUILD

## Deliverable
`.claude/skills/render/adapters/loop_to_leaderboard.py`

## What it does
A function that converts a venture loop's decide/output (a list of items/wedges, each with name, description, recommendation, fit level, and a merit/rank signal) into the leaderboard template's `items.json` data model. Plain-vocab translation and the ranking rules are baked in here so callers never hand-translate.

## Acceptance Criteria
- [ ] File exists at the deliverable path.
- [ ] Exposes `to_items(loop_output: dict, title: str, lead: str) -> dict` returning `{title, lead, recLegend, legend, items:[...]}` matching `templates/leaderboard/generate.py`.
- [ ] Each item has `id` (slug of name), `rank`, `name`, `desc`, `rec:{label,tone}`, `tag:{label,tone}`.
- [ ] Recommendation maps to tone: Build→c, Test first→b, Don't build→e.
- [ ] Fit maps to tag tone: New for you→a, Partly yours→b, Your strength→c. Fit NEVER changes item order (rank comes from the merit signal only).
- [ ] Contains a jargon ban-list (e.g. wedge, assay, GO-IF, fit, merit) and strips/translates those terms out of any produced string.
- [ ] Produces NO em dashes in any output string.
- [ ] No `print()` statements (sr_dev code-quality gate blocks debug statements in .py). Return values, do not print.

## Verify
`python -c "import ast; ast.parse(open('.claude/skills/render/adapters/loop_to_leaderboard.py').read())"` exits 0, and `grep -qE 'def to_items' .claude/skills/render/adapters/loop_to_leaderboard.py`.
