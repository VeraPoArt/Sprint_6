from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from locators.main_page import COOKIE_BUTTON_LOCATOR, SCOOTER_IMAGE_LOCATOR
from pages.main_page import MainPage
from pages.urls import URLs
from .base_page import BasePage
from locators.faq_page import *
from locators.main_page import SCOOTER_IMAGE_LOCATOR
import allure

class FaqPage(BasePage, URLs):
    @allure.step("Открытие главной страницы")
    def open(self, url=URLs.BASE_URL):  # Добавляем параметр url с значением по умолчанию
        self.driver.get(url)  # Открываем переданный URL

    @allure.step("Нажатие на кнопку 'Да все привыкли'")
    def click_cookie_button_faq(self):
        self.find_element(*COOKIE_BUTTON_LOCATOR).click()

    @allure.step("Ожидание исчезновения изображения с атрибутом 'alt=\"Scooter blueprint\"'")
    def wait_for_image_to_disappear(self):
        WebDriverWait(self.driver, 10).until(
            EC.invisibility_of_element_located(SCOOTER_IMAGE_LOCATOR)
        )

    @allure.step("Клик на вопрос")
    def click_question(self, question_locator):
        question_element = self.wait_for_element_to_be_visible(question_locator)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", question_element)
        self.wait_for_image_to_disappear()
        self.wait_for_element_to_be_visible(question_locator)
        question_element.click()

    @allure.step("Получение текста ответа")
    def get_answer_text(self, answer_locator):
        return self.get_text(*answer_locator)  # Используем метод get_text из BasePage
    



