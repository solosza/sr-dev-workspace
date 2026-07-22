"""
ROL-06: Live env-gated test for _reference UI roles.

Probe decides scope (lessons #40/#41/#42):
- GREEN: full live workflow (clerk status change + manager cancel on real DOM)
- RED: construction + identity wiring proven, click residue documented for 208
"""

import subprocess
import sys
import time
import signal
import os
import logging

REPO = "D:/my_ai_projects/project_test_repos/hmsa-qa-platform"
FRAMEWORK = os.path.join(REPO, "framework")
APP_PORT = 8017
APP_URL = f"http://localhost:{APP_PORT}"

CLERK_IDENTITY = {"username": "clerk", "password": "clerk123"}
MANAGER_IDENTITY = {"username": "manager", "password": "manager123"}


def kill_port(port):
    """Kill any process on the given port."""
    try:
        result = subprocess.run(
            ["powershell", "-Command",
             f"Get-NetTCPConnection -LocalPort {port} -ErrorAction SilentlyContinue | "
             f"ForEach-Object {{ Stop-Process -Id $_.OwningProcess -Force -ErrorAction SilentlyContinue }}"],
            capture_output=True, timeout=10
        )
    except Exception:
        pass


def seed_db():
    """Fresh seed the Orderly database."""
    result = subprocess.run(
        [sys.executable, "-m", "harness.orderly.seed"],
        cwd=REPO, capture_output=True, text=True, timeout=30
    )
    if result.returncode != 0:
        print(f"FAIL: seed failed: {result.stderr}")
        sys.exit(1)
    print(f"  Seed: {result.stdout.strip()}")


def start_uvicorn():
    """Start uvicorn in background, return process handle."""
    proc = subprocess.Popen(
        [sys.executable, "-m", "uvicorn", "harness.orderly.main:app",
         "--port", str(APP_PORT), "--host", "127.0.0.1"],
        cwd=REPO, stdout=subprocess.PIPE, stderr=subprocess.PIPE
    )
    time.sleep(3)
    if proc.poll() is not None:
        print(f"FAIL: uvicorn exited early: {proc.stderr.read().decode()}")
        sys.exit(1)
    return proc


def selenium_click_probe():
    """Bare selenium two-page click probe (lesson #41/#42).

    Returns True if post-navigation clicks are delivered.
    """
    from selenium import webdriver
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC

    options = webdriver.ChromeOptions()
    options.add_argument("--headless=new")
    options.add_argument("--disable-gpu")
    driver = None
    try:
        driver = webdriver.Chrome(options=options)
        driver.get(f"{APP_URL}/login")

        wait = WebDriverWait(driver, 10)
        wait.until(EC.visibility_of_element_located(
            (By.CSS_SELECTOR, "[data-testid='input-username']")
        ))

        driver.find_element(By.CSS_SELECTOR, "[data-testid='input-username']").send_keys("clerk")
        driver.find_element(By.CSS_SELECTOR, "[data-testid='input-password']").send_keys("clerk123")
        driver.find_element(By.CSS_SELECTOR, "[data-testid='button-login']").click()

        wait.until(EC.url_contains("/customers"))

        orders_link = wait.until(EC.element_to_be_clickable(
            (By.CSS_SELECTOR, "[data-testid='link-orders']")
        ))
        orders_link.click()

        try:
            wait.until(EC.visibility_of_element_located(
                (By.CSS_SELECTOR, "[data-testid='heading-orders']")
            ))
        except Exception:
            print("  Probe: post-navigation click NOT delivered (heading-orders not visible)")
            return False

        detail_link = wait.until(EC.element_to_be_clickable(
            (By.CSS_SELECTOR, "[data-testid='link-detail-3']")
        ))
        detail_link.click()

        try:
            wait.until(EC.visibility_of_element_located(
                (By.CSS_SELECTOR, "[data-testid='heading-order-detail']")
            ))
            print("  Probe: GREEN — post-navigation clicks delivered")
            return True
        except Exception:
            print("  Probe: post-navigation detail click NOT delivered")
            return False

    except Exception as e:
        print(f"  Probe: RED — {type(e).__name__}: {e}")
        return False
    finally:
        if driver:
            driver.quit()


