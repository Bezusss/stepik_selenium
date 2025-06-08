from classes import browser_init
from classes.browser_init import Browser
import time
import math
from selenium.webdriver.common.by import By


site = Browser()
link = 'http://suninjuly.github.io/redirect_accept.html'

site.open_page(link)

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    window = site.find_el(By.CSS_SELECTOR, "[type = 'submit']")
    window.click()

    second_window = site.driver.window_handles[1]
    first_window = site.driver.window_handles[0]

    site.driver.switch_to.window(second_window)

    x = site.find_el(By.ID, 'input_value').text
    result = calc(x)

    site.find_el(By.ID, 'answer').send_keys(result)
    site.find_el('xpath', '//button').click()

finally:
    time.sleep(5)
    site.close_page()