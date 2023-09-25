import pytest

from functions.level_2.five_replace_word import replace_word


@pytest.mark.parametrize(
    ("text", "replace_from", "replace_to", "expected_result"),
    [
        (
            'Asynchronous JavaScript or JavaScript that uses callbacks, is hard to get right intuitively.',
            'JavaScript', 'Python',
            'Asynchronous Python or Python that uses callbacks, is hard to get right intuitively.'
        ),
        (
            'Asynchronous JavaScript or JavaScript that uses callbacks, is hard to get right intuitively.',
            'GO', 'Python',
            'Asynchronous JavaScript or JavaScript that uses callbacks, is hard to get right intuitively.'
        ),
    ],
    ids=[
        "check_if_word_replacing_is_working_correctly",
        "if_replace_from_word_not_found_in_text_initial_text_would_remain_the_same",
    ]
)
def test__replace_word(text, replace_from, replace_to, expected_result):
    assert replace_word(text=text, replace_from=replace_from, replace_to=replace_to) == expected_result
