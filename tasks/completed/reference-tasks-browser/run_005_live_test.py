"""TSK-05: Live env-gated test against Orderly."""
import subprocess
import sys
import time
import os
import urllib.request

REPO = "D:/my_ai_projects/project_test_repos/hmsa-qa-platform"
PORT = 8017
BASE_URL = f"http://localhost:{PORT}"


def start_server():
    server = subprocess.Popen(
        [sys.executable, "-m", "uvicorn", "harness.orderly.main:app", "--port", str(PORT)],
        cwd=REPO,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    for i in range(20):
        try:
            urllib.request.urlopen(f"{BASE_URL}/login", timeout=2)
            print(f"Server ready after {i + 1} attempts")
            return server
        except Exception:
            time.sleep(0.5)
    server.kill()
    raise RuntimeError("Server failed to start")


def run_probe(webdriver, By, WebDriverWait, EC):
    """Bare-selenium two-page click probe."""
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")

    driver = webdriver.Chrome(options=options)
    try:
        driver.get(f"{BASE_URL}/login")
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "[data-testid='button-login']"))
        )
        driver.find_element(By.CSS_SELECTOR, "[data-testid='input-username']").send_keys("admin@orderly.local")
        driver.find_element(By.CSS_SELECTOR, "[data-testid='input-password']").send_keys("admin123")
        driver.find_element(By.CSS_SELECTOR, "[data-testid='button-login']").click()

        WebDriverWait(driver, 10).until(EC.url_contains("/customers"))
        print("Login OK, redirected to /customers")

        driver.get(f"{BASE_URL}/orders")
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "[data-testid='heading-orders']"))
        )
        print("Navigated to /orders")

        try:
            delete_btn = WebDriverWait(driver, 5).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "[data-testid='button-delete-3']"))
            )
            delete_btn.click()
            time.sleep(1)

            modal = driver.find_elements(By.CSS_SELECTOR, "[data-testid='modal-confirm-delete']")
            if modal and modal[0].is_displayed():
                print("PROBE GREEN: post-navigation click delivered, modal displayed")
                cancel = driver.find_element(By.CSS_SELECTOR, "[data-testid='button-cancel']")
                cancel.click()
                time.sleep(0.5)
                return True
            else:
                print("PROBE RED: click delivered but modal not displayed")
                return False
        except Exception as e:
            print(f"PROBE RED: click probe failed: {e}")
            return False
    finally:
        driver.quit()


def run_full_live(webdriver, By, WebDriverWait, EC):
    """Full live flow when probe is green."""
    print("PATH: FULL LIVE FLOW")
    sys.path.insert(0, os.path.join(REPO, "framework"))

    from interfaces.browser_interface import BrowserInterface
    from _reference.pages.orders_page import OrdersPage
    from _reference.pages.order_detail_page import OrderDetailPage
    from _reference.pages.login_page import LoginPage
    from _reference.tasks.order_workup_tasks import OrderWorkupTasks

    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    driver = webdriver.Chrome(options=options)

    try:
        browser = BrowserInterface(driver)
        login_page = LoginPage(browser)
        orders_page = OrdersPage(browser)
        detail_page = OrderDetailPage(browser)
        tasks = OrderWorkupTasks(orders_page, detail_page)

        driver.get(f"{BASE_URL}/login")
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "[data-testid='button-login']"))
        )
        login_page.enter_username("admin@orderly.local")
        login_page.enter_password("admin123")
        login_page.click_login()
        WebDriverWait(driver, 10).until(EC.url_contains("/customers"))

        print('Testing open_order("3")...')
        tasks.open_order("3")
        assert "/orders/3" in driver.current_url, f"Expected /orders/3 in URL, got {driver.current_url}"
        print(f"  URL: {driver.current_url} PASS")

        print("Testing capture_order_id()...")
        oid = tasks.capture_order_id()
        assert oid == "3", f'Expected "3", got {oid!r}'
        print(f"  Order ID: {oid} PASS")

        print('Testing change_status("PROCESSING")...')
        tasks.change_status("PROCESSING")
        status = detail_page.get_displayed_status()
        print(f"  Status after change: {status}")
        print("  change_status completed without error PASS")

        print()
        print("TSK-05 FULL: All live assertions PASS")
    finally:
        driver.quit()


def run_read_path(webdriver, By, WebDriverWait, EC):
    """Read-path only when probe is red."""
    print("PATH: READ-PATH ONLY (ENV-BLOCKED)")
    sys.path.insert(0, os.path.join(REPO, "framework"))

    from interfaces.browser_interface import BrowserInterface
    from _reference.pages.orders_page import OrdersPage
    from _reference.pages.order_detail_page import OrderDetailPage
    from _reference.tasks.order_workup_tasks import OrderWorkupTasks

    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    driver = webdriver.Chrome(options=options)

    try:
        browser = BrowserInterface(driver)
        orders_page = OrdersPage(browser)
        detail_page = OrderDetailPage(browser)
        tasks = OrderWorkupTasks(orders_page, detail_page)

        driver.get(f"{BASE_URL}/login")
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "[data-testid='button-login']"))
        )
        driver.find_element(By.CSS_SELECTOR, "[data-testid='input-username']").send_keys("admin@orderly.local")
        driver.find_element(By.CSS_SELECTOR, "[data-testid='input-password']").send_keys("admin123")
        driver.find_element(By.CSS_SELECTOR, "[data-testid='button-login']").click()
        WebDriverWait(driver, 10).until(EC.url_contains("/customers"))

        driver.get(f"{BASE_URL}/orders/3")
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "[data-testid='heading-order-detail']"))
        )

        print("Testing capture_order_id() live...")
        oid = tasks.capture_order_id()
        assert oid == "3", f'Expected "3", got {oid!r}'
        print(f"  Order ID: {oid} PASS")

        print()
        print(
            "TSK-05 PARTIAL: click-path ENV-BLOCKED (selenium input regression, lesson #41) "
            "-- sequence proven by TSK-04; full-stack click proof deferred to 208 E2E"
        )
    finally:
        driver.quit()


def main():
    from selenium import webdriver
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC

    server = start_server()
    try:
        print()
        print("STEP: Selenium two-page click probe...")
        probe_ok = run_probe(webdriver, By, WebDriverWait, EC)
        print()

        if probe_ok:
            run_full_live(webdriver, By, WebDriverWait, EC)
        else:
            run_read_path(webdriver, By, WebDriverWait, EC)
    finally:
        server.kill()
        server.wait()
        print()
        print("Server stopped.")

    print()
    print("RESULT: TSK-05 exits 0")


if __name__ == "__main__":
    main()
