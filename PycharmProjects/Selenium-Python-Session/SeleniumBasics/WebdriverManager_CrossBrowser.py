import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

browserName = "Chrome"

if browserName == "Chrome":
    driver = webdriver.Chrome(ChromeDriverManager().install())
elif browserName == "firefox":
    driver = webdriver.firefox(GeckoDriverManager().install())
elif browserName == "safari":
    driver = webdriver.Safari()
else:
    print("Please select browser")

driver.implicitly_wait(5)
driver.get("http://practice.automationtesting.in/my-account/")

driver.find_element(By.ID, "username").send_keys("ravimpantar@gmail.com")
driver.find_element(By.ID, "password").send_keys("C@r4sale@rent")
driver.find_element(By.NAME, "login").click()

time.sleep(5)
driver.quit()
