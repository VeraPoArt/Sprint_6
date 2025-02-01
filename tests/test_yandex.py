import time

import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from locators.header_page import YANDAX_URL
from pages.main_page import MainPage

@allure.testcase("Проверка функциональности логотипа Яндекс")
@allure.title("Проверка перехода по клику на логотип Яндекс")
@allure.severity(allure.severity_level.NORMAL) 


def test_client_side_delay(driver, base_url):
    page = MainPage(driver)
    page.open(f"{base_url}")
    page.click_logo_yandex()
    window_handles = driver.window_handles
    # Переключаемся на второе окно
    driver.switch_to.window(window_handles[1])
    WebDriverWait(driver, 20).until(
        EC.url_to_be(YANDAX_URL)
    )
    assert driver.current_url == YANDAX_URL


