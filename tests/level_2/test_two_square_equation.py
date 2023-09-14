import pytest

from functions.level_2.two_square_equation import solve_square_equation


def test__solve_square_equation__if_discriminant_is_less_than_0():
    square_coefficient = 3.0
    linear_coefficient = 3.0
    const_coefficient = 3.0

    assert solve_square_equation(square_coefficient, linear_coefficient, const_coefficient) == (None, None)


def test__solve_square_equation__if_square_coefficient_false_and_linear_coefficient_false():
    square_coefficient = 0
    linear_coefficient = 0
    const_coefficient = 0

    assert solve_square_equation(square_coefficient, linear_coefficient, const_coefficient) == (None, None)


def test__solve_square_equation__if_square_coefficient_false_but_linear_coefficient_true_get_only_root():
    square_coefficient = 0
    linear_coefficient = 3.0
    const_coefficient = 3.0

    assert solve_square_equation(square_coefficient, linear_coefficient, const_coefficient) == (-1.0, None)


def test__solve_square_equation__get_positive_discriminant_and_two_roots():
    square_coefficient = -4.0
    linear_coefficient = 3.0
    const_coefficient = 2.0

    assert solve_square_equation(square_coefficient, linear_coefficient, const_coefficient) == (1.175390529679106, -0.42539052967910607)


def test__solve_square_equation__get_two_roots_with_int_numbers():
    square_coefficient = -12
    linear_coefficient = -4
    const_coefficient = 3

    assert solve_square_equation(square_coefficient, linear_coefficient, const_coefficient) == (0.36037961002806324, -0.6937129433613967)


def test__solve_square_equation__get_two_roots_with_int_numbers():
    square_coefficient = -12
    linear_coefficient = -4
    const_coefficient = 3

    assert solve_square_equation(square_coefficient, linear_coefficient, const_coefficient) == (0.36037961002806324, -0.6937129433613967)


def test__solve_square_equation__check_for_typeerror_if_str_arguments():
    square_coefficient = '2'
    linear_coefficient = '4'
    const_coefficient = '3'

    with pytest.raises(TypeError) as e:
        assert solve_square_equation(square_coefficient, linear_coefficient, const_coefficient) is False
