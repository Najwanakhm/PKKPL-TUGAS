from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

website_url = "https://www.traveloka.com/id-id"
options = webdriver.ChromeOptions()
options.add_argument("--incognito")
options.add_argument("--start-maximized")

try:
    # Set up WebDriver
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    driver.get(website_url)

    # Click on the bus/travel ticket button
    bus_ticket_button = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Bus & Travel Tickets')]"))
    )
    bus_ticket_button.click()

    # Enter origin station
    origin_station_input = WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located((By.NAME, "originStation"))
    )
    origin_station_input.send_keys("Jakarta")

    # Enter destination station
    destination_station_input = WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located((By.NAME, "destinationStation"))
    )
    destination_station_input.send_keys("Bandung")

    # Enter travel date
    travel_date_input = WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located((By.NAME, "travelDate"))
    )
    travel_date_input.send_keys("2023-03-01")

    # Click on the search button
    search_button = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Search')]"))
    )
    search_button.click()

    # Wait for the search results to load
    WebDriverWait(driver, 20).until(
        EC.presence_of_all_elements_located((By.XPATH, "//div[contains(@class, 'search-result')]"))
    )

    print("Search results loaded!")

    # Keep the browser open for 60 seconds
    driver.implicitly_wait(5)
    time.sleep(60)

except TimeoutException as e:
    print(f"TimeoutException occurred: {str(e)}")
except Exception as e:
    print(f"Exception occurred: {str(e)}")
finally:
    # Close the browser
    if driver:
        driver.quit()
