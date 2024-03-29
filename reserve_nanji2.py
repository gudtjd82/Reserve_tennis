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

# 아이디 비번
# user_id = 'gudgh82'
user_pw = 'tjdgus02@@'

# 네이비즘 주소
navyism_url = 'http://time.navyism.com/?host=https%3A%2F%2Fyeyak.seoul.go.kr%2Fweb%2Fmain.do'
seonam_url = 'https://yeyak.seoul.go.kr/web/main.do'
# 마지막 alert 처리
finish = True

# 열려있는 크롬 창으로 크롤링
# url: string
# date: 'calendar_20230914' 형식의 string
# time_selections: 시작 시간을 포함한 string list
# ready_time: 시, 분, 초를 포함한 string list
# start_time: 시, 분, 초를 포함한 string list
def reserve_nanji2(user_id, url, date, time_selections, ready_time, start_time):
    # 스크린샷 저장 위치
    reserve_path = "./images/reserve1.png"
    time_path = "./images/time1.png"

    if ready_time != '0':
        time_options = webdriver.ChromeOptions()
        time_options.add_experimental_option("detach", True)
        time_options.add_argument('--blink-settings=imagesEnabled=false')
        driver_time = webdriver.Chrome(options=time_options)
        
        # 네이비즘 접속
        driver_time.get(navyism_url)
        WebDriverWait(driver_time, 3).until(EC.presence_of_element_located((By.ID, 'time_area')))
        driver_time.execute_script("window.stop();")
        driver_time.refresh()
        # driver_time.find_element(By.ID, 'msec_check').click()

        # 시간 체크
        driver_time.find_element(By.CSS_SELECTOR, '#time_area').click()
        time.sleep(1)
        time_check(driver_time, ready_time[0], ready_time[1], ready_time[2])
        # 시간 스크린샷
        # time_path = full_screenshot(driver_time, time_path)

    # 서남센터 테니스장 예약 페이지 접속
    options = Options()
    options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    driver.implicitly_wait(3)

    driver.get(seonam_url)
    # "팝업 닫기" 버튼 클릭
    # driver.find_element(By.XPATH, '/html/body/div/div[3]/div[2]/div/div[1]/div/div[2]/button').click()
    driver.implicitly_wait(3)

    # "로그인" 버튼 클릭
    # try: 
    state_elem = driver.find_element(By.CSS_SELECTOR, '#header > div.container > div > div.state > a')
    
    # 로그인
    if state_elem.get_attribute('text') == '로그인':
        state_elem.click()
        driver.implicitly_wait(3)

        elem_id = driver.find_element(By.ID, 'userid')
        pyperclip.copy(user_id)
        elem_id.click()
        ActionChains(driver).key_down(Keys.COMMAND).send_keys('a').key_up(Keys.COMMAND).perform()
        ActionChains(driver).key_down(Keys.COMMAND).send_keys('v').key_up(Keys.COMMAND).perform()

        elem_pw = driver.find_element(By.ID, 'userpwd')
        pyperclip.copy(user_pw)
        elem_pw.click()
        ActionChains(driver).key_down(Keys.COMMAND).send_keys('a').key_up(Keys.COMMAND).perform()
        ActionChains(driver).key_down(Keys.COMMAND).send_keys('v').key_up(Keys.COMMAND).perform()

        driver.find_element(By.CSS_SELECTOR, '#addUserForm > div.login_inp_box > button').click()
        driver.implicitly_wait(3)
    
    # 네이비즘 시간 체크
    if start_time != '0':
        time_check(driver_time, start_time[0], start_time[1], start_time[2])
        driver_time.close()
        # 시간 스크린샷
        # time_path = full_screenshot(driver_time, time_path)


    # 난지 테니스장 예약 페이지 이동
    driver.get(url)
    driver.implicitly_wait(3)

    # 팝업 닫기
    driver.find_element(By.XPATH, '/html/body/div/div[3]/div[2]/div/div[1]/div/div[2]/button').click()
    # 시간 스크린샷
    # time_path = full_screenshot(driver_time, time_path)

    #스크린샷
    # reserve_path = full_screenshot(driver, reserve_path)

    # 예약하기 클릭
    i = 0
    while True:
        driver.implicitly_wait(3)
        reserve_button = driver.find_element(By.XPATH, '/html/body/div/div[3]/div[2]/div/form[2]/div[1]/div[2]/div/div/a[1]')
        if i == 7:
            exit("이미 다 찼음")
        elif reserve_button.text == "예약하기":
            reserve_button.click()
            break
        else:
            time.sleep(2)
            print("새로고침")
            driver.refresh()
            driver.implicitly_wait(3)
            # 팝업 닫기
            driver.find_element(By.XPATH, '/html/body/div/div[3]/div[2]/div/div[1]/div/div[2]/button').click()
            i += 1

    driver.implicitly_wait(5)

    # 다음달로 넘기기
    driver.find_element(By.CSS_SELECTOR, '#calendar > div > button').click()

    # 시간 선택
    driver.find_element(By.ID, date).click()
    time_f = '#unit'
    time_b = ' > a'
    for time_sel in time_selections:
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

    if pg.size() == (1680, 1050):
        captcha_x, captcha_y = get_click_position()
        captcha_region = ((captcha_x, captcha_y, 236, 88))
    else:
        captcha_region = (899, 1272, 236, 88)
        

    # captcha 캡쳐하고 답 얻기
    dirName = 'reserve_nanji'
    while true:
        captcha_path = captureCaptcha(dirName, captcha_region)
        # os.system(f"open {captcha_path}")
        answer = result_img(captcha_path)
        print(f"answer: {answer}")
        time.sleep(1)

        # 답 입력
        pyperclip.copy(answer)
        driver.find_element(By.CSS_SELECTOR, '#simplecaptcha_answer').click()
        ActionChains(driver).key_down(Keys.COMMAND).send_keys('v').key_up(Keys.COMMAND).perform()

        # 인증 확인 클릭
        time.sleep(0.3)
        try:
            driver.find_element(By.CSS_SELECTOR, '#btn_captcha_accept').click()
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

    time.sleep(1)

    # 예약하기 클릭
    driver.find_element(By.CSS_SELECTOR, '#aform > div.book_box > div.right_box > div > div.common_btn_box > button').click()

    # alert 처리
    while finish:
        try:
            alert = driver.switch_to.alert
            alert.accept()
            break
        except:
            pass

    print("done!")

if __name__ == "__main__":
    user_id = "gudgh82"
    url = "https://url.kr/2dmhzr"
    date = "calendar_20240404"
    time_selections = "3"
    ready_time = '0'
    start_time = '0'
    reserve_nanji2(user_id, url, date, time_selections, ready_time, start_time)