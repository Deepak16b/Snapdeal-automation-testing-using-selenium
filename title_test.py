from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options

# Specify the path to your ChromeDriver
chrome_driver_path = r"C:\Users\deepa\Downloads\chromedriver-win64\chromedriver-win64\chromedriver.exe"

# Set up the Chrome driver
chrome_service = ChromeService(executable_path=chrome_driver_path)
chrome_options = Options()

driver = webdriver.Chrome(service=chrome_service, options=chrome_options)

# Open Snapdeal website
driver.get('https://www.snapdeal.com')

# Get the actual title
actual_title = driver.title
print(f"Actual Title: {actual_title}")

# Define the expected title
expected_title = "Shop Online for Men, Women & Kids Clothing, Shoes, Home Decor Items"

# Verify the title
if actual_title == expected_title:
    print("Test Passed: Title is correct.")
else:
    print("Test Failed: Title is incorrect.")

# Close the browser
driver.quit()
