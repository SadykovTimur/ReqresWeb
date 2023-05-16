from selenium.webdriver.common.by import By


class ResponseLocators:
    POST = (By.CSS_SELECTOR, 'li[data-id="register-successful"]')
    RESPONSE = (By.CSS_SELECTOR, 'pre[data-key="output-response"]')
