import math
import time
from classes import browser_init
from classes.browser_init import Browser
from selenium.webdriver.common.by import By

confirm_test = Browser()
confirm_test.open_page('https://suninjuly.github.io/alert_accept.html')

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    confirm_test.find_el('xpath', '//button').click()

    confirm = confirm_test.driver.switch_to.alert
    confirm.accept()

    val = confirm_test.find_el(By.ID, 'input_value').text
    result = calc(val)

    confirm_test.find_el(By.ID, 'answer').send_keys(result)

    confirm_test.find_el('xpath', '//button').click()

finally:
    time.sleep(5)
    confirm_test.close_page()