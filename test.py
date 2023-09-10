import pyperclip
import pyautogui as pg
import time
import sqlite3
import os
import re
import subprocess
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from time_check import *

options = Options()
options.add_experimental_option("detach", True)
driver_time = webdriver.Chrome(options=options)
driver_time.get('http://time.navyism.com/?host=https%3A%2F%2Fyeyak.seoul.go.kr%2Fweb%2Fmain.do')
driver_time.implicitly_wait(5)

driver_time.find_element(By.ID, 'msec_check').click()

time_check(driver_time, '13', '13', '00')
print("클릭!")