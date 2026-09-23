"""Unit tests for the Calculator module."""

import pytest

from src.calculator import Calculator


class TestCalculator:
    """Test suite covering Calculator operations."""

    def test_add(self) -> None:
        assert Calculator.add(2, 3) == 5
        assert Calculator.add(-1, 1) == 0
        assert Calculator.add(0, 0) == 0
        assert Calculator.add(2.5, 3.5) == 6.0

    def test_subtract(self) -> None:
        assert Calculator.subtract(10, 4) == 6
        assert Calculator.subtract(4, 10) == -6
        assert Calculator.subtract(0, 5) == -5

    def test_multiply(self) -> None:
        assert Calculator.multiply(3, 7) == 21
        assert Calculator.multiply(-2, 4) == -8
        assert Calculator.multiply(0, 100) == 0

    def test_divide(self) -> None:
        assert Calculator.divide(10, 2) == 5.0
        assert Calculator.divide(7, 2) == 3.5

    def test_divide_by_zero(self) -> None:
        with pytest.raises(ValueError, match="Cannot divide by zero."):
            Calculator.divide(10, 0)

    def test_power(self) -> None:
        assert Calculator.power(2, 3) == 8
        assert Calculator.power(5, 0) == 1
        assert Calculator.power(4, 0.5) == 2.0

    def test_average(self) -> None:
        assert Calculator.average([1, 2, 3, 4, 5]) == 3.0
        assert Calculator.average([10, 20]) == 15.0

    def test_average_empty(self) -> None:
        with pytest.raises(
            ValueError, match="Cannot calculate average of an empty list."
        ):
            Calculator.average([])

    @pytest.mark.parametrize(
        "val, expected",
        [
            (2, True),
            (3, False),
            (0, True),
            (-4, True),
            (-5, False),
        ],
    )
    def test_is_even(self, val: int, expected: bool) -> None:
        assert Calculator.is_even(val) is expected

    def test_is_even_invalid_type(self) -> None:
        with pytest.raises(TypeError, match="Input must be an integer."):
            Calculator.is_even("two")  # type: ignore
