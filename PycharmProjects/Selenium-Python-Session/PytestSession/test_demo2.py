import pytest


def test_L1():
    name = "Selenium"
    assert name.upper() == "SELENIUM"


def test_L2():
    assert True

@pytest.mark.login
def test_L3():
    assert True


@pytest.mark.login
def test_L4_login():
    assert 100 == 100
