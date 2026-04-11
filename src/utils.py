import json
import logging
import os

os.makedirs("../logs", exist_ok=True)
logger_utils = logging.getLogger("utils")
logger_utils.setLevel(logging.DEBUG)
file_handler = logging.FileHandler("..\\logs\\utils.log", "w", encoding="utf-8")
file_formatter = logging.Formatter("%(asctime)s %(filename)s %(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
logger_utils.addHandler(file_handler)


def financial_transactions(path_source: str) -> list[dict]:
    """Функцию принимает на вход путь до JSON-файла и возвращает список словарей с данными о финансовых транзакциях"""

    # path_source = input("Введите путь до файла с информацией о финансовых операциях:")
    # logger_utils.info(f"Введен путь к файлу: {path_source}")

    try:
        with open(path_source, "r", encoding="utf-8") as file:
            transactions = json.load(file)

        # Удаление пустых транзакций из списка операций
        for operation in transactions:
            if operation == {}:
                transactions.remove(operation)

        if type(transactions) is list and len(transactions) > 0:
            final_transactions = []
            for operation in transactions:
                operation['amount'] = operation['operationAmount']['amount']
                operation['currency_name'] = operation['operationAmount']['currency']['name']
                operation['currency_code'] = operation['operationAmount']['currency']['code']
                del operation['operationAmount']
                final_transactions.append(operation)
            logger_utils.info("Список финансовых операций сформирован")
            return final_transactions
        else:
            logger_utils.info("Список пустой, так как исходный файл пустой или не является списком")
            return []

    except Exception as e:
        logger_utils.error(f"Произошла ошибка: {e}")
        return []


# print(financial_transactions("../data/operations.json"))
