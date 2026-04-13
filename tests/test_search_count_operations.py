from src.search_count_operations import process_bank_operations, process_bank_search


def test_process_bank_search(test_set_filter_by_currency_transactions):
    """Функция тестирует нормальный случай поиска по ключевому слову"""

    results = process_bank_search(test_set_filter_by_currency_transactions, "счет")
    data_search = [
        {
            "id": 142264268,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206878",
            "amount": "79114.93",
            "currency_name": "USD",
            "currency_code": "USD",
            "description": "Перевод со счета на счет",
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188",
        },
        {
            "id": 873106923,
            "state": "EXECUTED",
            "date": "2019-03-23T01:09:46.296404",
            "amount": "43318.34",
            "currency_name": "руб.",
            "currency_code": "RUB",
            "description": "Перевод со счета на счет",
            "from": "Счет 44812258784861134719",
            "to": "Счет 74489636417521191160",
        },
    ]

    assert results == data_search


def test_process_bank_operations(test_set_filter_by_currency_transactions):
    """Функция тестирует нормальную группировку по описанию транзакций"""

    results = process_bank_operations(
        test_set_filter_by_currency_transactions, ["Перевод организации", "Перевод со счета на счет"]
    )
    data_expected = {"Перевод организации": 2, "Перевод со счета на счет": 2}

    assert results == data_expected
