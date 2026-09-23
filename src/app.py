"""Main application entry point."""

import argparse
import sys

from src.calculator import Calculator
from src.data_processor import DataProcessor


def run_summary(numbers: list[float]) -> dict:
    """Compute summary statistics using Calculator."""
    if not numbers:
        return {"count": 0, "sum": 0.0, "average": 0.0}
    total = sum(numbers)
    avg = Calculator.average(numbers)
    return {
        "count": len(numbers),
        "sum": total,
        "average": avg,
    }


def main() -> int:
    """CLI execution entrypoint."""
    parser = argparse.ArgumentParser(description="Study CI/CD Sample App")
    parser.add_argument(
        "--numbers",
        nargs="+",
        type=float,
        help="Space-separated list of numbers to compute summary for",
    )
    parser.add_argument(
        "--sanitize",
        type=str,
        help="Sanitize an input string",
    )

    args = parser.parse_args()

    if args.numbers is not None:
        stats = run_summary(args.numbers)
        print(
            f"Summary: Count={stats['count']}, Sum={stats['sum']}, Avg={stats['average']}"
        )
        return 0

    if args.sanitize:
        cleaned = DataProcessor.sanitize_user_input(args.sanitize)
        print(f"Sanitized: {cleaned}")
        return 0

    print("Study CI/CD CLI App is running. Use --help to see available arguments.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
