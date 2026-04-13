import unittest
from unittest.mock import patch

import pytest

from src.external_api import conversion_to_rub


def test_conversion_to_rub_for_rub():
    """Тест для транзакции в рублях"""

    assert (
        conversion_to_rub(
            {
                "id": 716496732,
                "state": "EXECUTED",
                "date": "2018-04-04T17:33:34.701093",
                "operationAmount": {"amount": "40701.91", "currency": {"name": "RUB", "code": "RUB"}},
                "description": "Перевод организации",
                "from": "Visa Gold 5999414228426353",
                "to": "Счет 72731966109147704472",
            }
        )
        == 40701.91
    )


def test_conversion_to_rub_other_currency():
    """Тест обработки, если в транзакции не RUB, EUR или USD"""

    with pytest.raises(ValueError):
        conversion_to_rub(
            {
                "id": 716496732,
                "state": "EXECUTED",
                "date": "2018-04-04T17:33:34.701093",
                "operationAmount": {"amount": "40701.91", "currency": {"name": "AED", "code": "AED"}},
                "description": "Перевод организации",
                "from": "Visa Gold 5999414228426353",
                "to": "Счет 72731966109147704472",
            }
        )


@patch("requests.get")
def test_external_api_normal_run_EUR(mock_get):
    """Тест работы функции с заглушкой данных по API"""

    mock_response = unittest.mock.Mock()

    mock_response.status_code = 200

    mock_response.json.return_value = {"result": "407981.9900"}

    mock_get.return_value = mock_response

    transaction = {
        "id": 716496732,
        "state": "EXECUTED",
        "date": "2018-04-04T17:33:34.701093",
        "operationAmount": {"amount": "40701.91", "currency": {"name": "EUR", "code": "EUR"}},
        "description": "Перевод организации",
        "from": "Visa Gold 5999414228426353",
        "to": "Счет 72731966109147704472",
    }

    result = conversion_to_rub(transaction)

    assert result == 407981.9900

    mock_get.assert_called_once()


@patch("requests.get")
def test_external_api_normal_run_USD(mock_get):
    """Тест работы функции с заглушкой данных по API"""

    mock_response = unittest.mock.Mock()

    mock_response.status_code = 200

    mock_response.json.return_value = {"result": "407981.9900"}

    mock_get.return_value = mock_response

    transaction = {
        "id": 716496732,
        "state": "EXECUTED",
        "date": "2018-04-04T17:33:34.701093",
        "operationAmount": {"amount": "40701.91", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод организации",
        "from": "Visa Gold 5999414228426353",
        "to": "Счет 72731966109147704472",
    }

    result = conversion_to_rub(transaction)

    assert result == 407981.9900

    mock_get.assert_called_once()
