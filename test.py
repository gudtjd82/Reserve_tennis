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
print(pg.size() == (1680, 1050))