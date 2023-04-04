import pytest


class TestDepends:

    @pytest.mark.dependency()
    def test_method1(self):
        print("method-1 is called")
        assert 1 + 2 == 3

    @pytest.mark.dependency(depends=["TestDepends::test_method1"])
    def test_method2(self):
        print("method-2 is called")

    def test_method3(self):
        print("method-3 is called")


class TestNew:
    @pytest.mark.dependency(depends=["TestDepends::test_method1"])
    def test_method3(self):
        print("method-3 is called")


