from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

# Setup webdriver
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

try:
    # Buka halaman utama Traveloka
    driver.get('https://www.traveloka.com')

    # Tunggu hingga tombol "Tiket Pesawat" muncul
    flight_tab = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, '//a[@href="/en/flight"]'))
    )
    flight_tab.click()

    # Tunggu hingga elemen input asal dan tujuan muncul
    origin_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//input[@placeholder="Origin"]'))
    )
    destination_input = driver.find_element(By.XPATH, '//input[@placeholder="Destination"]')

    # Masukkan kota asal dan kota tujuan
    origin_input.send_keys('Jakarta (CGK)')
    destination_input.send_keys('Bali (DPS)')

    # Pilih tanggal keberangkatan dan tanggal kembali
    departure_date = driver.find_element(By.XPATH, '//input[@placeholder="Departure Date"]')
    return_date = driver.find_element(By.XPATH, '//input[@placeholder="Return Date"]')

    # Menggunakan Javascript untuk menetapkan nilai tanggal karena elemen mungkin bersifat read-only
    driver.execute_script("arguments[0].value='2023-07-01';", departure_date)
    driver.execute_script("arguments[0].value='2023-07-10';", return_date)

    # Klik tombol "Cari"
    search_button = driver.find_element(By.XPATH, '//button[contains(text(),"Search")]')
    search_button.click()

    # Tunggu beberapa saat untuk memastikan halaman hasil pencarian dimuat
    WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.XPATH, '//div[contains(text(),"flights found")]'))
    )

    # Verifikasi hasil pencarian
    assert "flights found" in driver.page_source, "Penerbangan tidak ditemukan!"

except Exception as e:
    print("Terjadi error: ", e)

finally:
    # Tutup browser
    driver.quit()
