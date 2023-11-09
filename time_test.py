import pyperclip
import pyautogui as pg
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from time_check import *
from screenshot import *


def time_test(driver_time, time_path, diffs):

    options = Options()
    options.add_experimental_option("detach", True)
    

    # 네이비즘 접속
    
    
    # 시간 스크린샷
    # time_path = full_screenshot(driver_time, time_path)

    # 시간 체크
    time_txt = driver_time.find_element(By.ID, 'time_area').text

    time = re.findall("[0-9]+", time_txt)
    hour = time[3]
    minute = time[4]
    sec = str(int(time[5]) + 3)
    # print(hour + '시' + minute + '분' + time[5] + '초 시작')
    while True:
            start = driver_time.find_element(By.ID, 'time_area').text
            start_msec = driver_time.find_element(By.ID, 'msec_area').text

            start_time = re.findall("[0-9]+", start)
            # start_time[0]: 년 / start_time[1]: 월 / start_time[2]: 일 / start_time[3] 시 / start_time[4] 분 / start_time[5] 초
            if start_time[3]==hour and start_time[4]==minute and start_time[5]==sec:
                msec = re.findall('[0-9]+', start_msec)
                if(int(msec[0]) >=0):
                    break
    # 시간 스크린샷
    time_txt = driver_time.find_element(By.ID, 'time_area').text
    time = re.findall("[0-9]+", time_txt)
    hour = time[3]
    minute = time[4]
    before_sec = int(time[5])
    # print(hour + '시' + minute + '분' + time[5] + '초 접속 시작')
    # time_path = full_screenshot(driver_time, time_path)
    driver = webdriver.Chrome(options=options)
    driver.get('https://yeyak.seoul.go.kr/web/reservation/selectReservView.do?rsv_svc_id=S210219092115226884&code=T100&dCode=T108&sch_order=1&sch_choose_list=&sch_type=&sch_text=%EC%84%9C%EB%82%A8%EC%84%BC%ED%84%B0&sch_recpt_begin_dt=&sch_recpt_end_dt=&sch_use_begin_dt=&sch_use_end_dt=&svc_prior=N&sch_reqst_value=')
    # 시간 스크린샷
    time_txt = driver_time.find_element(By.ID, 'time_area').text
    time = re.findall("[0-9]+", time_txt)
    hour = time[3]
    minute = time[4]
    after_sec = int(time[5])
    # print(hour + '시' + minute + '분' + time[5] + '초 완료')
    # time_path = full_screenshot(driver_time, time_path)

    diff.append(abs(after_sec - before_sec))
    
    driver.close()
time_path = "./images/time1.png"
diff = list()

options = Options()
options.add_experimental_option("detach", True)
driver_time = webdriver.Chrome(options=options)
driver_time.get('http://time.navyism.com/?host=https%3A%2F%2Fyeyak.seoul.go.kr%2Fweb%2Fmain.do')
driver_time.implicitly_wait(10)
driver_time.find_element(By.ID, 'msec_check').click()
for i in range(0, 5):
    time_test(driver_time,time_path, diff)
print('평균' + str(sum(diff)/5) + '초')