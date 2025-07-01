from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, ElementClickInterceptedException
import time


def test_add_to_cart():
    # Specify the path to your ChromeDriver
    chrome_driver_path = r"C:\Users\deepa\Downloads\chromedriver-win64\chromedriver-win64\chromedriver.exe"
    # Set up the Chrome WebDriver
    chrome_service = ChromeService(executable_path=chrome_driver_path)
    chrome_options = Options()
    driver = webdriver.Chrome(service=chrome_service, options=chrome_options)

    try:
        driver.get('https://www.snapdeal.com')

        # Search for a product
        search_bar = driver.find_element(By.NAME, 'keyword')
        search_term = 'shoes men'
        search_bar.send_keys(search_term)
        search_bar.send_keys(Keys.RETURN)

        # Wait for search results and click on the first product
        product = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, '.product-tuple-listing .product-desc-rating'))
        )
        product.click()

        # Switch to the new tab (product details page)
        driver.switch_to.window(driver.window_handles[1])

        # Add to Cart
        add_to_cart_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, 'add-cart-button-id'))
        )
        add_to_cart_button.click()

        # Click "View Cart"
        view_cart_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CLASS_NAME, 'btn.btn-theme-secondary.open-cart'))
        )
        view_cart_button.click()

        # Wait for a few seconds to ensure the cart page loads completely
        print("Waiting for the cart page to load...")
        time.sleep(5)  # Adjust the sleep time if needed

        # Verify the product is added to the cart
        cart_icon = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '.cartQuantity'))
        )
        cart_quantity = cart_icon.text
        assert cart_quantity == '1', f"Expected cart quantity to be 1, but got {cart_quantity}"

        if cart_quantity == '1':
            print("Test Passed: Product is added to the cart and viewed successfully.")
        else:
            print("Test Failed: Cart quantity is incorrect.")

        # Click "Remove" button
        print("Attempting to click the 'Remove' button...")
        try:
            remove_button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.CLASS_NAME, 'remove-item-shortlist'))
            )
            driver.execute_script("arguments[0].scrollIntoView(true);", remove_button)
            time.sleep(1)  # Allow some time for scrolling
            remove_button.click()
            print("Remove button clicked.")
        except (ElementClickInterceptedException, TimeoutException):
            print("Remove button is not clickable or found.")
            driver.quit()
            return

        # Verify the cart is empty
        print("Waiting for the item to be removed from the cart...")
        time.sleep(5)  # Adjust the sleep time if needed
        try:
            empty_cart_message = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, '.cart-heading.clearfix'))
            )
            assert len(empty_cart_message.text) > 0, "Test case failed: Empty cart message not found."
            print("Test case passed: Empty cart message found.")
        except TimeoutException:
            cart_quantity = driver.find_element(By.CSS_SELECTOR, '.cartQuantity').text
            if cart_quantity == '1':
                print("Test Failed: Cart is not empty.")
            else:
                print("Test Passed: Cart is empty.")

    except TimeoutException:
        print("TimeoutException: Operation took too long.")
    finally:
        driver.quit()


# Run the test
test_add_to_cart()
