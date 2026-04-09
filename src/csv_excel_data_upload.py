import csv

import pandas as pd


def csv_data_upload(file_path: str) -> list[dict]:
    """Функция для считывания финансовых операций из CSV выдает список словарей с транзакциями"""

    try:
        csv_transactions_list = []
        with open(file_path, "r", encoding="utf-8") as file:
            reader = csv.DictReader(file, delimiter=";")
            csv_transactions_list = [row for row in reader]

        return csv_transactions_list

    except Exception as e:
        csv_transactions_list = []
        return csv_transactions_list


# print(csv_data_upload('../data/transactions_empty_1.csv'))


def excel_data_upload(file_path: str) -> list[dict]:
    """Функция для считывания финансовых операций из Excel выдает список словарей с транзакциями"""

    try:
        excel_data = pd.read_excel(file_path)
        excel_transactions_list = excel_data.to_dict(orient="records")

        return excel_transactions_list

    except Exception:
        return []


# print(excel_data_upload('../data/transactions_excel.xlsx'))
