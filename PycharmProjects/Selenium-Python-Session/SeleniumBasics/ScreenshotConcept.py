from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

options = webdriver.ChromeOptions()
options.headless = True
driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
driver.implicitly_wait(3)
driver.get('https://www.rediff.com/')
time.sleep(3)
s=lambda X:driver.execute_script('')
# driver.get_screenshot_as_file('reddit_1.png')
S = lambda X: driver.execute_script('return document.body.parentNode.scroll' + X)
driver.set_window_size(S('Width'), S('Height'))
driver.find_element_by_tag_name('Body').screenshot('reditt_full_2.png')
time.sleep(3)
driver.quit()


