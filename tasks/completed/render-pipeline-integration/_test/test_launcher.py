"""Task 007 (L2) — launcher serves page.html live, teardown leaves no listener.
Writes launcher-result.json, exits 0/1."""
import json
import os
import socket
import subprocess
import sys
import time
import urllib.request

ROOT = "D:/my_ai_projects/project_test_repos/sr_dev_workspace"
sys.path.insert(0, os.path.join(ROOT, ".claude/skills/render/lib"))
from serve_and_watch import serve  # noqa: E402

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "launcher-result.json")
SESSION = os.path.join(HERE, "session-l2")
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


items = {"title": "Launcher L2", "lead": "x", "items": [
    {"id": "a", "rank": "1", "name": "Row A", "desc": "d", "rec": {"label": "Build", "tone": "c"}, "tag": {"label": "New for you", "tone": "a"}}]}
items_json = os.path.join(SESSION, "items.json")
with open(items_json, "w", encoding="utf-8") as f:
    json.dump(items, f)

res = serve(items_json, SESSION)
check(res.get("ok"), "serve failed: %s" % res)
check(os.path.isfile(os.path.join(SESSION, "page.html")), "page.html not generated")
port, pid = res.get("port"), res.get("pid")

if port:
    try:
        body = urllib.request.urlopen("http://127.0.0.1:%d/" % port, timeout=3).read().decode("utf-8")
        check("Launcher L2" in body, "title not served")
    except Exception as e:  # noqa: BLE001
        fails.append("GET / failed: %s" % e)

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

with open(OUT, "w", encoding="utf-8") as f:
    json.dump({"ok": not fails, "fails": fails, "port": port}, f, indent=2)
sys.exit(0 if not fails else 1)
