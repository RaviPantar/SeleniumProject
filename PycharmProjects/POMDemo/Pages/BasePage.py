from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

class BasePage:

    def __init__(self,driver):
           self.driver=driver

    def do_click(self,by_locator):
        WebDriverWait(self.driver,5).until(ec.visiblity_of_element_located(by_locator)).click()

    def do_send_keys(self,by_locator,text):
        WebDriverWait(self.driver,5).until(ec.visiblity_of_element_located(by_locator)).click(text)

    def get_element_text(self):
        element = WebDriverWait(self.driver, 5).until(ec.visiblity_of_element_located(by_locator))
        return element.text

    def is_enabled(self,by_locator):
        element = WebDriverWait(self.driver, 5).until(ec.visiblity_of_element_located(by_locator))
        return bool(element)

    def get_title(self,title):
        WebDriverWait(self.driver, 5).until(ec.visiblity_of_element_located(by_locator))
        return self.driver.title

