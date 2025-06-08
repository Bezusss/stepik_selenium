from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

link = 'https://suninjuly.github.io/math.html'
browser = webdriver.Chrome()

try:
    browser.get(link)
    x_element = browser.find_element(By.CSS_SELECTOR, '#input_value')
    x = x_element.text
    y = calc(x)
    result = browser.find_element(By.ID, 'answer')
    result.send_keys(y)
    time.sleep(2)
    robot_check = browser.find_element(By.ID, 'robotCheckbox')
    robot_check.click()
    time.sleep(2)
    robot_rule = browser.find_element(By.ID , 'robotsRule')
    robot_rule.click()
    time.sleep(2)
    submit = browser.find_element('xpath', '//button')
    submit.click()

finally:
    time.sleep(10)
    browser.quit()