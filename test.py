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

time.sleep(2)
pg.click(256, 188)
pg.dragTo(415, 188, 0.2, button='left')
for _ in range(3):
        pg.click(320, 188)
        time.sleep(0.1)