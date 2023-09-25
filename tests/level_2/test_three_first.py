import pytest

from functions.level_2.three_first import first, NOT_SET


def test__first__if_nonempty_list_passed_return_first_value_from_items():
    assert first(items=[11, 9, 3, 5, 7, 2, 7, 1, 8], default=None) == 11


def test__first__if_empty_list_passed_return_none_from_default():
    assert first(items=[], default=None) == None


def test__first__if_empty_list_passed_and_default_get_notset_value_return_attributeerror():
    with pytest.raises(AttributeError) as e:
        first(items=[], default=NOT_SET) is False


def test__first__if_nonempty_str_passed_to_items_get_first_character():
    assert first(items='word', default=NOT_SET) == 'w'
