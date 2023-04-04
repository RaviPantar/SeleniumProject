from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(12)
driver.get('https://cgi-lib.berkeley.edu/ex/fup.html')
time.sleep(12)
driver.find_element(By.NAME, 'upfile').send_keys("C:\\Users\\UNIFY\\Desktop\\API.txt")
driver.find_element(By.XPATH, "//input[@type='submit']").click()
time.sleep(3)
driver.quit()
