from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Initialize the Chrome driver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Navigate to the Traveloka website
driver.get("https://www.traveloka.com/id-id")

# Wait for the login button to be clickable
login_button = WebDriverWait(driver, 360).until(
    EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Login')]"))
)

# Click the login button
login_button.click()

# Click on the Google login button
google_login_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Google')]"))
)
google_login_button.click()

# Switch to the Google login window
google_login_window = driver.window_handles[1]
driver.switch_to.window(google_login_window)

# Enter Google email
google_email_input = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.NAME, "Email"))
)
google_email_input.send_keys("2110817210006@mhs.ac.ulm.id")

# Click on the next button
next_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.NAME, "next"))
)
next_button.click()

# Enter Google password
google_password_input = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.NAME, "Passwd"))
)
google_password_input.send_keys("Banjar2003")

# Click on the signin button
signin_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.NAME, "signIn"))
)
signin_button.click()

# Wait for the login to be successful
WebDriverWait(driver, 10).until(
    EC.url_contains("https://www.traveloka.com/id-id/dashboard")
)

print("Logged in successfully with Google!")

# Prevent the browser from closing automatically
input("Press any key to close the browser...")

# Close the browser
driver.quit()