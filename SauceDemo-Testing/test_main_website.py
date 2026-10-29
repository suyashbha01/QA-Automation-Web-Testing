import random
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
import pytest
import os
import time



@pytest.mark.testcase1
def test_products_page(logged_in_driver):
    driver = logged_in_driver
    wait = WebDriverWait(driver, 10)

    # Verify Products page title
    inventory_title = wait.until(
        EC.visibility_of_element_located((By.CLASS_NAME, "title"))
    )
    assert inventory_title.text == "Products"

    # Verify product list is visible
    product_list = wait.until(
        EC.visibility_of_element_located(
            (By.CSS_SELECTOR, '[data-test="inventory-list"]')
        )
    )
    assert product_list.is_displayed()

    # Verify Sauce Labs Backpack name
    product_name = wait.until(
        EC.visibility_of_element_located((By.ID, "item_4_title_link"))
    )
    assert product_name.text == "Sauce Labs Backpack"

    # Verify all six products are visible
    product_all_list = wait.until(
        EC.visibility_of_all_elements_located(
            (By.CSS_SELECTOR, '[data-test="inventory-item"]')
        )
    )
    assert len(product_all_list) == 6

    # Verify sorting dropdown

    product_dropdown = wait.until(
    EC.visibility_of_element_located(
        (By.CSS_SELECTOR, '[data-test="product-sort-container"]')
    )
)

    assert product_dropdown.is_displayed()
    print("PASS: Sorting dropdown is visible.")

    #sorting selection + Collect all product prices

    sort_dropdown = Select(product_dropdown)

    sort_dropdown.select_by_visible_text("Name (A to Z)")
    print("PASS: Name (A to Z) selected")

    product_dropdown = wait.until(
        EC.visibility_of_element_located(
            (By.CSS_SELECTOR, '[data-test="product-sort-container"]')
        )
    )
    sort_dropdown = Select(product_dropdown)

    # Collect all product prices

    product_price = driver.find_elements(
        By.CSS_SELECTOR, '[data-test="inventory-item-price"]'
    )

    prices = [price.text for price in product_price]

    print("product prices:", prices)

    sort_dropdown.select_by_visible_text("Name (Z to A)")
    print("PASS: Name (Z to A) selected")

    product_dropdown = wait.until(
        EC.visibility_of_element_located(
            (By.CSS_SELECTOR, '[data-test="product-sort-container"]')
        )
    )
    sort_dropdown = Select(product_dropdown)

    # Collect all product prices

    product_price = driver.find_elements(
        By.CSS_SELECTOR, '[data-test="inventory-item-price"]'
    )

    prices = [price.text for price in product_price]

    print("product prices:", prices)

    sort_dropdown.select_by_visible_text("Price (low to high)")
    print("PASS: Price (low to high) selected")

    product_dropdown = wait.until(
        EC.visibility_of_element_located(
            (By.CSS_SELECTOR, '[data-test="product-sort-container"]')
        )
    )
    sort_dropdown = Select(product_dropdown)

    # Collect all product prices

    product_price = driver.find_elements(
        By.CSS_SELECTOR, '[data-test="inventory-item-price"]'
    )

    prices = [price.text for price in product_price]

    print("product prices:", prices)

    sort_dropdown.select_by_visible_text("Price (high to low)")
    print("PASS: Price (high to low) selected")

    # Collect all product prices

    product_price = driver.find_elements(
        By.CSS_SELECTOR, '[data-test="inventory-item-price"]'
    )

    prices = [price.text for price in product_price]

    print("product prices:", prices)
    
#================================================================================#
#Add to cart with condictons

