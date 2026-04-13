import json
from unittest import mock
from unittest.mock import patch

from src.utils import financial_transactions


@patch("builtins.open", new_callable=mock.mock_open)  # Мокаем открытие файла
def test_successful_load(mock_open):
    """Тест успешной загрузки данных"""
    # Создаем тестовые данные
    test_data = [
        {"id": 1, "operationAmount": {"amount": "31957.58", "currency": {"name": "руб.", "code": "RUB"}}},
        {"id": 2, "operationAmount": {"amount": "31957.58", "currency": {"name": "руб.", "code": "RUB"}}},
    ]
    mock_open.return_value.read.return_value = json.dumps(test_data)

    result = financial_transactions("test_path.json")

    mock_open.assert_called_once_with("test_path.json", "r", encoding="utf-8")
    assert isinstance(result, list)
    assert len(result) == 2
    assert result == [
        {"id": 1, "amount": "31957.58", "currency_name": "руб.", "currency_code": "RUB"},
        {"id": 2, "amount": "31957.58", "currency_name": "руб.", "currency_code": "RUB"},
    ]


@patch("builtins.open", new_callable=mock.mock_open)
def test_financial_transactions_empty(mock_open):
    """Тест: JSON-файл содержит пустой список"""
    test_data = []
    mock_open.return_value.read.return_value = json.dumps(test_data)
    result = financial_transactions("dummy_path.json")
    assert result == []


def test_financial_transactions_no_file():
    """Тест: файл не найден"""
    result = financial_transactions("no_file.json")
    assert result == []


@patch("builtins.open", new_callable=mock.mock_open)
def test_financial_transactions_not_a_list(mock_open):
    """Тест: JSON — не список (например, словарь)"""
    test_data = {"r": "t"}
    mock_open.return_value.read.return_value = json.dumps(test_data)
    result = financial_transactions("dummy_path.json")
    assert result == []
