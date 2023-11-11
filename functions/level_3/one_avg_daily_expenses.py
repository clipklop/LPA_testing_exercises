import collections
import decimal
from statistics import mean

# from functions.level_3.models import Expense
from models import Expense


def calculate_average_daily_expenses(expenses: list[Expense]) -> decimal.Decimal:
    total_expenses_dy_day = collections.defaultdict(decimal.Decimal)
    for expense in expenses:
        print(expense.spent_at)
        # total_expenses_dy_day[expense.spent_at.date()] += expense.amount
    return mean(total_expenses_dy_day.values())

import datetime
expenses = {
    'amount': 10,
    'currency': 'USD',
    'card': {
        'last_digits': '4849',
        'owner': 'Vasek'
    },
    'spent_in': 'Somewhere',
    'spent_at': datetime.datetime(2023, 11, 11, 13, 7, 5, 533855),
    'category': 'BAR_RESTAURANT',
}
print(calculate_average_daily_expenses(expenses))