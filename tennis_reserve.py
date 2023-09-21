import pyperclip
import pyautogui as pg
import time
import sqlite3
import os
import re
import subprocess
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from time_check import *


# 예약 코트 번호 링크
court8_url = 'https://yeyak.seoul.go.kr/web/reservation/selectReservView.do?rsv_svc_id=S210219092313243896&code=T100&dCode=T108&sch_order=1&sch_choose_list=&sch_type=&sch_text=%EC%84%9C%EB%82%A8%EC%84%BC%ED%84%B0%20%ED%85%8C%EB%8B%88%EC%8A%A4%EC%9E%A58%EB%B2%88%20%EC%BD%94%ED%8A%B8%20(%ED%8F%89%EC%9D%BC)&sch_recpt_begin_dt=&sch_recpt_end_dt=&sch_use_begin_dt=&sch_use_end_dt=&svc_prior=N&sch_reqst_value='
court5_url = 'https://yeyak.seoul.go.kr/web/reservation/selectReservView.do?rsv_svc_id=S210219091826906010&code=T100&dCode=T108&sch_order=1&sch_choose_list=&sch_type=&sch_text=%EC%84%9C%EB%82%A8%EC%84%BC%ED%84%B0&sch_recpt_begin_dt=&sch_recpt_end_dt=&sch_use_begin_dt=&sch_use_end_dt=&svc_prior=N&sch_reqst_value='

# 예약 날짜
# date = 'calendar_20230914'

