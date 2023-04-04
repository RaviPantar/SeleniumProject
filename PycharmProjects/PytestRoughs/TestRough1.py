import pytest


def test_total_divisible_by_5(input_total):
    assert input_total % 5 == 0


def test_total_divisible_by_10(input_total):
    assert input_total % 10 == 0


def test_total_divisible_by_9(input_total):
    assert input_total % 4 == 0


def test_total_divisble_by_15(input_total):
    assert input_total % 2 == 0
