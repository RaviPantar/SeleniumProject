import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://the-internet.herokuapp.com/windows")
driver.maximize_window()
driver.find_element(By.XPATH, "//a[contains(text(),'Click Here')]").click()
time.sleep(2)
window = driver.window_handles
driver.switch_to.window(window[1])
time.sleep(5)
print(driver.find_element(By.TAG_NAME, "h3").text)

#"window.scrollBy(0,document.body.scrollHeight);"
driver.get_screenshot_as_file("scn.png")
