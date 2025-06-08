from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

start_link = 'http://suninjuly.github.io/find_link_text'
true_link = str(math.ceil(math.pow(math.pi, math.e) * 10000))

try:
    # Открываем первую ссылку
    browser = webdriver.Chrome()
    browser.get(start_link)

    # Переход по валидной ссылке
    button_link = browser.find_element(By.LINK_TEXT, true_link)
    button_link.click()

    # Заполнение формы
    input1 = browser.find_element(By.TAG_NAME, "input")
    input1.send_keys("Ivan")
    input2 = browser.find_element(By.NAME, "last_name")
    input2.send_keys("Petrov")
    input3 = browser.find_element(By.CLASS_NAME, "city")
    input3.send_keys("Smolensk")
    input4 = browser.find_element(By.ID, "country")
    input4.send_keys("Russia")
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()


finally:
    time.sleep(10)
    browser.quit()
