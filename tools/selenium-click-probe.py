#!/usr/bin/env python3
"""
Selenium click-fault probe — env-sanity preflight for post-navigation click delivery.
Standalone: stdlib + selenium only, no framework imports.
Serves its own pages, launches headless Chrome, tests click delivery after navigation.
Exit 0 = DELIVERED, exit 1 = DEAD.
"""
import argparse
import http.server
import json
import os
import signal
import socket
import sys
import threading
import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

PAGE1_HTML = """\
<!DOCTYPE html>
<html><head><title>Probe Page 1</title></head>
<body>
<h1>Probe Page 1</h1>
<a id="nav-link" href="/page2">Go to Page 2</a>
</body></html>
"""

PAGE2_HTML = """\
<!DOCTYPE html>
<html><head><title>Probe Page 2</title></head>
<body>
<h1>Probe Page 2</h1>
<button id="probe-btn" onclick="document.getElementById('flag').textContent='CLICKED'">Click Me</button>
<span id="flag">NOT_CLICKED</span>
</body></html>
"""


class ProbeHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/" or self.path == "/page1":
            body = PAGE1_HTML.encode()
        elif self.path == "/page2":
            body = PAGE2_HTML.encode()
        else:
            self.send_error(404)
            return
        self.send_response(200)
        self.send_header("Content-Type", "text/html")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def log_message(self, format, *args):
        pass


class QuietServer(http.server.HTTPServer):
    def handle_error(self, request, client_address):
        pass


def find_free_port():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind(("127.0.0.1", 0))
        return s.getsockname()[1]


def run_trial(port, trial_num, total):
    t0 = time.perf_counter()
    driver = None
    try:
        opts = Options()
        opts.add_argument("--headless=new")
        opts.add_argument("--disable-gpu")
        opts.add_argument("--no-sandbox")
        opts.add_argument("--disable-dev-shm-usage")
        svc = Service(log_output=os.devnull)
        driver = webdriver.Chrome(options=opts, service=svc)
        wait = WebDriverWait(driver, 10)

        t_start = time.perf_counter()
        driver.get(f"http://127.0.0.1:{port}/page1")
        wait.until(EC.presence_of_element_located((By.ID, "nav-link")))
        t_page1 = time.perf_counter()

        driver.find_element(By.ID, "nav-link").click()
        wait.until(EC.presence_of_element_located((By.ID, "probe-btn")))
        t_nav = time.perf_counter()

        driver.find_element(By.ID, "probe-btn").click()
        time.sleep(0.3)
        t_click = time.perf_counter()

        flag = driver.find_element(By.ID, "flag").text
        t_check = time.perf_counter()

        delivered = flag == "CLICKED"
        verdict = "DELIVERED" if delivered else "DEAD"

        print(
            f"  trial {trial_num}/{total}: {verdict}  "
            f"page1={t_page1 - t_start:.3f}s  "
            f"nav={t_nav - t_page1:.3f}s  "
            f"click={t_click - t_nav:.3f}s  "
            f"total={t_check - t0:.3f}s"
        )
        return delivered
    except Exception as e:
        t_err = time.perf_counter()
        print(f"  trial {trial_num}/{total}: ERROR  {e}  total={t_err - t0:.3f}s")
        return False
    finally:
        if driver:
            try:
                driver.quit()
            except Exception:
                pass


def main():
    parser = argparse.ArgumentParser(description="Selenium click-fault probe")
    parser.add_argument("--trials", type=int, default=3, help="Number of trials (default: 3)")
    args = parser.parse_args()

    port = find_free_port()
    server = QuietServer(("127.0.0.1", port), ProbeHandler)
    server_thread = threading.Thread(target=server.serve_forever, daemon=True)
    server_thread.start()

    print(f"PROBE: serving on 127.0.0.1:{port}, {args.trials} trial(s)")

    delivered_count = 0
    try:
        for i in range(1, args.trials + 1):
            if run_trial(port, i, args.trials):
                delivered_count += 1
    finally:
        server.shutdown()

    rate = delivered_count / args.trials
    overall = "DELIVERED" if delivered_count == args.trials else "DEAD"
    print(f"PROBE: {overall}  ({delivered_count}/{args.trials} delivered, rate={rate:.0%})")

    sys.exit(0 if overall == "DELIVERED" else 1)


if __name__ == "__main__":
    main()
