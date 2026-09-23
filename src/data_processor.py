"""Data processing module for transforming and filtering records."""

import json
from typing import Any


class DataProcessor:
    """Processes tabular and dictionary data records."""

    @staticmethod
    def filter_by_key(
        records: list[dict[str, Any]], key: str, value: Any
    ) -> list[dict[str, Any]]:
        """Filter a list of records where record[key] == value."""
        return [item for item in records if item.get(key) == value]

    @staticmethod
    def calculate_total_amount(
        records: list[dict[str, Any]], field: str = "amount"
    ) -> float:
        """Calculate the sum of a numeric field in records."""
        total: float = 0.0
        for item in records:
            val = item.get(field, 0.0)
            if isinstance(val, (int, float)):
                total += float(val)
        return total

    @staticmethod
    def parse_json_payload(json_str: str) -> dict[str, Any] | None:
        """Safely parse a JSON string into a dictionary."""
        try:
            parsed = json.loads(json_str)
            if isinstance(parsed, dict):
                return parsed
            return None
        except json.JSONDecodeError, TypeError:
            return None

    @staticmethod
    def sanitize_user_input(text: str) -> str:
        """Strip leading/trailing spaces and convert dangerous tags to escaped form."""
        if not isinstance(text, str):
            raise TypeError("Expected string input.")
        cleaned = text.strip()
        cleaned = cleaned.replace("<", "&lt;").replace(">", "&gt;")
        return cleaned
