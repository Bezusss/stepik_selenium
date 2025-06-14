from classes import browser_init
from classes.browser_init import Browser
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_registration1():

    link = 'http://suninjuly.github.io/registration1.html'
    test1 = Browser()

    try:
        test1.open_page(link)
        test1.find_el(By.CSS_SELECTOR, '[placeholder = "Input your first name"]').send_keys('Jim')
        test1.find_el(By.CSS_SELECTOR, '[placeholder = "Input your last name"]').send_keys('Milton')
        test1.find_el(By.CSS_SELECTOR, '[placeholder = "Input your email"]').send_keys('JM@mail.com')

        test1.find_el(By.CSS_SELECTOR, '[type="Submit"]').click()

        wait = WebDriverWait(test1.driver,5)
        success_msg = wait.until(EC.visibility_of_element_located(('xpath', '//h1'))).text

        assert "Congratulations! You have successfully registered!" in success_msg, "❌ Тест не пройден: сообщение об успехе не найдено"
        print("Тест успешно пройден!!!")

    finally:
        test1.close_page()

def test_registration2():
    link = 'http://suninjuly.github.io/registration1.html'
    test1 = Browser()

    try:
        test1.open_page(link)
        test1.find_el(By.CSS_SELECTOR, '[placeholder = "Input your first name"]').send_keys('Jim')
        test1.find_el(By.CSS_SELECTOR, '[placeholder = "Input your last name"]').send_keys('Milton')
        test1.find_el(By.CSS_SELECTOR, '[placeholder = "Input your email"]').send_keys('JM@mail.com')
        test1.find_el(By.CSS_SELECTOR, '[placeholder = "Input your phone:"]').send_keys('+694009009999')
        test1.find_el(By.CSS_SELECTOR, '[placeholder = "Input your address:"]').send_keys('California')

        test1.find_el(By.CSS_SELECTOR, '[type="Submit"]').click()

        wait = WebDriverWait(test1.driver,5)
        success_msg = wait.until(EC.visibility_of_element_located(('xpath', '//h1'))).text

        assert "Congratulations! You have successfully registered!" in success_msg, "❌ Тест не пройден: сообщение об успехе не найдено"
        print("Тест успешно пройден!!!")

    finally:
        test1.close_page()