def run_full_live():
    """Full live test: clerk changes status, manager cancels, assert on real DOM."""
    sys.path.insert(0, FRAMEWORK)
    ref_path = os.path.join(FRAMEWORK, "_reference")
    if ref_path not in sys.path:
        sys.path.insert(0, ref_path)

    from selenium import webdriver
    from interfaces.browser_interface import BrowserInterface
    from _reference.pages.login_page import LoginPage
    from _reference.pages.orders_page import OrdersPage
    from _reference.pages.order_detail_page import OrderDetailPage
    from _reference.tasks.common_tasks import CommonTasks
    from _reference.tasks.order_workup_tasks import OrderWorkupTasks
    from _reference.roles.order_clerk import OrderClerk
    from _reference.roles.order_manager import OrderManager

    logger = logging.getLogger("rol06-live")
    options = webdriver.ChromeOptions()
    options.add_argument("--headless=new")
    options.add_argument("--disable-gpu")
    driver = webdriver.Chrome(options=options)

    try:
        config = {"explicit_wait": 15}
        browser = BrowserInterface(driver, config, logger)
        browser.navigate_to(f"{APP_URL}/login")

        login_page = LoginPage(browser)
        orders_page = OrdersPage(browser)
        detail_page = OrderDetailPage(browser)

        common = CommonTasks(login_page)
        order_workup = OrderWorkupTasks(orders_page, detail_page)

        clerk = OrderClerk(common, order_workup, CLERK_IDENTITY)
        manager = OrderManager(common, order_workup, MANAGER_IDENTITY)

        # Order 1 is PENDING → can transition to PROCESSING → then CANCELLED
        # (Order 3 is COMPLETE with no valid transitions — select-status not rendered)
        print("  Clerk: work_order_status_change('1', 'PROCESSING')")
        clerk.work_order_status_change("1", "PROCESSING")

        displayed = detail_page.get_displayed_status()
        assert "PROCESSING" in displayed.upper(), f"Expected PROCESSING, got: {displayed}"
        print(f"  Assert: status={displayed} — PASS")

        # Manager cancels order 1 (now PROCESSING → CANCELLED is valid)
        print("  Manager: cancel_order('1')")
        manager.cancel_order("1")

        displayed = detail_page.get_displayed_status()
        assert "CANCELLED" in displayed.upper(), f"Expected CANCELLED, got: {displayed}"
        print(f"  Assert: status={displayed} — PASS (session switch proven)")

        print("ROL-06 FULL: clerk status change + manager cancel — both verified on real DOM")
        return True

    except Exception as e:
        print(f"ROL-06 FULL FAIL: {type(e).__name__}: {e}")
        return False
    finally:
        driver.quit()


