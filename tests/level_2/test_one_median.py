from functions.level_2.one_median import get_median_value


def test__get_median_value__if_items_list_is_empty():
    test_list = []

    assert get_median_value(test_list) is None


def test__get_median_value__items_consist_one_value():
    test_list = [11]

    assert get_median_value(test_list) == 11


def test__get_median_value__items_list_of_odd_numbers():
    test_list = [11, 9, 3, 5, 7, 2, 7, 1, 8]

    assert get_median_value(test_list) == 6


def test__get_median_value__items_list_of_even_numbers():
    test_list = [11, 9, 3, 5, 7, 2, 7, 1]

    assert get_median_value(test_list) == 7
