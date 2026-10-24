from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import os
import time

# 1. Start Chrome
driver = webdriver.Chrome()

# 2. Create explicit wait
wait = WebDriverWait(driver, 10)

# 3. Open Web page
driver.get("https://the-internet.herokuapp.com/login")



# 4. Find username field
username = driver.find_element(By.ID, "username")

# 5. Enter wrong username, clear it, then enter correct username
username.send_keys("wronguser")
username.clear()

# 6. Read the HTML attribute
print(username.get_attribute("type"))

username.send_keys("tomsmith")


# 7. Find password field
password = driver.find_element(By.ID, "password")
password.send_keys("SuperSecretPassword!")


# 8. Wait until Login button is clickable
login_button = wait.until(
    EC.element_to_be_clickable(
        (By.CSS_SELECTOR, ".radius[type='submit']")
    )
)

# 9. Click Login
login_button.click()


# 10. Wait until Secure Area is visible
secure_area = wait.until(
    EC.visibility_of_element_located((By.TAG_NAME, "h2"))
)

# 11. Read and validate Secure Area text
print(secure_area.text)
assert secure_area.text == "Secure Area"

# 12. Validate page title
assert driver.title == "The Internet"

print("Test passed")


driver = webdriver.Chrome()
wait = WebDriverWait(driver, 10)

# ==================================================
# DROPDOWN
# ==================================================

driver.get("https://the-internet.herokuapp.com/dropdown")

dropdown_element = wait.until(
    EC.presence_of_element_located((By.ID, "dropdown"))
)

dropdown = Select(dropdown_element)

# Select by value
dropdown.select_by_value("2")
print(dropdown.first_selected_option.text)

# Select by visible text
dropdown.select_by_visible_text("Option 1")
print(dropdown.first_selected_option.text)

# Select by index
dropdown.select_by_index(1)
print(dropdown.first_selected_option.text)


# ==================================================
# CHECKBOXES
# ==================================================

driver.get("https://the-internet.herokuapp.com/checkboxes")

checkboxes = wait.until(
    EC.presence_of_all_elements_located(
        (By.CSS_SELECTOR, "input[type='checkbox']")
    )
)

# Check initial state
print(checkboxes[0].is_selected())
print(checkboxes[1].is_selected())

# Select checkbox 1
checkboxes[0].click()

# Verify selected
print(checkboxes[0].is_selected())

# Unselect checkbox 1
checkboxes[0].click()

# Verify unselected
print(checkboxes[0].is_selected())



# ==================================================
# RADIO BUTTONS
# ==================================================

driver.get("https://www.w3schools.com/html/html_forms.asp")

radio_buttons = driver.find_elements(
    By.CSS_SELECTOR, "input[type='radio']"
)

print(len(radio_buttons))

# Select HTML
driver.execute_script("arguments[0].click();", radio_buttons[0])

print(radio_buttons[0].is_selected())

# Select CSS
driver.execute_script("arguments[0].click();", radio_buttons[1])

print(radio_buttons[0].is_selected())
print(radio_buttons[1].is_selected())

# Select JavaScript
javascript_radio = driver.find_element(By.ID, "javascript")

javascript_radio.click()

print(javascript_radio.is_selected())

# ==================================================
# ALERTS
# ==================================================

driver.get("https://the-internet.herokuapp.com/javascript_alerts")

# Click the JS Alert button
alert_button = driver.find_element(
    By.XPATH, "//button[text()='Click for JS Alert']"
)

alert_button.click()

# Switch to the alert
alert = driver.switch_to.alert

# Print alert message
print(alert.text)

# Accept the alert
alert.accept()

# ==================================================
# JS CONFIRM
# ==================================================

confirm_button = driver.find_element(
    By.XPATH, "//button[text()='Click for JS Confirm']"
)

confirm_button.click()

confirm_alert = driver.switch_to.alert

print(confirm_alert.text)

confirm_alert.dismiss()



# ==================================================
# JS PROMPT
# ==================================================

prompt_button = driver.find_element(
    By.XPATH, "//button[text()='Click for JS Prompt']"
)

prompt_button.click()

prompt_alert = driver.switch_to.alert

print(prompt_alert.text)

prompt_alert.send_keys("Suyash")
prompt_alert.accept()

result = driver.find_element(By.ID, "result")

print(result.text)

assert result.text == "You entered: Suyash"


# ==================================================
# IFRAMES
# ==================================================

driver.get("https://the-internet.herokuapp.com/iframe")

iframe = driver.find_element(By.ID, "mce_0_ifr")

driver.switch_to.frame(iframe)

editor = driver.find_element(By.ID, "tinymce")

# Put text inside the editor
driver.execute_script(
    "arguments[0].innerHTML = 'Selenium iframe practice';",
    editor
)

# Verify the text
print(editor.get_attribute("innerHTML"))

# Switch back to the main page
driver.switch_to.default_content()

# ==================================================
# WINDOWS / TABS
# ==================================================

driver.get("https://the-internet.herokuapp.com/windows")

# Current window ID
main_window = driver.current_window_handle
print(main_window)

