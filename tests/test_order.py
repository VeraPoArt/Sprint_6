import time

import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from data import Data, TestData
from locators.order_form_order_page import *
from locators.order_rent_order_page import *
from locators.popup_order_page import *
from locators.track_order_page import *
from pages.main_page import MainPage
from pages.order_form_order_page import OrderFormOrderPage
from pages.order_rent_order_page import RentFormOrderPage
from pages.popup_order_page import PopupOrderPage
from pages.track_order_page import TrackOrderPage
import re
import pytest

from pages.urls import URLs


@allure.testcase("Проверка функциональности оформления заказа с учетом задержек на клиентской стороне")
@allure.title("Проверка задержки отклика при оформлении заказа в клиентском интерфейсе")
@allure.severity(allure.severity_level.NORMAL)  


@pytest.mark.parametrize("data_set", [
    {
        "button": "HEADER",
        "name": Data.name_1,
        "sname": Data.sname_1,
        "address": Data.address_1,
        "metro": "Преображенская площадь",
        "telephone": Data.telephone_1,
        "day": "Сегодня",
        "renta": TestData.renta_1,
        "comment": Data.comment_1,
    },
    {
        "button": "RULES",
        "name": Data.name_2,
        "sname": Data.sname_2,
        "address": Data.address_2,
        "metro": "Сокольники",
        "telephone": Data.telephone_2,
        "day": "Завтра",
        "renta": TestData.renta_2,
        "comment": Data.comment_2,
    },
])
def test_order_form(driver, data_set):
    # Шаг 1: Открываем главную страницу и принимаем cookies
    page = MainPage(driver)
    page.open(f"{URLs.BASE_URL}")
    page.click_cookie_button()

    page.click_button_login_header(data_set["button"])

    # Шаг 3: Переходим на страницу заказа
    order_page = OrderFormOrderPage(driver)
    
    order_page.enter_responsible_name(data_set["name"])
    order_page.enter_last_name(data_set["sname"])
    order_page.enter_address(data_set["address"])

    # Шаг 5: Ожидаем, пока выпадающий список станет доступным для клика
    order_page.wait_for_search_input_clickable()
    # Шаг 7: Выбираем метро
    order_page.select_metro(data_set["metro"])

    # Шаг 8: Вводим номер телефона
    order_page.enter_phone(data_set["telephone"])

    # Шаг 9: Кликаем по кнопке "Далее"
    order_page.click_next_button()

    # Шаг 10: Ожидаем появления заголовка "Про аренду"
    order_page.wait_for_header_rent()

    # Шаг 11: Проверяем, что элемент 'Про аренду' видим
    assert order_page.get_header_rent_element() is not None, "Элемент 'Про аренду' не найден на странице!"  
    # Шаг 12: Переходим на страницу аренды
    rent_page = RentFormOrderPage(driver)

    # Шаг 13: Вводим дату доставки
    rent_page.enter_delivery_date(data_set["day"])

    # Шаг 14: Выбираем длительность аренды
    rent_page.select_duration(data_set["renta"])

    # Шаг 15: Выбираем чекбокс
    rent_page.select_checkbox()

    # Шаг 16: Вводим комментарий
    rent_page.enter_comment(data_set["comment"])

    # Шаг 17: Кликаем на кнопку "Заказать"
    rent_page.click_order_button()

    # Шаг 18: Ожидаем появления попапа
    rent_page.wait_for_popup()

    # Шаг 19: Проверяем, что попап отображается
    popup_page = PopupOrderPage(driver)
    assert popup_page.get_popup_header_element() is not None, "Попап не отображается или заголовок неверен!"    
    # Шаг 20: Подтверждаем заказ в попапе
    popup_page.click_yes_button()
    popup_page.wait_for_popup()

    # Шаг 21: Получаем номер заказа
    order_number = popup_page.get_order_number()

    # Шаг 22: Проверяем, что текст 'Заказ оформлен' отображается
    assert popup_page.get_order_confirmed_text_element() is not None, "Текст 'Заказ оформлен' не найден на странице!" 
    # Шаг 23: Кликаем на кнопку "Просмотр статуса"
    popup_page.click_view_status_button()
    # Шаг 24: Переходим на страницу отслеживания
    track_page = TrackOrderPage(driver)
    # Шаг 25: Получаем номер заказа с поля ввода на странице отслеживания
    tracked_order_number = track_page.get_order_number_from_input()
    # Шаг 26: Сравниваем номер заказа
    assert tracked_order_number == order_number, f"Номера заказов не совпадают! Ожидалось: {order_number}, получено: {tracked_order_number}"
    # Шаг 27: Обновляем страницу
