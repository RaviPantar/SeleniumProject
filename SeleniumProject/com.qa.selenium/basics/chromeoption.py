import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

chrome_option = webdriver.ChromeOptions()
chrome_option.add_argument("--start-maximized")
chrome_option.add_argument("headless")
chrome_option.add_argument("--ignore-certicate-errors")
driver = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_option)
driver.get("https://the-internet.herokuapp.com/windows")
print(driver.title)
