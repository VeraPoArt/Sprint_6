import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


#@pytest.fixture(scope="session")
#def base_url():
    #return "https://qa-scooter.praktikum-services.ru/"



@pytest.fixture(scope="function")
def driver():
    # Создаем и возвращаем драйвер для Firefox
    driver = webdriver.Firefox()
    driver.maximize_window()
    yield driver
    driver.quit()

