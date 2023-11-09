from time_check import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys

url = 'https://yeyak.seoul.go.kr/web/reservation/selectReservView.do?rsv_svc_id=S210219091826906010&code=T100&dCode=T108&sch_order=1&sch_choose_list=&sch_type=&sch_text=%EC%84%9C%EB%82%A8%EC%84%BC%ED%84%B0&sch_recpt_begin_dt=&sch_recpt_end_dt=&sch_use_begin_dt=&sch_use_end_dt=&svc_prior=N&sch_reqst_value='
options = Options()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=options)
driver.get(url)