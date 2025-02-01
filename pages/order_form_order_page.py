from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from locators.order_form_order_page import *
from locators.order_rent_order_page import *
from .base_page import BasePage
from locators.main_page import LOGIN_BUTTON_HEADER
from selenium.webdriver.support import expected_conditions as EC
import allure
from selenium.webdriver.common.by import By
from data import *
from locators.order_form_order_page import SELECT_METRO_1, SELECT_METRO_2  # Импортируем локаторы


class OrderFormOrderPage(BasePage):


    # Методы для взаимодействия с элементами


    @allure.step("Ввод имени ответственного")
    def enter_responsible_name(self, name):
        self.send_keys(INPUT_RESPONSIBLE, name)  # Используем send_keys


    @allure.step("Ввод фамилии ответственного")
    def enter_last_name(self, last_name):
        self.send_keys(INPUT_FIELD, last_name)  # Используем send_keys

    @allure.step("Ввод адреса")
    def enter_address(self, address):
        self.send_keys(INPUT_FIELD_WITH_PLACEHOLDER, address)  # Используем send_keys

    @allure.step("Выбор метро: {metro}")
    def select_metro(self, metro):
        self.find_element(*SELECT_SEARCH_INPUT).click()
        if metro == "Преображенская площадь":
            self.find_element(*SELECT_METRO_1).click()
        elif metro == "Сокольники":
            self.find_element(*SELECT_METRO_2).click()
        else:
            raise ValueError("Неизвестное метро")

    @allure.step("Ввод номера телефона")
    def enter_phone(self, phone):
        self.send_keys(SELECT_PHONE, phone)  # Используем send_keys

    @allure.step("Клик по кнопке 'Далее'")
    def click_next_button(self):
        self.click(ORDER_NEXT_BUTTON)  # Клик по кнопке

    @allure.step("Ожидание заголовка 'Про аренду'")
    def wait_for_header_rent(self):
        self.wait_for_element_to_be_visible(HEADER_RENT)  # Ожидание видимости заголовка




