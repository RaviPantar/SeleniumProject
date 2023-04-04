import pytest
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver


@pytest.fixture(scope='class')
def test_setup_module(request):
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get("https://www.facebook.com/")
    driver.maximize_window()
    request.cls.driver = driver
    driver.close()


@pytest.mark.usefixtures("test_setup_module")
class TestExample:
    def test_title(self):
        print(self.driver.title)
