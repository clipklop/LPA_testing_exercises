import pytest

from functions.level_2.five_replace_word import replace_word


def test__replace_word__check_if_word_replacing_is_working_correctly():
    text = 'Asynchronous JavaScript or JavaScript that uses callbacks, is hard to get right intuitively.'
    replace_from = 'JavaScript'
    replace_to = 'Python'

    actual_result = 'Asynchronous Python or Python that uses callbacks, is hard to get right intuitively.'

    assert replace_word(text=text, replace_from=replace_from, replace_to=replace_to) == actual_result


def test__replace_word__check_if_replace_from_word_not_found_in_text_initial_text_would_remain_the_same():
    text = 'Asynchronous JavaScript or JavaScript that uses callbacks, is hard to get right intuitively.'
    replace_from = 'GO'
    replace_to = 'Python'

    assert replace_word(text=text, replace_from=replace_from, replace_to=replace_to) == text


def test__replace_word__check_if_another_data_type_in_text_except_for_str_would_raise_attribute_error():
    text = 42
    replace_from = 'JavaScript'
    replace_to = 'Python'

    with pytest.raises(AttributeError):
        assert replace_word(text=text, replace_from=replace_from, replace_to=replace_to) == text


def test__replace_word__check_if_another_data_type_in_replace_from_except_for_str_would_raise_attribute_error():
    text = 'Asynchronous JavaScript or JavaScript that uses callbacks, is hard to get right intuitively.'
    replace_from = 42
    replace_to = 'Python'

    with pytest.raises(AttributeError):
        assert replace_word(text=text, replace_from=replace_from, replace_to=replace_to) == text


def test__replace_word__check_if_another_data_type_in_replace_to_except_for_str_would_raise_type_error():
    text = 'Asynchronous JavaScript or JavaScript that uses callbacks, is hard to get right intuitively.'
    replace_from = 'JavaScript'
    replace_to = 42

    with pytest.raises(TypeError):
        assert replace_word(text=text, replace_from=replace_from, replace_to=replace_to) == text

