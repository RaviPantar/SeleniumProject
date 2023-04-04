import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://mail.rediff.com/cgi-bin/login.cgi')
# element = WebDriverWait(driver, 10).until(lambda x: x.find_element_by_id("someId"))
wait = WebDriverWait(driver, 10)
driver.find_element(By.NAME, 'proceed').click()
alert = wait.until(ec.element_to_be_clickable(driver.find_element(By.ID, 'name')))



driver.quit()
