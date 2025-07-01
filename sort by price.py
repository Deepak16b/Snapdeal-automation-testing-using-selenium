from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time

# Specify the path to your ChromeDriver
chrome_driver_path = r"C:\Users\deepa\Downloads\chromedriver-win64\chromedriver-win64\chromedriver.exe"

# Set up the Chrome WebDriver
chrome_service = ChromeService(executable_path=chrome_driver_path)
chrome_options = Options()

driver = webdriver.Chrome(service=chrome_service, options=chrome_options)

def test_sort_by_price_low_to_high():
    driver.get('https://www.snapdeal.com')

    # Close any pop-up if it appears
    try:
        close_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), '✕')]"))
        )
        close_button.click()
    except TimeoutException:
        print("Popup did not appear or could not be closed.")

    # Locate the search bar and perform a search
    search_bar = driver.find_element(By.ID, 'inputValEnter')
    search_bar.send_keys('clothes')
    search_bar.send_keys(Keys.RETURN)

    try:
        # Wait for the search results to load
        search_results = WebDriverWait(driver, 20).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, '.product-tuple-listing'))
        )
        assert len(search_results) > 0, "No search results found."
        print("Test Passed: Search results are displayed.")
    except TimeoutException:
        print("Test Failed: Search results did not load in time.")
    except AssertionError as e:
        print(f"Test Failed: {e}")
        return

    try:
        # Wait for the sort by option to be clickable and click on it
        sort_by = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.CLASS_NAME, 'sort-label'))
        )
        sort_by.click()
    except TimeoutException:
        print("Test Failed: Sort by option did not appear in time.")
        return

    try:
        # Wait for the "Price Low To High" option to be clickable and click on it
        price_low_to_high = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//li[@data-sorttype='plth']"))
        )
        price_low_to_high.click()
    except TimeoutException:
        print("Test Failed: 'Price Low To High' option did not appear in time.")
        return

    # Wait for a few seconds to allow the sorted results to load
    time.sleep(5)

    try:
        # Wait for the sorted results to load
        sorted_results = WebDriverWait(driver, 20).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, '.product-tuple-listing'))
        )
        assert len(sorted_results) > 0, "No sorted results found."
        print("Test Passed: Sorted results are displayed.")
    except TimeoutException:
        print("Test Failed: Sorted results did not load in time.")
    except AssertionError as e:
        print(f"Test Failed: {e}")

# Run the test case
test_sort_by_price_low_to_high()

# Close the browser
driver.quit()
