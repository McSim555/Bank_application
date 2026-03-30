import json


def financial_transactions(path_source: str) -> list[dict]:
    """Функцию принимает на вход путь до JSON-файла и возвращает список словарей с данными о финансовых транзакциях"""

    try:
        with open(path_source, "r", encoding="utf-8") as file:
            transactions = json.load(file)
            if type(transactions) == list and len(transactions) > 0:
                return transactions
            else:
                return []

    except Exception:
        return []
