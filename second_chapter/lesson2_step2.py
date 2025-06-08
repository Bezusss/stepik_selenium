from select import select
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from classes import browser_init
from classes.browser_init import Browser
import time
import math

link = 'https://suninjuly.github.io/selects1.html'
test = Browser()

try:
    test.open_page(link)
    count_sum = int(test.find_el(By.ID, 'num1').text) + int(test.find_el(By.ID,'num2').text)

    # test.find_el(By.ID, 'dropdown').click()

    select = Select(test.find_el(By.ID, 'dropdown'))
    select.select_by_value(str(count_sum))

    test.find_el('xpath', '//button[text()="Submit"]').click()

finally:
    time.sleep(5)
    test.close_page()