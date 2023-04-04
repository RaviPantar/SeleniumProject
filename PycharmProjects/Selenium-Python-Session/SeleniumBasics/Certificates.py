import time

from selenium import webdriver
from selenium.webdriver import DesiredCapabilities
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

# option = Options()
# option.add_argument('__allow-running-insecure-content')
# option.add_argument('__ignore-certificate-errors')

# desired_Capabilities = DesiredCapabilities().CHROME.copy()
# desired_Capabilities['acceptInsecureCerts'] = True

option = Options()
option.set_capability('acceptInsecureCerts', True)
driver = webdriver.Chrome(ChromeDriverManager().install(),chrome_options=option)  # options=option desired_capabilities=desired_Capabilities
time.sleep(3)
driver.get('https://expired.badssl.com/')
time.sleep(5)
profile = webdriver.FirefoxProfile()

driver.quit()
