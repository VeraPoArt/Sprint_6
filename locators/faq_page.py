from selenium.webdriver.common.by import By

RENTAL_PRICE_LOCATOR = (By.XPATH, ".//div[@id='accordion__heading-0']")
RENTAL_PRICE_TEXT_LOCATOR = (By.XPATH, ".//div[@id='accordion__panel-0']")

RENTAL_POLICY_SINGLE_ORDER_LOCATOR = (By.XPATH, ".//div[@id='accordion__heading-1']")
RENTAL_POLICY_SINGLE_ORDER_TEXT_LOCATOR = (By.XPATH, ".//div[@id='accordion__panel-1']")

RENTAL_PERIOD_LOCATOR = (By.XPATH, ".//div[@id='accordion__heading-2']")
RENTAL_PERIOD_TEXT_LOCATOR = (By.XPATH, ".//div[@id='accordion__panel-2']")

SCOOTER_AVAILABILITY_LOCATOR = (By.XPATH, ".//div[@id='accordion__heading-3']")
SCOOTER_AVAILABILITY_TEXT_LOCATOR = (By.XPATH, ".//div[@id='accordion__panel-3']")

SUPPORT_CONTACT_LOCATOR = (By.XPATH, ".//div[@id='accordion__heading-4']")
SUPPORT_CONTACT_TEXT_LOCATOR = (By.XPATH, ".//div[@id='accordion__panel-4']")

SCOOTER_BATTERY_LOCATOR = (By.XPATH, ".//div[@id='accordion__heading-5']")
SCOOTER_BATTERY_TEXT_LOCATOR = (By.XPATH, ".//div[@id='accordion__panel-5']")

ORDER_CANCELLATION_LOCATOR = (By.XPATH, ".//div[@id='accordion__heading-6']")
ORDER_CANCELLATION_TEXT_LOCATOR = (By.XPATH, ".//div[@id='accordion__panel-6']")

DELIVERY_AREA_LOCATOR = (By.XPATH, ".//div[@id='accordion__heading-7']")
DELIVERY_AREA_TEXT_LOCATOR = (By.XPATH, ".//div[@id='accordion__panel-7']")

LIST_QUESTION = [
    RENTAL_PRICE_LOCATOR,
    RENTAL_POLICY_SINGLE_ORDER_LOCATOR,
    RENTAL_PERIOD_LOCATOR,
    SCOOTER_AVAILABILITY_LOCATOR,
    SUPPORT_CONTACT_LOCATOR,
    SCOOTER_BATTERY_LOCATOR,
    ORDER_CANCELLATION_LOCATOR,
    DELIVERY_AREA_LOCATOR
]

LIST_ANSWER = [
    RENTAL_PRICE_TEXT_LOCATOR,
    RENTAL_POLICY_SINGLE_ORDER_TEXT_LOCATOR,
    RENTAL_PERIOD_TEXT_LOCATOR,
    SCOOTER_AVAILABILITY_TEXT_LOCATOR,
    SUPPORT_CONTACT_TEXT_LOCATOR,
    SCOOTER_BATTERY_TEXT_LOCATOR,
    ORDER_CANCELLATION_TEXT_LOCATOR,
    DELIVERY_AREA_TEXT_LOCATOR
]

