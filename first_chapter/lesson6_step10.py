from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link = "http://suninjuly.github.io/registration1.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    first_name_input = browser.find_element(By.CSS_SELECTOR, '.form-control.first[placeholder = "Input your first name"]')
    first_name_input.send_keys('Джош')
    last_name_input = browser.find_element(By.CSS_SELECTOR, '.form-control.second[placeholder = "Input your last name"]')
    last_name_input.send_keys('Дилдон')
    email_input = browser.find_element(By.CSS_SELECTOR, '.form-control.third')
    email_input.send_keys('joshdildon@gmail.com')
    sub_button = browser.find_element(By.CSS_SELECTOR, '.btn.btn-default')

    sub_button.click()

    time.sleep(2)

    welcome_text_elt = browser.find_element(By.TAG_NAME, 'h1')
    welcome_text_elt = welcome_text_elt.text

    assert "Congratulations! You have successfully registered!" == welcome_text_elt

finally:
    time.sleep(5)
    browser.quit()
