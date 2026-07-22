"""
Chromedriver verbose-log probe against Orderly app.
Tests post-navigation click delivery on the actual app where the fault was observed.
"""
import subprocess, sys, time, os, json

PORT = 8019
LOG_PATH = "D:/my_ai_projects/project_test_repos/sr_dev_workspace/scratchpad/chromedriver_verbose_orderly.log"
APP_ROOT = "D:/my_ai_projects/project_test_repos/hmsa-qa-platform"

def start_orderly():
    proc = subprocess.Popen(
        [sys.executable, "-m", "uvicorn", "harness.orderly.main:app",
         "--host", "127.0.0.1", "--port", str(PORT)],
        cwd=APP_ROOT,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    time.sleep(3)
    return proc

def run_probe():
    from selenium import webdriver
    from selenium.webdriver.chrome.service import Service
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC

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

        # Login page (first document)
        driver.get(f"{base}/login")
        time.sleep(1)

        user_field = driver.find_element(By.NAME, "username")
        user_field.send_keys("admin")
        pass_field = driver.find_element(By.NAME, "password")
        pass_field.send_keys("admin")
        login_btn = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
        login_btn.click()
        time.sleep(2)
        results.append(f"After login: URL={driver.current_url}")

        # Navigate to customers (the default redirect after login)
        driver.get(f"{base}/customers")
        time.sleep(2)

        # Inject listener
        driver.execute_script("""
            window.__clickLog = [];
            document.addEventListener('click', function(e) {
                window.__clickLog.push({
                    target: e.target.tagName + '#' + (e.target.id || '') + '.' + (e.target.className || ''),
                    text: (e.target.textContent || '').substring(0, 30),
                    x: e.clientX, y: e.clientY,
                    ts: Date.now()
                });
            }, true);
        """)

        # Try clicking various elements on the post-nav page
        clickables = driver.find_elements(By.CSS_SELECTOR, "a, button, [onclick], tr[data-id], .clickable")
        results.append(f"Found {len(clickables)} clickable elements on /customers")

        delivered = 0
        total = min(16, max(len(clickables), 10))

        for i in range(total):
            try:
                # Re-find elements each time in case page changed
                clickables = driver.find_elements(By.CSS_SELECTOR, "a, button, [onclick]")
                if not clickables:
                    results.append(f"Click {i}: no clickables found")
                    continue

                target = clickables[i % len(clickables)]
                tag = target.tag_name
                text = (target.text or "")[:30]

                before = driver.execute_script("return window.__clickLog.length")
                target.click()
                time.sleep(0.5)

                # Check if we navigated away
                if "/customers" not in driver.current_url and "/login" not in driver.current_url:
                    results.append(f"Click {i}: navigated to {driver.current_url}, returning to /customers")
                    driver.get(f"{base}/customers")
                    time.sleep(1)
                    # Re-inject listener
                    driver.execute_script("""
                        window.__clickLog = [];
                        document.addEventListener('click', function(e) {
                            window.__clickLog.push({
                                target: e.target.tagName + '#' + (e.target.id || ''),
                                ts: Date.now()
                            });
                        }, true);
                    """)
                    delivered += 1
                    continue

                after = driver.execute_script("return window.__clickLog.length")
                click_delivered = after > before
                if click_delivered:
                    delivered += 1
                results.append(f"Click {i}: {tag} '{text}' → {'DELIVERED' if click_delivered else 'DROPPED'} (log {before}→{after})")

            except Exception as e:
                err = str(e)[:80]
                results.append(f"Click {i}: error — {err}")

        results.append(f"\nSUMMARY: {delivered}/{total} clicks delivered ({total - delivered} dropped)")

    finally:
        driver.quit()

    return results

def main():
    print("Starting Orderly on port 8019...")
    orderly = start_orderly()

    try:
        print("Running chromedriver probe against Orderly...")
        results = run_probe()
        for r in results:
            print(r)

        print(f"\nChromedriver verbose log: {LOG_PATH}")
        if os.path.exists(LOG_PATH):
            print(f"Log size: {os.path.getsize(LOG_PATH)} bytes")
    finally:
        orderly.terminate()
        try:
            orderly.wait(timeout=5)
        except:
            orderly.kill()
        print("Orderly stopped.")

if __name__ == "__main__":
    main()
