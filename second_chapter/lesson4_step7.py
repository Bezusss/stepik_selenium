from classes import browser_init
from classes.browser_init import Browser
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


site = Browser()
link = 'http://suninjuly.github.io/wait2.html'
site.driver.implicitly_wait(5)
try:
    site.open_page(link)
    button = WebDriverWait(site.driver, 5).until(
        EC.element_to_be_clickable((By.ID, "verify"))
    )
    button.click()

    verify_message = site.find_el(By.ID, 'verify_message')
    assert 'successful' in verify_message.text

finally:
    site.close_page()
