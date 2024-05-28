import pyperclip
import pyautogui as pg
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from time_check import *
from screenshot import *
from cp_msg import *
from card_pay import *
from preprocessing import *
from captchaCracker import *
from check_click import *

def main():
    date_in = input("날짜를 입력하세요. (ex. 20240220) : ")
    timeSel_in = input("원하는 파트를 입력하세요. (0=>6시, 1=>7시) : ")
    time_selection = timeSel_in.split()
    date = 'calendar_' + date_in

    time.sleep(2)

    options = Options()
    options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    driver.implicitly_wait(3)


    # 동의합니다
    try:
        driver.find_element(By.CSS_SELECTOR, '#aform > div.book_box > div.left_box > div:nth-child(6) > div.total_agree > span > label').click()
    except:
        exit("\"동의합니다\" 버튼이 없습니다.")

    # 인증번호 발송
    # driver.find_element(By.CSS_SELECTOR, '#aform > div.book_box > div.left_box > div:nth-child(5) > table > tbody > tr:nth-child(7) > td > div:nth-child(2) > button').click()

    # 이메일
    pyperclip.copy("gudtjd82")
    driver.find_element(By.CSS_SELECTOR, '#form_email1').click()
    time.sleep(0.2)
    ActionChains(driver).key_down(Keys.COMMAND).send_keys('a').key_up(Keys.COMMAND).perform()
    ActionChains(driver).key_down(Keys.COMMAND).send_keys('v').key_up(Keys.COMMAND).perform()
    time.sleep(0.2)

    pyperclip.copy("naver.com")
    driver.find_element(By.CSS_SELECTOR, '#form_email2').click()
    time.sleep(0.2)
    ActionChains(driver).key_down(Keys.COMMAND).send_keys('a').key_up(Keys.COMMAND).perform()
    ActionChains(driver).key_down(Keys.COMMAND).send_keys('v').key_up(Keys.COMMAND).perform()
    time.sleep(0.2)

    # CAPTCHA 클릭
    if pg.size() == (1680, 1050):   # Mac Monitor
        pg.click(474, 252)
        time.sleep(0.2)
        pg.click(474, 252)
        # captcha_region = (459, 908, 236, 88)
        # captcha_x, captcha_y = get_click_position()
        # captcha_region = ((captcha_x, captcha_y, 236, 88))
    else:       # Desktop Monitor
        pg.click(913, 252)
        time.sleep(0.2)
        pg.click(913, 252)
        # captcha_region = (899, 1272, 236, 88)
    
    while True:
        try:
            alert = driver.switch_to.alert
            alert.accept()
            break
        except:
            pass
        

    
    # 예약하기 클릭
    book_btn_elem = driver.find_element(By.CSS_SELECTOR, '#aform > div.book_box > div.right_box > div.info_wrap > ul')
    #macro4 > button
    try:
        real_btn = book_btn_elem.find_element(By.CLASS_NAME, 'active')
    except:
        exit("예약하기 버튼을 찾지 못함")
    if real_btn is not None:
        real_btn.click()
    else:
        exit("예약하기 버튼을 찾지 못함")
    exit()

if __name__ == "__main__":
    main()