# Snapdeal Automation Testing with Selenium

This project contains a collection of Selenium-based Python scripts for automating various functionalities of the [Snapdeal](https://www.snapdeal.com) website.

## 📌 Features Automated

- 🔍 Search Functionality (`Search_bar.py`)
- 🛒 Add to Cart (`addtocart.py`)
- ❌ Remove from Cart (`removefromcart.py`)
- 🔐 Login Flow (`login.py`, `login_alt.py`)
- 🔃 Apply Filters (`apply filter.py`)
- 💰 Sort by Price (`sort by price.py`)
- 🧪 Title Validation (`title_test.py`)
- 📸 Screenshots of OTP flow (`before_otp.png`, etc.)

## 🛠 Tech Stack

- **Language**: Python
- **Automation Tool**: Selenium WebDriver
- **Browser**: Google Chrome
- **Driver**: ChromeDriver (manually downloaded and used in code)

## 📂 Project Structure

.
├── .idea/ # PyCharm project config
├── Search_bar.py # Search test
├── addtocart.py # Add to cart test
├── removefromcart.py # Remove item from cart test
├── apply filter.py # Filter functionality test
├── sort by price.py # Sort feature test
├── login.py # Login test
├── login_alt.py # Alternate login flow
├── title_test.py # Title validation test
├── before_otp.png # Screenshot before OTP
├── before_otp_*.png # Timestamped OTP screenshot



## ✅ Requirements

- Python 3.x
- Google Chrome browser
- Compatible version of ChromeDriver

### Install Required Packages
```bash
pip install selenium
