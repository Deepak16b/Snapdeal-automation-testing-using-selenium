from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException


def test_add_to_cart():
    # Specify the path to your ChromeDriver
    chrome_driver_path = r"C:\Users\deepa\Downloads\chromedriver-win64\chromedriver-win64\chromedriver.exe"

    # Set up the Chrome WebDriver
    chrome_service = ChromeService(executable_path=chrome_driver_path)
    chrome_options = Options()
    driver = webdriver.Chrome(service=chrome_service, options=chrome_options)

    try:
        driver.get('https://www.snapdeal.com')

        try:
            # Search for a product
            search_bar = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.NAME, 'keyword'))
            )
            search_term = 'shoes men'
            search_bar.send_keys(search_term)
            search_bar.send_keys(Keys.RETURN)
            print("Search performed.")
        except TimeoutException:
            print("TimeoutException: Search bar did not appear.")
            driver.quit()
            return
        except NoSuchElementException:
            print("Search bar not found.")
            driver.quit()
            return

        try:
            # Wait for search results and click on the first product
            product = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, '.product-tuple-listing .product-desc-rating'))
            )
            product.click()
            print("Product clicked.")
        except TimeoutException:
            print("TimeoutException: Product did not appear or could not be clicked.")
            driver.quit()
            return
        except NoSuchElementException:
            print("Product not found.")
            driver.quit()
            return

        # Switch to the new tab (product details page)
        driver.switch_to.window(driver.window_handles[1])

        try:
            # Add to Cart
            add_to_cart_button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.ID, 'add-cart-button-id'))
            )
            add_to_cart_button.click()
            print("Add to cart button clicked.")
        except TimeoutException:
            print("TimeoutException: Add to cart button did not appear or could not be clicked.")
            driver.quit()
            return
        except NoSuchElementException:
            print("Add to cart button not found.")
            driver.quit()
            return

        try:
            # Verify the product is added to the cart
            cart_icon = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, '.cartQuantity'))
            )
            cart_quantity = cart_icon.text
            assert cart_quantity == '1', f"Expected cart quantity to be 1, but got {cart_quantity}"

            print("Test Passed: Product is added to the cart.")
        except TimeoutException:
            print("TimeoutException: Cart quantity did not appear in time.")
        except NoSuchElementException:
            print("Cart quantity not found.")
        except AssertionError as e:
            print(f"Test Failed: {e}")
    finally:
        driver.quit()
        print("Browser closed.")


# Run the test
test_add_to_cart()
