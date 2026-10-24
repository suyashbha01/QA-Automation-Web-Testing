
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import re



@pytest.fixture
def logged_in_driver():
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 10)

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

    wait.until(EC.url_contains("inventory.html"))

    yield driver

    driver.quit()

    
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        driver = item.funcargs.get("logged_in_driver")

        if driver:
            os.makedirs("screenshots", exist_ok=True)

            safe_name = re.sub(r'[^\w.-]', '_', item.name)
            screenshot_path = os.path.join(
                "screenshots",
                f"{safe_name}.png"
            )

            driver.save_screenshot(screenshot_path)
            print(f"\nFailure screenshot saved: {screenshot_path}")



