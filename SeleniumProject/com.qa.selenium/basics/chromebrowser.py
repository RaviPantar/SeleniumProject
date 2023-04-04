from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get("https://facebook.com")
driver.maximize_window()
print(driver.title)
print(driver.current_url)
driver.back()
driver.refresh()
driver.forward()
driver.close()