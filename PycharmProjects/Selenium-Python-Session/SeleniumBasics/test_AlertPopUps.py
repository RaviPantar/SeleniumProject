from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(12)
driver.get('https://mail.rediff.com/cgi-bin/login.cgi')
time.sleep(12)
driver.find_element(By.XPATH, "//input[@name='proceed']").click()
alert = driver.switch_to.alert
print(alert.text)
alert.accept()

driver.quit()
