import pytest

from functions.level_2.one_median import get_median_value


def test__get_median_value__if_items_list_is_empty_returns_none():
    assert get_median_value(items=[]) is None


@pytest.mark.xfail(reason='unable to handle list of one value only')
def test__get_median_value__items_consist_one_value_returns_that_number():
    assert get_median_value(items=[11]) == 11


@pytest.mark.xfail(reason='incorrect calculation for odd and even numbers')
@pytest.mark.parametrize(
    ("items", "expected_result"),
    [
        ([11, 9, 3, 5, 7, 2, 7, 1, 8], 7),
        ([11, 9, 3, 5, 7, 2, 7, 1, 8, 10], 9),
    ],
    ids=[
        "items_list_of_odd_numbers_returns_median_value", 
        "items_list_of_even_numbers_returns_median_value"
    ]
)
def test__get_median_value(items, expected_result):
    assert get_median_value(items=items) == expected_result
