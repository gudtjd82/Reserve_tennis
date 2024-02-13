import pyperclip
import pyautogui as pg
import time
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from time_check import *
from screenshot import *
from cp_msg import *
from card_pay import *

# 예약 날짜
# date = 'calendar_20230914'

# 아이디 비번
user_pw = 'tjdgus02@@'

# 네이비즘 주소
navyism_url = 'http://time.navyism.com/?host=https%3A%2F%2Fyeyak.seoul.go.kr%2Fweb%2Fmain.do'
# 마지막 alert 처리
finish = True


# url: string
# date: 'calendar_20230914' 형식의 string
# time_selections: 시작 시간을 포함한 string list
# ready_time: 시, 분, 초를 포함한 string list
# start_time: 시, 분, 초를 포함한 string list
def reserve_seonam(user_id, url, date, time_selections, light_use, ready_time, start_time):
    user_id = user_id
    # 스크린샷 저장 위치
    reserve_path = "./images/reserve1.png"
    time_path = "./images/time1.png"

    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)

    time_options = webdriver.ChromeOptions()
    time_options.add_experimental_option("detach", True)
    time_options.add_argument('--blink-settings=imagesEnabled=false')
    

    driver_time = webdriver.Chrome(options=time_options)
    if ready_time != '0':
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
    # PROXY = "15.204.161.192:18080"
    # options.add_argument(f'--proxy-server={PROXY}')
    driver = webdriver.Chrome(options=options)
    # driver.get("http://{}:{}".format(PROXY_HOST, PROXY_PORT))
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
    # driver.find_element(By.XPATH, '/html/body/div/div[3]/div[2]/div/div/div/div[1]/form/ul[2]/li[1]/a/span').click()
    # driver.implicitly_wait(10)


    # 로그인
    elem_id = driver.find_element(By.ID, 'userid')
    pyperclip.copy(user_id)
    elem_id.click()
    ActionChains(driver).key_down(Keys.COMMAND).send_keys('v').key_up(Keys.COMMAND).perform()

    elem_pw = driver.find_element(By.ID, 'userpwd')
    pyperclip.copy(user_pw)
    elem_pw.click()
    ActionChains(driver).key_down(Keys.COMMAND).send_keys('v').key_up(Keys.COMMAND).perform()

    driver.find_element(By.CSS_SELECTOR, '#addUserForm > div.login_inp_box > button').click()
    driver.implicitly_wait(10)

    # 네이비즘 시간 체크
    if start_time != '0':
        time_check(driver_time, start_time[0], start_time[1], start_time[2])
        # 시간 스크린샷
        # time_path = full_screenshot(driver_time, time_path)
    start = time.time()  # 시작 시간 저장
    # 서남센터 테니스장 예약 페이지 이동
    driver.get(url)

    # 팝업 닫기
    driver.find_element(By.XPATH, '/html/body/div/div[3]/div[2]/div/div[1]/div/div[2]/button').click()
    # 시간 스크린샷
    # time_path = full_screenshot(driver_time, time_path)
    print("코드 실행 시간 :", time.time() - start)  
    
    #스크린샷
    reserve_path = full_screenshot(driver, reserve_path)
    # 예약하기 클릭

    i = 0
    while True:
        reserve_button = driver.find_element(By.XPATH, '/html/body/div/div[3]/div[2]/div/form[2]/div[1]/div[2]/div/div/a[1]')
        if i == 5:
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
    # driver.find_element(By.CSS_SELECTOR, '#calendar > div > button').click()
    # while True:
    #     try:
    #         alert = driver.switch_to.alert
    #         alert.accept()
    #         break
    #     except:
    #         pass
    
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
            reserve_path = full_screenshot(driver, reserve_path)
            time_path = full_screenshot(driver_time, time_path)

    # 동의합니다
    try:
        driver.find_element(By.CSS_SELECTOR, '#aform > div.book_box > div.left_box > div:nth-child(6) > div.total_agree > span > label').click()
    except:
        exit("\"동의합니다\" 버튼이 없습니다.")

    # 두 자녀 이상, 라이트 유무
    if light_use:
        driver.find_element(By.CSS_SELECTOR, '#user_cnt_area > div:nth-child(15) > div:nth-child(1) > div > div > div > button.user_plus').click()
    else:
        driver.find_element(By.CSS_SELECTOR, '#user_cnt_area > div:nth-child(12) > div:nth-child(1) > div > div > div > button.user_plus').click()
    driver.implicitly_wait(5)

    # 주소 입력
    addr = "초록마을로 26길 49"
    addr_fill = False
    try:
        ## 주소 검색 클릭
        driver.find_element(By.CSS_SELECTOR, '#aform > div.book_box > div.left_box > div:nth-child(5) > table > tbody > tr:nth-child(5) > td > button').click()
    except:
        addr_fill = True
    if not addr_fill:
        ## 윈도우 전환
        driver.switch_to.window(driver.window_handles[1])
        ## 주소 입력
        addr_elem = driver.find_element(By.ID, 'keyword')
        pyperclip.copy(addr)
        addr_elem.click()
        ActionChains(driver).key_down(Keys.COMMAND).send_keys('v').key_up(Keys.COMMAND).perform()
        driver.find_element(By.CSS_SELECTOR, '#searchContentBox > fieldset > span > input[type=button]:nth-child(2)').click()
        ## 주소 선택
        driver.find_element(By.CSS_SELECTOR, '#roadAddrTd1\ style\=').click()
        ## 상세 주소 입력
        pyperclip.copy("301호")
        driver.find_element(By.ID, 'rtAddrDetail').click()
        ActionChains(driver).key_down(Keys.COMMAND).send_keys('v').key_up(Keys.COMMAND).perform()
        ## 주소입력 버튼 클릭
        driver.find_element(By.CSS_SELECTOR, '#resultData > div > a').click()
        # 윈도우 전환
        driver.switch_to.window(driver.window_handles[0])

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

    if user_id != 'gudtjd82':
        exit("인증번호 전송까지 완료")

    # 인증번호 복사
    cp_msg()

    # 인증 번호 입력
    num_elem = driver.find_element(By.CSS_SELECTOR, '#form_cert')
    num_elem.click()
    ActionChains(driver).key_down(Keys.COMMAND).send_keys('v').key_up(Keys.COMMAND).perform()

    # 인증 확인 클릭
    driver.implicitly_wait(5)
    driver.find_element(By.CSS_SELECTOR, '#form_fnCon').click()
    driver.implicitly_wait(5)
    time.sleep(0.6)

    # 예약하기 클릭
    book_btn_elem = driver.find_element(By.CSS_SELECTOR, '#aform > div.book_box > div.right_box > div.info_wrap > ul')
    try:
        real_btn = book_btn_elem.find_element(By.CLASS_NAME, 'btn_book')
    except:
        exit("예약하기 버튼을 찾지 못함")
    if real_btn is not None:
        real_btn.click()
    else:
        exit("예약하기 버튼을 찾지 못함")

    ## 노트북 모니터
    # reserve_loc = pg.locateCenterOnScreen('./images/reserve_button.png', confidence=0.5, region=(2240, 1470, 600, 600))
    # reserve_loc = pg.locateOnScreen('./images/reserve_region.png', confidence=0.7)

    # print(reserve_loc)
    # pg.click(reserve_loc)

    #alert 처리
    while finish:
        try:
            alert = driver.switch_to.alert
            alert.accept()
            break
        except:
            pass
    
    #alert 처리
    while finish:
        try:
            alert = driver.switch_to.alert
            alert.dismiss()
            break
        except:
            pass

    
    # 결제하기
    driver.find_element(By.CSS_SELECTOR, '#contents > div.common_btn_box.pcs3 > a.common_btn.blue').click()
    #alert 처리
    while finish:
        try:
            alert = driver.switch_to.alert
            alert.dismiss()
            break
        except:
            pass
    driver.find_element(By.CSS_SELECTOR, '#commonForm > div > div.right_box > div > div.common_btn_box > button').click()

    time.sleep(10)

    if pg.size() == (1680, 1050):
        card_pay_laptop()
    else:
        card_pay_desktop()