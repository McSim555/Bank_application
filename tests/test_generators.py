import pytest

from src.generators import filter_by_currency, transaction_descriptions


def test_filter_by_currency(test_set_filter_by_currency_transactions):
    expected_result = [
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702",
        },
        {
            "id": 142264268,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206878",
            "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод со счета на счет",
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188",
        },
        {
            "id": 895315941,
            "state": "EXECUTED",
            "date": "2018-08-19T04:27:37.904916",
            "operationAmount": {"amount": "56883.54", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод с карты на карту",
            "from": "Visa Classic 6831982476737658",
            "to": "Visa Platinum 8990922113665229",
        },
    ]

    result = []
    for _ in range(2):
        result = list(filter_by_currency(test_set_filter_by_currency_transactions))
    assert expected_result == result


def test_filter_by_currency_other_currency(test_set_filter_by_currency_transactions):

    expected_result = [{'id': 873106923, 'state': 'EXECUTED', 'date': '2019-03-23T01:09:46.296404', 'operationAmount': {'amount': '43318.34', 'currency': {'name': 'руб.', 'code': 'RUB'}}, 'description': 'Перевод со счета на счет', 'from': 'Счет 44812258784861134719', 'to': 'Счет 74489636417521191160'}, {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689', 'operationAmount': {'amount': '67314.70', 'currency': {'name': 'руб.', 'code': 'RUB'}}, 'description': 'Перевод организации', 'from': 'Visa Platinum 1246377376343588', 'to': 'Счет 14211924144426031657'}]
    result = []
    for _ in range(2):
        result = list(filter_by_currency(test_set_filter_by_currency_transactions, 'RUB'))
    assert expected_result == result


def test_filter_by_currency_no_currency_key(test_filter_by_currency_no_currency_code):
    with pytest.raises(KeyError):
        filter_by_currency(test_filter_by_currency_no_currency_code)

def test_filter_by_currency_currency_empty():
    with pytest.raises(KeyError):
        filter_by_currency(tuple(
    [
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {
                "amount": "9824.07",
                "currency": {
                    "name": "USD",
                    "code": ""
                }
            },
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702"
        },
        {
            "id": 142264268,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206878",
            "operationAmount": {
                "amount": "79114.93",
                "currency": {
                    "name": "USD",
                    "code": ""
                }
            },
            "description": "Перевод со счета на счет",
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188"
        },

    ]
))

def test_filter_by_currency_none():
    with pytest.raises(KeyError):
        filter_by_currency(tuple([{}]))


def test_transactions_description(test_set_filter_by_currency_transactions):
    expected_result = ['Перевод организации', 'Перевод со счета на счет', 'Перевод со счета на счет', 'Перевод с карты на карту', 'Перевод организации']
    result = []
    for _ in range(5):
        result = list(transaction_descriptions(test_set_filter_by_currency_transactions))
    assert expected_result == result


def test_transactions_description_none():
    with pytest.raises(KeyError):
        transaction_descriptions(tuple([{}]))


def test_transactions_description_no_description_key():
    with pytest.raises(KeyError):
        transaction_descriptions(tuple((
    [
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {
                "amount": "9824.07",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702"
        }])))

def test_transaction_descriptions_description_empty():
    with pytest.raises(KeyError):
        transaction_descriptions(tuple(
    [
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {
                "amount": "9824.07",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702"
        }]))