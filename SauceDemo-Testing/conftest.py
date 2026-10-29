
import pytest
import os
import re

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def create_chrome_options():
    options = webdriver.ChromeOptions()

    # Run visibly on your computer; headless in GitHub Actions
    if os.getenv("GITHUB_ACTIONS") == "true":
        options.add_argument("--headless")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")

    options.add_argument("--window-size=1920,1080")
    return options


@pytest.fixture
def logged_in_driver():
    driver = webdriver.Chrome(options=create_chrome_options())
    wait = WebDriverWait(driver, 15)

    try:
        driver.get("https://www.saucedemo.com/")

        username = wait.until(
            EC.visibility_of_element_located((By.ID, "user-name"))
        )
        password = wait.until(
            EC.visibility_of_element_located((By.ID, "password"))
        )
        login_button = wait.until(
            EC.element_to_be_clickable((By.ID, "login-button"))
        )

        username.send_keys("standard_user")
        password.send_keys("secret_sauce")
        login_button.click()

        # Verify successful login
        wait.until(EC.url_contains("inventory.html"))

        wait.until(
            EC.visibility_of_element_located(
                (By.CSS_SELECTOR, ".inventory_item")
            )
        )

        yield driver

    finally:
        driver.quit()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        driver = item.funcargs.get("logged_in_driver")

        if driver:
            os.makedirs("screenshots", exist_ok=True)

            safe_name = re.sub(r"[^\w.-]", "_", item.name)
            screenshot_path = os.path.join(
                "screenshots",
                f"{safe_name}.png"
            )

            driver.save_screenshot(screenshot_path)
            print(f"\nFailure screenshot saved: {screenshot_path}")
