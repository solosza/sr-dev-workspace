"""Test 007: Full Circle E2E — Programmatic (L3)

Both directions in one run: page → server → annotate → session-reply → status → confirm.
Session side is SIMULATED by the test (writing session-reply.json).

Task 007 of backlog 233 (render-reply-channel).
Gates: RC-06, RC-07.
"""

import hashlib
import json
import os
import shutil
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
GENERATE_SCRIPT = os.path.join(
    WORKSPACE, ".claude", "skills", "render", "templates", "review-board", "generate.py"
)
REVIEW_STATUS_PATH = os.path.join(
    WORKSPACE, ".claude", "state", "review-status.json"
)

SAMPLE_ITEMS = [
    {"number": "145", "title": "Research kernel compat", "scope": "backlog",
     "priority": "high", "summary": "Check kernel compat with GNHF"},
    {"number": "188", "title": "Add dry-run mode", "scope": "backlog",
     "priority": "normal", "summary": "Wire test:true through the pipeline"},
    {"number": "201", "title": "Update docs", "scope": "backlog",
     "priority": "normal", "summary": "Refresh architecture docs"},
]

LIVE_SESSION_PORT = 52105


def hash_file(path):
    with open(path, "rb") as f:
        return hashlib.sha256(f.read()).hexdigest()


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


def get_status(port):
    req = urllib.request.Request(
        f"http://127.0.0.1:{port}/status", method="GET"
    )
    resp = urllib.request.urlopen(req, timeout=5)
    return resp.status, resp.read()


def port_is_free(port):
    import socket
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        s.connect(("127.0.0.1", port))
        s.close()
        return False
    except (ConnectionRefusedError, OSError):
        return True
    finally:
        try:
            s.close()
        except Exception:
            pass


def get_dir_listing(d):
    return sorted(os.listdir(d))


