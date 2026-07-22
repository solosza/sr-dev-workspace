"""L3 Test: Realistic flow through ApiInterface primitives against live Orderly.

Gate: AIF-06 — end-to-end flow using ONLY ApiInterface primitives (no api-objects).
Flow: POST customer → POST order (PENDING) → process (PROCESSING) → process (COMPLETE)
      → GET verify COMPLETE → invalid transition (400) → DELETE (204) → GET (404).
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
    logger = logging.getLogger("l3_api")
    logger.setLevel(logging.DEBUG)
    logger.propagate = False
    if not logger.handlers:
        handler = logging.StreamHandler(io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8"))
        logger.addHandler(handler)
    return ApiInterface(session, config, logger)


def run_flow(api):
    customer_id = None
    order_id = None

    # 1. POST customer
    resp = api.post("/api/customers/", json={"name": "L3 Flow User", "email": "l3@test.com"})
    assert isinstance(resp, ApiResponse), "Must return ApiResponse"
    assert resp.status == 201, f"POST customer: expected 201, got {resp.status}"
    assert resp.response_time >= 0, "response_time must be populated"
    customer_id = resp.body["id"]
    print(f"OK: POST customer → 201 (id={customer_id})")

    # 2. POST order (PENDING)
    resp = api.post("/api/orders/", json={"customer_id": customer_id, "total": 99.95})
    assert resp.status == 201, f"POST order: expected 201, got {resp.status}"
    assert resp.body["status"] == "PENDING", f"New order should be PENDING, got {resp.body['status']}"
    assert resp.response_time >= 0, "response_time must be populated"
    order_id = resp.body["id"]
    print(f"OK: POST order → 201 PENDING (id={order_id})")

    # 3. POST process → PROCESSING
    resp = api.post(f"/api/orders/{order_id}/process")
    assert resp.status == 200, f"Process PENDING→PROCESSING: expected 200, got {resp.status}"
    assert resp.body["status"] == "PROCESSING", f"Expected PROCESSING, got {resp.body['status']}"
    assert resp.response_time >= 0, "response_time must be populated"
    print("OK: POST process → 200 PROCESSING")

    # 4. POST process → COMPLETE
    resp = api.post(f"/api/orders/{order_id}/process")
    assert resp.status == 200, f"Process PROCESSING→COMPLETE: expected 200, got {resp.status}"
    assert resp.body["status"] == "COMPLETE", f"Expected COMPLETE, got {resp.body['status']}"
    assert resp.response_time >= 0, "response_time must be populated"
    print("OK: POST process → 200 COMPLETE")

    # 5. GET verify COMPLETE
    resp = api.get(f"/api/orders/{order_id}")
    assert resp.status == 200, f"GET order detail: expected 200, got {resp.status}"
    assert resp.body["status"] == "COMPLETE", f"Order should be COMPLETE, got {resp.body['status']}"
    assert resp.response_time >= 0, "response_time must be populated"
    print("OK: GET order → 200 COMPLETE verified")

    # 6. Invalid transition — COMPLETE is terminal, process returns 400
    resp = api.post(f"/api/orders/{order_id}/process")
    assert resp.status == 400, f"Invalid transition: expected 400, got {resp.status}"
    assert isinstance(resp, ApiResponse), "4xx must be returned as ApiResponse, not raised"
    assert "detail" in resp.body, f"400 body should have 'detail', got {resp.body}"
    assert resp.response_time >= 0, "response_time must be populated"
    print(f"OK: POST process on COMPLETE → 400 (detail: {resp.body['detail']!r})")

    # 7. DELETE order
    resp = api.delete(f"/api/orders/{order_id}")
    assert resp.status == 204, f"DELETE order: expected 204, got {resp.status}"
    assert resp.response_time >= 0, "response_time must be populated"
    print("OK: DELETE order → 204")

    # 8. GET deleted order → 404
    resp = api.get(f"/api/orders/{order_id}")
    assert resp.status == 404, f"GET deleted order: expected 404, got {resp.status}"
    assert isinstance(resp, ApiResponse), "404 must be returned as ApiResponse, not raised"
    assert resp.response_time >= 0, "response_time must be populated"
    print("OK: GET deleted order → 404")

    return customer_id, order_id


def main():
    proc = None
    try:
        proc = boot_orderly()
    except RuntimeError as e:
        print(f"L3-BLOCKED: {e}")
        sys.exit(2)

    try:
        api = make_api()
        customer_id, order_id = run_flow(api)
        print(f"\nPASS: L3 live flow complete (customer={customer_id}, order={order_id})")
        sys.exit(0)
    except Exception as e:
        print(f"\nFAIL: L3 live flow: {e}")
        sys.exit(1)
    finally:
        if proc:
            proc.kill()
            proc.wait()


if __name__ == "__main__":
    main()
