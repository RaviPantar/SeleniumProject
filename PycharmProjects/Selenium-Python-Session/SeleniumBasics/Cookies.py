from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(3)
driver.get('https://www.rediff.com/')
time.sleep(12)
driver.delete_all_cookies()
cookies = driver.get_cookies()
for cook in cookies:
    print(cook)


driver.quit()
