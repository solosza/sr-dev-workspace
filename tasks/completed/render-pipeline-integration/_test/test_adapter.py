"""Task 006 — adapter functional test. Writes result to adapter-result.json, exits 0/1."""
import json
import os
import sys

ROOT = "D:/my_ai_projects/project_test_repos/sr_dev_workspace"
sys.path.insert(0, os.path.join(ROOT, ".claude/skills/render/adapters"))
from loop_to_leaderboard import to_items  # noqa: E402

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "adapter-result.json")

# Sample loop output: merit orders, fit must NOT reorder. Includes jargon + an em dash.
sample = {"items": [
    {"name": "A high-merit low-fit", "description": "the assay wedge that wins", "rec": "Build", "fit": "low", "merit": 9},
    {"name": "B mid", "description": "cheap check then upsell", "rec": "Test first", "fit": "high", "merit": 5},
    {"name": "C high-fit low-merit", "description": "our pet wedge — feels close", "rec": "Build", "fit": "high", "merit": 2},
    {"name": "D bottom", "description": "kill it", "rec": "Don't build", "fit": "low", "merit": 1},
]}

fails = []


def check(cond, msg):
    if not cond:
        fails.append(msg)


out = to_items(sample, "Ways to do it, ranked", "how good each is")

# schema
check(set(out) >= {"title", "lead", "recLegend", "legend", "items"}, "missing top-level keys")
check(len(out["items"]) == 4, "wrong item count")
for it in out["items"]:
    check(set(it) >= {"id", "rank", "name", "desc", "rec", "tag"}, "item missing keys: %s" % it.get("name"))
    check(it["rec"]["tone"] in ("c", "b", "e"), "bad rec tone")
    check(it["tag"]["tone"] in ("a", "b", "c"), "bad tag tone")

# rank on MERIT only — order must be A, B, C, D regardless of fit
order = [it["name"][0] for it in out["items"]]
check(order == ["A", "B", "C", "D"], "merit ordering wrong (fit leaked into rank?): %s" % order)

# high-fit low-merit C must NOT outrank low-fit high-merit A
check(out["items"][0]["name"].startswith("A"), "high-fit item jumped the rank")

# plain vocabulary + no em dash across every shown string
blob = json.dumps(out, ensure_ascii=False).lower()
for jarg in ("wedge", "assay", "kill", "—"):
    check(jarg not in blob, "jargon/em-dash leaked: %r" % jarg)

result = {"ok": not fails, "fails": fails, "order": order}
with open(OUT, "w", encoding="utf-8") as f:
    json.dump(result, f, indent=2, ensure_ascii=False)
sys.exit(0 if not fails else 1)
