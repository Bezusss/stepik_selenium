from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link = 'https://suninjuly.github.io/math.html'
browser = webdriver.Chrome()
browser.get(link)

try:
# Чекаем радиокнопку человека (что она есть)
    # people_radio = browser.find_element(By.ID, 'peopleRule')
    # people_checked = people_radio.get_attribute('checked')
    # print('value of "people radio": ', people_checked)
    #
    # assert people_checked == "true",'''People radio
    #  is not selected by default'''

# Чекаем радиокнопку робота (что ее нет)
    robots_radio = browser.find_element(By.ID, 'robotsRule')
    robots_checked = robots_radio.get_attribute('checked')
    print('value of "robotsRule": ', robots_checked)

    assert robots_checked is None

finally:
    time.sleep(1)
    browser.quit()