# fixture inside fixture
import pytest


class Test1:

    @pytest.fixture()
    def myfixture(self):
        return "hello"

    @pytest.fixture()
    def myfixture1(self, myfixture):
        return myfixture + "fixture"

    def test_method1(self, myfixture1):
        print("method 1 is called")
        print(myfixture1)