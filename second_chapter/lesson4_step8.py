import time

from classes import browser_init
from classes.browser_init import Browser
import math
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

link = 'http://suninjuly.github.io/explicit_wait2.html'
site = Browser()

try:
    site.open_page(link)
    # site.driver.implicitly_wait(5)

    price = WebDriverWait(site.driver, 12).until(EC.text_to_be_present_in_element((By.ID, 'price'),'$100'))

    site.find_el(By.ID,'book').click()

    x = site.find_el(By.ID, 'input_value')
    result = calc(x.text)

    site.find_el(By.ID, 'answer').send_keys(result)
    site.find_el(By.ID,'solve').click()

finally:
    time.sleep(10)
    site.close_page()