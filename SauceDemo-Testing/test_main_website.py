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

    cart_remove = wait.until(
        EC.visibility_of_element_located(
            (By.CSS_SELECTOR, '[data-test="shopping-cart-badge"]')
        )
    )
    quanity = cart_remove.text

    assert quanity == "1"

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

    cart_badge = wait.until(
        EC.visibility_of_element_located(
            (By.CSS_SELECTOR, '[data-test="shopping-cart-badge"]')
        )
    )

    assert cart_badge.text == "2"

    print("PASS: Two random products were added to the cart.")

    random_button = wait.until(
        EC.presence_of_all_elements_located(
            (By.CSS_SELECTOR, '[data-test^="remove-"]')
        )
    )

    random_remove = random.choice(random_button)
    random_remove.click()

    cart_badge = wait.until(
        EC.visibility_of_element_located(
            (By.CSS_SELECTOR, '[data-test="shopping-cart-badge"]')
        )
    )

    quanity = cart_badge.text

    assert quanity == "1"

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

    wait.until(
    EC.url_contains("cart.html")
    )

    wait.until(
        EC.text_to_be_present_in_element(
            (By.CSS_SELECTOR, '[data-test="title"]'),
            "Your Cart"
        )
    )

    verify_cart = wait.until(
        EC.visibility_of_element_located(
            (By.CSS_SELECTOR, '[data-test="title"]')
        )
    )

    check = verify_cart.text
    assert check == "Your Cart"

    checkout_button = wait.until(
        EC.element_to_be_clickable(
            (By.CSS_SELECTOR, '[data-test="checkout"]')
        )
    )

    checkout_button.click()

    validate = wait.until(
        EC.visibility_of_element_located(
            (By.CSS_SELECTOR, '[data-test="title"]')
        )
    )

    assert validate.text == "Checkout: Your Information"

    print("PASS: Checkout information page opened.")

    

#============================================================================#


