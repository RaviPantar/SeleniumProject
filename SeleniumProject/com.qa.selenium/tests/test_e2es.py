import time
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from utilities.BaseClass import BaseClass
from pageObjects.HomePage import HomePage


# @pytest.mark.usefixtures("setup")
class TestOne(BaseClass):

    def test_e2e(self):
        homepage = HomePage(self.driver)
        checkOutPage = homepage.shopItem()
        checkOutPage.addProduct().click()
        checkOutPage.checkOut().click()
        confirmationPage = checkOutPage.btncheckout()
        confirmationPage.selcountry().send_keys("India")
        self.verifyLinkPresence("India")
        confirmationPage.btn_purchase().click()
        msg = confirmationPage.success_msg().text
        assert "Success!" in msg
