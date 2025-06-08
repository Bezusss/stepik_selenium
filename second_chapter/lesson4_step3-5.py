from classes import browser_init
from classes.browser_init import Browser
from selenium.webdriver.common.by import By
import time

site = Browser()
link = 'https://suninjuly.github.io/wait1.html'
site.driver.implicitly_wait(5)
try:
    site.open_page(link)
    site.find_el(By.ID, 'verify').click()

    verify_message = site.find_el(By.ID, 'verify_message')
    assert 'successful' in verify_message.text

finally:
    site.close_page()
