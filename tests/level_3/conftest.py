import datetime

import pytest

from functions.level_3.models import Expense


@pytest.fixture
def expense_model():
    return [Expense(amount=10, currency='USD', card={'last_digits': '4849', 'owner': 'Vasek'},
            spent_in='Somewhere', spent_at=datetime.datetime(2023, 11, 11, 13, 7, 5, 533855),
            category='BAR_RESTAURANT'),
            ]

@pytest.fixture
def expense_models():
    return [Expense(amount=10, currency='USD', card={'last_digits': '4849', 'owner': 'Vasek'},
            spent_in='Somewhere', spent_at=datetime.datetime(2023, 11, 11, 13, 7, 5, 533855),
            category='BAR_RESTAURANT'),
            Expense(amount=99, currency='USD', card={'last_digits': '4849', 'owner': 'Vasek'},
            spent_in='Somewhere', spent_at=datetime.datetime(2023, 5, 9, 13, 7, 5, 832199),
            category='BAR_RESTAURANT'),
            ]
