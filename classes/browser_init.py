from selenium import webdriver
from selenium.webdriver.common import by

class Browser:
    def __init__(self):
        """Инициализация браузера (Chrome) при создании экземпляра класса"""
        self.driver = webdriver.Chrome()

    def open_page(self,url):
        """Открыть нужную страницу"""
        self.driver.get(url)

    def close_page(self):
        """Закрыть страницу"""
        self.driver.quit()

    def find_el(self, selector_type, locator):
        """Найти элемент на странице"""
        return self.driver.find_element(selector_type, locator)

    def find_elts(self, selector_type, locator):
        """Найти элеменеты на странице"""
        return self.driver.find_elements(selector_type, locator)
