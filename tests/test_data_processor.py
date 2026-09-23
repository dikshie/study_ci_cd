"""Unit tests for DataProcessor module."""

import pytest

from src.data_processor import DataProcessor


class TestDataProcessor:
    """Test suite for DataProcessor."""

    def test_filter_by_key(self) -> None:
        records = [
            {"id": 1, "status": "active"},
            {"id": 2, "status": "inactive"},
            {"id": 3, "status": "active"},
        ]
        result = DataProcessor.filter_by_key(records, "status", "active")
        assert len(result) == 2
        assert result[0]["id"] == 1
        assert result[1]["id"] == 3

    def test_calculate_total_amount(self) -> None:
        records = [
            {"item": "book", "amount": 15.5},
            {"item": "pen", "amount": 2.5},
            {"item": "notebook", "amount": "invalid"},
        ]
        total = DataProcessor.calculate_total_amount(records, "amount")
        assert total == 18.0

    def test_parse_json_payload_valid(self) -> None:
        raw = '{"name": "Alice", "role": "admin"}'
        parsed = DataProcessor.parse_json_payload(raw)
        assert parsed == {"name": "Alice", "role": "admin"}

    def test_parse_json_payload_invalid(self) -> None:
        assert DataProcessor.parse_json_payload("not valid json") is None
        assert DataProcessor.parse_json_payload('["list", "not", "dict"]') is None
        assert DataProcessor.parse_json_payload(None) is None  # type: ignore

    def test_sanitize_user_input(self) -> None:
        raw_text = "  <script>alert('hack')</script>  "
        clean = DataProcessor.sanitize_user_input(raw_text)
        assert clean == "&lt;script&gt;alert('hack')&lt;/script&gt;"

    def test_sanitize_invalid_type(self) -> None:
        with pytest.raises(TypeError, match="Expected string input."):
            DataProcessor.sanitize_user_input(123)  # type: ignore
