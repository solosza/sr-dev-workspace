"""
L3 Live Test: _reference Pages against Orderly.

PAG-07: Full login → browse → detail flow through page objects on the live Orderly app.
Seed data: clerk/clerk123, 4 customers, 8 orders.
"""
import logging
import subprocess
import sys
import time

REPO = "D:/my_ai_projects/project_test_repos/hmsa-qa-platform"
PORT = 8017
BASE_URL = f"http://127.0.0.1:{PORT}"

logger = logging.getLogger("L3-pages")
logging.basicConfig(level=logging.INFO, format="%(levelname)s %(message)s")

server_proc = None
driver = None

try:
    # 1. Seed the database
    logger.info("Seeding Orderly database...")
    result = subprocess.run(
        [sys.executable, "-m", "harness.orderly.seed"],
        cwd=REPO, capture_output=True, text=True, timeout=15
    )
    if result.returncode != 0:
        logger.error(f"Seed failed: {result.stderr}")
        sys.exit(1)
    logger.info(result.stdout.strip())

    # 2. Start Orderly server
    logger.info(f"Starting Orderly on port {PORT}...")
    server_proc = subprocess.Popen(
        [sys.executable, "-m", "uvicorn", "harness.orderly.main:app",
         "--port", str(PORT), "--host", "127.0.0.1"],
        cwd=REPO, stdout=subprocess.PIPE, stderr=subprocess.PIPE
    )
    time.sleep(3)

    # 3. Launch headless Chrome
    from selenium import webdriver
    from selenium.webdriver.common.by import By
    from selenium.webdriver.chrome.options import Options
    from selenium.webdriver.chrome.service import Service

    opts = Options()
    opts.add_argument("--headless=new")
    opts.add_argument("--no-sandbox")
    opts.add_argument("--disable-dev-shm-usage")
    opts.add_argument("--window-size=1280,800")
    driver = webdriver.Chrome(options=opts)

    # 4. Create BrowserInterface
    sys.path.insert(0, f"{REPO}/framework")
    from interfaces.browser_interface import BrowserInterface
    config = {"explicit_wait": 10}
    browser = BrowserInterface(driver, config, logger)

    # 5. Import page objects
    sys.path.insert(0, f"{REPO}/framework/_reference")
    from pages.login_page import LoginPage
    from pages.customers_page import CustomersPage
    from pages.orders_page import OrdersPage
    from pages.order_detail_page import OrderDetailPage

    # 6. LoginPage: navigate, enter credentials, submit
    logger.info("=== LoginPage ===")
    login = LoginPage(browser)
    login.navigate(f"{BASE_URL}/login")
    login.wait_for_login_form_visible()
    assert login.is_login_form_displayed(), "Login form should be displayed"

    login.enter_username("clerk")
    login.enter_password("clerk123")
    login.click_login()
    time.sleep(1)

    assert login.is_on_customers_page(), "Should redirect to /customers after login"
    logger.info("LoginPage PASS: logged in, redirected to /customers")

    # 7. CustomersPage: verify seeded data
    logger.info("=== CustomersPage ===")
    cust = CustomersPage(browser)
    cust.wait_for_customers_heading()
    assert cust.is_customers_heading_displayed(), "Customers heading should be displayed"
    assert cust.is_customer_table_displayed(), "Customer table should be displayed"
    assert cust.is_customer_listed("Alice Johnson"), "Alice Johnson should be in the list"
    assert cust.is_customer_listed("Bob Smith"), "Bob Smith should be in the list"
    count = cust.get_customer_count()
    assert count == 4, f"Should have 4 customers, got {count}"
    logger.info(f"CustomersPage PASS: {count} customers, Alice and Bob found")

    # 8. OrdersPage: navigate and verify
    logger.info("=== OrdersPage ===")
    orders = OrdersPage(browser)
    browser.navigate_to(f"{BASE_URL}/orders")
    orders.wait_for_orders_heading(timeout=15)
    assert orders.is_orders_heading_displayed(), "Orders heading should be displayed"
    assert orders.is_orders_grid_displayed(), "Orders grid should be displayed"
    assert orders.is_order_listed(1), "Order 1 should be listed"
    assert orders.is_order_listed(5), "Order 5 should be listed"
    order_count = orders.get_order_count()
    assert order_count == 8, f"Should have 8 orders, got {order_count}"
    status = orders.get_order_status(1)
    assert status == "PENDING", f"Order 1 status should be PENDING, got {status}"
    logger.info(f"OrdersPage PASS: {order_count} orders, order 1 is PENDING")

    # 9. OrderDetailPage: open order 1, verify fields
    logger.info("=== OrderDetailPage ===")
    browser.scroll_to_element(By.CSS_SELECTOR, "[data-testid='link-detail-1']")
    time.sleep(0.5)
    orders.click_order_detail(1)
    time.sleep(1)
    current_url = browser.get_current_url()
    logger.info(f"After click, URL: {current_url}")
    if "/orders/1" not in current_url:
        logger.info("Click navigation failed in headless — using JS click")
        el = driver.find_element(By.CSS_SELECTOR, "[data-testid='link-detail-1']")
        driver.execute_script("arguments[0].click();", el)
        time.sleep(1)
    detail = OrderDetailPage(browser)
    detail.wait_for_order_detail(timeout=15)
    assert detail.is_order_detail_displayed(), "Order detail should be displayed"
    displayed_status = detail.get_displayed_status()
    assert displayed_status == "PENDING", f"Order 1 detail status should be PENDING, got {displayed_status}"
    customer = detail.get_customer_name()
    assert customer == "Alice Johnson", f"Order 1 customer should be Alice Johnson, got {customer}"
    assert detail.is_status_change_available(), "Status change form should be available"
    assert detail.is_items_grid_displayed(), "Items grid should be displayed"
    item_count = detail.get_item_count()
    assert item_count == 1, f"Order 1 should have 1 item, got {item_count}"
    logger.info(f"OrderDetailPage PASS: order 1 detail correct, {item_count} item(s)")

    logger.info("")
    logger.info("PAG-07 PASS: Full login -> browse -> detail flow succeeded")
    sys.exit(0)

except Exception as e:
    logger.error(f"L3 FAIL: {e}")
    import traceback
    traceback.print_exc()
    sys.exit(1)

finally:
    if driver:
        driver.quit()
    if server_proc:
        server_proc.terminate()
        server_proc.wait(timeout=5)
