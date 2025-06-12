from classes import browser_init
from classes.browser_init import Browser
from selenium.webdriver.common.by import By
import time

site = Browser()

site.open_page('https://ya.ru/')
time.sleep(5)
site.close_page()