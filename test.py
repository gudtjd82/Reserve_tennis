import pyperclip
import pyautogui as pg
import time
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from time_check import *
from screenshot import *
from get_location import *
from get_location import *

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

time_options = webdriver.ChromeOptions()
time_options.add_experimental_option("detach", True)
time_options.add_argument('--blink-settings=imagesEnabled=false')


driver_time = webdriver.Chrome(options=time_options)

driver_time.get('http://time.navyism.com/?host=https%3A%2F%2Fyeyak.seoul.go.kr%2Fweb%2Fmain.do')