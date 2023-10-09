from selenium import webdriver
from selenium.webdriver.common.by import By

# Initialize the Chrome driver
driver = webdriver.Chrome()

try:
    # Navigate to the login page
    driver.get("http://localhost:5000")

    # Find the username and password fields and enter credentials
    username_field = driver.find_element(By.ID, "username")
    password_field = driver.find_element(By.ID, "password")

    # Enter the username and password
    username_field.send_keys("admin")
    password_field.send_keys("admin")

    # Find the login button and click it
    login_button = driver.find_element(By.XPATH, "//input[@type='submit']")
    login_button.click()

    # Wait for a few seconds to allow the login process to complete
    driver.implicitly_wait(5)

    # Check if login was successful (you may add more specific checks here)
    if "Login successful!" in driver.page_source:
        print("Login successful!")
    else:
        print("Login failed.")

finally:
    # Close the browser
    driver.quit()