from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

options = webdriver.ChromeOptions()
options.headless = False
options.add_argument('--incognito')
#options.add_argument('--headless')
driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
driver.implicitly_wait(8)
driver.get('https://www.amazon.in/')
time.sleep(8)
print(driver.title)
driver.quit()
