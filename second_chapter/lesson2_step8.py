from classes import browser_init
from classes.browser_init import Browser
import time
from selenium.webdriver.common.by import By
import os


site = Browser()
site.open_page('https://suninjuly.github.io/file_input.html')

try:
# Заполняем поля
    site.find_el(By.CSS_SELECTOR, "[name='firstname']").send_keys("Дмитрий")
    site.find_el(By.CSS_SELECTOR, "[name='lastname']").send_keys("Иванов")
    site.find_el(By.CSS_SELECTOR, "[name ='email']").send_keys("Нескажу")
# Указываем текущую директорию, затем путь до файла от текущей директории, записываем путь до файла в переменную
    current_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(current_dir, '../files/test.txt')
    aboslute_file_path = os.path.abspath(file_path)
# Передаем файл кнопке "Выберите файл"
    site.find_el(By.ID,'file').send_keys(aboslute_file_path)

    site.find_el('xpath','//button').click()


finally:
    time.sleep(5)
    site.close_page()