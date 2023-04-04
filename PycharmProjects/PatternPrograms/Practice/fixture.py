import pytest


@pytest.fixture(scope="function",autouse=True)
def myfixture():
    print("my fixture")


def test_my_test1():
    print("test method1")


def test_my_test1():
    print("test method1")
