import pytest

from functions.level_2.four_sentiment import check_tweet_sentiment


@pytest.mark.parametrize(
    ("text", "good_words", "bad_words", "expected_result"),
    [
        (
            "You probably often encountered the concept of personalizing your taste in products you find online.",
            {'taste',}, {'rediska',}, 'GOOD'
        ),
        (
            "For example, users create wishlists or shopping lists of various products, a personal book library as they buy and read books in library",
            {'taste',}, {'library',}, 'BAD'
        ),
        (
            "Users create wishlists or shopping lists of various products in library, a personal book library as they buy and read books in library not in the database",
            {'library',}, {'database',}, 'GOOD'
        ),
        (
            "You probably often encountered the concept of personalizing your taste in products you find online or library library.",
            {'or',}, {'library',}, None
        ),
        (
            "You probably often encountered the concept of personalizing your taste in products you find online.",
            ['concept'], ['rediska'], "GOOD"
        ),
    ],
    ids=[
        "if_we_found_good_words_returns_good",
        "if_we_found_bad_words_returns_bad",
        "if_we_found_more_good_words_than_bad_words_returns_good",
        "if_we_found_same_number_of_good_and_bad_words_returns_none",
        "if_other_datatypes_in_args_would_work_returns_good_if_case_is_positive"
    ]
)
def test__check_tweet_sentiment(text, good_words, bad_words, expected_result):
    assert check_tweet_sentiment(text=text, good_words=good_words, bad_words=bad_words) == expected_result
