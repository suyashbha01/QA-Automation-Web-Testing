"""
Selenium Revision Main File
Runs ALL practice tests automatically in one run and creates an HTML report at the end.
Website used for most examples: https://the-internet.herokuapp.com/
"""

from pathlib import Path
import os
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys


BASE_URL = "https://the-internet.herokuapp.com"
SCREENSHOT_DIR = Path("screenshots")
DOWNLOAD_DIR = Path("downloads")


def start_browser():
    """Create Chrome with a download folder configured."""
    SCREENSHOT_DIR.mkdir(exist_ok=True)
    DOWNLOAD_DIR.mkdir(exist_ok=True)

    options = webdriver.ChromeOptions()
    options.add_experimental_option(
        "prefs",
        {
            "download.default_directory": str(DOWNLOAD_DIR.resolve()),
            "download.prompt_for_download": False,
            "download.directory_upgrade": True,
        },
    )

    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    return driver


def test_login(driver):
    driver.get(f"{BASE_URL}/login")
    wait = WebDriverWait(driver, 10)

    username = wait.until(EC.visibility_of_element_located((By.ID, "username")))
    password = driver.find_element(By.ID, "password")

    username.send_keys("tomsmith")
    password.send_keys("SuperSecretPassword!")

    login_button = wait.until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, ".radius[type='submit']"))
    )
    login_button.click()

    heading = wait.until(
        EC.visibility_of_element_located((By.TAG_NAME, "h2"))
    )
    assert heading.text == "Secure Area"
    print("Login test passed")


def test_dropdown(driver):
    driver.get(f"{BASE_URL}/dropdown")
    wait = WebDriverWait(driver, 10)

    dropdown_element = wait.until(
        EC.presence_of_element_located((By.ID, "dropdown"))
    )
    dropdown = Select(dropdown_element)

    dropdown.select_by_value("2")
    assert dropdown.first_selected_option.text == "Option 2"

    dropdown.select_by_visible_text("Option 1")
    assert dropdown.first_selected_option.text == "Option 1"

    # Index 0 is the placeholder, so index 1 selects Option 1.
    dropdown.select_by_index(1)
    assert dropdown.first_selected_option.text == "Option 1"
    print("Dropdown checks passed")


def test_checkboxes(driver):
    driver.get(f"{BASE_URL}/checkboxes")
    wait = WebDriverWait(driver, 10)

    checkboxes = wait.until(
        EC.presence_of_all_elements_located(
            (By.CSS_SELECTOR, "input[type='checkbox']")
        )
    )
    first_checkbox = checkboxes[0]

    # Make the test deterministic: select only if currently unchecked.
    if not first_checkbox.is_selected():
        first_checkbox.click()
    assert first_checkbox.is_selected()

    first_checkbox.click()
    assert not first_checkbox.is_selected()
    print("Checkbox checks passed")


def test_radio_buttons(driver):
    # This public page is used for radio-button practice.
    driver.get("https://www.w3schools.com/html/html_forms.asp")
    radios = WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located(
            (By.CSS_SELECTOR, "input[type='radio']")
        )
    )
    if len(radios) < 2:
        raise AssertionError("Expected at least two radio buttons on the page")

    radios[0].click()
    assert radios[0].is_selected()
    radios[1].click()
    assert radios[1].is_selected()
    print("Radio-button checks passed")


def test_alerts(driver):
    driver.get(f"{BASE_URL}/javascript_alerts")

    driver.find_element(
        By.XPATH, "//button[text()='Click for JS Alert']"
    ).click()
    alert = driver.switch_to.alert
    print("Alert text:", alert.text)
    alert.accept()

    driver.find_element(
        By.XPATH, "//button[text()='Click for JS Confirm']"
    ).click()
    confirm = driver.switch_to.alert
    print("Confirm text:", confirm.text)
    confirm.dismiss()

    driver.find_element(
        By.XPATH, "//button[text()='Click for JS Prompt']"
    ).click()
    prompt = driver.switch_to.alert
    prompt.send_keys("Suyash")
    prompt.accept()

    result = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "result"))
    )
    assert result.text == "You entered: Suyash"
    print("Alert checks passed")


def test_iframe(driver):
    driver.get(f"{BASE_URL}/iframe")
    wait = WebDriverWait(driver, 10)

    iframe = wait.until(
        EC.presence_of_element_located((By.ID, "mce_0_ifr"))
    )
    driver.switch_to.frame(iframe)

    editor = wait.until(
        EC.presence_of_element_located((By.ID, "tinymce"))
    )
    driver.execute_script(
        "arguments[0].innerHTML = 'Selenium iframe practice';", editor
    )
    assert "Selenium iframe practice" in editor.get_attribute("innerHTML")

    driver.switch_to.default_content()
    print("Iframe check passed")


