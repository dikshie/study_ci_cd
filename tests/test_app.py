"""Unit tests for the App CLI and helpers."""

from unittest.mock import patch

from src.app import main, run_summary


def test_run_summary_numbers() -> None:
    stats = run_summary([10.0, 20.0, 30.0])
    assert stats["count"] == 3
    assert stats["sum"] == 60.0
    assert stats["average"] == 20.0


def test_run_summary_empty() -> None:
    stats = run_summary([])
    assert stats["count"] == 0
    assert stats["sum"] == 0.0
    assert stats["average"] == 0.0


def test_main_with_numbers(capsys) -> None:  # type: ignore
    with patch("sys.argv", ["app.py", "--numbers", "1", "2", "3"]):
        exit_code = main()
        captured = capsys.readouterr()
        assert exit_code == 0
        assert "Summary: Count=3, Sum=6.0, Avg=2.0" in captured.out


def test_main_with_sanitize(capsys) -> None:  # type: ignore
    with patch("sys.argv", ["app.py", "--sanitize", "<hello>"]):
        exit_code = main()
        captured = capsys.readouterr()
        assert exit_code == 0
        assert "Sanitized: &lt;hello&gt;" in captured.out


def test_main_no_args(capsys) -> None:  # type: ignore
    with patch("sys.argv", ["app.py"]):
        exit_code = main()
        captured = capsys.readouterr()
        assert exit_code == 0
        assert "Study CI/CD CLI App is running" in captured.out
