import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


def test_google():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.implicitly_wait(12)
    driver.get('https://www.google.com')
    time.sleep(4)
    assert driver.title == "Google"
    driver.quit()


def test_facebook():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.implicitly_wait(12)
    driver.get('https://www.facebook.com')
    time.sleep(4)
    assert driver.title == "Facebook-log in or sign up"
    driver.quit()


def test_instagram():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.implicitly_wait(12)
    driver.get('https://www.instagram.com/')
    time.sleep(4)
    assert driver.title == "Instagram"
    driver.quit()


def test_gmail():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.implicitly_wait(12)
    driver.get('https://www.gmail.com')
    time.sleep(4)
    assert driver.title == "Gmail"
    driver.quit()


def test_rediff():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.implicitly_wait(12)
    driver.get('https://www.rediff.com/')
    time.sleep(4)
    assert driver.title == "Rediff.com: News | Rediffmail | Stock Quotes | Shopping"
    driver.quit()


def test_spicejet():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.implicitly_wait(12)
    driver.get('https://www.spicejet.com/')
    time.sleep(4)
    assert driver.title == "SpiceJet - Flight Booking for Domestic and International, Cheap Air Tickets"
    driver.quit()

# pip install pytest-xdist
# pytest -s test_webpage_login.py -n 4
