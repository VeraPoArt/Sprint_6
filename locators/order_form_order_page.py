from selenium.webdriver.common.by import By
# Локатор для первого поля (Input_Responsible__1jDKN)
INPUT_RESPONSIBLE = (By.CSS_SELECTOR, '.Input_InputContainer__3NykH:nth-child(1) > .Input_Responsible__1jDKN')

# Локатор для второго поля (Input_Input__1iN_Z)
INPUT_FIELD = (By.CSS_SELECTOR, '.Input_InputContainer__3NykH:nth-child(2) > .Input_Input__1iN_Z')

# Локатор для поля Адрес
INPUT_FIELD_WITH_PLACEHOLDER = (By.CSS_SELECTOR, '.Input_InputContainer__3NykH:nth-child(3) > .Input_Input__1iN_Z')

# Локатор для выпадающего списка
SELECT_SEARCH_INPUT = (By.CSS_SELECTOR, '.select-search__input')

# Локатор для выбора метро

SELECT_METRO_1 = (By.XPATH, ".//div[text()='Преображенская площадь']")  # Локатор для первой станции метро
SELECT_METRO_2 = (By.XPATH, ".//div[text()='Сокольники']")  # Локатор для второй станции метро
# Локатор для телефона
SELECT_PHONE = (By.CSS_SELECTOR, ".Input_InputContainer__3NykH:nth-child(5) > .Input_Input__1iN_Z")


# Локатор для кнопки "Далее"
ORDER_NEXT_BUTTON = (By.CSS_SELECTOR, ".Button_Middle__1CSJM")

