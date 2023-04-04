import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome("E:\\Testing\\Python\\Drivers\\chromedriver.exe")
driver.get("https://www.google.com")


driver.find_element(By.NAME, 'q').send_keys("Ravi Pantar")
optionlist = driver.find_elements(By.CSS_SELECTOR, 'ul,bw4e9b,li,span')
print(len(optionlist))
list(optionlist)
for ele in optionlist:
    print(optionlist.index(ele))

time.sleep(2)
driver.quit()
