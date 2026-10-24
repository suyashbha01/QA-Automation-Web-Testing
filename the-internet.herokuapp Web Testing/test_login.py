import pytest
from pages.login_page import LoginPage


@pytest.mark.smoke
def test_login(driver):
    driver.get("https://the-internet.herokuapp.com/login")

    login_page = LoginPage(driver)
    login_page.enter_username("tomsmith")
    login_page.enter_password("SuperSecretPassword!")
    login_page.click_login()
    login_page.verify_login_success()


@pytest.mark.parametrize(
    "username, password",
    [
        ("tomsmith", "WrongPassword123"),
        ("", ""),
    ],
)
@pytest.mark.regression
def test_login_invalid_scenarios(driver, username, password):
    driver.get("https://the-internet.herokuapp.com/login")

    login_page = LoginPage(driver)

    if username:
        login_page.enter_username(username)

    if password:
        login_page.enter_password(password)

    login_page.click_login()
    login_page.verify_login_failure()
    