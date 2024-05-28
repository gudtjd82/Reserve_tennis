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

    # 시간 선택
    driver.find_element(By.ID, date).click()
    time_f = '#unit'
    time_b = ' > a'
    for time_sel in time_selection:
        time_str = time_f + time_sel + time_b
        try:
            driver.find_element(By.CSS_SELECTOR, time_str).click()
        except:
            print("Error:", time_str, "가 없음")
            # 스크린샷
            # reserve_path = full_screenshot(driver, reserve_path)
            # time_path = full_screenshot(driver_time, time_path)

    # 동의합니다
    try:
        driver.find_element(By.CSS_SELECTOR, '#aform > div.book_box > div.left_box > div:nth-child(6) > div.total_agree > span > label').click()
    except:
        exit("\"동의합니다\" 버튼이 없습니다.")

    # 이용 인원
    driver.find_element(By.CSS_SELECTOR, '#user_cnt_area > div > div:nth-child(1) > div > div > div > button.user_plus').click()

    # 인증번호 발송
    # driver.find_element(By.CSS_SELECTOR, '#aform > div.book_box > div.left_box > div:nth-child(5) > table > tbody > tr:nth-child(7) > td > div:nth-child(2) > button').click()

    # captcha 새로고침
    driver.find_element(By.CSS_SELECTOR, '#aform > div.book_box > div.left_box > div:nth-child(5) > table > tbody > tr:nth-child(7) > td > div > div.captcha_attr > button.btn_refresh').click()
    driver.implicitly_wait(3)
    driver.find_element(By.CSS_SELECTOR, '#simplecaptcha_answer').click()
    time.sleep(0.1)

    if pg.size() == (1680, 1050):
        # Mac Monitor
        captcha_region = (459, 908, 236, 88)
        # captcha_x, captcha_y = get_click_position()
        # captcha_region = ((captcha_x, captcha_y, 236, 88))
    else:
        # Desktop Monitor
        captcha_region = (899, 1272, 236, 88)
        

    # captcha 캡쳐하고 답 얻기
    dirName = 'reserve_nanji'
    while True:
        captcha_path = captureCaptcha(dirName, captcha_region)
        # os.system(f"open {captcha_path}")
        answer = result_img(captcha_path)
        print(f"answer: {answer}")
        time.sleep(0.5)

        # 답 입력
        pyperclip.copy(answer)
        driver.find_element(By.CSS_SELECTOR, '#simplecaptcha_answer').click()
        ActionChains(driver).key_down(Keys.COMMAND).send_keys('v').key_up(Keys.COMMAND).perform()

        # 인증 확인 클릭
        time.sleep(0.3)
        try:
            # driver.find_element(By.CSS_SELECTOR, '#btn_captcha_accept').click()
            driver.implicitly_wait(3)
            break
        except:
            while True:
                try:
                    alert = driver.switch_to.alert
                    alert.accept()
                    break
                except:
                    pass
            # captcha 새로고침
            driver.find_element(By.CSS_SELECTOR, '#aform > div.book_box > div.left_box > div:nth-child(5) > table > tbody > tr:nth-child(7) > td > div > div.captcha_attr > button.btn_refresh').click()
            time.sleep(0.5)
            pass

    time.sleep(0.5)

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

if __name__ == "__main__":
    main()