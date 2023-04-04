import time

import pytest
from utilities.BaseClass import BaseClass
from pageObjects.HomePage import HomePage


class TestHomePage(BaseClass):

    def test_formsubmission(self, getData):
        log = self.getLogger()
        homepage = HomePage(self.driver)
        homepage.getName().send_keys(getData["FirstName"])
        log.info("First Name is"+getData["FirstName"])
        homepage.getEmail().send_keys(getData["Email"])
        log.info("First Name is" + getData["Email"])
        homepage.getPassword().send_keys(getData["Pass"])
        log.info("First Name is" + getData["Pass"])
        homepage.getBioSex(getData["sex"])
        log.info("First Name is" + getData["sex"])
        homepage.getCheckbox().click()
        homepage.getStatus("Employed").click()
        homepage.getDOB().send_keys("28-07-1994")
        homepage.getSubmit().click()
        log.info("submission success")
        text = homepage.getMsg().text
        assert "Most!" in text
        self.driver.refresh()

    @pytest.fixture(params=[{"FirstName": "Ravi", "Email": "Pantar", "Pass": "ESCS", "sex": "Male"},
                            {"FirstName": "Raju", "Email": "Paasin@", "Pass": "ESCS@ascs", "sex": "Female"}])
    def getData(self, request):
        return request.param

    #@pytest.fixture(params=HomePageData.getTestData("Testcase2"))
    #def getData(self, request):
        #return request.param
