import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://www.amazon.in/')
time.sleep(15)
best_sellers = driver.find_element(By.XPATH, "//a[contains(text(),'Best Sellers')]")
time.sleep(5)
# driver.execute_script("arguments[0].click();", best_sellers)
# title = driver.execute_script("return document.title;")
# print(title)
# driver.execute_script("history.go(0);")
# inner_text = driver.execute_script("return document.documentElement.innerText;")
#driver.execute_script("arguments[0].style.border='3px solid red'", best_sellers)
time.sleep(5)
# driver.execute_script("alert('hello selenium');")
start_here = driver.find_element(By.LINK_TEXT, 'Start here')
# driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
# time.sleep(5)
driver.execute_script("arguments[0].scrollIntoView(true);", start_here)
time.sleep(5)
driver.quit()
driver.execute_script()