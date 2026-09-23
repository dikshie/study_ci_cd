"""Calculator and Math Utilities module."""


class Calculator:
    """A simple calculator class demonstrating unit testing & CI practices."""

    @staticmethod
    def add(a: float, b: float) -> int | float:
        """Add two numbers."""
        return a + b

    @staticmethod
    def subtract(a: float, b: float) -> int | float:
        """Subtract b from a."""
        return a - b

    @staticmethod
    def multiply(a: float, b: float) -> int | float:
        """Multiply two numbers."""
        return a * b

    @staticmethod
    def divide(a: float, b: float) -> float:
        """Divide a by b with division-by-zero check."""
        if b == 0:
            raise ValueError("Cannot divide by zero.")
        return a / b

    @staticmethod
    def power(base: float, exponent: float) -> float:
        """Raise base to exponent."""
        return float(base**exponent)

    @staticmethod
    def average(numbers: list[int | float]) -> float:
        """Calculate the arithmetic mean of a list of numbers."""
        if not numbers:
            raise ValueError("Cannot calculate average of an empty list.")
        return sum(numbers) / len(numbers)

    @staticmethod
    def is_even(n: int) -> bool:
        """Check if an integer is even."""
        if not isinstance(n, int):
            raise TypeError("Input must be an integer.")
        return n % 2 == 0
