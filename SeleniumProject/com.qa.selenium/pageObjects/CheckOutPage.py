from selenium.webdriver.common.by import By
from pageObjects.ConfirmationPage import ConfirmationPage

class CheckOutPage:
    product = (By.XPATH, "//*[contains(text(),'iphone X')]//following::div[1]//button")
    checkout = (By.XPATH, "//a[contains(text(),'Checkout')]")
    btn_checkout = (By.XPATH, "//button[contains(text(), 'Checkout')]")

    def __init__(self, driver):
        self.driver = driver

    def addProduct(self):
        return self.driver.find_element(*CheckOutPage.product)

    def checkOut(self):
        return self.driver.find_element(*CheckOutPage.checkout)

    def btncheckout(self):
        self.driver.find_element(*CheckOutPage.btn_checkout).click()
        return ConfirmationPage(self.driver)

