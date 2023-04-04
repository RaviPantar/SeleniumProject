import time

import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


def setup_module():
    global driver
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.implicitly_wait(10)
    driver.delete_all_cookies()
    driver.get("http://www.google.com")


def teardown_module():
    driver.quit()


def test_google_title():
    assert driver.title == "Google"


def test_google_url():
    print(driver.current_url)
    assert driver.current_url == "https://www.google.com/?gws_rd=ssl"


#pip install pytest-html
# pytest test_google_test.py -v -s --html=google_test_report.html
# pip install pytest-xdist
