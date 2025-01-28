from selenium.webdriver.support.wait import WebDriverWait
import allure

from locators.main_page import LOGIN_BUTTON_HEADER
from .base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC
import allure
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from locators.base_page import *
from .base_page import BasePage


class MainPage(BasePage):

    @allure.step("Нажатие на логотип 'Яндекс'")
    def click_logo_yandex(self):
        self.find_element(*YANDEX_LOGO).click()

    @allure.step("Нажатие на логотип 'Самокат'")
    def click_logo_samokat(self):
        self.find_element(*SAMOKAT_LOGO).click()

    @allure.step("Нажатие на кнопку 'Заказать'")
    def click_button_login_header(self):
        self.find_element(*LOGIN_BUTTON_HEADER).click()



