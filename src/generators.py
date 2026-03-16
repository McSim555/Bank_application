from typing import Generator


def filter_by_currency(transactions: list, currency_default="USD") -> filter:
    """Функция фильтрует транзакции по валюте"""

    i = 0
    for tran in transactions:
        if (
            tran is not None
            and "code" in tran["operationAmount"]["currency"]
            and tran["operationAmount"]["currency"]["code"] != ""
        ):
            if tran["operationAmount"]["currency"]["code"] == currency_default:
                i += 1
        else:
            raise KeyError("Отсутствует код валюты в введенных операциях или на входе пустые данные")

    if i == 0:
        raise ValueError("Нет транзакций с искомым кодом валюты")

    transactions_filtered = filter(
        lambda x: x["operationAmount"]["currency"]["code"] == currency_default, transactions
    )

    return transactions_filtered


def transaction_descriptions(transactions: list) -> Generator[str]:
    """Генератор, который принимает список словарей с транзакциями и возвращает описание каждой операции по очереди"""

    if transactions is not None and len(transactions) > 0:
        for tran in transactions:
            if tran is not None and "description" in tran and tran["description"] != "":
                continue
            else:
                raise KeyError("Отсутствует описание в введенных операциях или на входе пустые данные")
    else:
        raise ValueError("Отсутствуют данные на входе")
    transaction_description = (tr["description"] for tr in transactions)

    return transaction_description


def card_number_generator(start_card_number: str, end_card_number: str) -> Generator[str]:
    """Генератор, который выдает номера банковских карт в формате XXXX XXXX XXXX XXXX"""

    if start_card_number == "" or end_card_number == "":
        raise ValueError('Не указаны начало и/или конец диапазона')

    if len(start_card_number) > 16 or len(end_card_number) >16:
        raise ValueError('Максимальное количество цифр в номере карты 16')

    if start_card_number.isdigit() and end_card_number.isdigit():
        start_card_number = int(start_card_number)
        end_card_number = int(end_card_number)
    else:
        raise TypeError('Неверный формат цифр диапазона')

    if start_card_number > end_card_number:
        raise ValueError("Начальный номер карты больше конечного номера")
    else:
        i = start_card_number
        while i <= end_card_number:
            card_number = i
            card_number_str = str(card_number).zfill(16)
            card_number_final = (
                card_number_str[:4]
                + " "
                + card_number_str[4:8]
                + " "
                + card_number_str[8:12]
                + " "
                + card_number_str[12:]
            )
            yield card_number_final
            i += 1
