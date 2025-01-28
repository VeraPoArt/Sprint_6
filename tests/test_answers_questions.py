import pytest
from conftest import base_url
from locators.faq_page import *
from data import *
from pages.faq_page import FaqPage


@pytest.mark.parametrize("question_locator, answer_locator, expected_answer", [
    (rental_price_locator, rental_price_text_locator, rental_price),
    (rental_policy_single_order_locator, rental_policy_single_order_text_locator, rental_policy_single_order),
    (rental_period_locator, rental_period_text_locator, rental_period),
    (scooter_availability_locator, scooter_availability_text_locator, scooter_availability),
    (support_contact_locator, support_contact_text_locator, support_contact),
    (scooter_battery_locator, scooter_battery_text_locator, scooter_battery),
    (order_cancellation_locator, order_cancellation_text_locator, order_cancellation),
    (delivery_area_locator, delivery_area_text_locator, delivery_area)
])
def test_question_answer(driver, question_locator, answer_locator, expected_answer, base_url):
    # Создаем объект страницы
    page = FaqPage(driver)
    # Открываем страницу
    page.open(f"{base_url}")
    # Клик на вопрос
    page.click_question(question_locator)
    # Получаем текст ответа
    actual_answer = page.get_answer_text(answer_locator)
    # Проверяем, что ответ соответствует ожидаемому
    assert actual_answer == expected_answer, f"Expected: {expected_answer}, but got: {actual_answer}"