@pytest.mark.testcase7
def test_checkout_empty_fields(logged_in_driver):
    driver = logged_in_driver
    wait = WebDriverWait(driver, 10)

    # Add products to cart
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

    # Open cart
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

    # Click Checkout
    checkout_button = wait.until(
        EC.element_to_be_clickable(
            (By.CSS_SELECTOR, '[data-test="checkout"]')
        )
    )
    checkout_button.click()

    wait.until(
        EC.text_to_be_present_in_element(
            (By.CSS_SELECTOR, '[data-test="title"]'),
            "Checkout: Your Information"
        )
    )
    print("PASS: Checkout information page opened.")

    # Locate Continue button
    check_button = wait.until(
        EC.element_to_be_clickable(
            (By.CSS_SELECTOR, '[data-test="continue"]')
        )
    )

    # Test 1: All fields are empty
    check_button.click()

    wait.until(
        EC.text_to_be_present_in_element(
            (By.CSS_SELECTOR, '[data-test="error"]'),
            "Error: First Name is required"
        )
    )

    error_message = driver.find_element(
        By.CSS_SELECTOR, '[data-test="error"]'
    )
    assert error_message.text == "Error: First Name is required"
    print("PASS: First Name is required.")

    driver.find_element(
        By.CSS_SELECTOR, '[data-test="error-button"]'
    ).click()

    # Test 2: First Name is filled, but Last Name is empty
    first_name = wait.until(
        EC.element_to_be_clickable(
            (By.CSS_SELECTOR, '[data-test="firstName"]')
        )
    )
    first_name.clear()
    first_name.send_keys("Suyash")

    wait.until(
        lambda d: d.find_element(
            By.CSS_SELECTOR, '[data-test="firstName"]'
        ).get_attribute("value") == "Suyash"
    )
    print("First Name entered:", first_name.get_attribute("value"))

    check_button = wait.until(
        EC.element_to_be_clickable(
            (By.CSS_SELECTOR, '[data-test="continue"]')
        )
    )
    check_button.click()

    wait.until(
        EC.text_to_be_present_in_element(
            (By.CSS_SELECTOR, '[data-test="error"]'),
            "Error: Last Name is required"
        )
    )

    error_message = driver.find_element(
        By.CSS_SELECTOR, '[data-test="error"]'
    )
    assert error_message.text == "Error: Last Name is required"
    print("PASS: Last Name is required.")

    driver.find_element(
        By.CSS_SELECTOR, '[data-test="error-button"]'
    ).click()

    # Test 3: First Name and Last Name are filled, but Postal Code is empty
    last_name = wait.until(
        EC.element_to_be_clickable(
            (By.CSS_SELECTOR, '[data-test="lastName"]')
        )
    )
    last_name.clear()
    last_name.send_keys("Bhargava")

    wait.until(
        lambda d: d.find_element(
            By.CSS_SELECTOR, '[data-test="lastName"]'
        ).get_attribute("value") == "Bhargava"
    )
    print("Last Name entered:", last_name.get_attribute("value"))

    check_button = wait.until(
        EC.element_to_be_clickable(
            (By.CSS_SELECTOR, '[data-test="continue"]')
        )
    )
    check_button.click()

    wait.until(
        EC.text_to_be_present_in_element(
            (By.CSS_SELECTOR, '[data-test="error"]'),
            "Error: Postal Code is required"
        )
    )

    error_message = driver.find_element(
        By.CSS_SELECTOR, '[data-test="error"]'
    )
    assert error_message.text == "Error: Postal Code is required"
    print("PASS: Postal Code is required.")

    driver.find_element(
        By.CSS_SELECTOR, '[data-test="error-button"]'
    ).click()

    # Enter Postal Code
    postal_code = wait.until(
        EC.element_to_be_clickable(
            (By.CSS_SELECTOR, '[data-test="postalCode"]')
        )
    )
    postal_code.clear()
    postal_code.send_keys("201005")

    wait.until(
        lambda d: d.find_element(
            By.CSS_SELECTOR, '[data-test="postalCode"]'
        ).get_attribute("value") == "201005"
    )
    print("Postal Code entered:", postal_code.get_attribute("value"))

    # Continue to Checkout Overview
    check_button = wait.until(
        EC.element_to_be_clickable(
            (By.CSS_SELECTOR, '[data-test="continue"]')
        )
    )
    check_button.click()

    wait.until(
        EC.text_to_be_present_in_element(
            (By.CSS_SELECTOR, '[data-test="title"]'),
            "Checkout: Overview"
        )
    )

    overview_title = driver.find_element(
        By.CSS_SELECTOR, '[data-test="title"]'
    )
    assert overview_title.text == "Checkout: Overview"
    print("PASS: Redirected to Checkout Overview.")

    # Verify product names
    overview_products = wait.until(
        EC.visibility_of_all_elements_located(
            (By.CSS_SELECTOR, '[data-test="inventory-item-name"]')
        )
    )

    product_names = [product.text for product in overview_products]

    assert "Sauce Labs Backpack" in product_names
    assert "Sauce Labs Bike Light" in product_names
    assert len(overview_products) == 2
    print("PASS: Both products are displayed.")

    # Verify product prices
    price_check = wait.until(
        EC.visibility_of_all_elements_located(
            (By.CSS_SELECTOR, '[data-test="inventory-item-price"]')
        )
    )

    assert price_check[0].text == "$29.99"
    assert price_check[1].text == "$9.99"
    print("PASS: Both product prices are correct.")

    # Verify item subtotal
    item_total = wait.until(
        EC.visibility_of_element_located(
            (By.CSS_SELECTOR, '[data-test="subtotal-label"]')
        )
    )
    assert item_total.text == "Item total: $39.98"
    print("Item Total:", item_total.text)

    # Verify tax
    verify_tax = wait.until(
        EC.visibility_of_element_located(
            (By.CSS_SELECTOR, '[data-test="tax-label"]')
        )
    )
    assert verify_tax.text == "Tax: $3.20"
    print("Tax:", verify_tax.text)

    # Verify final total
    final_total = wait.until(
        EC.visibility_of_element_located(
            (By.CSS_SELECTOR, '[data-test="total-label"]')
        )
    )
    assert final_total.text == "Total: $43.18"
    print("Final Total:", final_total.text)


