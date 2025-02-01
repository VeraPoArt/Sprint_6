from selenium.webdriver.common.by import By

from datetime import datetime, timedelta

# Получаем завтрашнюю дату
tomorrow = datetime.now() + timedelta(days=1)
# Извлекаем день месяца (например, 2 для 2 февраля)
tomorrow_day = tomorrow.day
# Формируем нужный класс для завтрашнего дня (например, для 2 февраля это будет react-datepicker__day--002)
tomorrow_class = f'react-datepicker__day--{tomorrow_day:03}'

# Создаём локатор с динамически вычисленным классом
CALENDAR_DAY_2 = (By.CSS_SELECTOR, f'div.react-datepicker__day.{tomorrow_class}')


HEADER_RENT = (By.XPATH, "//div[contains(@class, 'Order_Header__BZXOb') and text()='Про аренду']") #Локатор заголовка "Про аренду"

# Локаторы для страницы заказа самоката
INPUT_DELIVERY_DATE = (By.CSS_SELECTOR, 'input[placeholder="* Когда привезти самокат"]')
CALENDAR_DAY = (By.CSS_SELECTOR, 'div.react-datepicker__day.react-datepicker__day--today')  

CALENDAR_DAY_1 = (By.CSS_SELECTOR, 'div.react-datepicker__day.react-datepicker__day--today')  # Локатор для первой станции метро
#CALENDAR_DAY_2 = (By.CSS_SELECTOR, 'div.react-datepicker__day.react-datepicker__day--tomorrow')
DROPDOWN_DURATION = (By.CSS_SELECTOR, '.Dropdown-control')
DROPDOWN_OPTION = (By.CSS_SELECTOR, 'div.Dropdown-option:nth-child(2)')  # Выбор "сутки"
CHECKBOX = (By.CSS_SELECTOR, 'input#black')
COMMENT_INPUT = (By.CSS_SELECTOR, 'input[placeholder="Комментарий для курьера"]')
ORDER_BUTTON = (By.XPATH, "//button[contains(@class, 'Button_Button__ra12g') and contains(@class, 'Button_Middle__1CSJM') and text()='Заказать']")


