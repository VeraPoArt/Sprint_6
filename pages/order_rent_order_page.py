from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from locators.order_form_order_page import *
from locators.order_rent_order_page import *
from locators.popup_order_page import *
from pages.urls import URLs
from .base_page import BasePage
from locators.main_page import *
from selenium.webdriver.support import expected_conditions as EC
import allure
from selenium.webdriver.common.by import By
import re  # Импортируем модуль для работы с регулярными выражениями
from data import *
from locators.order_rent_order_page import *





class RentFormOrderPage(BasePage, URLs):


    @allure.step("Открытие главной страницы")
    def open(self, url=URLs.BASE_URL):  # Добавляем параметр url с значением по умолчанию
        self.driver.get(url)  # Открываем переданный URL

    @allure.step("Ввод даты доставки: {day}")
    def enter_delivery_date(self, day):
        self.find_element(*INPUT_DELIVERY_DATE).click()  # Кликаем на поле даты
        if day == "Сегодня":    
            self.find_element(*CALENDAR_DAY_1).click()  # Кликаем на сегодняшний день
        elif day == "Завтра":
            self.find_element(*CALENDAR_DAY_2).click()  # Кликаем на завтрашний день

    @allure.step("Выбор продолжительности аренды: {renta}")
    def select_duration(self, renta):
        self.click(DROPDOWN_DURATION)  # Кликаем на выпадающий список
        self.click(DROPDOWN_OPTION)  # Выбираем "двое суток"

    @allure.step("Клик на чекбокс")
    def select_checkbox(self):
        self.click(CHECKBOX)  # Кликаем на чекбокс

    @allure.step("Ввод комментария: {comment}")
    def enter_comment(self, comment):
        self.send_keys(COMMENT_INPUT, comment)  # Вводим комментарий

    @allure.step("Клик на кнопку 'Заказать'")
    def click_order_button(self):
        self.click(ORDER_BUTTON)  # Кликаем на кнопку "Заказать"

    @allure.step("Ожидание видимости попапа")
    def wait_for_popup(self):
        self.wait_for_element_to_be_visible(POPUP_HEADER)  # Ожидаем видимости попапа

