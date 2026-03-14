def filter_by_currency(transactions: list, currency_default="USD"):
    """Функция фильтрует транзакции по валюте"""

    for tran in transactions:
        if "code" in tran["operationAmount"]["currency"] and tran["operationAmount"]["currency"]["code"] != "" :
            continue
        else:
            raise KeyError('Отсутствует код валюты в введенных операциях')

    transactions_filtered = (
        filter(lambda x: x["operationAmount"]["currency"]["code"] == currency_default, transactions)
        )

    return transactions_filtered

# usd_transactions = filter_by_currency([{
#           "id": 939719570,
#           "state": "EXECUTED",
#           "date": "2018-06-30T02:08:58.425572",
#           "operationAmount": {
#               "amount": "9824.07",
#               "currency": {
#                   "name": "USD",
#               }
#           },
#           "description": "Перевод организации",
#           "from": "Счет 75106830613657916952",
#           "to": "Счет 11776614605963066702"
#       },
#       {
#               "id": 142264268,
#               "state": "EXECUTED",
#               "date": "2019-04-04T23:20:05.206878",
#               "operationAmount": {
#                   "amount": "79114.93",
#                   "currency": {
#                       "name": "USD",
#                   }
#               },
#               "description": "Перевод со счета на счет",
#               "from": "Счет 19708645243227258542",
#               "to": "Счет 75651667383060284188"
#        },
#         {
#             "id": 939719570,
#             "state": "EXECUTED",
#             "date": "2018-06-30T02:08:58.425572",
#             "operationAmount": {
#                 "amount": "9824.07",
#                 "currency": {
#                     "name": "EUR",
#                 }
#             },
#             "description": "Перевод организации",
#             "from": "Счет 75106830613657916952",
#             "to": "Счет 11776614605963066702"
#         }
#     ], "USD")
# for _ in range(2):
#     print(next(usd_transactions))
#     print(type(usd_transactions))