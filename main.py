from reserve_seonam import *
from reserve_nanji import *

url_list_day = list([0,1,2,3,4,5,6,7,8,9,10])
url_list_wkend = list([0,1,2,3,4,5,6,7,8,9,10])

url_list_day[3] = 'https://yeyak.seoul.go.kr/web/reservation/selectReservView.do?rsv_svc_id=S210219091235657961&code=T100&dCode=T108&sch_order=1&sch_choose_list=&sch_type=&sch_text=%EC%84%9C%EB%82%A8%EC%84%BC%ED%84%B0&sch_recpt_begin_dt=&sch_recpt_end_dt=&sch_use_begin_dt=&sch_use_end_dt=&svc_prior=N&sch_reqst_value='
url_list_day[5] = 'https://yeyak.seoul.go.kr/web/reservation/selectReservView.do?rsv_svc_id=S210219091826906010&code=T100&dCode=T108&sch_order=1&sch_choose_list=&sch_type=&sch_text=%EC%84%9C%EB%82%A8%EC%84%BC%ED%84%B0&sch_recpt_begin_dt=&sch_recpt_end_dt=&sch_use_begin_dt=&sch_use_end_dt=&svc_prior=N&sch_reqst_value='
url_list_day[6] = 'https://yeyak.seoul.go.kr/web/reservation/selectReservView.do?rsv_svc_id=S210219092004901944&code=T100&dCode=T108&sch_order=1&sch_choose_list=&sch_type=&sch_text=%EC%84%9C%EB%82%A8%EC%84%BC%ED%84%B0&sch_recpt_begin_dt=&sch_recpt_end_dt=&sch_use_begin_dt=&sch_use_end_dt=&svc_prior=N&sch_reqst_value='
url_list_day[8] = 'https://yeyak.seoul.go.kr/web/reservation/selectReservView.do?rsv_svc_id=S210219092313243896&code=T100&dCode=T108&sch_order=1&sch_choose_list=&sch_type=&sch_text=%EC%84%9C%EB%82%A8%EC%84%BC%ED%84%B0%208%EB%B2%88&sch_recpt_begin_dt=&sch_recpt_end_dt=&sch_use_begin_dt=&sch_use_end_dt=&svc_prior=N&sch_reqst_value='
url_list_day[9] = 'https://yeyak.seoul.go.kr/web/reservation/selectReservView.do?rsv_svc_id=S210219092430823699&code=T100&dCode=T108&sch_order=1&sch_choose_list=&sch_type=&sch_text=%EC%84%9C%EB%82%A8%EC%84%BC%ED%84%B0%209%EB%B2%88&sch_recpt_begin_dt=&sch_recpt_end_dt=&sch_use_begin_dt=&sch_use_end_dt=&svc_prior=N&sch_reqst_value='

url_list_wkend[8] = 'https://yeyak.seoul.go.kr/web/reservation/selectReservView.do?rsv_svc_id=S210330154443511753&code=T100&dCode=T108&sch_order=1&sch_choose_list=&sch_type=&sch_text=%EC%84%9C%EB%82%A8%208%EB%B2%88&sch_recpt_begin_dt=&sch_recpt_end_dt=&sch_use_begin_dt=&sch_use_end_dt=&svc_prior=N&sch_reqst_value='

print("*******$ conda activate macro를 입력했는지 확인하세요!!*******")
i = int(input("예약하실 코드 번호를 입력하세요 : "))
day_weekend = input("주말/공휴일인가요? (y/n) : ")
date_in = input("날짜를 입력하세요. (ex. 20230920) : ")
timeSel_in = input("원하는 파트를 입력하세요. (0=>6시, 1=>7시) : ")
ready_in = input("준비 시각을 입력하세요 (0시 0분 0초) : ")
start_in = input("시작 시각을 입력하세요 (0시 0분 0초) : ")

# 'calendar_20230914' 형식
date = 'calendar_' + date_in

# '1' = 6시 시작
time_selection = timeSel_in.split()

ready_time = ready_in.split()
start_time = start_in.split()

if day_weekend.upper() == 'N':
    reserve_tennis(url_list_day[i], date, time_selection, ready_time, start_time)
else:
    reserve_tennis(url_list_wkend[i], date, time_selection, ready_time, start_time)