from selenium.webdriver.common.by import By

rental_price_locator = (By.XPATH, ".//div[@id='accordion__heading-0']")
rental_price_text_locator = (By.XPATH, ".//div[@id='accordion__panel-0']")

rental_policy_single_order_locator = (By.XPATH, ".//div[@id='accordion__heading-1']")
rental_policy_single_order_text_locator = (By.XPATH, ".//div[@id='accordion__panel-1']")

rental_period_locator = (By.XPATH, ".//div[@id='accordion__heading-2']")
rental_period_text_locator = (By.XPATH, ".//div[@id='accordion__panel-2']")

scooter_availability_locator = (By.XPATH, ".//div[@id='accordion__heading-3']")
scooter_availability_text_locator = (By.XPATH, ".//div[@id='accordion__panel-3']")

support_contact_locator = (By.XPATH, ".//div[@id='accordion__heading-4']")
support_contact_text_locator = (By.XPATH, ".//div[@id='accordion__panel-4']")

scooter_battery_locator = (By.XPATH, ".//div[@id='accordion__heading-5']")
scooter_battery_text_locator = (By.XPATH, ".//div[@id='accordion__panel-5']")

order_cancellation_locator = (By.XPATH, ".//div[@id='accordion__heading-6']")
order_cancellation_text_locator = (By.XPATH, ".//div[@id='accordion__panel-6']")

delivery_area_locator = (By.XPATH, ".//div[@id='accordion__heading-7']")
delivery_area_text_locator = (By.XPATH, ".//div[@id='accordion__panel-7']")

list_question = [
    rental_price_locator,
    rental_policy_single_order_locator,
    rental_period_locator,
    scooter_availability_locator,
    support_contact_locator,
    scooter_battery_locator,
    order_cancellation_locator,
    delivery_area_locator
]
list_answer = [
    rental_price_text_locator,
    rental_policy_single_order_text_locator,
    rental_period_text_locator,
    scooter_availability_text_locator,
    support_contact_text_locator,
    scooter_battery_text_locator,
    order_cancellation_text_locator,
    delivery_area_text_locator
]