def test_windows(driver):
    driver.get(f"{BASE_URL}/windows")
    main_window = driver.current_window_handle

    driver.find_element(By.CSS_SELECTOR, "a[href='/windows/new']").click()
    WebDriverWait(driver, 10).until(lambda d: len(d.window_handles) == 2)

    new_window = next(
        handle for handle in driver.window_handles if handle != main_window
    )
    driver.switch_to.window(new_window)

    heading = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.TAG_NAME, "h3"))
    )
    assert heading.text == "New Window"

    driver.close()
    driver.switch_to.window(main_window)
    print("Window/tab check passed")


def test_mouse_actions(driver):
    driver.get(f"{BASE_URL}/hovers")
    figures = WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.CLASS_NAME, "figure"))
    )
    actions = ActionChains(driver)
    actions.move_to_element(figures[0]).perform()

    caption = figures[0].find_element(By.CLASS_NAME, "figcaption")
    WebDriverWait(driver, 10).until(lambda d: caption.is_displayed())
    assert caption.is_displayed()
    print("Hover check passed")

    # Right-click and double-click are demonstrated on the same target.
    actions.context_click(figures[0]).perform()
    actions.double_click(figures[0]).perform()
    print("Right-click and double-click actions performed")


def test_drag_and_drop(driver):
    driver.get(f"{BASE_URL}/drag_and_drop")
    source = driver.find_element(By.ID, "column-a")
    target = driver.find_element(By.ID, "column-b")
    ActionChains(driver).drag_and_drop(source, target).perform()
    print("Drag-and-drop action performed; verify the displayed column labels")


def test_keyboard_actions(driver):
    driver.get(f"{BASE_URL}/key_presses")
    input_box = driver.find_element(By.ID, "target")
    input_box.send_keys("Selenium Testing")
    input_box.send_keys(Keys.CONTROL, "a")
    input_box.send_keys(Keys.BACKSPACE)
    input_box.send_keys(Keys.TAB)
    input_box.send_keys(Keys.ESCAPE)
    print("Keyboard actions performed")


def test_screenshot(driver):
    driver.get(f"{BASE_URL}/login")
    screenshot_path = SCREENSHOT_DIR / "login_page.png"
    saved = driver.save_screenshot(str(screenshot_path))
    assert saved, "Selenium could not save the screenshot"
    print(f"Screenshot saved to: {screenshot_path.resolve()}")


def test_browser_and_navigation(driver):
    driver.get(f"{BASE_URL}/login")
    driver.maximize_window()
    print("Title:", driver.title)
    print("URL:", driver.current_url)

    driver.get(f"{BASE_URL}/checkboxes")
    driver.back()
    print("After back:", driver.current_url)

    driver.forward()
    print("After forward:", driver.current_url)

    driver.refresh()
    print("Page refreshed")


def test_file_upload(driver):
    file_path = os.environ.get("SELENIUM_UPLOAD_FILE", "").strip().strip('"')
    if not file_path:
        raise SkipTest("Set SELENIUM_UPLOAD_FILE to a valid local file path to run upload")
    if not Path(file_path).is_file():
        raise AssertionError(f"Upload file does not exist: {file_path}")

    driver.get(f"{BASE_URL}/upload")
    upload_input = driver.find_element(By.ID, "file-upload")
    upload_input.send_keys(str(Path(file_path).resolve()))
    driver.find_element(By.ID, "file-submit").click()

    uploaded_name = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "uploaded-files"))
    )
    assert Path(file_path).name in uploaded_name.text
    print("File upload check passed")


def test_file_download(driver):
    driver.get(f"{BASE_URL}/download")
    before = set(os.listdir(DOWNLOAD_DIR))

    driver.find_element(By.CSS_SELECTOR, "#content a").click()

    # Poll for a new completed download rather than relying only on sleep().
    deadline = time.time() + 30
    downloaded_files = set()
    while time.time() < deadline:
        current = set(os.listdir(DOWNLOAD_DIR))
        completed = {
            name for name in current
            if not name.endswith(".crdownload")
        }
        downloaded_files = completed - before
        if downloaded_files:
            break
        time.sleep(0.5)

    assert downloaded_files, "No completed download was detected"
    print("Downloaded file(s):", sorted(downloaded_files))



class SkipTest(Exception):
    pass
    # Raised when a test needs optional setup that has not been provided.


TOPICS = [
    ("Login", test_login),
    ("Dropdowns", test_dropdown),
    ("Checkboxes", test_checkboxes),
    ("Radio buttons", test_radio_buttons),
    ("JavaScript alerts", test_alerts),
    ("Iframes", test_iframe),
    ("Windows and tabs", test_windows),
    ("Mouse actions", test_mouse_actions),
    ("Drag and drop", test_drag_and_drop),
    ("Keyboard actions", test_keyboard_actions),
    ("Screenshots", test_screenshot),
    ("Browser and navigation controls", test_browser_and_navigation),
    ("File upload", test_file_upload),
    ("File download", test_file_download),
]


