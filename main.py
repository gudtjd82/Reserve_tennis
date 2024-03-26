from reserve_seonam import *
from reserve_nanji import *
from reserve_nanji2 import *

url_seonam_day = list([0,1,2,3,4,5,6,7,8,9,10])
url_seonam_wkend = list([0,1,2,3,4,5,6,7,8,9,10])
url_nanji = dict()

url_seonam_day[5] = 'https://url.kr/wg1iac'
url_seonam_day[6] = 'https://url.kr/etwcyq'
url_seonam_day[7] = 'https://url.kr/ukafhl'
url_seonam_day[8] = 'https://url.kr/nidpj1'
url_seonam_day[9] = 'https://url.kr/j2cua9'

url_seonam_wkend[7] = 'https://url.kr/lxahib'
url_seonam_wkend[8] = 'https://url.kr/25cuso'

url_nanji['A'] = 'https://url.kr/vkga8n'
url_nanji['B'] = 'https://url.kr/ilpo2e'
url_nanji['C'] = 'https://url.kr/9gj2yk'
url_nanji['D'] = 'https://url.kr/2dmhzr'

active = input("conda activate macro를 입력했나요!!!! (y/n): ")
if active == 'n':
    exit()

location = int(input("예약하실 테니스장 번호를 선택해주세요.(1.서남 / 2.난지(새창) / 3.난지(현재창)): "))
# user_id = input("아이디를 입력하세요 : ")
# user_pw = input("비밀번호를 입력하세요 : ")

if location == 1:
    user_id = input("아이디를 입력하세요 : ")
    i = int(input("예약하실 코트 번호를 입력하세요 : "))
    date_in = input("날짜를 입력하세요. (ex. 20240220) : ")
    timeSel_in = input("원하는 파트를 입력하세요. (0=>6시, 1=>7시) : ")
    day_weekend = input("주말/공휴일인가요? (y/n) : ")
    light_in = input("라이트를 사용합니까? (y/n) : ")
    ready_in = input("준비 시각을 입력하세요 (00시 00분 00초) : ")
    start_in = input("시작 시각을 입력하세요 (00시 00분 00초) : ")
    

    # 'calendar_20230914' 형식
    date = 'calendar_' + date_in
    # date = 'cal_' + date_in

    # '1' = 6시 시작
    time_selection = timeSel_in.split()

    if light_in == 'y':
        light_use = True
    elif light_in == 'n':
        light_use = False

    if ready_in != '0':
        ready_time = ready_in.split()
    else:
        ready_time = ready_in

    if start_in != '0':
        start_time = start_in.split()
    else:
        start_time = '0'
    
    if day_weekend.upper() == 'N':
        reserve_seonam(user_id, url_seonam_day[i], date, time_selection, light_use, ready_time, start_time)
    else:
        reserve_seonam(user_id, url_seonam_wkend[i], date, time_selection, light_use, ready_time, start_time)

elif location == 2:
    user_id = input("아이디를 입력하세요 : ")
    a = input("예약하실 코트 번호를 입력하세요 (A, B, C, D) : ")
    date_in = input("날짜를 입력하세요. (ex. 20240220) : ")
    timeSel_in = input("원하는 파트를 입력하세요. (0=>9~11시, 1=>13~15시. 2=>15~17시) : ")
    ready_in = input("준비 시각을 입력하세요 (00시 00분 00초) : ")
    start_in = input("시작 시각을 입력하세요 (00시 00분 00초) : ")
    

    # 'calendar_20230914' 형식
    date = 'calendar_' + date_in
    # date = 'cal_' + date_in

    # '0' = 9시~11시
    time_selection = timeSel_in.split()

    if ready_in != '0':
        ready_time = ready_in.split()
    else:
        ready_time = ready_in

    if start_in != '0':
        start_time = start_in.split()
    else:
        start_time = '0'

    reserve_nanji(user_id, url_nanji[a.upper()], date, time_selection, ready_time, start_time)

elif location == 3:
    user_id = input("아이디를 입력하세요 : ")
    a = input("예약하실 코트 번호를 입력하세요 (A, B, C, D) : ")
    date_in = input("날짜를 입력하세요. (ex. 20240220) : ")
    timeSel_in = input("원하는 파트를 입력하세요. (0=>9~11시, 1=>13~15시. 2=>15~17시) : ")
    ready_in = input("준비 시각을 입력하세요 (00시 00분 00초) : ")
    start_in = input("시작 시각을 입력하세요 (00시 00분 00초) : ")
    

    # 'calendar_20230914' 형식
    date = 'calendar_' + date_in
    # date = 'cal_' + date_in

    # '0' = 9시~11시
    time_selection = timeSel_in.split()

    if ready_in != '0':
        ready_time = ready_in.split()
    else:
        ready_time = ready_in

    if start_in != '0':
        start_time = start_in.split()
    else:
        start_time = '0'

    reserve_nanji2(user_id, url_nanji[a.upper()], date, time_selection, ready_time, start_time)