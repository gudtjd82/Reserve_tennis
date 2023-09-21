import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def full_screenshot(driver, output_path):
    total_width = driver.execute_script("return document.body.scrollWidth")
    total_height = driver.execute_script("return document.body.scrollHeight")

    # driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    # driver.implicitly_wait(10)

    driver.set_window_size(total_width, total_height)

    time.sleep(1)
    driver.save_screenshot(output_path)
    driver.maximize_window()

chrome_options = Options()
chrome_options.add_argument('--headless')
driver = webdriver.Chrome(options=chrome_options)

