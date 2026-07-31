"""Task 008 (L3) + 007 (L2) — end-to-end: adapter -> serve -> rows -> teardown.
Writes e2e-result.json, exits 0/1."""
import html as _html
import json
import os
import socket
import subprocess
import sys
import time
import urllib.request

ROOT = "D:/my_ai_projects/project_test_repos/sr_dev_workspace"
sys.path.insert(0, os.path.join(ROOT, ".claude/skills/render/adapters"))
sys.path.insert(0, os.path.join(ROOT, ".claude/skills/render/lib"))
from loop_to_leaderboard import to_items  # noqa: E402
from serve_and_watch import serve  # noqa: E402

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "e2e-result.json")
SESSION = os.path.join(HERE, "session")
os.makedirs(SESSION, exist_ok=True)

fails = []


def check(c, m):
    if not c:
        fails.append(m)


def port_open(port):
    s = socket.socket()
    s.settimeout(0.5)
    try:
        s.connect(("127.0.0.1", port))
        return True
    except OSError:
        return False
    finally:
        s.close()


sample = {"items": [
    {"name": "Deep workup", "description": "the real money", "rec": "Build", "fit": "high", "merit": 9},
    {"name": "Founder check", "description": "cheap hook", "rec": "Test first", "fit": "high", "merit": 5},
    {"name": "General tool", "description": "too broad", "rec": "Don't build", "fit": "low", "merit": 1},
]}

data = to_items(sample, "E2E ways to do it", "ranked")
items_json = os.path.join(SESSION, "items.json")
with open(items_json, "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False)

res = serve(items_json, SESSION)
check(res.get("ok"), "serve failed: %s" % res)
port = res.get("port")
pid = res.get("pid")

html = ""
if port:
    time.sleep(0.3)
    try:
        html = urllib.request.urlopen("http://127.0.0.1:%d/" % port, timeout=3).read().decode("utf-8")
    except Exception as e:  # noqa: BLE001
        fails.append("GET / failed: %s" % e)
    # /status
    try:
        st = urllib.request.urlopen("http://127.0.0.1:%d/status" % port, timeout=3).read().decode("utf-8")
        check("status" in st, "/status missing status field")
    except Exception as e:  # noqa: BLE001
        fails.append("GET /status failed: %s" % e)

# rows + rec labels present (unescape first — generate.py html-escapes apostrophes)
text = _html.unescape(html)
for name in ("Deep workup", "Founder check", "General tool"):
    check(name in text, "row missing: %s" % name)
for lab in ("Build", "Test first", "Don't build"):
    check(lab in text, "rec label missing: %s" % lab)
check("—" not in text, "em dash in served html")

# teardown
if pid:
    if os.name == "nt":
        subprocess.run(["taskkill", "/F", "/PID", str(pid)], capture_output=True)
    else:
        try:
            os.kill(pid, 9)
        except OSError:
            pass
    time.sleep(0.5)
    check(not port_open(port), "port still listening after teardown")

result = {"ok": not fails, "fails": fails, "port": port, "rows_found": [n for n in ("Deep workup", "Founder check", "General tool") if n in html]}
with open(OUT, "w", encoding="utf-8") as f:
    json.dump(result, f, indent=2, ensure_ascii=False)
sys.exit(0 if not fails else 1)