@pytest.mark.testcase2
def test_Addtocart_page(logged_in_driver):
    driver = logged_in_driver
    wait = WebDriverWait(driver, 10)

    Backpack_button = wait.until(
        EC.element_to_be_clickable(
            (By.CSS_SELECTOR, '[data-test="add-to-cart-sauce-labs-backpack"]')
        )
    )

    Backpack_button.click()

    product_name2 = wait.until(
        EC.element_to_be_clickable(
            (By.CSS_SELECTOR, '[data-test="add-to-cart-sauce-labs-bike-light"]')
        )
    )

    product_name2.click()



    cart_button = wait.until(
        EC.element_to_be_clickable(
            (By.CSS_SELECTOR, '[data-test="shopping-cart-link"]')
        )
    )

    cart_button.click()

    wait.until(
    EC.text_to_be_present_in_element(
        (By.CSS_SELECTOR, '[data-test="title"]'),
        "Your Cart"
        )
    )

    cart_heading = wait.until(
    EC.visibility_of_element_located(
        (By.CSS_SELECTOR, '[data-test="title"]')
        )
    )

    assert cart_heading.text == "Your Cart"

    product_name = wait.until(
        EC.visibility_of_all_elements_located(
            (By.CSS_SELECTOR, '[data-test="inventory-item-name"]')
        )
    )

    actual_names =  [product.text for product in product_name]

    assert "Sauce Labs Backpack" in actual_names
    assert "Sauce Labs Bike Light" in actual_names

    product_quanity = wait.until(
        EC.visibility_of_all_elements_located(
            (By.CSS_SELECTOR, '[data-test="item-quantity"]')
        )
    )

    actual_quantities = [quantity.text for quantity in product_quanity]
    assert actual_quantities == ["1", "1"]


    cart_button2 = wait.until(
        EC.visibility_of_element_located(
            (By.CSS_SELECTOR, '[data-test="shopping-cart-badge"]')
        )
    )

    assert cart_button2.text == "2"

    print("PASS: Both product names are correct.")
    print("PASS: Both product quantities are 1.")
    print("PASS: Cart badge count is 2.")
#===============================================================================#

@pytest.mark.testcase3
def test_random_add_to_cart(logged_in_driver):
    driver = (logged_in_driver)
    wait = WebDriverWait(driver, 10)

    #choose random product

    random_product = wait.until(
    EC.presence_of_all_elements_located(
        (By.CLASS_NAME, "btn_inventory")
        )
    )

    select_product = random.sample(random_product, 2)


    for product in select_product:
        product.click()

    addtocart = wait.until(
        EC.visibility_of_element_located(
            (By.CSS_SELECTOR, '[data-test="shopping-cart-badge"]')
        )
    )
    
    quanity = addtocart.text

    assert quanity == "2"
    
    print("PASS: 2 random product was added to the cart.")

#============================================================================#

@pytest.mark.testcase4
def test_remove_from_cart(logged_in_driver):
    driver = logged_in_driver
    wait = WebDriverWait(driver, 10)

    backpack_button = wait.until(
        EC.element_to_be_clickable(
            (By.CSS_SELECTOR, '[data-test="add-to-cart-sauce-labs-backpack"]')
        )
    )
    backpack_button.click()

    cart_badge = wait.until(
        EC.visibility_of_element_located(
            (By.CSS_SELECTOR, '[data-test="shopping-cart-badge"]')
        )
    )
    assert cart_badge.text == "1"

    remove_button = wait.until(
        EC.element_to_be_clickable(
            (By.CSS_SELECTOR, '[data-test="remove-sauce-labs-backpack"]')
        )
    )
    remove_button.click()

    wait.until(
        EC.invisibility_of_element_located(
            (By.CSS_SELECTOR, '[data-test="shopping-cart-badge"]')
        )
    )

    print("PASS: Product removed and cart badge disappeared.")

#========================================================================#

@pytest.mark.testcase5
def test_random_remove_from_cart(logged_in_driver):
    driver = logged_in_driver
    wait = WebDriverWait(driver, 10)

    random_product = wait.until(
        EC.presence_of_all_elements_located(
            (By.CLASS_NAME, "btn_inventory")
        )
    )

    select_product = random.sample(random_product, 2)

    for product in select_product:
        product.click()

    wait.until(
        EC.text_to_be_present_in_element(
            (By.CSS_SELECTOR, '[data-test="shopping-cart-badge"]'),
            "2"
        )
    )

    print("PASS: Two random products were added to the cart.")

    random_button = wait.until(
        EC.presence_of_all_elements_located(
            (By.CSS_SELECTOR, '[data-test^="remove-"]')
        )
    )

    random.choice(random_button).click()

    wait.until(
        EC.text_to_be_present_in_element(
            (By.CSS_SELECTOR, '[data-test="shopping-cart-badge"]'),
            "1"
        )
    )

    cart_badge = driver.find_element(
        By.CSS_SELECTOR, '[data-test="shopping-cart-badge"]'
    )

    assert cart_badge.text == "1"
    print("PASS: One random product was removed from the cart.")


