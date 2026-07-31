"""serve_and_watch.py — Launcher for the render step.

Wraps the mechanics proven by hand: given an items.json and a session dir, it
  1. runs templates/leaderboard/generate.py to write <session_dir>/page.html,
  2. starts lib/render_server.py on 127.0.0.1 as a DETACHED background process
     (so it outlives this launcher), redirecting its stdout to <session_dir>/port.txt,
  3. reads the port back from port.txt,
  4. writes <session_dir>/serve-status.json with the port + pid.

The caller (the session) opens the browser and arms the annotations watcher.
Paths resolve from THIS file, never from cwd (a cwd-relative data path breaks under a
different working directory). No print() — status goes to serve-status.json.

Public: serve(items_json, session_dir) -> dict  (also runnable as a CLI for tests)
"""
import json
import os
import subprocess
import sys
import time

_RENDER_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
_GEN = os.path.join(_RENDER_ROOT, "templates", "leaderboard", "generate.py")
_SERVER = os.path.join(_RENDER_ROOT, "lib", "render_server.py")

# Windows flags: detach the server into its own process group so it survives launcher exit.
_DETACHED = 0
if os.name == "nt":
    _DETACHED = 0x00000008 | 0x00000200  # DETACHED_PROCESS | CREATE_NEW_PROCESS_GROUP


def _status(session_dir, obj):
    with open(os.path.join(session_dir, "serve-status.json"), "w", encoding="utf-8") as f:
        json.dump(obj, f)


def _read_port(port_file, timeout=10.0):
    deadline = time.time() + timeout
    while time.time() < deadline:
        if os.path.isfile(port_file):
            text = open(port_file, encoding="utf-8").read()
            for line in text.splitlines():
                line = line.strip()
                if line.startswith("PORT="):
                    return int(line.split("=", 1)[1])
        time.sleep(0.2)
    return None


def serve(items_json, session_dir):
    """Generate page.html, start the server detached, return {port, pid, url, session_dir}."""
    session_dir = os.path.abspath(session_dir)
    os.makedirs(session_dir, exist_ok=True)
    items_json = os.path.abspath(items_json)

    gen = subprocess.run(
        [sys.executable, _GEN, items_json, session_dir],
        capture_output=True, text=True,
    )
    if gen.returncode != 0 or not os.path.isfile(os.path.join(session_dir, "page.html")):
        result = {"ok": False, "stage": "generate", "error": gen.stderr.strip()}
        _status(session_dir, result)
        return result

    port_file = os.path.join(session_dir, "port.txt")
    if os.path.isfile(port_file):
        os.remove(port_file)
    port_handle = open(port_file, "w", encoding="utf-8")
    proc = subprocess.Popen(
        [sys.executable, _SERVER, session_dir],
        stdout=port_handle, stderr=subprocess.DEVNULL,
        creationflags=_DETACHED, close_fds=True,
    )
    port = _read_port(port_file)
    result = {
        "ok": port is not None,
        "port": port,
        "pid": proc.pid,
        "url": ("http://127.0.0.1:%d/" % port) if port else None,
        "session_dir": session_dir,
    }
    _status(session_dir, result)
    return result


def _main():
    if len(sys.argv) != 3:
        return 2
    result = serve(sys.argv[1], sys.argv[2])
    return 0 if result.get("ok") else 1


if __name__ == "__main__":
    sys.exit(_main())
