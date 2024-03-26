from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import re

def time_compare(time, hour, minute, sec):
    target_hour = int(hour)
    target_min = int(minute)
    target_sec = int(sec)
    cur_hour = int(time[3])
    cur_min = int(time[4])
    cur_sec = int(time[5])

    target_time = 10000*target_hour + 100*target_min + target_sec
    cur_time = 10000*cur_hour + 100*cur_min + cur_sec

    if cur_hour >= 20:
        return False
    return target_time <= cur_time

def time_check(driver_time, hour, minute, sec):
        
    time_txt = driver_time.find_element(By.ID, 'time_area').text
    time = re.findall("[0-9]+", time_txt)
    prev_hour = time[3]
    # prev_sec = time[5]
    while True:
        try:
            time_txt = driver_time.find_element(By.ID, 'time_area').text
            # msec_txt = driver_time.find_element(By.ID, 'msec_area').text
        except:
            print("refresh!")
            driver_time.refresh()
            driver_time.implicitly_wait(10)
            driver_time.find_element(By.CSS_SELECTOR, '#time_area').click()
            print("time_txt: ", time_txt)
        time = re.findall("[0-9]+", time_txt)
        # if prev_sec != time[5]:
        #     print("time_txt: ", time_txt)
        #     prev_sec = time[5]
        # time[0]: 년 / time[1]: 월 / time[2]: 일 / time[3] 시 / time[4] 분 / time[5] 초
        if time_compare(time, hour, minute, sec):
            # msec = re.findall('[0-9]+', msec_txt)
            # if(int(msec[0]) >=0):
            print("On Time!")
            return
        if prev_hour != time[3]:
            driver_time.find_element(By.ID, 'buttonFight').click()
            driver_time.find_element(By.CSS_SELECTOR, '#time_area').click()
            prev_hour = time[3]