def main():
    session_dir = tempfile.mkdtemp(prefix="rrt007_")
    server_proc = None
    passed = 0
    total = 7
    port = None

    try:
        # --- Pre-test: hash live review-status.json ---
        review_hash_before = None
        if os.path.isfile(REVIEW_STATUS_PATH):
            review_hash_before = hash_file(REVIEW_STATUS_PATH)
            print(f"Pre-test: review-status.json hash = {review_hash_before[:16]}...")
        else:
            print("Pre-test: review-status.json not found (skip live-state check)")

        # --- Step 1: Create items.json (3 samples) + generate page ---
        items_path = os.path.join(session_dir, "items.json")
        with open(items_path, "w", encoding="utf-8") as f:
            json.dump(SAMPLE_ITEMS, f, indent=2, ensure_ascii=False)

        result = subprocess.run(
            [sys.executable, GENERATE_SCRIPT, items_path, session_dir],
            capture_output=True, text=True, timeout=30,
        )
        assert result.returncode == 0, f"generate.py failed: {result.stderr}"
        page_path = os.path.join(session_dir, "page.html")
        assert os.path.isfile(page_path), "page.html not created"
        with open(page_path, "r", encoding="utf-8") as f:
            page_content = f.read()
        assert 'id="card-145"' in page_content, "No card for item #145"
        assert 'id="card-188"' in page_content, "No card for item #188"
        print(f"PASS [1/{total}] Items.json (3 samples) + page generated with cards 145, 188")
        passed += 1

        # --- Step 2: Start server + capture port ---
        server_proc = subprocess.Popen(
            [sys.executable, SERVER_SCRIPT, session_dir],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        )
        line = server_proc.stdout.readline().decode().strip()
        assert line.startswith("PORT="), f"Expected PORT=<n>, got: {line!r}"
        port = int(line.split("=", 1)[1])
        time.sleep(0.2)

        resp = urllib.request.urlopen(f"http://127.0.0.1:{port}/", timeout=5)
        assert resp.status == 200, f"Server GET / returned {resp.status}"
        print(f"PASS [2/{total}] Server started on port {port}, GET / -> 200")
        passed += 1

        # --- Step 3: Circle 1 — reject → confirms → status byte-exact → confirm ---
        reject_annotation = {
            "target": "145",
            "action": "reject",
            "raw_words": "e2e reason",
            "at": "2026-07-15T22:00:00Z",
        }
        status_code, _ = post_json(port, reject_annotation)
        assert status_code == 200, f"POST reject returned {status_code}"

        session_reply = {
            "status": "processing",
            "at": "2026-07-15T22:00:01Z",
            "confirms": [
                {"target": "145", "question": "Are you sure you want to reject #145?"}
            ],
            "results": [],
        }
        reply_path = os.path.join(session_dir, "session-reply.json")
        reply_bytes = json.dumps(session_reply, indent=2, ensure_ascii=False).encode("utf-8")
        with open(reply_path, "wb") as f:
            f.write(reply_bytes)

        status_code, status_body = get_status(port)
        assert status_code == 200, f"GET /status returned {status_code}"
        assert status_body == reply_bytes, (
            f"GET /status not byte-exact.\n"
            f"Expected ({len(reply_bytes)} bytes): {reply_bytes[:100]!r}\n"
            f"Got      ({len(status_body)} bytes): {status_body[:100]!r}"
        )

        confirm_annotation = {
            "target": "145",
            "action": "confirm",
            "raw_words": None,
            "at": "2026-07-15T22:00:02Z",
        }
        status_code, _ = post_json(port, confirm_annotation)
        assert status_code == 200, f"POST confirm returned {status_code}"

        annotations_path = os.path.join(session_dir, "annotations.json")
        with open(annotations_path, "r", encoding="utf-8") as f:
            stored = json.load(f)
        assert isinstance(stored, list) and len(stored) == 2, (
            f"Expected 2-entry array, got {type(stored).__name__} len={len(stored) if isinstance(stored, list) else 'N/A'}"
        )
        assert stored[0] == reject_annotation, f"Entry 0 mismatch: {stored[0]}"
        assert stored[1] == confirm_annotation, f"Entry 1 mismatch: {stored[1]}"
        assert stored[0]["raw_words"] == "e2e reason", (
            f"raw_words not verbatim: {stored[0]['raw_words']!r}"
        )
        print(f"PASS [3/{total}] Circle 1: reject -> confirms in session-reply -> GET /status byte-exact -> confirm -> annotations.json 2-entry, order preserved, raw_words verbatim")
        passed += 1

        # --- Step 4: Circle 2 — dry run ---
        baseline_listing = get_dir_listing(session_dir)

        dry_run_annotation = {
            "target": "188",
            "action": "accept",
            "raw_words": None,
            "at": "2026-07-15T22:00:03Z",
            "test": True,
        }
        status_code, _ = post_json(port, dry_run_annotation)
        assert status_code == 200, f"POST dry-run returned {status_code}"

        dry_run_reply = {
            "status": "processing",
            "at": "2026-07-15T22:00:04Z",
            "confirms": [],
            "results": [],
            "dry_run_ack": ["188"],
        }
        dry_reply_bytes = json.dumps(dry_run_reply, indent=2, ensure_ascii=False).encode("utf-8")
        with open(reply_path, "wb") as f:
            f.write(dry_reply_bytes)

        status_code, status_body = get_status(port)
        assert status_code == 200, f"GET /status returned {status_code}"
        assert status_body == dry_reply_bytes, (
            f"GET /status dry-run not byte-exact.\n"
            f"Expected ({len(dry_reply_bytes)} bytes): {dry_reply_bytes[:100]!r}\n"
            f"Got      ({len(status_body)} bytes): {status_body[:100]!r}"
        )

        after_listing = get_dir_listing(session_dir)
        expected_listing = sorted(set(baseline_listing) | {"annotations.json"})
        assert after_listing == expected_listing, (
            f"Unexpected files after dry-run.\n"
            f"Baseline: {baseline_listing}\n"
            f"After:    {after_listing}\n"
            f"Expected: {expected_listing}"
        )
        print(f"PASS [4/{total}] Circle 2: dry-run POST (test:true) -> dry_run_ack in session-reply -> GET /status byte-exact -> no unexpected side effects")
        passed += 1

        # --- Step 5: Verify annotations.json has dry-run entry appended ---
        with open(annotations_path, "r", encoding="utf-8") as f:
            stored_final = json.load(f)
        assert len(stored_final) == 3, f"Expected 3 entries, got {len(stored_final)}"
        assert stored_final[2] == dry_run_annotation, f"Entry 2 (dry-run) mismatch: {stored_final[2]}"
        assert stored_final[2].get("test") is True, "Dry-run entry missing test:true"
        print(f"PASS [5/{total}] annotations.json: 3 entries total, dry-run entry has test:true, order preserved")
        passed += 1

        # --- Step 6: Live-state safety ---
        if review_hash_before is not None:
            review_hash_after = hash_file(REVIEW_STATUS_PATH)
            assert review_hash_before == review_hash_after, (
                f"review-status.json modified! before={review_hash_before[:16]} after={review_hash_after[:16]}"
            )
            print(f"PASS [6/{total}] Live-state safety: review-status.json hash unchanged")
        else:
            print(f"PASS [6/{total}] Live-state safety: review-status.json absent (no live state to protect)")
        passed += 1

        # --- Step 7: Teardown by PID ---
        pid = server_proc.pid
        server_proc.kill()
        server_proc.wait(timeout=5)
        server_proc = None

        for _ in range(20):
            if port_is_free(port):
                break
            time.sleep(0.2)
        assert port_is_free(port), f"Port {port} still bound after server kill (PID {pid})"
        print(f"PASS [7/{total}] Teardown: server PID {pid} killed, port {port} free, no stray listeners")
        passed += 1

        print(f"\nAll {passed}/{total} checks passed. Full Circle E2E green. Exit 0.")

    except Exception as e:
        print(f"\nFAIL: {e}", file=sys.stderr)
        import traceback
        traceback.print_exc(file=sys.stderr)
        sys.exit(1)
    finally:
        if server_proc and server_proc.poll() is None:
            server_proc.kill()
            try:
                server_proc.wait(timeout=5)
            except Exception:
                pass
        shutil.rmtree(session_dir, ignore_errors=True)


if __name__ == "__main__":
    main()
