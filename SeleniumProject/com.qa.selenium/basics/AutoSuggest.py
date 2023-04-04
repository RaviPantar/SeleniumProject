import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get("https://rahulshettyacademy.com/dropdownsPractise/")
driver.maximize_window()

driver.find_element(By.XPATH, "//input[@id='autosuggest']").send_keys("Ind")
time.sleep(5)
countries = driver.find_elements(By.XPATH, "//li[@class='ui-menu-item']//a")

for country in countries:
    if country.text == "India":
        country.click()
        break