def write_html_report(results):
    # Write a self-contained HTML summary after every test has finished.
    report_path = Path("selenium_test_report.html").resolve()
    counts = {status: sum(1 for result in results if result["status"] == status)
              for status in ("PASS", "FAIL", "SKIP")}

    def esc(value):
        return (str(value).replace("&", "&amp;").replace("<", "&lt;")
                .replace(">", "&gt;").replace('"', "&quot;"))

    rows = []
    for result in results:
        screenshot = result.get("screenshot")
        screenshot_html = esc(screenshot) if screenshot else "—"
        rows.append(
            "<tr>"
            f"<td>{esc(result['name'])}</td>"
            f"<td class='{result['status'].lower()}'>{result['status']}</td>"
            f"<td>{esc(result['duration'])} sec</td>"
            f"<td>{esc(result['details'])}</td>"
            f"<td>{screenshot_html}</td>"
            "</tr>"
        )

    html = f'''<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>Selenium Test Report</title>
<style>
body{{font-family:Arial,sans-serif;margin:28px;color:#222}} h1{{margin-bottom:6px}} .summary{{display:flex;gap:14px;flex-wrap:wrap;margin:22px 0}}
.card{{border:1px solid #ddd;border-radius:8px;padding:14px 22px;min-width:100px}} .pass{{color:#137333;font-weight:bold}} .fail{{color:#b3261e;font-weight:bold}} .skip{{color:#8a5a00;font-weight:bold}}
table{{border-collapse:collapse;width:100%}} th,td{{border:1px solid #ddd;padding:10px;text-align:left;vertical-align:top}} th{{background:#f3f4f6}} tr:nth-child(even){{background:#fafafa}} .note{{color:#555;margin-top:20px}}
</style></head><body>
<h1>Selenium Automation Test Report</h1><p>Generated after the complete test run.</p>
<div class="summary"><div class="card"><strong>Total</strong><h2>{len(results)}</h2></div>
<div class="card"><strong>Passed</strong><h2 class="pass">{counts['PASS']}</h2></div>
<div class="card"><strong>Failed</strong><h2 class="fail">{counts['FAIL']}</h2></div>
<div class="card"><strong>Skipped</strong><h2 class="skip">{counts['SKIP']}</h2></div></div>
<table><thead><tr><th>Test</th><th>Status</th><th>Duration</th><th>Details</th><th>Failure screenshot</th></tr></thead>
<tbody>{''.join(rows)}</tbody></table>
<p class="note">Failure screenshots, when available, are saved in the screenshots folder. Public practice websites may change or temporarily be unavailable.</p>
</body></html>'''
    report_path.write_text(html, encoding="utf-8")
    return report_path

#------------------------------------------------------------------------------------#


def main():
    print("\nSELENIUM AUTOMATION: RUNNING ALL TESTS")
    print("No menu selection is required. Please leave the run to finish.")
    results = []

    for number, (label, test_function) in enumerate(TOPICS, start=1):
        print(f"\n[{number}/{len(TOPICS)}] Running: {label}")
        started = time.time()
        driver = None
        status = "PASS"
        details = "Test completed successfully"
        screenshot = ""

        try:
            driver = start_browser()
            test_function(driver)
        except SkipTest as error:
            status = "SKIP"
            details = str(error)
            print(f"SKIPPED: {details}")
        except Exception as error:
            status = "FAIL"
            details = f"{type(error).__name__}: {error}"
            print(f"FAILED: {details}")
            if driver is not None:
                screenshot_path = SCREENSHOT_DIR / f"failed_{number:02d}.png"
                try:
                    if driver.save_screenshot(str(screenshot_path)):
                        screenshot = str(screenshot_path.resolve())
                        print(f"Failure screenshot: {screenshot}")
                except Exception as screenshot_error:
                    details += f" | Screenshot error: {screenshot_error}"
        finally:
            if driver is not None:
                try:
                    driver.quit()
                except Exception:
                    pass

        duration = round(time.time() - started, 2)
        results.append({"name": label, "status": status, "duration": duration,
                        "details": details, "screenshot": screenshot})
        print(f"Result: {status} ({duration} sec)")

    report_path = write_html_report(results)
    passed = sum(1 for result in results if result["status"] == "PASS")
    failed = sum(1 for result in results if result["status"] == "FAIL")
    skipped = sum(1 for result in results if result["status"] == "SKIP")
    print("\n========== FINAL SUMMARY ==========")
    print(f"Total: {len(results)} | Passed: {passed} | Failed: {failed} | Skipped: {skipped}")
    print(f"HTML report created: {report_path}")
    print("Open selenium_test_report.html in your browser to view the report.")


if __name__ == "__main__":
    main()
