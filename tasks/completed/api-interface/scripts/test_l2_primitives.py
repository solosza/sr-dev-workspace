"""L2 Test: ApiInterface primitives against live Orderly API.

Gates: AIF-04 (negative path), AIF-05 (each verb, ApiResponse fields).
"""
import io
import logging
import os
import subprocess
import sys
import time

import requests

REPO = "D:/my_ai_projects/project_test_repos/hmsa-qa-platform"
PORT = 8018
BASE_URL = f"http://127.0.0.1:{PORT}"

sys.path.insert(0, REPO)
sys.path.insert(0, os.path.join(REPO, "framework"))

from interfaces.api_interface import ApiInterface, ApiResponse


def boot_orderly():
    env = os.environ.copy()
    env["DATABASE_URL"] = f"sqlite:///{REPO}/harness/orderly/orderly.db"
    subprocess.run(
        [sys.executable, "-m", "harness.orderly.seed"],
        cwd=REPO, env=env, check=True, capture_output=True,
    )
    proc = subprocess.Popen(
        [sys.executable, "-m", "uvicorn", "harness.orderly.main:app",
         "--port", str(PORT), "--host", "127.0.0.1"],
        cwd=REPO, env=env, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
    )
    deadline = time.monotonic() + 15
    while time.monotonic() < deadline:
        try:
            requests.get(f"{BASE_URL}/login", timeout=1)
            return proc
        except requests.ConnectionError:
            time.sleep(0.3)
    proc.kill()
    raise RuntimeError("Orderly failed to start on port %d" % PORT)


def make_api():
    session = requests.Session()
    config = {"base_url": BASE_URL, "default_timeout": 10}
    logger = logging.getLogger("l2_api")
    logger.setLevel(logging.DEBUG)
    logger.propagate = False
    if not logger.handlers:
        handler = logging.StreamHandler(io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8"))
        logger.addHandler(handler)
    return ApiInterface(session, config, logger)


def test_get_list(api):
    resp = api.get("/api/customers/")
    assert resp.status == 200, f"Expected 200, got {resp.status}"
    assert isinstance(resp.body, list), f"Body should be list, got {type(resp.body)}"
    assert len(resp.body) >= 4, f"Seed has 4 customers, got {len(resp.body)}"
    assert resp.response_time > 0, "response_time must be > 0"


def test_post_create(api):
    resp = api.post("/api/customers/", json={"name": "Test User", "email": "test@l2.com"})
    assert resp.status == 201, f"Expected 201, got {resp.status}"
    assert isinstance(resp.body, dict), f"Body should be dict, got {type(resp.body)}"
    assert "id" in resp.body, "Body missing 'id'"
    assert resp.body["name"] == "Test User"
    assert resp.body["email"] == "test@l2.com"
    assert resp.response_time > 0
    return resp.body["id"]


def test_get_single(api, customer_id):
    resp = api.get(f"/api/customers/{customer_id}")
    assert resp.status == 200, f"Expected 200, got {resp.status}"
    assert isinstance(resp.body, dict), f"Body should be dict, got {type(resp.body)}: {resp.body!r}"
    assert resp.body["id"] == customer_id, f"Expected id={customer_id}, got {resp.body['id']}"
    assert resp.response_time >= 0, f"response_time must be >= 0, got {resp.response_time}"


def test_post_create_order(api, customer_id):
    resp = api.post("/api/orders/", json={"customer_id": customer_id, "total": 42.50})
    assert resp.status == 201, f"Expected 201, got {resp.status}"
    assert resp.body["status"] == "PENDING"
    assert resp.response_time > 0
    return resp.body["id"]


def test_post_process(api, order_id):
    resp = api.post(f"/api/orders/{order_id}/process")
    assert resp.status == 200, f"Expected 200, got {resp.status}"
    assert resp.body["status"] == "PROCESSING"
    assert resp.response_time > 0


def test_delete(api, order_id):
    resp = api.delete(f"/api/orders/{order_id}")
    assert resp.status == 204, f"Expected 204, got {resp.status}"
    assert resp.response_time > 0


class CaptureHandler(logging.Handler):
    def __init__(self):
        super().__init__()
        self.records = []

    def emit(self, record):
        self.records.append(record)


def test_negative_path():
    session = requests.Session()
    config = {"base_url": "http://127.0.0.1:1", "default_timeout": 2}

    logger = logging.getLogger("l2_negative")
    logger.setLevel(logging.DEBUG)
    logger.propagate = False
    for h in logger.handlers[:]:
        logger.removeHandler(h)
    capture = CaptureHandler()
    logger.addHandler(capture)

    api = ApiInterface(session, config, logger)

    propagated = False
    exc_type = None
    try:
        api.get("/should-fail")
    except Exception as e:
        propagated = True
        exc_type = type(e).__name__

    assert propagated, "Exception must propagate from ApiInterface on unreachable host"

    error_logs = [r for r in capture.records if r.levelno >= logging.ERROR]
    assert len(error_logs) >= 1, \
        f"ApiInterface must log error before re-raising (got {len(error_logs)} error logs, exc={exc_type})"
    assert "failed" in error_logs[0].getMessage().lower(), \
        f"Error log should mention 'failed', got: {error_logs[0].getMessage()}"

    logger.removeHandler(capture)


def main():
    proc = None
    try:
        proc = boot_orderly()
        api = make_api()

        passed = 0
        total = 0

        total += 1
        try:
            test_get_list(api)
            print("OK: GET /api/customers/ (list)")
            passed += 1
        except Exception as e:
            print(f"FAIL: GET /api/customers/ (list): {e}")

        total += 1
        new_customer_id = None
        try:
            new_customer_id = test_post_create(api)
            print("OK: POST /api/customers/ (create)")
            passed += 1
        except Exception as e:
            print(f"FAIL: POST /api/customers/ (create): {e}")

        total += 1
        try:
            cid = new_customer_id or 1
            test_get_single(api, cid)
            print("OK: GET /api/customers/{id} (single)")
            passed += 1
        except Exception as e:
            print(f"FAIL: GET /api/customers/{{id}} (single): {e}")

        total += 1
        order_id = None
        try:
            order_id = test_post_create_order(api, new_customer_id or 1)
            print("OK: POST /api/orders/ (create)")
            passed += 1
        except Exception as e:
            print(f"FAIL: POST /api/orders/ (create): {e}")

        total += 1
        try:
            test_post_process(api, order_id or 1)
            print("OK: POST /api/orders/{id}/process")
            passed += 1
        except Exception as e:
            print(f"FAIL: POST /api/orders/{{id}}/process: {e}")

        total += 1
        try:
            test_delete(api, order_id or 1)
            print("OK: DELETE /api/orders/{id}")
            passed += 1
        except Exception as e:
            print(f"FAIL: DELETE /api/orders/{{id}}: {e}")

        total += 1
        try:
            test_negative_path()
            print("OK: NEGATIVE PATH (unreachable host, exception propagates + log)")
            passed += 1
        except Exception as e:
            print(f"FAIL: NEGATIVE PATH: {e}")

        print(f"\n{'PASS' if passed == total else 'FAIL'}: {passed}/{total} L2 primitive tests")
        sys.exit(0 if passed == total else 1)

    finally:
        if proc:
            proc.kill()
            proc.wait()


if __name__ == "__main__":
    main()
