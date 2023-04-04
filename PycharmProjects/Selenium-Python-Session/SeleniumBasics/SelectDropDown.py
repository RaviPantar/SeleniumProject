import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://www.orangehrm.com/orangehrm-30-day-trial/")
ele_indus = driver.find_element(By.ID, 'Form_submitForm_Country')
#Select(ele_indus).select_by_value("India")
Select(ele_indus).select_by_index(4)


time.sleep(2)
driver.quit()