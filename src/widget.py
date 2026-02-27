def mask_account_card(card_or_account_number: str) -> str:
    """Функция принимает название и номер карты или номер счета и возвращает в замаскированном виде"""
    from src import masks

    if "Счет" in card_or_account_number:  # Проверка введен счет или карта
        # Формирование замаскированного вывода для счета:
        masked_account = "Счет " + masks.get_mask_account(int(card_or_account_number[5:]))
        return masked_account
    else:
        # Формирование замаскированного вывода для карты:
        masked_card = card_or_account_number[:-16] + masks.get_mask_card_number(int(card_or_account_number[-16:]))
        return masked_card


def get_date(input_date: str) -> str:
    """Функция принимает набор данных, содержащих дату, и возвращает только дату в заданном формате"""
    cleaned_date = input_date[:10]  # Отрезаем лишнее
    date_list = cleaned_date.split("-")  # Разбиваем сторку на три элемента: год, месяц, день
    target_date = date_list[2] + "." + date_list[1] + "." + date_list[0]  # Сборка даты в заданном формате

    return target_date
