# How to call a fixture from test method
import pytest


class Test1:

    @pytest.fixture(scope="class")
    def my_fixture(self):
        print("this is my fixture")

    def test_method1(self, my_fixture):
        print("test method 1")


    def test_method2(self,my_fixture):
        print("test method 2")

