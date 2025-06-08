import time
from classes import browser_init
from classes.browser_init import Browser

browser = Browser()
browser.driver.execute_script("document.title='Script"
                              " executing';alert('Robots at work');")

time.sleep(5)
browser.close_page()