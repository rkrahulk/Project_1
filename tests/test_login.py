# test_login.py
"""
Selenium test script for: User login with valid credentials
Test Case:
- Username and password fields are mandatory
- Login button should be enabled after input
- User should be redirected to dashboard on success
- Error message should appear for invalid credentials
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import pytest

# Replace these with the actual URL and valid test credentials
def get_test_data():
    return {
        "url": "https://yourapp.example.com/login",
        "valid_username": "testuser",
        "valid_password": "securepassword",
        "dashboard_url": "https://yourapp.example.com/dashboard",
        "invalid_username": "invaliduser",
        "invalid_password": "wrongpassword"
    }

@pytest.fixture(scope="module")
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()

def test_login_with_valid_credentials(driver):
    data = get_test_data()
    driver.get(data["url"])
    
    username_field = driver.find_element(By.ID, "username")
    password_field = driver.find_element(By.ID, "password")
    login_button = driver.find_element(By.ID, "loginBtn")

    # Check mandatory fields
    assert username_field.is_displayed() and password_field.is_displayed(), "Username and password fields must be visible"

    # Enter credentials
    username_field.send_keys(data["valid_username"])
    password_field.send_keys(data["valid_password"])

    # Login button should be enabled
    assert login_button.is_enabled(), "Login button should be enabled after input"
    login_button.click()

    # Wait for redirect
    time.sleep(2)
    assert driver.current_url == data["dashboard_url"], "User should be redirected to dashboard on success"


def test_login_with_invalid_credentials(driver):
    data = get_test_data()
    driver.get(data["url"])
    
    username_field = driver.find_element(By.ID, "username")
    password_field = driver.find_element(By.ID, "password")
    login_button = driver.find_element(By.ID, "loginBtn")

    # Enter invalid credentials
    username_field.send_keys(data["invalid_username"])
    password_field.send_keys(data["invalid_password"])
    login_button.click()

    # Wait for error
    time.sleep(1)
    error_msg = driver.find_element(By.ID, "errorMsg")
    assert error_msg.is_displayed(), "Error message should appear for invalid credentials"
    assert "invalid" in error_msg.text.lower()
