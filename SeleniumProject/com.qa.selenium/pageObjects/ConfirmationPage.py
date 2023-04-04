from selenium.webdriver.common.by import By


class ConfirmationPage:
    country = (By.XPATH, "//input[@id='country']")
    purchase = (By.XPATH, "//input[@value='Purchase']")
    success = (By.XPATH, "//*[contains(text(),'Success!')]")

    def __init__(self, driver):
        self.driver = driver

    def selcountry(self):
        return self.driver.find_element(*ConfirmationPage.country)

    def btn_purchase(self):
        return self.driver.find_element(*ConfirmationPage.purchase)

    def success_msg(self):
        return self.driver.find_element(*ConfirmationPage.success)
