import pytest


@pytest.mark.parametrize("Names",["Ravi","Raj","Rahim"])
def test_method(Names):
    print(Names)