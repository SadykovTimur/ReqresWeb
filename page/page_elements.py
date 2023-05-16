from page.base_page import BasePage
from locators.elements_locators import ResponseLocators



class ReqresResponse(BasePage):
    locators = ResponseLocators

    def check_status_code(self):
        self.element_is_clickable(self.locators.POST).click()

    def check_response(self):
        self.element_is_clickable(self.locators.POST).click()
        a = self.element_is_visible(self.locators.RESPONSE).text
        return a



