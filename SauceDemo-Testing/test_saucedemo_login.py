
from selenium import webdriver 
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
wait = WebDriverWait(driver, 10)


def open_login_page():
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

    return username, password, login_button


try:
    # 1. Verify login page elements
    username, password, login_button = open_login_page()


    assert username.is_displayed()
    assert password.is_displayed()
    assert login_button.is_displayed()

    print("PASS: Login page elements are visible.")

    # 2. Test invalid password
    username.send_keys("standard_user")
    password.send_keys("wrong_password")
    login_button.click()

    error_message = wait.until(
        EC.visibility_of_element_located(
            (By.CSS_SELECTOR, '[data-test="error"]')
        )
    )

    assert "Username and password do not match" in error_message.text
    print("PASS: Invalid password test.")

    # 3. Test both fields empty
    username, password, login_button = open_login_page()

    login_button.click()

    error_message = wait.until(
        EC.visibility_of_element_located(
            (By.CSS_SELECTOR, '[data-test="error"]')
        )
    )

    assert "Username is required" in error_message.text
    print("PASS: Empty credentials test.")

    # 4. Test empty username
    username, password, login_button = open_login_page()

    password.send_keys("secret_sauce")
    login_button.click()

    error_message = wait.until(
        EC.visibility_of_element_located(
            (By.CSS_SELECTOR, '[data-test="error"]')
        )
    )

    assert "Username is required" in error_message.text
    print("PASS: Empty username test.")

    # 5. Test empty password
    username, password, login_button = open_login_page()

    username.send_keys("standard_user")
    login_button.click()

    error_message = wait.until(
        EC.visibility_of_element_located(
            (By.CSS_SELECTOR, '[data-test="error"]')
        )
    )

    assert "Password is required" in error_message.text
    print("PASS: Empty password test.")

    # 6. Test successful login
    username, password, login_button = open_login_page()

    username.send_keys("standard_user")
    password.send_keys("secret_sauce")
    login_button.click()

    wait.until(EC.url_contains("inventory.html"))

    inventory_title = wait.until(
        EC.visibility_of_element_located(
            (By.CLASS_NAME, "title")
        )
    )

    assert inventory_title.text == "Products"
    print("PASS: Successful login test.")

finally:
    driver.quit()
