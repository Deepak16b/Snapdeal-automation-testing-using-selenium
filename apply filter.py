from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException

# Specify the path to your ChromeDriver
chrome_driver_path = r"C:\Users\deepa\Downloads\chromedriver-win64\chromedriver-win64\chromedriver.exe"

chrome_service = ChromeService(executable_path=chrome_driver_path)
chrome_options = Options()

driver = webdriver.Chrome(service=chrome_service, options=chrome_options)

def test_filter_category():
    driver.get('https://www.snapdeal.com')

    # Close any pop-up if it appears (adjust the selector if needed)
    try:
        close_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), '✕')]"))
        )
        close_button.click()
        print("Popup closed.")
    except TimeoutException:
        print("Popup did not appear or could not be closed.")
    except NoSuchElementException:
        print("Close button not found.")

    # Find the search bar and enter the search query (update the selector as needed)
    try:
        search_bar = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, 'inputValEnter'))
        )
        search_bar.send_keys('clothes')
        search_bar.send_keys(Keys.RETURN)
        print("Search bar found and query entered.")
    except NoSuchElementException:
        print("Search bar not found.")
        driver.quit()
        return

    # Wait for and click on the "Sports Wear For Men" category using the catid
    try:
        sports_wear_category = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, f'[catid="109"]'))
        )
        sports_wear_category.click()
        print("Sports Wear For Men category clicked.")
    except TimeoutException:
        print("Sports Wear For Men category not found.")
        driver.quit()
        return
    except NoSuchElementException:
        print("Sports Wear For Men category not found.")
        driver.quit()
        return

    # Check for filtered results (modify the selector as needed)
    try:
        filtered_results = WebDriverWait(driver, 20).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, '.product-tuple-listing'))
        )
        assert len(filtered_results) > 0, "No filtered results found."
        print("Test Passed: Category filter applied and results are displayed.")
    except TimeoutException:
        print("Test Failed: Filtered results did not load in time.")
        print(driver.page_source)  # Print the page source for debugging
    except AssertionError as e:
        print(f"Test Failed: {e}")
        print(driver.page_source)  # Print the page source for debugging

    # Close the browser after the test
    driver.quit()

# Run the test case
test_filter_category()
