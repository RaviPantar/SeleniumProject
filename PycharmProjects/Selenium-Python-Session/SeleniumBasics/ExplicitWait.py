from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import time

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://app.hubspot.com/login')
print(driver.title)
wait = WebDriverWait(driver, 15)
wait.until(ec.title_contains('Login'))
print(driver.title)

#email_id = wait.until(ec.presence_of_element_located((By.ID, 'username')))

driver.quit()
