from statistics import mean, StatisticsError

import pytest

from functions.level_3.one_avg_daily_expenses import calculate_average_daily_expenses


def test__calculate_average_daily_expenses__check_if_mean_calculates_correctly_with_one_element(expense_model):
    assert calculate_average_daily_expenses(expense_model) == mean([10])


def test__calculate_average_daily_expenses__check_if_mean_calculates_correctly_with_few_elements(expense_models):
    assert calculate_average_daily_expenses(expense_models) == mean([10, 99])


@pytest.mark.xfail(reason='unable to handle empty list')
def test__calculate_average_daily_expenses__check_if_list_is_empty():
    with pytest.raises(StatisticsError):
        assert calculate_average_daily_expenses([]) is None
