from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(12)
driver.get('https://www.amazon.in/')
time.sleep(12)
driver.find_element(By.LINK_TEXT, 'Best Sellers').click()
driver.back()
time.sleep(2)
driver.forward()
time.sleep(2)
driver.quit()
