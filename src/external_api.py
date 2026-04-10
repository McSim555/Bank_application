import os

import requests
from dotenv import load_dotenv


def conversion_to_rub(transaction: dict) -> float:
    """функцию принимает на вход транзакцию и возвращает сумму транзакции в рублях, если транзакция была в USD или EUR,
    происходит обращение к внешнему API для получения текущего курса валют и конвертации суммы операции в рубли"""

    if transaction["operationAmount"]["currency"]["code"] == "RUB":
        amount = transaction["operationAmount"]["amount"]
        return float(amount)

    elif (
        transaction["operationAmount"]["currency"]["code"] == "EUR"
        or transaction["operationAmount"]["currency"]["code"] == "USD"
    ):
        url = "https://api.apilayer.com/exchangerates_data/convert"
        load_dotenv("../.env")
        API_KEY = os.getenv("API_KEY")
        headers = {"apikey": API_KEY}
        if transaction["operationAmount"]["currency"]["code"] == "EUR":
            payload = {"amount": transaction["operationAmount"]["amount"], "from": "USD", "to": "RUB"}
        else:
            payload = {"amount": transaction["operationAmount"]["amount"], "from": "USD", "to": "RUB"}

        response = requests.get(url, headers=headers, params=payload)
        result = response.json()["result"]
        return float(result)

    else:
        raise ValueError("Конвертация такой валюты не предусмотрена")


# r = conversion_to_rub({
#         "id": 716496732,
#         "state": "EXECUTED",
#         "date": "2018-04-04T17:33:34.701093",
#         "operationAmount": {"amount": "40701.91", "currency": {"name": "USD", "code": "USD"}},
#         "description": "Перевод организации",
#         "from": "Visa Gold 5999414228426353",
#         "to": "Счет 72731966109147704472",
#     })
# print(r)
