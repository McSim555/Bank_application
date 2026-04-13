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

    except Exception:
        csv_transactions_list = []
        return csv_transactions_list


# print(csv_data_upload('../data/transactions_empty_1.csv'))


def excel_data_upload(file_path: str) -> list[dict]:
    """Функция для считывания финансовых операций из Excel выдает список словарей с транзакциями"""

    try:
        excel_data = pd.read_excel(file_path)
        i = 0
        for transaction in excel_data["from"].notnull():
            if transaction is False:
                excel_data.loc[i, "from"] = ""
            i += 1

        i = 0
        for transaction in excel_data["id"].notnull():
            if transaction is False:
                excel_data = excel_data.dropna(subset=["id"])
            i += 1

        excel_transactions_list = excel_data.to_dict(orient="records")

        excel_transactions_list_new = []
        for operation in excel_transactions_list:
            operation["id"] = int(operation["id"])
            excel_transactions_list_new.append(operation)

        return excel_transactions_list_new

    except Exception:
        return []


# print(excel_data_upload('../data/transactions_excel.xlsx'))
