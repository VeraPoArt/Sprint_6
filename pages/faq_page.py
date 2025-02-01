from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .base_page import BasePage
from locators.faq_page import *
import allure

class FaqPage(BasePage):
    @allure.step("Клик на вопрос")
    def click_question(self, question_locator):
        question_element = self.wait_for_element_to_be_visible(question_locator)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", question_element)
        question_element.click()

    @allure.step("Получение текста ответа")
    def get_answer_text(self, answer_locator):
        return self.get_text(*answer_locator)  # Используем метод get_text из BasePage


