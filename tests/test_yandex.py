import time

import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from pages.main_page import MainPage
from pages.urls import URLs

@allure.testcase("Проверка функциональности логотипа Яндекс")
@allure.title("Проверка перехода по клику на логотип Яндекс")
@allure.severity(allure.severity_level.NORMAL) 


def test_client_side_delay(driver):
    page = MainPage(driver)
    page.open(f"{URLs.BASE_URL}order")
    page.click_logo_yandex()
    window_handles = driver.window_handles
    # Переключаемся на второе окно
    driver.switch_to.window(window_handles[1])
    page.wait_for_url_yandex()
    assert page.is_current_url_yandex(), "Текущий URL не соответствует ожидаемому!"



