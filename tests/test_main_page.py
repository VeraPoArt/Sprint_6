import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.main_page import MainPage


@allure.testcase("TMS-012", "Client Side Delay")
@allure.title("Проверка задержки на клиенте")
@allure.severity(allure.severity_level.NORMAL)

def test_01(driver2, base_url):
    page = MainPage(driver2)
    page.open(f"{base_url}")
    page.click_button_login_header()

def test_client_side_delay(driver2, base_url):
    page = MainPage(driver2)
    page.open(f"{base_url}")
    page.click_logo_yandex()
    window_handles = driver2.window_handles
    # Переключаемся на второе окно
    driver2.switch_to.window(window_handles[1])
    WebDriverWait(driver2, 10).until(
        EC.url_to_be('https://dzen.ru/?yredirect=true')
    )
    assert driver2.current_url == 'https://dzen.ru/?yredirect=true'
