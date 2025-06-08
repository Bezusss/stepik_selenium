from classes import browser_init
from classes.browser_init import Browser
import time
import math
from selenium import webdriver
from selenium.webdriver.common.by import By


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

link = 'https://suninjuly.github.io/get_attribute.html'
test = Browser()

try:
    test.open_page(link)
    val = test.find_el(By.TAG_NAME, 'img')
### Узнаем значение "сундука" с помощью метода get_attribute
    res = val.get_attribute('valuex')
### Получаем результат функции "calc"
    result = calc(res)

    inp = test.find_el(By.ID, 'answer')
### Вводим результат выполнения функции в input
    inp.send_keys(result)

    rob_checkbox = test.find_el(By.ID, 'robotCheckbox')
    rob_checkbox.click()

    rob_radiobutton = test.find_el(By.ID, 'robotsRule')
    rob_radiobutton.click()

    final_click = test.find_el('xpath', '//button')
    final_click.click()


finally:
    time.sleep(10)
    test.close_page()