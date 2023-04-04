from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(12)
driver.get('https://admin:admin@the-internet.herokuapp.com/basic_auth')
time.sleep(12)