from selenium.webdriver.support.wait import WebDriverWait
import allure

from locators.main_page import COOKIE_BUTTON_LOCATOR, LOGIN_BUTTON_HEADER
from locators.rules_page import RULES_BUTTON_LOCATOR
from .base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC
import allure
from selenium.webdriver.support import expected_conditions as EC

from locators.header_page import *
from .base_page import BasePage


class MainPage(BasePage):

    @allure.step("Ожидание появления логотипа 'Яндекс'")
    def wait_for_yandex_logo(self):
        self.wait_for_element_to_be_visible(YANDEX_LOGO)  # Используем метод ожидания из BasePage

    @allure.step("Ожидание появления логотипа 'Самокат'")
    def wait_for_samokat_logo(self):
        self.wait_for_element_to_be_visible(SAMOKAT_LOGO)  # Используем метод ожидания из BasePage

    @allure.step("Нажатие на логотип 'Яндекс'")
    def click_logo_yandex(self):
        self.find_element(*YANDEX_LOGO).click()

    @allure.step("Нажатие на логотип 'Самокат'")
    def click_logo_samokat(self):
        self.find_element(*SAMOKAT_LOGO).click()

    @allure.step("Нажатие на кнопку 'Заказать'")
    def click_button_login_header(self, button):
        if button == "HEADER":
            self.find_element(*LOGIN_BUTTON_HEADER).click()
        elif button == "RULES":
            self.find_element(*RULES_BUTTON_LOCATOR).click()

    @allure.step("Нажатие на кнопку 'Да все привыкли'")
    def click_cookie_button(self):
        self.find_element(*COOKIE_BUTTON_LOCATOR).click()



