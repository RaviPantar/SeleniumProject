import pytest


@pytest.mark.login
def test_method1():
    print("test method1")


@pytest.mark.login
def test_method2():
    print("test method2")


def test_method3():
    print("test method3")