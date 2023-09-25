from functions.level_2.four_sentiment import check_tweet_sentiment


def test__check_tweet_sentiment__check_if_we_found_good_words():
    text = """You probably often encountered the concept of personalizing your taste in products you 
    find online. For example, users create wishlists or shopping lists of various products, a personal
    book library as they buy and read books, sewing fabric preferences, or song library they listen 
    to often. Your personal wishlist is stored in a database so you can view it when needed."""
    good_words = {'taste',}
    bad_words = {'rediska',}

    assert check_tweet_sentiment(text=text, good_words=good_words, bad_words=bad_words) == 'GOOD'


def test__check_tweet_sentiment__check_if_we_found_bad_words():
    text = """You probably often encountered the concept of personalizing your taste in products you 
    find online. For example, users create wishlists or shopping lists of various products, a personal
    book library as they buy and read books, sewing fabric preferences, or song library they listen 
    to often. Your personal wishlist is stored in a database so you can view it when needed."""
    good_words = {'tasty',}
    bad_words = {'library',}


    assert check_tweet_sentiment(text=text, good_words=good_words, bad_words=bad_words) == 'BAD'


def test__check_tweet_sentiment__check_if_we_found_more_good_words_than_bad_words():
    text = """You probably often encountered the concept of personalizing your taste in products you 
    find online. For example, users create wishlists or shopping lists of various products, a personal
    book library as they buy and read books, sewing fabric preferences, or song library they listen 
    to often. Your personal wishlist is stored in a database so you can view it when needed."""
    good_words = {'library',}
    bad_words = {'database',}

    assert check_tweet_sentiment(text=text, good_words=good_words, bad_words=bad_words) == 'GOOD'


def test__check_tweet_sentiment__check_if_we_found_both_good_and_bad_words():
    text = """You probably often encountered the concept of personalizing your taste in products you 
    find online. For example, users create wishlists or shopping lists of various products, a personal
    book library as they buy and read books, sewing fabric preferences, or song library they listen 
    to often. Your personal wishlist is stored in a database so you can view it when needed."""
    good_words = {'or',}
    bad_words = {'library',}


    assert check_tweet_sentiment(text=text, good_words=good_words, bad_words=bad_words) == None


def test__check_tweet_sentiment__check_if_other_datatypes_in_args_would_work():
    text = """You probably often encountered the concept of personalizing your taste in products you 
    find online. For example, users create wishlists or shopping lists of various products, a personal
    book library as they buy and read books, sewing fabric preferences, or song library they listen 
    to often. Your personal wishlist is stored in a database so you can view it when needed."""
    good_words = ['concept']
    bad_words = ['rediska']


    assert check_tweet_sentiment(text=text, good_words=good_words, bad_words=bad_words) == 'GOOD'
