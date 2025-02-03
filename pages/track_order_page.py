import allure
from .base_page import BasePage
from locators.track_order_page import ORDER_NUMBER_INPUT_LOCATOR
from pages.urls import URLs

class TrackOrderPage(BasePage, URLs):

    @allure.step("Открытие главной страницы")
    def open(self, url=URLs.BASE_URL):  # Добавляем параметр url с значением по умолчанию
        self.driver.get(url)  # Открываем переданный URL

    @allure.step("Получение номера заказа из поля ввода")
    def get_order_number_from_input(self):
        # Получаем значение из поля ввода с номером заказа
        return self.find_element(*ORDER_NUMBER_INPUT_LOCATOR).get_attribute("value")