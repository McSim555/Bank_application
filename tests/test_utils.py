from unittest.mock import mock_open, patch

from src.utils import financial_transactions


@patch("builtins.open", mock_open(read_data='[{"id": 1, "amount": 100}]'))
def test_financial_transactions():
    """Тест: корректный JSON-файл с данными"""
    result = financial_transactions("dummy_path.json")
    assert result == [{"id": 1, "amount": 100}]


@patch("builtins.open", mock_open(read_data="[]"))
def test_financial_transactions_empty():
    """Тест: JSON-файл содержит пустой список"""
    result = financial_transactions("dummy_path.json")
    assert result == []


def test_financial_transactions_no_file():
    """Тест: файл не найден"""
    result = financial_transactions("no_file.json")
    assert result == []


@patch("builtins.open", mock_open(read_data='{"r": "t"}'))
def test_financial_transactions_not_a_list():
    """Тест: JSON — не список (например, словарь)"""
    result = financial_transactions("dummy_path.json")
    assert result == []
