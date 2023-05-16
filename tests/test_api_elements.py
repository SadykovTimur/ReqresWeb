from selenium.webdriver.common.by import By
from page.page_elements import ReqresResponse


class TestElements:

    class TestReqresResponse:

        def test_check_status_code(self, driver):
            page = ReqresResponse(driver, 'https://reqres.in/')
            page.open()
            driver.execute_script("scrollBy(0,+1200);")
            page.check_status_code()
            assert driver.find_element(By.CSS_SELECTOR, 'span[class="response-code"]').text == '200'
            print('Test successful  "status code is 200"')


        def test_check_response(self, driver):
            page = ReqresResponse(driver, 'https://reqres.in/')
            page.open()
            driver.execute_script("scrollBy(0,+1200);")
            a = page.check_response()
            result = ''.join(a.split())
            assert result == '{"id":4,"token":"QpwL5tke4Pnpja7X4"}'
            print(result)
            print('Test successful "Response correct"')

