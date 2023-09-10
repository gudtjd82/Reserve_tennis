from tennis_reserve import *

url_list = list([0,1,2,3,4,5,6,7,8,9,10])

url_list[3] = 'https://yeyak.seoul.go.kr/web/reservation/selectReservView.do?rsv_svc_id=S210219091235657961&code=T100&dCode=T108&sch_order=1&sch_choose_list=&sch_type=&sch_text=%EC%84%9C%EB%82%A8%EC%84%BC%ED%84%B0&sch_recpt_begin_dt=&sch_recpt_end_dt=&sch_use_begin_dt=&sch_use_end_dt=&svc_prior=N&sch_reqst_value='
url_list[5] = 'https://yeyak.seoul.go.kr/web/reservation/selectReservView.do?rsv_svc_id=S210219091826906010&code=T100&dCode=T108&sch_order=1&sch_choose_list=&sch_type=&sch_text=%EC%84%9C%EB%82%A8%EC%84%BC%ED%84%B0&sch_recpt_begin_dt=&sch_recpt_end_dt=&sch_use_begin_dt=&sch_use_end_dt=&svc_prior=N&sch_reqst_value='
url_list[6] = 'https://yeyak.seoul.go.kr/web/reservation/selectReservView.do?rsv_svc_id=S210219092004901944&code=T100&dCode=T108&sch_order=1&sch_choose_list=&sch_type=&sch_text=%EC%84%9C%EB%82%A8%EC%84%BC%ED%84%B0&sch_recpt_begin_dt=&sch_recpt_end_dt=&sch_use_begin_dt=&sch_use_end_dt=&svc_prior=N&sch_reqst_value='
url_list[8] = 'https://yeyak.seoul.go.kr/web/reservation/selectReservView.do?rsv_svc_id=S210219092313243896&code=T100&dCode=T108&sch_order=1&sch_choose_list=&sch_type=&sch_text=%EC%84%9C%EB%82%A8%EC%84%BC%ED%84%B0%208%EB%B2%88&sch_recpt_begin_dt=&sch_recpt_end_dt=&sch_use_begin_dt=&sch_use_end_dt=&svc_prior=N&sch_reqst_value='
url_list[9] = 'https://yeyak.seoul.go.kr/web/reservation/selectReservView.do?rsv_svc_id=S210219092430823699&code=T100&dCode=T108&sch_order=1&sch_choose_list=&sch_type=&sch_text=%EC%84%9C%EB%82%A8%EC%84%BC%ED%84%B0%209%EB%B2%88&sch_recpt_begin_dt=&sch_recpt_end_dt=&sch_use_begin_dt=&sch_use_end_dt=&svc_prior=N&sch_reqst_value='

i = int(input("예약하실 코드 번호를 입력하세요 : "))
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

reserve_tennis(url_list[i], date, time_selection, ready_time, start_time)