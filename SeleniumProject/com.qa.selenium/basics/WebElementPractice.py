import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.maximize_window()

# static_dropdown
dropdown = Select(driver.find_element(By.ID, "exampleFormControlSelect1"))
driver.maximize_window()
time.sleep(10)
dropdown.select_by_index(1)
time.sleep(10)
