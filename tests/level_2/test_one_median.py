from functions.level_2.one_median import get_median_value


def test__get_median_value_if_empty_list():
    # test_list = [11, 9, 3, 5, 5, 2, 7, 1, 8]
    test_list = []

    assert get_median_value(test_list) is None


def test__get_median_value_list_with_one_value():
    test_list = [11]

    assert get_median_value(test_list) == 11


def test__get_median_value_check_even_list():
    # test_list = [11, 9, 3, 5, 5, 2, 7, 1, 8]
    test_list = []

    assert get_median_value(test_list) is None


def test__get_median_value_check_odd_list():
    # test_list = [11, 9, 3, 5, 5, 2, 7, 1, 8]
    test_list = []

    assert get_median_value(test_list) is None
