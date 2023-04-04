import pytest


def test_m1_login():
    name = "Selenium"
    assert name.upper() == "SELENIUM"


@pytest.mark.login
def test_m2():
    assert True


def test_m3():
    assert True


@pytest.mark.login
def test_m4():
    assert 100 == 100

# py.test -m login
# pytest -v test_demo.py -m login
