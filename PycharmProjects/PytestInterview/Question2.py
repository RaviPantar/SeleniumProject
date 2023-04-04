# How to run specific mehod before all the test method in a class using fixture
import pytest


class Test:

    @pytest.fixture(scope="class", autouse=True)
    def my_method(self, request):
        print("my method")

        def teardown():
            print("teardown method is called")
        request.addfinalizer(teardown())

    def test_method1(self):
        print("test method 1")

    def test_method2(self):
        print("test method 2")
