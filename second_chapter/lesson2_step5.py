import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from classes import browser_init
from classes.browser_init import Browser

browser = Browser()
browser.open_page("https://SunInJuly.github.io/execute_script.html")
button = browser.find_el(By.TAG_NAME, "button")

### JS скрипт, который проскролит страницу по указанным параметрам
# browser.driver.execute_script("window.scrollBy(0, 100);")
### JS скрипт, которой делает кнопку закрытую футером - видимой для нажатия
browser.driver.execute_script("return arguments[0].scrollIntoView(true);", button)
button.click()

time.sleep(5)
browser.close_page()