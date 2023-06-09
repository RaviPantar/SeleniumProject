from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import pytest

driver = None


@pytest.fixture(scope='module')
def init_driver():
    global driver
    print("-------------setUp---------------------")
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.implicitly_wait(10)
    driver.delete_all_cookies()
    driver.get("http://www.google.com")

    yield
    print("____________________")
    driver.quit()


def test_google_title(init_driver):
    assert driver.title == "Google"


# pytest test_google_fixture.py -v -s --html=test_google_fixture_report.html
@pytest.mark.usefixtures("init_driver")
def test_google_url():
    print(driver.current_url)
    assert driver.current_url == "https://www.google.com/"

# pip install pytest -html
# pytest test_google_test.py -v -s --html=google_test_report.html
# pip install pytest-xdist
