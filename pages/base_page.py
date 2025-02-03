from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import allure
from selenium.common.exceptions import TimeoutException

from pages.urls import URLs

class BasePage:
    def __init__(self, driver, timeout=60):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    @allure.step("Открытие страницы")
    def open(self):
        self.driver.get(f'{URLs.BASE_URL}')

    @allure.step("Поиск элемента с локатором")
    def find_element(self, *locator):
        return self.driver.find_element(*locator)

    @allure.step("Поиск множества элементов с локатором")
    def find_elements(self, *locator):
        return self.driver.find_elements(*locator)

    @allure.step("Ожидание видимости элемента с локатором")
    def wait_for_element_to_be_visible(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))
         


    @allure.step("Ожидание кликабельности элемента с локатором")
    def wait_for_element_clickable(self, locator, timeout=60):
        WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable(locator)
        )
        return WebDriverWait(self.driver, timeout).until(
        EC.element_to_be_clickable(locator)
    )

    @allure.step("Получение текста элемента")
    def get_text(self, *locator):
        return self.find_element(*locator).text

    @allure.step("Клик по элементу")
    def click(self, locator):
        self.wait_for_element_to_be_visible(locator)  # Ожидание видимости элемента
        element = self.driver.find_element(*locator)  # Находим элемент
        element.click()  # Кликаем по элементу

    @allure.step("Ввод текста в элемент")
    def send_keys(self, locator, text):
        self.wait_for_element_to_be_visible(locator)  # Ожидание видимости элемента
        element = self.driver.find_element(*locator)  # Находим элемент
        element.clear()  # Очищаем поле перед вводом
        element.send_keys(text)  # Вводим текст