#============================================================================#

@pytest.mark.testcase6
def test_checkout_from_validaction(logged_in_driver):
    driver = logged_in_driver
    wait = WebDriverWait(driver, 10)

    add_product = wait.until(
        EC.element_to_be_clickable(
            (By.CSS_SELECTOR, '[data-test="add-to-cart-sauce-labs-backpack"]')
        )
    )
    add_product.click()

    add_product2 = wait.until(
        EC.element_to_be_clickable(
            (By.CSS_SELECTOR, '[data-test="add-to-cart-sauce-labs-bike-light"]')
        )
    )
    add_product2.click()

    cart_button = wait.until(
        EC.element_to_be_clickable(
            (By.CSS_SELECTOR, '[data-test="shopping-cart-link"]')
        )
    )
    cart_button.click()

    cart_title = wait.until(
        EC.visibility_of_element_located(
            (By.CSS_SELECTOR, '[data-test="title"]')
        )
    )
    assert cart_title.text == "Your Cart"

    checkout_button = wait.until(
    EC.element_to_be_clickable(
        (By.CSS_SELECTOR, '[data-test="checkout"]')
    )
)

    checkout_button.click()

    wait.until(EC.url_contains("checkout-step-one.html"))

    checkout_title = wait.until(
    EC.visibility_of_element_located(
        (By.CSS_SELECTOR, '[data-test="title"]')
    )
)

    assert checkout_title.text == "Checkout: Your Information"

    

#============================================================================#


@pytest.mark.testcase7
def test_checkout_empty_fields(logged_in_driver):
    driver = logged_in_driver
    wait = WebDriverWait(driver, 15)

    # Add products to cart
    wait.until(
        EC.element_to_be_clickable(
            (By.CSS_SELECTOR, '[data-test="add-to-cart-sauce-labs-backpack"]')
        )
    ).click()

    wait.until(
        EC.element_to_be_clickable(
            (By.CSS_SELECTOR, '[data-test="add-to-cart-sauce-labs-bike-light"]')
        )
    ).click()

    # Open cart
    wait.until(
        EC.element_to_be_clickable(
            (By.CSS_SELECTOR, '[data-test="shopping-cart-link"]')
        )
    ).click()

    wait.until(
        EC.visibility_of_element_located(
            (By.CSS_SELECTOR, '[data-test="title"]')
        )
    )

    # Click Checkout
    checkout_button = wait.until(
    EC.element_to_be_clickable(
        (By.CSS_SELECTOR, '[data-test="checkout"]')
    )
)

    checkout_button.click()

    wait.until(EC.url_contains("checkout-step-one.html"))

    checkout_title = wait.until(
    EC.visibility_of_element_located(
        (By.CSS_SELECTOR, '[data-test="title"]')
    )
)

    assert checkout_title.text == "Checkout: Your Information"



#=================================================================#


@pytest.mark.testcase8
def test_final_page(logged_in_driver):
    driver = logged_in_driver
    wait = WebDriverWait(driver, 15)

    # Add product to cart
    wait.until(
        EC.element_to_be_clickable(
            (By.CSS_SELECTOR, '[data-test="add-to-cart-sauce-labs-backpack"]')
        )
    ).click()

    # Open cart
    wait.until(
        EC.element_to_be_clickable(
            (By.CSS_SELECTOR, '[data-test="shopping-cart-link"]')
        )
    ).click()

    # Click Checkout
    wait.until(
        EC.element_to_be_clickable(
            (By.CSS_SELECTOR, '[data-test="checkout"]')
        )
    ).click()

    # Enter checkout information
    first_name = wait.until(
        EC.visibility_of_element_located(
            (By.CSS_SELECTOR, '[data-test="firstName"]')
        )
    )
    first_name.send_keys("Suyash")

    last_name = wait.until(
        EC.visibility_of_element_located(
            (By.CSS_SELECTOR, '[data-test="lastName"]')
        )
    )
    last_name.send_keys("Bhargava")

    postal_code = wait.until(
        EC.visibility_of_element_located(
            (By.CSS_SELECTOR, '[data-test="postalCode"]')
        )
    )
    postal_code.send_keys("201301")

    # Verify values were entered
    assert first_name.get_attribute("value") == "Suyash"
    assert last_name.get_attribute("value") == "Bhargava"
    assert postal_code.get_attribute("value") == "201301"

    # Continue to checkout overview
    wait.until(
        EC.element_to_be_clickable(
            (By.CSS_SELECTOR, '[data-test="continue"]')
        )
    ).click()

    wait.until(
        EC.text_to_be_present_in_element(
            (By.CSS_SELECTOR, '[data-test="title"]'),
            "Checkout: Overview"
        )
    )

    title = driver.find_element(
        By.CSS_SELECTOR, '[data-test="title"]'
    )
    assert title.text == "Checkout: Overview"

    # Finish checkout
    wait.until(
        EC.element_to_be_clickable(
            (By.CSS_SELECTOR, '[data-test="finish"]')
        )
    ).click()

    # Verify successful checkout
    wait.until(
        EC.text_to_be_present_in_element(
            (By.CSS_SELECTOR, '[data-test="title"]'),
            "Checkout: Complete!"
        )
    )

    complete_title = driver.find_element(
        By.CSS_SELECTOR, '[data-test="title"]'
    )
    assert complete_title.text == "Checkout: Complete!"

    print("PASS: Checkout completed successfully.")