# url: string
# date: 'calendar_20230914' 형식의 string
# time_selections: 시작 시간을 포함한 string list
# ready_time: 시, 분, 초를 포함한 string list
# start_time: 시, 분, 초를 포함한 string list
def reserve_tennis(url, date, time_selections, ready_time, start_time):
    options = Options()
    options.add_experimental_option("detach", True)

    # 네이비즘 접속
    driver_time = webdriver.Chrome(options=options)
    driver_time.get('http://time.navyism.com/?host=https%3A%2F%2Fyeyak.seoul.go.kr%2Fweb%2Fmain.do')
    driver_time.implicitly_wait(5)
    driver_time.find_element(By.ID, 'msec_check').click()

    # 시간 체크
    time_check(driver_time, ready_time[0], ready_time[1], ready_time[2])

    # 서남센터 테니스장 예약 페이지 접속
    
    driver = webdriver.Chrome(options=options)
    driver.get(url)
    driver.maximize_window()
    driver.implicitly_wait(5)

    # "팝업 닫기" 버튼 클릭
    driver.find_element(By.XPATH, '/html/body/div/div[3]/div[2]/div/div[1]/div/div[2]/button').click()
    driver.implicitly_wait(3)

    # "로그인" 버튼 클릭
    driver.find_element(By.XPATH, '/html/body/div/header/div[1]/div/div[1]/a').click()
    driver.implicitly_wait(5)

    # "네이버 아이디로 로그인" 버튼 클릭
    driver.find_element(By.XPATH, '/html/body/div/div[3]/div[2]/div/div/div/div[1]/form/ul[2]/li[1]/a/span').click()
    driver.implicitly_wait(10)


    # 네이버 로그인

    user_id = 'gudtjd82'
    elem_id = driver.find_element(By.ID, 'id')
    pyperclip.copy(user_id)
    elem_id.click()
    ActionChains(driver).key_down(Keys.COMMAND).send_keys('v').key_up(Keys.COMMAND).perform()
    # elem_id.send_keys(Keys.COMMAND, 'v')
    # pg.keyDown('command')
    # pg.press('v')
    # pg.keyUp('command')
    time.sleep(0.5)

    user_pw = 'tjdgus0204##'
    elem_pw = driver.find_element(By.ID, 'pw')
    pyperclip.copy(user_pw)
    # elem_pw.send_keys(Keys.COMMAND, 'v')
    elem_pw.click()
    ActionChains(driver).key_down(Keys.COMMAND).send_keys('v').key_up(Keys.COMMAND).perform()

    time.sleep(0.5)

    driver.find_element(By.ID, 'log.login').click()
    driver.implicitly_wait(10)

    # 팝업 닫기 클릭
    driver.find_element(By.XPATH, '/html/body/div/div[6]/div/div[2]/button').click()
    driver.implicitly_wait(5)

    # 네이비즘 시간 체크
    time_check(driver_time, start_time[0], start_time[1], start_time[2])

    # 서남센터 8번 테니스장 예약 페이지 이동
    driver.get(url)

    # 팝업 닫기
    driver.find_element(By.XPATH, '/html/body/div/div[3]/div[2]/div/div[1]/div/div[2]/button').click()

    # 예약하기 클릭
    driver.find_element(By.XPATH, '/html/body/div/div[3]/div[2]/div/form[2]/div[1]/div[2]/div/div/a[1]').click()
    driver.implicitly_wait(10)

    # 날짜 선택
    driver.find_element(By.ID, date).click()
    driver.implicitly_wait(3)

    # 시간 선택
    time_li = list('#unit* > a')
    for time_sel in time_selections:
        time_li[5] = time_sel
        driver.find_element(By.CSS_SELECTOR, ''.join(time_li)).click()
    driver.implicitly_wait(5)

    # 동의합니다
    driver.find_element(By.CSS_SELECTOR, '#aform > div.book_box > div.left_box > div:nth-child(6) > div.total_agree > span > label').click()

    # 두 자녀 이상
    driver.find_element(By.CSS_SELECTOR, '#user_cnt_area > div:nth-child(12) > div:nth-child(1) > div > div > div > button.user_plus').click()
    driver.implicitly_wait(5)

    # 인증번호 발송
    driver.find_element(By.CSS_SELECTOR, '#aform > div.book_box > div.left_box > div:nth-child(5) > table > tbody > tr:nth-child(6) > td > div:nth-child(2) > button').click()

    # alert 처리
    while True:
        try:
            alert = driver.switch_to.alert
            alert.accept()
            break
        except:
            pass


    # 인증번호 복사
    conn = sqlite3.connect(os.environ['HOME'] + '/Library/Messages/chat.db')
    cur = conn.cursor()

    latest_rowid = None

    while True:
        cur.execute("select rowid, text from message order by date desc limit 1")

        rowid, text = cur.fetchone()

        if latest_rowid is None:
            latest_rowid = rowid
        
        if latest_rowid != rowid:
            latest_rowid = rowid
            numbers = re.findall(r'\d{4,6}', text)
            if len(numbers) == 1:
                number = numbers[0]
                process = subprocess.Popen('pbcopy', env={'LANG': 'en_US.UTF-8'}, stdin=subprocess.PIPE)
                process.communicate(number.encode('utf-8'))
                break

    # 인증 번호 입력
    num_elem = driver.find_element(By.CSS_SELECTOR, '#form_cert')
    num_elem.click()
    ActionChains(driver).key_down(Keys.COMMAND).send_keys('v').key_up(Keys.COMMAND).perform()

    # 인증 확인 클릭
    driver.implicitly_wait(5)
    driver.find_element(By.CSS_SELECTOR, '#form_fnCon').click()
    driver.implicitly_wait(5)

    time.sleep(0.6)
    # reserve_loc = pg.locateOnScreen('./images/reserve_region.png', confidence=0.9)
    # pg.moveTo(reserve_loc.left, reserve_loc.top)

    # reserve_loc = pg.locateCenterOnScreen('./images/reserve_button.png', confidence=0.5, region=(1550, 730, 400, 400))
    # pg.moveTo(reserve_loc)
    # print(reserve_loc)

    # 예약하기 버튼 찾아서 클릭
    reserve_loc = pg.locateCenterOnScreen('./images/reserve_button.png', confidence=0.5, region=(1550, 730, 400, 400))
    # reserve_loc = pg.locateOnScreen('./images/reserve_region.png', confidence=0.7)
    print(reserve_loc)
    pg.click(reserve_loc)

    #alert 처리
    while True:
        try:
            alert = driver.switch_to.alert
            alert.accept()
            break
        except:
            pass

    #alert 처리
    while True:
        try:
            alert = driver.switch_to.alert
            alert.dismiss()
            break
        except:
            pass