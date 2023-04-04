# How to run specific mehod before each test method in a class using fixture
import pytest


@pytest.fixture(scope="function", autouse=True)
# @pytest.fixture(autouse=True)
def my_methods():
    print("my method")


def test_method1():
    print("test method 1")


def test_method2():
    print("test method 2")
