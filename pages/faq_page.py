from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .base_page import BasePage

class FaqPage(BasePage):
    def click_question(self, locator):
        question_element = self.wait_for_element_visible(locator)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", question_element)
        question_element.click()

    def get_answer_text(self, answer_locator):
        return self.get_text(*answer_locator)  # Используем метод get_text из BasePage