# All currently open windows
windows = driver.window_handles
print(windows)

# Find and click the link that opens a new window
new_window_link = driver.find_element(
    By.CSS_SELECTOR, "a[href='/windows/new']"
)

new_window_link.click()

# Get all windows again
windows = driver.window_handles
print(windows)

#Switch to the new window 

driver.switch_to.window(windows[1])

print(driver.current_window_handle)
print(driver.title)

#Verify new window

# Switch to the new window
driver.switch_to.window(windows[1])

print(driver.current_window_handle)
print(driver.title)

# Verify new window
new_window_heading = driver.find_element(By.TAG_NAME, "h3")

print(new_window_heading.text)

assert new_window_heading.text == "New Window"

# Switch back to the original window
driver.switch_to.window(main_window)

print(driver.current_window_handle)
print(driver.title)

# Close the current window
#driver.close()

# Quit the entire browser session
#driver.quit()

# ==================================================
# MOUSE ACTIONS
# ==================================================

driver = webdriver.Chrome()

driver.get("https://the-internet.herokuapp.com/hovers")

user_image = driver.find_elements(
    By.CLASS_NAME, "figure"
)[0]

actions = ActionChains(driver)

actions.move_to_element(user_image).perform()

hover_text = driver.find_element(
    By.CLASS_NAME, "figcaption"
)

print(hover_text.text)

# Right-click on the image
actions.context_click(user_image).perform()

# Double-click
actions.double_click(user_image).perform()


# ==================================================
# DRAG AND DROP
# ==================================================

driver.get("https://the-internet.herokuapp.com/drag_and_drop")

source = driver.find_element(By.ID, "column-a")
target = driver.find_element(By.ID, "column-b")

actions = ActionChains(driver)

actions.drag_and_drop(source, target).perform()

# ==================================================
# KEYBOARD ACTIONS
# ==================================================

from selenium.webdriver.common.keys import Keys

driver.get("https://the-internet.herokuapp.com/key_presses")

input_box = driver.find_element(By.ID, "target")

# Type text
input_box.send_keys("Selenium Testing")

# Select all text
input_box.send_keys(Keys.CONTROL, "a")

# Delete selected text
input_box.send_keys(Keys.BACKSPACE)

print("Keyboard actions completed")


# ==================================================
# KEYBOARD SHORTCUTS
# ==================================================

driver.get("https://the-internet.herokuapp.com/login")

username = driver.find_element(By.ID, "username")

username.send_keys("Selenium Testing")

# Select all text
username.send_keys(Keys.CONTROL, "a")

print("Text selected")


# Copy selected text
username.send_keys(Keys.CONTROL, "c")

# Clear the field
username.clear()

# Paste the copied text
username.send_keys(Keys.CONTROL, "v")

print(username.get_attribute("value"))


# ==================================================
# SCREENSHOTS
# ==================================================

driver.get("https://the-internet.herokuapp.com/login")

driver.save_screenshot("login_page.png")

print("Screenshot saved successfully")

driver.save_screenshot("login_page.png")

# Take screenshot when a test fails

try:
    username = driver.find_element(By.ID, "username")
    username.send_keys("Suyash")

    assert username.get_attribute("value") == "Wrong Value"

except AssertionError:
    driver.save_screenshot("login_test_failed.png")
    print("Test failed - screenshot saved")


# ==================================================
# BROWSER CONTROLS
# ==================================================

#driver = webdriver.Chrome()

#driver.get("https://the-internet.herokuapp.com/login")

# Maximize
#driver.maximize_window()
#print("Browser maximized")

# Minimize
#driver.minimize_window()
#print("Browser minimized")

# Fullscreen
#driver.fullscreen_window()
#print("Browser fullscreen")

# ==================================================
# NAVIGATION CONTROLS
# ==================================================

driver.get("https://the-internet.herokuapp.com/login")

# Go to another page
driver.get("https://the-internet.herokuapp.com/checkboxes")

# Go back
driver.back()
print("Current URL:", driver.current_url)

# Go forward
driver.forward()
print("Current URL:", driver.current_url)

# Refresh the page
driver.refresh()
print("Page refreshed")

print("Page title:", driver.title)


# ==================================================
# FILE DOWNLOAD
# ==================================================

download_folder = os.path.join(os.getcwd(), "downloads")

options = webdriver.ChromeOptions()

prefs = {
    "download.default_directory": download_folder,
    "download.prompt_for_download": False,
    "download.directory_upgrade": True
}

options.add_experimental_option("prefs", prefs)

driver.quit()

driver = webdriver.Chrome(options=options)

driver.get("https://the-internet.herokuapp.com/download")

print("Download page opened")


# Find the first download link
download_link = driver.find_element(By.CSS_SELECTOR, "#content a")

# Click download
download_link.click()

print("Download started")

# Wait for download to finish
time.sleep(3)

# Check downloaded files
files = os.listdir(download_folder)

print("Downloaded files:", files)

assert len(files) > 0, "Download failed - no file found"

print("Download verified successfully")


driver.quit()