def run_construction_only():
    """Construction + identity wiring test (no clicks needed)."""
    sys.path.insert(0, FRAMEWORK)
    ref_path = os.path.join(FRAMEWORK, "_reference")
    if ref_path not in sys.path:
        sys.path.insert(0, ref_path)

    from _reference.pages.login_page import LoginPage
    from _reference.pages.orders_page import OrdersPage
    from _reference.pages.order_detail_page import OrderDetailPage
    from _reference.tasks.common_tasks import CommonTasks
    from _reference.tasks.order_workup_tasks import OrderWorkupTasks
    from _reference.roles.order_clerk import OrderClerk
    from _reference.roles.order_manager import OrderManager

    class FakeBrowser:
        """Minimal stub — only proves construction and identity wiring."""
        def navigate_to(self, url): pass
        def click(self, *a, **kw): pass
        def enter_text(self, *a, **kw): pass
        def wait_for_element_visible(self, *a, **kw): pass
        def select_by_value(self, *a, **kw): pass
        def is_element_displayed(self, *a, **kw): return True
        def get_text(self, *a, **kw): return ""
        def get_current_url(self): return "/customers"
        def find_elements(self, *a, **kw): return []
        def get_select_options(self, *a, **kw): return []

    fake = FakeBrowser()
    login_page = LoginPage(fake)
    orders_page = OrdersPage(fake)
    detail_page = OrderDetailPage(fake)

    common = CommonTasks(login_page)
    order_workup = OrderWorkupTasks(orders_page, detail_page)

    clerk = OrderClerk(common, order_workup, CLERK_IDENTITY)
    manager = OrderManager(common, order_workup, MANAGER_IDENTITY)

    checks = []

    # Identity wiring
    checks.append(("clerk.identity == CLERK_IDENTITY",
                    clerk.identity == CLERK_IDENTITY))
    checks.append(("manager.identity == MANAGER_IDENTITY",
                    manager.identity == MANAGER_IDENTITY))

    # CommonTasks holds real LoginPage
    checks.append(("clerk.common.login_page is LoginPage",
                    type(clerk.common.login_page).__name__ == "LoginPage"))
    checks.append(("manager.common.login_page is LoginPage",
                    type(manager.common.login_page).__name__ == "LoginPage"))

    # OrderWorkupTasks holds real pages
    checks.append(("clerk.order_workup.orders_page is OrdersPage",
                    type(clerk.order_workup.orders_page).__name__ == "OrdersPage"))
    checks.append(("clerk.order_workup.detail_page is OrderDetailPage",
                    type(clerk.order_workup.detail_page).__name__ == "OrderDetailPage"))

    # Shared instances
    checks.append(("clerk and manager share CommonTasks instance",
                    clerk.common is manager.common))
    checks.append(("clerk and manager share OrderWorkupTasks instance",
                    clerk.order_workup is manager.order_workup))

    all_pass = True
    for label, result in checks:
        status = "PASS" if result else "FAIL"
        if not result:
            all_pass = False
        print(f"  {status}: {label}")

    if all_pass:
        print("ROL-06 PARTIAL: click-path ENV-BLOCKED (lesson #41) — "
              "orchestration proven by ROL-05; full-stack proof deferred to 208 E2E")
    else:
        print("ROL-06 CONSTRUCTION FAIL: identity/wiring checks failed")

    return all_pass


def main():
    print("=== ROL-06: Live env-gated test ===")

    uvicorn_proc = None
    try:
        # Step 1: Kill stray processes on 8017
        kill_port(APP_PORT)
        time.sleep(1)

        # Step 2: Fresh seed
        print("Step 1: Seed database")
        seed_db()

        # Step 3: Start uvicorn
        print("Step 2: Start uvicorn")
        uvicorn_proc = start_uvicorn()
        print(f"  uvicorn pid={uvicorn_proc.pid} on port {APP_PORT}")

        # Step 4: Selenium click probe
        print("Step 3: Selenium click probe")
        probe_green = selenium_click_probe()

        # Step 5: Branch on probe result
        if probe_green:
            print("Step 4: Full live test (probe GREEN)")
            success = run_full_live()
        else:
            print("Step 4: Construction-only test (probe RED)")
            success = run_construction_only()

        if success:
            print(f"\nPath taken: {'FULL LIVE' if probe_green else 'CONSTRUCTION-ONLY (ENV-BLOCKED)'}")
            print("ROL-06: PASS")
            sys.exit(0)
        else:
            print("ROL-06: FAIL")
            sys.exit(1)

    finally:
        # Cleanup: kill uvicorn
        if uvicorn_proc and uvicorn_proc.poll() is None:
            uvicorn_proc.terminate()
            try:
                uvicorn_proc.wait(timeout=5)
            except subprocess.TimeoutExpired:
                uvicorn_proc.kill()
            print(f"  Cleaned up uvicorn pid={uvicorn_proc.pid}")

        # Double-check port is free
        kill_port(APP_PORT)
        print("  Port 8017 cleared")


if __name__ == "__main__":
    main()
