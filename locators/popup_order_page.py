from selenium.webdriver.common.by import By

POPUP_HEADER = (By.XPATH, "//div[contains(text(), 'Хотите оформить заказ?')]")
YES_BUTTON_LOCATOR = (By.XPATH, "//button[contains(@class, 'Button_Button__ra12g') and contains(@class, 'Button_Middle__1CSJM') and text()='Да']")
ORDER_CONFIRMED_TEXT_LOCATOR = (By.XPATH, "//div[contains(text(), 'Заказ оформлен')]")
ORDER_NUMBER_LOCATOR = (By.XPATH, "//div[contains(@class, 'Order_Text__2broi')]")
VIEW_STATUS_BUTTON_LOCATOR = (By.XPATH, "//button[contains(@class, 'Button_Button__ra12g') and contains(@class, 'Button_Middle__1CSJM') and text()='Посмотреть статус']")