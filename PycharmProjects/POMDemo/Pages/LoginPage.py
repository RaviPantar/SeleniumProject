from Pages.BasePage import BasePage
from selenium.webdriver.common.by import By

class LoginPage(BasePage):

    Email=(By.ID,'username')
    Password=(By.ID,'password')
    Login_Button=(By.NAME,'Login')

    def __init__(self,driver):
        super().__init__(driver)

    def get_login_page_title(self):
        return BasePage.get_title()
