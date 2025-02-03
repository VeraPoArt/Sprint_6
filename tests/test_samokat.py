import time

import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from pages.main_page import MainPage
from pages.urls import URLs

@allure.testcase("Проверка функциональности логотипа Самокат")
@allure.title("Проверка перехода по клику на логотип Самокат")
@allure.severity(allure.severity_level.NORMAL)  # Уровень критичности: нормальный
def test_logo_samokat(driver):
    page = MainPage(driver)
    page.open(f"{URLs.BASE_URL}order")
    page.click_logo_samokat()
    assert page.is_current_url_samokat(), "Текущий URL не соответствует ожидаемому!"