from locators.popup_order_page import *
from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from locators.order_form_order_page import *
from locators.order_rent_order_page import *
from locators.popup_order_page import *
from .base_page import BasePage
from locators.main_page import *
from selenium.webdriver.support import expected_conditions as EC
import allure
from selenium.webdriver.common.by import By
import re


class PopupOrderPage(BasePage):

    @allure.step("Клик на кнопку 'Да'")
    def click_yes_button(self):
        self.click(YES_BUTTON_LOCATOR)  # Кликаем на кнопку "Да"

    @allure.step("Ожидание видимости попапа с текстом 'Заказ оформлен'")
    def wait_for_popup(self):
        # Ожидаем видимости элемента с текстом "Заказ оформлен"
        self.wait_for_element_to_be_visible(ORDER_CONFIRMED_TEXT_LOCATOR)

    @allure.step("Получение номера заказа")
    def get_order_number(self):
        # Ожидаем, пока элемент с номером заказа станет видимым
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(ORDER_NUMBER_LOCATOR))
        
        # Получаем текст элемента с номером заказа
        order_text = self.find_element(*ORDER_NUMBER_LOCATOR).text
        print(f"Текст с номером заказа: {order_text}")  # Отладочное сообщение
        match = re.search(r'\d{5,6}', order_text)  # Ищем 5 или 6 цифр подряд через регулярку
        return match.group(0)  # Возвращаем найденный номер (если не найден, будет выброшено исключение)
    
    @allure.step("Клик на кнопку 'Посмотреть статус'")
    def click_view_status_button(self):
        # Кликаем на кнопку "Посмотреть статус"
        self.click(VIEW_STATUS_BUTTON_LOCATOR)
        # Ожидание загрузки страницы отслеживания
        WebDriverWait(self.driver, 10).until(EC.url_contains("track"))