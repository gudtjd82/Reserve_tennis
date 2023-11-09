import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# return new_path
def full_screenshot(driver, output_path):
    total_width = driver.execute_script("return document.body.scrollWidth")
    total_height = driver.execute_script("return document.body.scrollHeight")

    # driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")


    driver.set_window_size(total_width, total_height)

    driver.implicitly_wait(10)
    driver.save_screenshot(output_path)
    driver.maximize_window()

    l = list(output_path)
    l[-5] = str(int(l[-5]) + 1)

    return ''.join(l)

