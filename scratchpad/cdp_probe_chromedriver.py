"""
Chromedriver verbose-log probe for selenium click fault (backlog 235).
Uses bare HTML pages on port 8019 for framework-free reproduction.
Captures chromedriver verbose log for CDP command analysis.
"""
import subprocess, sys, time, os, json

PORT = 8019
LOG_PATH = "D:/my_ai_projects/project_test_repos/sr_dev_workspace/scratchpad/chromedriver_verbose.log"
SERVER_SCRIPT = "D:/my_ai_projects/project_test_repos/sr_dev_workspace/scratchpad/bare_server.py"

def start_server():
    proc = subprocess.Popen(
        [sys.executable, SERVER_SCRIPT],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    time.sleep(1)
    return proc

def run_probe():
    from selenium import webdriver
    from selenium.webdriver.chrome.service import Service
    from selenium.webdriver.common.by import By

    service = Service(
        log_output=LOG_PATH,
        service_args=["--verbose"],
    )
    options = webdriver.ChromeOptions()
    options.add_argument("--disable-gpu")
    options.add_argument("--disable-backgrounding-occluded-windows")

    driver = webdriver.Chrome(service=service, options=options)
    results = []

    try:
        base = f"http://127.0.0.1:{PORT}"

        # Page A — first document
        driver.get(f"{base}/page_a.html")
        time.sleep(1)

        driver.execute_script("""
            window.__clickLog = [];
            document.addEventListener('click', function(e) {
                window.__clickLog.push({
                    target: e.target.id || e.target.tagName,
                    x: e.clientX, y: e.clientY,
                    ts: Date.now(), page: 'A'
                });
            }, true);
        """)

        # Click button on Page A (first-document, should work)
        btn = driver.find_element(By.ID, "test-btn")
        btn.click()
        time.sleep(0.5)
        result_text = driver.find_element(By.ID, "result").text
        log_count = driver.execute_script("return window.__clickLog.length")
        results.append(f"Page A click: result='{result_text}', DOM events={log_count}")

        # Navigate to Page B
        driver.get(f"{base}/page_b.html")
        time.sleep(2)

        # Inject listener on Page B
        driver.execute_script("""
            window.__clickLog = [];
            document.addEventListener('click', function(e) {
                window.__clickLog.push({
                    target: e.target.id || e.target.tagName,
                    x: e.clientX, y: e.clientY,
                    ts: Date.now(), page: 'B'
                });
            }, true);
        """)

        # Click button on Page B (post-navigation, drops expected)
        for i in range(10):
            btn = driver.find_element(By.ID, "test-btn")
            btn.click()
            time.sleep(0.5)
            result_text = driver.find_element(By.ID, "result").text
            log_count = driver.execute_script("return window.__clickLog.length")
            results.append(f"Page B click {i}: result='{result_text}', DOM events={log_count}")

        final_log = driver.execute_script("return JSON.stringify(window.__clickLog)")
        results.append(f"Page B click log: {final_log}")

    finally:
        driver.quit()

    return results

def main():
    print("Starting bare server on port 8019...")
    server = start_server()

    try:
        print("Running chromedriver verbose probe...")
        results = run_probe()
        for r in results:
            print(r)

        print(f"\nChromedriver verbose log: {LOG_PATH}")
        if os.path.exists(LOG_PATH):
            print(f"Log size: {os.path.getsize(LOG_PATH)} bytes")
    finally:
        server.terminate()
        try:
            server.wait(timeout=5)
        except:
            server.kill()
        print("Server stopped.")

if __name__ == "__main__":
    main()
