import pytest
from conftest import base_url
from locators.faq_page import *
from data import *
from pages.faq_page import FaqPage
from pages.base_page import BasePage
import allure

@allure.title('Проверка ответов на вопросы в FAQ')  # Декоратор для заголовка теста
@allure.description('На странице FAQ проверяем, что ответы на вопросы соответствуют ожидаемым значениям.')  # Описание теста
@allure.severity(allure.severity_level.NORMAL)  # Уровень серьезности

@pytest.mark.parametrize("question_locator, answer_locator, expected_answer", [
    (RENTAL_PRICE_LOCATOR, RENTAL_PRICE_TEXT_LOCATOR, rental_price),
    (RENTAL_POLICY_SINGLE_ORDER_LOCATOR, RENTAL_POLICY_SINGLE_ORDER_TEXT_LOCATOR, rental_policy_single_order),
    (RENTAL_PERIOD_LOCATOR, RENTAL_PERIOD_TEXT_LOCATOR, rental_period),
    (SCOOTER_AVAILABILITY_LOCATOR, SCOOTER_AVAILABILITY_TEXT_LOCATOR, scooter_availability),
    (SUPPORT_CONTACT_LOCATOR, SUPPORT_CONTACT_TEXT_LOCATOR, support_contact),
    (SCOOTER_BATTERY_LOCATOR, SCOOTER_BATTERY_TEXT_LOCATOR, scooter_battery),
    (ORDER_CANCELLATION_LOCATOR, ORDER_CANCELLATION_TEXT_LOCATOR, order_cancellation),
    (DELIVERY_AREA_LOCATOR, DELIVERY_AREA_TEXT_LOCATOR, delivery_area)
])
def test_question_answer(driver, question_locator, answer_locator, expected_answer, base_url):
    page = FaqPage(driver)
    
    page.open(f"{base_url}")

    page.click_question(question_locator)

    actual_answer = page.get_answer_text(answer_locator)

    assert actual_answer == expected_answer, f"Expected: {expected_answer}, but got: {actual_answer}"
