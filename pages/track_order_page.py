import allure
from .base_page import BasePage
from locators.track_order_page import ORDER_NUMBER_INPUT_LOCATOR

class TrackOrderPage(BasePage):
    @allure.step("Получение номера заказа из поля ввода")
    def get_order_number_from_input(self):
        # Получаем значение из поля ввода с номером заказа
        return self.find_element(*ORDER_NUMBER_INPUT_LOCATOR).get_attribute("value")