#================================================================#


@pytest.mark.testcase9
def test_slidebar_menu(logged_in_driver):
    driver = logged_in_driver
    wait = WebDriverWait(driver, 15)

    # Open sidebar
    slide_menu_button = wait.until(
        EC.element_to_be_clickable(
            (By.CSS_SELECTOR, "#react-burger-menu-btn")
        )
    )
    slide_menu_button.click()

    # Verify sidebar is visible
    slide_menu = wait.until(
        EC.visibility_of_element_located(
            (By.CSS_SELECTOR, ".bm-menu")
        )
    )
    assert slide_menu.is_displayed(), "Sidebar menu did not open"

    # Verify All Items
    all_items = wait.until(
        EC.visibility_of_element_located(
            (By.ID, "inventory_sidebar_link")
        )
    )
    assert all_items.text == "All Items"

    # Verify Dynamic Catalog
    dynamic_catalog = wait.until(
        EC.visibility_of_element_located(
            (By.ID, "dynamic_catalog_sidebar_link")
        )
    )
    assert "Dynamic Catalog" in dynamic_catalog.text

    # Open Dynamic Catalog if submenu is not visible
    lazy_load_xpath = "//*[normalize-space()='Lazy Load']"

    lazy_load_elements = driver.find_elements(
        By.XPATH, lazy_load_xpath
    )

    if not any(element.is_displayed() for element in lazy_load_elements):
        dynamic_catalog.click()

    # Verify all three submenu links are visible and clickable
    submenu_links = ["Lazy Load", "Spinner", "Slider"]

    for link_name in submenu_links:
        link = wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, f"//*[normalize-space()='{link_name}']")
            )
        )

        assert link.is_displayed(), (
            f"{link_name} is not visible"
        )
        assert link.is_enabled(), (
            f"{link_name} is not enabled"
        )

        print(f"PASS: {link_name} is visible and clickable")

    # Verify About
    about = wait.until(
        EC.visibility_of_element_located(
            (By.ID, "about_sidebar_link")
        )
    )
    assert about.is_displayed()

    # Verify Logout
    logout = wait.until(
        EC.visibility_of_element_located(
            (By.ID, "logout_sidebar_link")
        )
    )
    assert logout.is_displayed()

    # Verify Reset App State
    reset = wait.until(
        EC.visibility_of_element_located(
            (By.ID, "reset_sidebar_link")
        )
    )
    assert reset.is_displayed()

    print("PASS: Sidebar and all eight menu options verified.")

#======================================================================#

@pytest.mark.testcase10
def test_cross_X_button(logged_in_driver):
    driver = logged_in_driver
    wait = WebDriverWait(driver, 10)

    # Open sidebar
    slide_menu_button = wait.until(
        EC.element_to_be_clickable(
            (By.CSS_SELECTOR, "#react-burger-menu-btn")
        )
    )
    slide_menu_button.click()

    # Close sidebar using X button
    close_button = wait.until(
        EC.element_to_be_clickable(
            (By.ID, "react-burger-cross-btn")
        )
    )
    close_button.click()

    # Verify sidebar is closed
    wait.until(
        EC.invisibility_of_element_located(
            (By.CSS_SELECTOR, ".bm-menu")
        )
    )

    print("PASS: Sidebar closed successfully.")

