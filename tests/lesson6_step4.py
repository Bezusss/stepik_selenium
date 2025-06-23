import pytest
from classes import browser_init
from classes.browser_init import Browser
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math

answer = math.log(int(time.time()))

test_links = [
    "https://stepik.org/lesson/236895/step/1",
    "https://stepik.org/lesson/236896/step/1",
    "https://stepik.org/lesson/236897/step/1",
    "https://stepik.org/lesson/236898/step/1",
    "https://stepik.org/lesson/236899/step/1",
    "https://stepik.org/lesson/236903/step/1",
    "https://stepik.org/lesson/236904/step/1",
    "https://stepik.org/lesson/236905/step/1"
]

@pytest.mark.parametrize('url', test_links)
def test_login_on_stepik_and_complite_task(browser, url):
    try:
        browser.open_page(url)
        wait = WebDriverWait(browser.driver, 10)
        wait.until(EC.element_to_be_clickable((By.ID, 'ember479'))).click()

        wait.until(EC.visibility_of_element_located((By.ID,'id_login_email'))).send_keys('<Почта>')
        browser.find_el(By.ID, 'id_login_password').send_keys('<Пароль>')

        browser.find_el('xpath', '//button[text()="Войти"]').click()
        time.sleep(5)
        ### Ввод ответа
        wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,"[placeholder='Напишите ваш ответ здесь...']"))).send_keys(answer)
        wait.until(EC.element_to_be_clickable(('xpath',"//button[text()='Отправить']"))).click()

        answer_of_stepik = wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'smart-hints__hint')))

        assert answer_of_stepik.text == 'Correct!', 'Задание не решено'

    finally:
        time.sleep(5)
        browser.close_page()
