import pytest

from functions.level_2.two_square_equation import solve_square_equation


@pytest.mark.parametrize(
    ("square_coefficient", "linear_coefficient", "const_coefficient", "expected_result"),
    [
        (3.0, 3.0, 3.0, (None, None)),
        (0, 0, 0, (None, None)),
        (0, 3.0, 3.0, (-1.0, None)),
        (-4.0, 3.0, 2.0, (1.175390529679106, -0.42539052967910607)),
        (-12, -4, 3, (0.36037961002806324, -0.6937129433613967)),

    ],
    ids=[
        "if_discriminant_is_less_than_0_returns_none",
        "if_square_coefficient_false_and_linear_coefficient_false_returns_none",
        "if_square_coefficient_false_but_linear_coefficient_true_returns_one_root",
        "if_discriminant_positive_float_returns_two_roots",
        "if_coefficients_are_ints_returns_two_roots",
    ]
)
def test__solve_square_equation(square_coefficient, linear_coefficient, const_coefficient, expected_result):
    assert solve_square_equation(square_coefficient, linear_coefficient, const_coefficient) == expected_result
