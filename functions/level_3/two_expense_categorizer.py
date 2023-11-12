# from functions.level_3.models import Expense, ExpenseCategory
from models import Expense, ExpenseCategory


def guess_expense_category(expense: Expense) -> ExpenseCategory | None:
    triggers_map = {
        ExpenseCategory.BAR_RESTAURANT: {"asador", "julis", "doc", "set", "bastard"},
        ExpenseCategory.SUPERMARKET: {"chinar", "sas", "green apple", "meat house", "clean house"},
        ExpenseCategory.ONLINE_SUBSCRIPTIONS: {"apple.com/bill", "leetcode.com", "zoom.us", "netflix"},
        ExpenseCategory.MEDICINE_PHARMACY: {"farm", "pharm", "alfa-pharm", "maname"},
        ExpenseCategory.THEATRES_MOVIES_CULTURE: {"tomsarkgh", "moscow cinema", "kino park", "cinema galleria"},
        ExpenseCategory.TRANSPORT: {"gg platform", "www.taxi.yandex.ru", "bolt.eu", "yandex go"},
    }
    for possible_category, triggers in triggers_map.items():
        for trigger in triggers:
            print(trigger)
            if is_string_contains_trigger(expense.spent_in, trigger):
                return possible_category
    return None


def is_string_contains_trigger(original_string: str, trigger: str) -> bool:
    allowed_delimiters = {" ", ",", ".", "-", "/", "\\"}

    original_string = original_string.lower()
    return (
            original_string == trigger
            or any(original_string.startswith(f"{trigger}{p}") for p in allowed_delimiters)
            or any(original_string.endswith(f"{p}{trigger}") for p in allowed_delimiters)
            or any(
                f"{d}{trigger}{p}" in original_string
                for p in allowed_delimiters for d in allowed_delimiters
            )
    )

import datetime
print(guess_expense_category(
Expense(amount=10, currency='USD', card={'last_digits': '4849', 'owner': 'Vasek'},
            spent_in='ONLINE_SUBSCRIPTIONS', spent_at=datetime.datetime(2023, 11, 11, 13, 7, 5, 533855),
            category='BAR_RESTAURANT')
))