from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time
import random
from datetime import datetime

def current_time():
    return datetime.now().strftime("%d-%m-%Y %H:%M:%S")


log_contents = ""

def log(message):
    global log_contents
    log_contents += f"{message}\n"
    print(message)  # Print to console as well


chrome_driver_path = "chromedriver-win64/chromedriver.exe"
chrome_profile_path = "D:\LPU\Frugal Testing\customDir"

chrome_options = Options()
chrome_options.add_argument(f"user-data-dir={chrome_profile_path}")

service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service, options=chrome_options)
wait = WebDriverWait(driver, 5)  # Set a wait time

try:
    driver.get("https://www.expedia.com/")
    log(f"[{current_time()}] Navigated to Expedia")
    log(f"Current URL: {driver.current_url}")
    log(f"Page Title: {driver.title}")


    # Click on "English" beside the globe icon
    try:
        language_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="app-layer-base"]/div[2]/div[1]/header/div/section/div/div/div[2]/button')))

        language_button.click()
        log(f"[{current_time()}] Clicked on language button")
        time.sleep(random.uniform(2, 5))
        
        # Select "India" and "English"
        india_option = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="site-selector"]/option[19]')))
        india_option.click()
        log(f"[{current_time()}] Selected India as region")
        time.sleep(random.uniform(2, 5))

        english_option = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="language-selector"]/option')))
        english_option.click()
        log(f"[{current_time()}] Selected English as language")
        time.sleep(6)

        # Capture screenshot
        screenshot_path = "D:/LPU/Frugal Testing/2.region_changed.png"
        driver.save_screenshot(screenshot_path)
        log(f"[{current_time()}] Screenshot saved at {screenshot_path}")

        save_pref = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="app-layer-disp-settings-picker"]/section/div[5]/button')))
        save_pref.click()
        log(f"[{current_time()}] Viewing Flights in India")
        time.sleep(7)

    except TimeoutException:
        log("Language selection failed")

    # Click on the Flights tab
    try:
        flights_tab = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="multi-product-search-form-1"]/div/div/div/div/div[1]/ul/li[2]/a')))
        flights_tab.click()
        log(f"[{current_time()}] Clicked on Flights tab")

        # Capture screenshot
        screenshot_path = "D:/LPU/Frugal Testing/3.flight_tab.png"
        driver.save_screenshot(screenshot_path)
        log(f"[{current_time()}] Screenshot saved at {screenshot_path}")

    except TimeoutException:
        log("Flights tab not found")
        time.sleep(random.uniform(3, 6))

    try:
        # Click on One-Way Trip
        one_way = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="search_form_product_selector_flights"]/div/div/div[1]/div/div[1]/div/ul/li[2]/a')))
        one_way.click()

        # Capture screenshot
        screenshot_path = "D:/LPU/Frugal Testing/4.one_way.png"
        driver.save_screenshot(screenshot_path)
        log(f"[{current_time()}] Screenshot saved at {screenshot_path}")

    except TimeoutException:
        log("One-way option not found")
        time.sleep(random.uniform(2, 5))

    # Enter departure city
    try:
        departure_city_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="FlightSearchForm_ONE_WAY"]/div/div[1]/div/div[1]/div/div/div[2]/div[1]/button')))
        departure_city_button.click()

        departure_city_input = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="origin_select"]')))
        departure_city_input.clear()
        departure_city_input.send_keys("Kolkata")

        # Capture screenshot
        screenshot_path = "D:/LPU/Frugal Testing/5.depart_city.png"
        driver.save_screenshot(screenshot_path)
        log(f"[{current_time()}] Screenshot saved at {screenshot_path}")

        departure_city_input.send_keys(u'\ue007')  # press enter
        log(f"[{current_time()}] Entered departure city")
        time.sleep(random.uniform(2, 5))

        # Enter destination city
        destination_city_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="FlightSearchForm_ONE_WAY"]/div/div[1]/div/div[2]/div/div/div[2]/div[1]/button')))
        destination_city_button.click()

        destination_city_input = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="destination_select"]')))
        destination_city_input.clear()
        destination_city_input.send_keys("Hyderabad")

        # Capture screenshot
        screenshot_path = "D:/LPU/Frugal Testing/6.dest_city.png"
        driver.save_screenshot(screenshot_path)
        log(f"[{current_time()}] Screenshot saved at {screenshot_path}")

        destination_city_input.send_keys(u'\ue007')  # Press Enter
        log(f"[{current_time()}] Entered destination city")
        time.sleep(random.uniform(2, 5))

    except TimeoutException as e:
        log(f"Error entering city information: {e}")

    # Click on the departure date
    try:
        departure_date_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="FlightSearchForm_ONE_WAY"]/div/div[2]/div/div/div/div/button')))
        departure_date_button.click()
        time.sleep(random.uniform(2, 5))

        # Select "9 September 2024"
        specific_date = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="FlightSearchForm_ONE_WAY"]/div/div[2]/div/section/div[2]/div/div/div[3]/div/div[2]/table/tbody/tr[5]/td[1]/div/div[2]/div')))
        specific_date.click()
        #time.sleep(random.uniform(2, 5))

        # Capture screenshot
        screenshot_path = "D:/LPU/Frugal Testing/7.date_selection.png"
        driver.save_screenshot(screenshot_path)
        log(f"[{current_time()}] Screenshot saved at {screenshot_path}")

        # Click on done
        date_done = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="FlightSearchForm_ONE_WAY"]/div/div[2]/div/section/footer/div/button')))
        date_done.click()

        log(f"[{current_time()}] Departure date selected: 9 September 2024")

    except TimeoutException:
        log("Error selecting departure date")

    # Click on "Travellers"
    try:
        travellers_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="FlightSearchForm_ONE_WAY"]/div/div[3]/div/div[1]/button')))
        travellers_button.click()
        #time.sleep(random.uniform(2, 5))

        # Select "2 Adults"
        adult_option = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="FlightSearchForm_ONE_WAY"]/div/div[3]/div/div[2]/div/div/section/div[1]/div/div/button[2]/span')))
        adult_option.click()

        # Capture screenshot
        screenshot_path = "D:/LPU/Frugal Testing/8.travellers.png"
        driver.save_screenshot(screenshot_path)
        log(f"[{current_time()}] Screenshot saved at {screenshot_path}")

        time.sleep(random.uniform(2, 5))
        
        # Click Done
        done_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="travelers_selector_done_button"]')))
        done_button.click()
        log(f"[{current_time()}] Selected 2 adults and clicked Done")
        #time.sleep(random.uniform(2, 5))

    except TimeoutException:
        log("Error in travellers selection")

    # Click on the SEARCH Button
    try:
        search_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="search_button"]')))
        search_button.click()
        log(f"[{current_time()}] Clicked on SEARCH button")
        time.sleep(random.uniform(2, 5))

    except TimeoutException:
        log("SEARCH button not found")

    # Click on the first flight available
    try:
        # Wait until the buttons for selecting flights are clickable
        first_flight = wait.until(EC.element_to_be_clickable((By.XPATH, '(//button[@data-test-id="select-link"])[1]')))
        first_flight.click()
        time.sleep(8)

        # Capture screenshot
        screenshot_path = "D:/LPU/Frugal Testing/9.first_flight.png"
        driver.save_screenshot(screenshot_path)
        log(f"[{current_time()}] Screenshot saved at {screenshot_path}")

        # Selecting the flight
        select_first_flight = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="AQreAQrLAXY1LXNvcy1lNDk5NjRiYTVmNmI0NjJmOWM4NjQyZjc0MDljY2JhNi0xOTMtMi01MTJ-Mi5TfkFRb0NDQnNTQndpb0d4QUpHQmdvQWxnQmNBQjZESFJ5WVhabGJHWjFjMmx2Ym9nQnc5Nm9SWkFCRUF-QVFvb0NpWUl0b29CRWdNek16UVl3cUFCSUljZUtLaXcyQUl3cjdIWUFqaFNRQUJZQVhJRVVqQkpVQklLQ0FzUUFSZ0lLZ0kyUlJnQ0lnUUlBUkFDS0FJd0F3EQAAAAAA3cVAKgUSAwoBMRInChYKCjIwMjQtMDktMjMSA0NDVRoDSFlEEgcSBUNPQUNIGgIQAiABGggIARIEGgAiACABMgsI____________AToA"]/div/div[3]/div/button')))
        select_first_flight.click()
        log(f"[{current_time()}] Clicked on the first available flight")
        time.sleep(random.uniform(2, 5))

    except TimeoutException:
        log("No flights available")

    # Capture screenshot
    screenshot_path = "D:/LPU/Frugal Testing/10.flight_selected.png"
    driver.save_screenshot(screenshot_path)
    log(f"[{current_time()}] Screenshot saved at {screenshot_path}")

    log(f"[{current_time()}] Script completed successfully")
    
except Exception as e:
    log(f"An unexpected error occurred: {e}")

# finally:
#     driver.quit()
#     log("Browser closed")

# Write the accumulated logs to a text file
with open("output.txt", "w") as f:
    f.write(log_contents)
