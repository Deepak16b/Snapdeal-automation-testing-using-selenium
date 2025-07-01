from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

# Specify the path to your ChromeDriver
chrome_driver_path = r"C:/Users/deepa/Downloads/chrome-win64/chrome-win64/chrome.exe"

chrome_service = ChromeService(executable_path=chrome_driver_path)
chrome_options = Options()

driver = webdriver.Chrome(service=chrome_service, options=chrome_options)

try:
    driver.get('https://www.snapdeal.com')

    try:
        # Handle potential pop-ups (if any, otherwise this part can be skipped)
        close_button = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, '.close'))
        )
        close_button.click()
    except TimeoutException:
        print("Login popup did not appear or could not be closed.")

    search_bar = driver.find_element(By.NAME, 'keyword')

    search_term = 'dress'  # Changed search term to 'shoes'
    search_bar.send_keys(search_term)
    search_bar.send_keys(Keys.RETURN)

    try:
        results = WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, '.product-tuple-listing'))
        )

        assert len(results) > 0, "No search results found."

        if len(results) > 0:
            print("Test Passed: Search results are displayed.")
        else:
            print("Test Failed: No search results found.")
    except TimeoutException:
        print("TimeoutException: No search results found within the given time period.")
finally:
    driver.quit()
