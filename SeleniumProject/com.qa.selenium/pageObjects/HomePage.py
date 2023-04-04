from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from pageObjects.CheckOutPage import CheckOutPage


class HomePage:
    shop = (By.XPATH, "//a[contains(text(),'Shop')]")
    Name = (By.NAME, "name")
    Email = (By.NAME, "email")
    Password = (By.ID, "exampleInputPassword1")
    checkbox = (By.ID, 'exampleCheck1')
    sex = (By.XPATH, "//select[@id='exampleFormControlSelect1']")
    status = (By.XPATH, "//div[@class='form-check form-check-inline']")
    bday = (By.XPATH, "//input[@name='bday']")
    submit = (By.XPATH, "//input[@value='Submit']")
    success = (By.XPATH, "//*[contains(text(),'Success!')]")

    def __init__(self, driver):
        self.driver = driver

    def shopItem(self):
        self.driver.find_element(*HomePage.shop).click()
        checkoutPage = CheckOutPage(self.driver)
        return checkoutPage

    def getName(self):
        return self.driver.find_element(*HomePage.Name)

    def getEmail(self):
        return self.driver.find_element(*HomePage.Email)

    def getPassword(self):
        return self.driver.find_element(*HomePage.Password)

    def getCheckbox(self):
        return self.driver.find_element(*HomePage.checkbox)

    def getBioSex(self, text):
        return Select(self.driver.find_element(*HomePage.sex)).select_by_visible_text(text)

    def getStatus(self, text):
        status = self.driver.find_elements(*HomePage.status)
        for i in status:
            if (i.is_selected() == False):
                if i.text == text:
                    break
        return i

    def getDOB(self):
        return self.driver.find_element(*HomePage.bday)

    def getSubmit(self):
        return self.driver.find_element(*HomePage.submit)

    def getMsg(self):
        return self.driver.find_element(*HomePage.success)
