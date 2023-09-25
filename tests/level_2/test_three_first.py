import pytest

from functions.level_2.three_first import first, NOT_SET


def test__first__if_nonempty_list_passed_return_first_value_from_items():
    items = [11, 9, 3, 5, 7, 2, 7, 1, 8]
    default = None

    assert first(items=items, default=default) == 11


def test__first__if_empty_list_passed_return_none_from_default():
    items = []
    default = None

    assert first(items=items, default=default) == None


def test__first__if_empty_list_passed_and_default_get_notset_value_return_attributeerror():
    items = []
    default = NOT_SET

    with pytest.raises(AttributeError) as e:
        assert first(items=items, default=default) is False


def test__first__if_nonempty_str_passed_to_items_get_first_character():
    items = 'word'
    default = NOT_SET

    assert first(items=items, default=default) == 'w'


def test__first__if_noniterable_object_passed_as_items_get_typeerror():
    items = 42
    default = NOT_SET

    with pytest.raises(TypeError) as e:
        assert first(items=items, default=default) is False
