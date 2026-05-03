# Gate Contract — Cloner Canvas/SVG Blind Spot Fix

## Gates

| ID | Check | Method | Pass Criteria | Fail Action |
|----|-------|--------|---------------|-------------|
| BUILD-01 | Sanity check section exists | grep | `grep -q "Sanity Check" .claude/skills/website-cloner/references/extraction.md` | Add section |
| BUILD-02 | Hydration wait section exists | grep | `grep -q "Hydration Wait" .claude/skills/website-cloner/references/extraction.md` | Add section |
| BUILD-03 | SVG text extraction section exists | grep | `grep -q "SVG Text" .claude/skills/website-cloner/references/extraction.md` | Add section |
| BUILD-04 | Canvas detection section exists | grep | `grep -q "Canvas Detection" .claude/skills/website-cloner/references/extraction.md` | Add section |
| BUILD-05 | CSS divergence section exists | grep | `grep -q "Custom Property" .claude/skills/website-cloner/references/extraction.md` | Add section |
| BUILD-06 | SKILL.md edge cases updated | grep | `grep -q "canvas" .claude/skills/website-cloner/SKILL.md` | Update table |
| FUNC-01 | Sanity check JS detects uniform defaults | run_code | `browser_evaluate` returns `flagged: true` for uniform 16px/24px/400 data | Fix logic |
| TEST-01 | Full extraction non-breaking | run_code | Extract example.com without errors, snapshot returned | Fix extraction |
