import time

import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from locators.header_page import SAMOKAT_URL
from pages.main_page import MainPage

@allure.testcase("Проверка функциональности логотипа Самокат")
@allure.title("Проверка перехода по клику на логотип Самокат")
@allure.severity(allure.severity_level.NORMAL)  # Уровень критичности: нормальный
def test_logo_samokat(driver, base_url):
    page = MainPage(driver)
    page.open(f"{base_url}order")
    page.click_logo_samokat()
    WebDriverWait(driver, 20).until(
        EC.url_to_be(SAMOKAT_URL)
    )
    assert driver.current_url == SAMOKAT_URL