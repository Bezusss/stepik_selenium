from selenium.webdriver.common.by import By
from classes import browser_init
from classes.browser_init import Browser
import time
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

link = 'https://suninjuly.github.io/execute_script.html'
site = Browser()
site.open_page(link)

try:
    x = int(site.find_el(By.ID, 'input_value').text)
    result = calc(x)

    site.driver.execute_script("window.scrollBy(0, 100);")

    site.find_el(By.ID, 'answer').send_keys(result)

    site.find_el(By.ID, 'robotsRule').click()
    site.find_el(By.ID,'robotCheckbox').click()

    site.find_el('xpath', '//button').click()

finally:
    time.sleep(5)
    site.close_page()
