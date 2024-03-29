import pyperclip
import pyautogui as pg
import time
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from time_check import *
from screenshot import *
from get_location import *
from get_location import *
from captchaCracker import *
from check_click import *
from preprocessing import *

time.sleep(1)
# captcha_path = "./captchaCrack/imgs/reserve_nanji/1.png"
# answer = result_img(captcha_path)
# print(f"answer: {answer}")
# img = pg.screenshot(region=(899, 800, 236, 88))
# img.save("./images/sc_test.png")
# print("code starts!")
# captcha_x, captcha_y = get_click_position()
# captcha_region = ((captcha_x, captcha_y, 236, 88))
# print(captcha_region)
# dirName = 'reserve_nanji'
# captcha_path = captureCaptcha(dirName, captcha_region)
# # os.system(f"open {captcha_path}")
# answer = result_img(captcha_path)
# print(f"answer: {answer}")
# print("code end!"

options = Options()
options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
driver = webdriver.Chrome(options=options)
# driver.maximize_window()
# driver.implicitly_wait(3)
# driver.get(seonam_url)
# time.sleep(2)
# state_elem = driver.find_element(By.CSS_SELECTOR, '#header > div.container > div > div.state > a')

# captcha 캡쳐하고 열기
reserve_button = driver.find_element(By.XPATH, '/html/body/div/div[3]/div[2]/div/form[2]/div[1]/div[2]/div/div/a[1]')
print(reserve_button.text)