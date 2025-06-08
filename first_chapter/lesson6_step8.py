from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link = 'http://suninjuly.github.io/find_xpath_form'

try:
    browser = webdriver.Chrome()
    browser.get(link)

    elements_fields = browser.find_elements(By.CLASS_NAME ,'form-control')
    for element in elements_fields:
        element.send_keys('test')

    true_button = browser.find_element('xpath', '//button[text()="Submit"]')
    true_button.click()

finally:
    time.sleep(15)
    browser.quit()

