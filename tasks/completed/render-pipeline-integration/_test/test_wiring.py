"""Task 017 — every ranked-output loop references the render step. Writes wiring-result.json."""
import json
import os
import sys

ROOT = "D:/my_ai_projects/project_test_repos/sr_dev_workspace"
LOOPS = ["assay", "competition", "deep-dive", "expand", "small", "lateral", "source"]
NEEDLE = "step-serve-and-watch"
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "wiring-result.json")

results = {}
for loop in LOOPS:
    skill_dir = os.path.join(ROOT, ".claude/skills", loop)
    found = False
    for base, _dirs, files in os.walk(skill_dir):
        for fn in files:
            if fn.endswith(".md"):
                try:
                    if NEEDLE in open(os.path.join(base, fn), encoding="utf-8").read():
                        found = True
                except OSError:
                    pass
    results[loop] = found

ok = all(results.values())
with open(OUT, "w", encoding="utf-8") as f:
    json.dump({"ok": ok, "loops": results}, f, indent=2)
sys.exit(0 if ok else 1)
