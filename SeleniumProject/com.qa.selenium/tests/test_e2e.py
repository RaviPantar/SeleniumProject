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
        homepage.shopItem().click()
        self.driver.find_element(By.NAME, 'name').send_keys("Ravi Pantar")
        time.sleep(1)
        self.driver.find_element(By.NAME, 'email').send_keys("ravimpantar@gmail.com")
        time.sleep(1)
        self.driver.find_element(By.ID, 'exampleInputPassword1').send_keys("Escs@Ascs")
        time.sleep(1)
        Checkbox = self.driver.find_element(By.ID, 'exampleCheck1')
        if (Checkbox.is_selected() == False):
            self.driver.find_element(By.ID, 'exampleCheck1').click()
        time.sleep(1)
        Sel = Select(self.driver.find_element(By.XPATH, '//select[@id="exampleFormControlSelect1"]'))
        Sel.select_by_visible_text("Female")
        time.sleep(1)
        status = self.driver.find_elements(By.XPATH, '//div[@class="form-check form-check-inline"]')
        for i in status:
            if (i.is_selected() == False):
                if i.text == "Employed":
                    i.click()
        time.sleep(1)
        self.driver.find_element(By.XPATH, '//input[@name="bday"]').send_keys("28-07-1994")
        time.sleep(1)
        self.driver.find_element(By.XPATH, '//input[@value="Submit"]').click()
