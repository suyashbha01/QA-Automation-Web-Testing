
import pytest
import pytest_html
from pathlib import Path
from selenium import webdriver


@pytest.fixture
def driver(request):
    browser = webdriver.Chrome()
    request.node.driver = browser

    yield browser

    browser.quit()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        browser = getattr(item, "driver", None)

        if browser:
            screenshot_folder = Path("screenshots")
            screenshot_folder.mkdir(exist_ok=True)

            screenshot_path = screenshot_folder / f"{item.name}.png"
            browser.save_screenshot(str(screenshot_path))

            report.extras = getattr(report, "extras", [])
            report.extras.append(
                pytest_html.extras.image(str(screenshot_path))
            )


