from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import NoSuchElementException

# Setup webdriver
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

try:
    # Buka halaman utama Traveloka
    driver.get('https://www.traveloka.com')

    # Tambahkan implicitly wait
    driver.implicitly_wait(10)  # seconds

    try:
        # Klik pada tab "Hotel" dengan menggunakan teks di dalamnya
        hotel_tab = driver.find_element(By.XPATH, '//a[contains(text(), "Hotel")]')
        hotel_tab.click()

        # Masukkan nama kota atau nama hotel
        city_input = driver.find_element(By.ID, 'hotel-destination')
        city_input.send_keys('Bali')

        # Pilih tanggal check-in dan check-out
        checkin_date = driver.find_element(By.ID, 'hotel-checkin-date')
        checkin_date.send_keys('2023-07-01')

        checkout_date = driver.find_element(By.ID, 'hotel-checkout-date')
        checkout_date.send_keys('2023-07-05')

        # Pilih jumlah tamu dan kamar
        guest_room_input = driver.find_element(By.ID, 'hotel-room-guest')
        guest_room_input.click()
        # Berikan sedikit waktu untuk pilihan tamu muncul
        driver.implicitly_wait(1)
        guest_room_input.send_keys('2 dewasa, 1 kamar')

        # Klik tombol "Cari"
        search_button = driver.find_element(By.XPATH, '//*[@id="hotel-form"]/div[4]/button')
        search_button.click()

        # Tunggu beberapa saat untuk memastikan halaman hasil pencarian dimuat
        driver.implicitly_wait(5)

        # Verifikasi hasil pencarian
        assert "Daftar hotel" in driver.page_source, "Hotel tidak ditemukan!"

    except NoSuchElementException as e:
        print("Elemen tidak ditemukan:", e)

finally:
    # Tutup browser
    driver.quit()