#=======================================================================#

@pytest.mark.testcase11
def test_alliteam(logged_in_driver):
    driver = logged_in_driver
    wait = WebDriverWait(driver, 10)

    # Open sidebar
    wait.until(
        EC.element_to_be_clickable(
            (By.CSS_SELECTOR, "#react-burger-menu-btn")
        )
    ).click()

    # Click All Items
    all_Iteams = wait.until(
        EC.element_to_be_clickable(
            (By.CSS_SELECTOR, "[data-test='inventory-sidebar-link']")
        )
    )
    assert all_Iteams.is_displayed(), "All Items is not visible"
    all_Iteams.click()

    # Verify inventory page
    wait.until(EC.url_contains("inventory.html"))

    assert "inventory.html" in driver.current_url, \
        "All Items did not navigate to inventory page"

    products = wait.until(
        EC.visibility_of_all_elements_located(
            (By.CSS_SELECTOR, ".inventory_item")
        )
    )
    assert len(products) > 0, "No products are displayed"

#==========================================================================#

@pytest.mark.testcase12
def test_aboutus(logged_in_driver):
    driver = logged_in_driver
    wait = WebDriverWait(driver, 10)

    # Open sidebar
    wait.until(
        EC.element_to_be_clickable(
            (By.CSS_SELECTOR, "#react-burger-menu-btn")
        )
    ).click()

    verify_about = wait.until(
        EC.visibility_of_element_located(
            (By.CSS_SELECTOR, "[data-test='about-sidebar-link']")
        )
    )

    assert verify_about.is_displayed(), "About link is not visible"

    about_url = verify_about.get_attribute("href")

    assert about_url and "saucelabs.com" in about_url, \
        "About link does not point to Sauce Labs"

    print("PASS: About link points to Sauce Labs.")

#=====================================================================#

@pytest.mark.testcase13
def test_Reset_App_State(logged_in_driver):
    driver = logged_in_driver
    wait = WebDriverWait(driver, 10)

    # Add product to cart
    wait.until(
        EC.element_to_be_clickable(
            (By.CSS_SELECTOR, '[data-test="add-to-cart-sauce-labs-backpack"]')
        )
    ).click()

    # Verify cart badge
    wait.until(
        EC.visibility_of_element_located(
            (By.CSS_SELECTOR, "[data-test='shopping-cart-badge']")
        )
    )

    # Open sidebar
    wait.until(
        EC.element_to_be_clickable(
            (By.CSS_SELECTOR, "#react-burger-menu-btn")
        )
    ).click()

    Reset_App_State = wait.until(
        EC.element_to_be_clickable(
            (By.CSS_SELECTOR, "[data-test='reset-sidebar-link']")
        )
    )
    Reset_App_State.click()

    # Verify cart badge is removed
    wait.until(
        EC.invisibility_of_element_located(
            (By.CSS_SELECTOR, "[data-test='shopping-cart-badge']")
        )
    )

    assert "inventory.html" in driver.current_url, \
        "Reset App State did not keep the inventory page open"

    print("PASS: App state was reset.")

#========================================================================#

@pytest.mark.testcase14
def test_logout(logged_in_driver):
    driver = logged_in_driver
    wait = WebDriverWait(driver, 15)

    # Open sidebar
    wait.until(
        EC.element_to_be_clickable(
            (By.CSS_SELECTOR, "#react-burger-menu-btn")
        )
    ).click()

    logout = wait.until(
        EC.element_to_be_clickable(
            (By.CSS_SELECTOR, "[data-test='logout-sidebar-link']")
        )
    )

    assert logout.is_displayed(), "Logout is not visible"
    logout.click()

    # Verify login page
    wait.until(
        EC.visibility_of_element_located(
            (By.ID, "user-name")
        )
    )

    assert driver.find_element(
        By.ID, "user-name"
    ).is_displayed(), "Logout did not return to the login page"

    assert driver.find_element(
        By.ID, "login-button"
    ).is_displayed(), "Login button is not visible after logout"

    print("PASS: Logout completed successfully.")





