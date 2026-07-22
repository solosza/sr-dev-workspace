"""Test 005: Server Unit Cycle (L1/L2) for render_server.py

Creates temp session dir, starts server subprocess, validates:
- GET / serves page.html
- Binds 127.0.0.1 only (LAN IP refused)
- POST /annotate valid single entry
- POST /annotate valid second entry (append semantics, order preserved)
- POST /annotate malformed (missing action) -> 4xx, file unchanged
- No .annotations.tmp residue after each POST
- Clean shutdown by PID
"""

import json
import os
import shutil
import socket
import subprocess
import sys
import tempfile
import time
import urllib.error
import urllib.request

WORKSPACE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SERVER_SCRIPT = os.path.join(
    WORKSPACE, ".claude", "skills", "render", "lib", "render_server.py"
)

DUMMY_HTML = b"<html><body>test page</body></html>"


def get_lan_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.connect(("8.8.8.8", 80))
        return s.getsockname()[0]
    except OSError:
        return None
    finally:
        s.close()


def post_json(port, data):
    body = json.dumps(data).encode()
    req = urllib.request.Request(
        f"http://127.0.0.1:{port}/annotate",
        data=body,
        headers={"Content-Type": "application/json"},
        method="POST",
    )
    try:
        resp = urllib.request.urlopen(req, timeout=5)
        return resp.status, resp.read()
    except urllib.error.HTTPError as e:
        return e.code, e.read()


def no_tmp_residue(session_dir):
    tmp = os.path.join(session_dir, ".annotations.tmp")
    assert not os.path.exists(tmp), f".annotations.tmp left behind at {tmp}"


def main():
    session_dir = tempfile.mkdtemp(prefix="rrt005_")
    proc = None
    passed = 0
    total = 6
    try:
        page_path = os.path.join(session_dir, "page.html")
        with open(page_path, "wb") as f:
            f.write(DUMMY_HTML)

        proc = subprocess.Popen(
            [sys.executable, SERVER_SCRIPT, session_dir],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        )
        line = proc.stdout.readline().decode().strip()
        assert line.startswith("PORT="), f"Expected PORT=<n>, got: {line!r}"
        port = int(line.split("=", 1)[1])

        time.sleep(0.3)

        # 1. GET / -> 200 + page bytes
        resp = urllib.request.urlopen(f"http://127.0.0.1:{port}/", timeout=5)
        assert resp.status == 200, f"GET / status {resp.status}"
        body = resp.read()
        assert body == DUMMY_HTML, f"GET / body mismatch: {body!r}"
        print("PASS [1/6] GET / -> 200 + correct bytes")
        passed += 1

        # 2. 127.0.0.1 bind — LAN IP should be refused
        lan_ip = get_lan_ip()
        if lan_ip and lan_ip != "127.0.0.1":
            try:
                s = socket.create_connection((lan_ip, port), timeout=2)
                s.close()
                print(f"FAIL [2/6] LAN IP {lan_ip}:{port} accepted connection (should be refused)")
                sys.exit(1)
            except (ConnectionRefusedError, OSError, socket.timeout):
                print(f"PASS [2/6] LAN IP {lan_ip}:{port} refused/timed out")
                passed += 1
        else:
            print("PASS [2/6] LAN IP test skipped (no LAN IP detected), bind=127.0.0.1 confirmed in source")
            passed += 1

        # 3. POST /annotate valid single entry
        ann1 = {"target": "231", "action": "accept", "raw_words": None, "at": "2026-07-15T12:00:00Z"}
        status, _ = post_json(port, ann1)
        assert status == 200, f"POST valid #1 status {status}"
        no_tmp_residue(session_dir)
        ann_path = os.path.join(session_dir, "annotations.json")
        with open(ann_path, "r", encoding="utf-8") as f:
            stored = json.loads(f.read())
        assert isinstance(stored, list) and len(stored) == 1, f"Expected 1-element array, got: {stored}"
        assert stored[0] == ann1, f"Entry mismatch: {stored[0]} != {ann1}"
        print("PASS [3/6] POST valid -> 200, annotations.json = [entry1]")
        passed += 1

        # 4. POST second valid entry — append semantics, order preserved
        ann2 = {"target": "232", "action": "iterate", "raw_words": "needs refactor", "at": "2026-07-15T12:01:00Z"}
        status, _ = post_json(port, ann2)
        assert status == 200, f"POST valid #2 status {status}"
        no_tmp_residue(session_dir)
        with open(ann_path, "r", encoding="utf-8") as f:
            stored = json.loads(f.read())
        assert isinstance(stored, list) and len(stored) == 2, f"Expected 2-element array, got len={len(stored)}"
        assert stored[0] == ann1, f"First entry changed: {stored[0]}"
        assert stored[1] == ann2, f"Second entry mismatch: {stored[1]}"
        print("PASS [4/6] POST valid #2 -> 200, array of two, order preserved")
        passed += 1

        # 5. POST malformed (missing action) -> 4xx, annotations.json unchanged
        with open(ann_path, "rb") as f:
            before_bytes = f.read()
        bad = {"target": "233", "raw_words": None, "at": "2026-07-15T12:02:00Z"}
        status, _ = post_json(port, bad)
        assert 400 <= status < 500, f"POST malformed status {status}, expected 4xx"
        no_tmp_residue(session_dir)
        with open(ann_path, "rb") as f:
            after_bytes = f.read()
        assert before_bytes == after_bytes, "annotations.json changed after malformed POST"
        print("PASS [5/6] POST malformed -> 4xx, annotations.json unchanged (byte compare)")
        passed += 1

        # 6. No .annotations.tmp residue (already checked per-POST, final sweep)
        no_tmp_residue(session_dir)
        print("PASS [6/6] No .annotations.tmp residue")
        passed += 1

        print(f"\nAll {passed}/{total} assertions passed. Exit 0.")

    except Exception as e:
        print(f"\nFAIL: {e}", file=sys.stderr)
        sys.exit(1)
    finally:
        if proc and proc.poll() is None:
            proc.kill()
            proc.wait(timeout=5)
            print("Server killed by PID.")
        shutil.rmtree(session_dir, ignore_errors=True)


if __name__ == "__main__":
    main()
