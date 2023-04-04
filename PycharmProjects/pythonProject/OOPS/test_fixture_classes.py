from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium import webdriver
import pytest


@pytest.fixture(scope='class')
def init_chrome_driver(request):
    ch_driver = webdriver.Chrome(ChromeDriverManager().install())
    request.cls.driver = ch_driver
    yield
    ch_driver.close()


@pytest.fixture(scope='class')
def init_firefox_driver(request):
    ch_driver = webdriver.firefox(GeckoDriverManager().install())
    request.cls.driver = ch_driver
    yield
    ch_driver.close()


@pytest.mark.usefixtures("init_chrome_driver")
class Base_chrome_Test:
    pass


class Test_Google_Chrome(Base_chrome_Test):
    def test_google_title_chrome(self):
        self.driver.get("http://www.google.com")
        assert self.driver.title == "Google"