#=================================================================#
@pytest.mark.testcase8
def test_final_page(logged_in_driver):

    driver = logged_in_driver
    wait = WebDriverWait(driver, 10)

    # Add product to cart
    add_product = wait.until(
    EC.element_to_be_clickable(
        (By.CSS_SELECTOR, '[data-test="add-to-cart-sauce-labs-backpack"]')
        )
    )
    add_product.click()

# Open cart
    cart_button = wait.until(
    EC.element_to_be_clickable(
        (By.CSS_SELECTOR, '[data-test="shopping-cart-link"]')
        )
    )
    cart_button.click()

# Click Checkout
    checkout_button = wait.until(
    EC.element_to_be_clickable(
        (By.CSS_SELECTOR, '[data-test="checkout"]')
        )
    )
    checkout_button.click()

# Enter checkout information
    wait.until(
    EC.visibility_of_element_located(
        (By.CSS_SELECTOR, '[data-test="firstName"]')
        )
    ).send_keys("Suyash")

    driver.find_element(By.CSS_SELECTOR, '[data-test="lastName"]').send_keys("Bhargava")
    driver.find_element(By.CSS_SELECTOR, '[data-test="postalCode"]').send_keys("201005")

# Click Continue
    driver.find_element(By.CSS_SELECTOR, '[data-test="continue"]').click()

# Click Finish
    finish_button = wait.until(
    EC.element_to_be_clickable(
        (By.CSS_SELECTOR, '[data-test="finish"]')
        )
    )
    finish_button.click()

    #verify the thank you message

    verify_message = wait.until(
        EC.visibility_of_element_located(
            (By.CSS_SELECTOR, '[data-test="complete-header"]')
        )
    )

    assert verify_message.text == "Thank you for your order!"
    print("PASS: Thank You message is correct. ")

    #verify genrate PDF

    verify_genrate_pdf = wait.until(
        EC.visibility_of_element_located(
            (By.CSS_SELECTOR, '[data-test="generate-pdf-order"]')
        )
    )

    assert verify_genrate_pdf.is_displayed()
    assert verify_genrate_pdf.text == "Generate PDF order"
    print("PASS: Generate PDF order button is visible.")


    verify_genrate_pdf_button = wait.until(
        EC.element_to_be_clickable(
            (By.CSS_SELECTOR, '[data-test="generate-pdf-order"]')
        )
    )

    assert verify_genrate_pdf_button.text == "Generate PDF order"
    print("PASS: Generate PDF order button is visible.")

    verify_genrate_pdf_button.click()
    
    download_path = os.path.join(os.path.expanduser("~"), "Downloads")

    pdf_files_before = {
    file for file in os.listdir(download_path)
    if file.lower().endswith(".pdf")
    
    }

    verify_genrate_pdf_button.click()

    # Verify PDF download
    timeout = time.time() + 20
    new_pdf_files = set()

    while time.time() < timeout:
        pdf_files_after = {
        file for file in os.listdir(download_path)
        if file.lower().endswith(".pdf")
        and not file.lower().endswith(".crdownload")
    }

        new_pdf_files = pdf_files_after - pdf_files_before

        if new_pdf_files:
            break

        time.sleep(1)

    assert new_pdf_files, "FAIL: PDF file was not downloaded."

    print("PASS: PDF downloaded successfully:", new_pdf_files)


    back_button_flow = wait.until(
        EC.element_to_be_clickable(
            (By.CSS_SELECTOR, '[data-test="back-to-products"]')
        )
    )

    assert back_button_flow.text == "Back Home"
    print("PASS: Back Home button is visible.")
    back_button_flow.click()


    inventory_title = wait.until(
        EC.visibility_of_element_located(
            (By.CSS_SELECTOR,'[data-test="title"]')
        )
    )

    assert inventory_title.text == "Products"
    print("PASS: Back Home returned to the Products page.")

    









    
